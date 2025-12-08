"""RAG (Retrieval-Augmented Generation) core logic."""

from typing import List, Optional, Dict, Any
import logging

logger = logging.getLogger(__name__)


class RAGService:
    """Service for RAG operations including embeddings and vector search."""

    def __init__(self):
        """Initialize RAG service."""
        self.collection_name = "physical_ai_textbook"
        self.embedding_model = "text-embedding-3-small"
        self.chat_model = "gpt-4-turbo-preview"
        self._openai_client = None
        self._qdrant_client = None

    @property
    def openai_client(self):
        """Lazy load OpenAI client."""
        if self._openai_client is None:
            from openai import OpenAI
            from app.core.config import settings
            self._openai_client = OpenAI(api_key=settings.openai_api_key)
        return self._openai_client

    @property
    def qdrant_client(self):
        """Lazy load Qdrant client."""
        if self._qdrant_client is None:
            from qdrant_client import QdrantClient
            from app.core.config import settings
            if settings.qdrant_api_key:
                self._qdrant_client = QdrantClient(
                    url=settings.qdrant_host,
                    api_key=settings.qdrant_api_key
                )
            else:
                self._qdrant_client = QdrantClient(host=settings.qdrant_host, port=6333)
        return self._qdrant_client

    def generate_embedding(self, text: str) -> List[float]:
        """Generate embedding vector for given text using OpenAI."""
        try:
            response = self.openai_client.embeddings.create(
                model=self.embedding_model,
                input=text
            )
            return response.data[0].embedding
        except Exception as e:
            logger.error(f"Failed to generate embedding: {str(e)}")
            raise RuntimeError(f"Failed to generate embedding: {str(e)}")

    async def search_context(self, query_text: str, top_k: int = 5) -> List[Dict[str, Any]]:
        """Search for relevant context in Qdrant vector database."""
        try:
            query_embedding = self.generate_embedding(query_text)
            search_results = self.qdrant_client.search(
                collection_name=self.collection_name,
                query_vector=query_embedding,
                limit=top_k
            )
            return [
                {
                    "text": hit.payload.get("text", ""),
                    "file": hit.payload.get("file", ""),
                    "score": hit.score,
                }
                for hit in search_results
            ]
        except Exception as e:
            logger.error(f"Failed to search context: {str(e)}")
            raise RuntimeError(f"Failed to search context: {str(e)}")

    async def generate_response(
        self,
        query_text: str,
        context_chunks: List[str],
        selected_text: Optional[str] = None
    ) -> str:
        """Generate response using OpenAI chat completion with retrieved context."""
        try:
            if selected_text:
                context = f"SELECTED TEXT:\n{selected_text}\n\nRELATED CONTENT:\n" + "\n\n".join(context_chunks)
            else:
                context = "\n\n".join(context_chunks)

            response = self.openai_client.chat.completions.create(
                model=self.chat_model,
                messages=[
                    {
                        "role": "system",
                        "content": (
                            "You are a helpful assistant for a Physical AI textbook. "
                            "Answer questions based on the provided context. "
                            "Be precise, educational, and cite specific concepts when relevant."
                        )
                    },
                    {
                        "role": "user",
                        "content": f"Context:\n{context}\n\nQuestion: {query_text}"
                    }
                ],
                temperature=0.7,
                max_tokens=1000
            )
            return response.choices[0].message.content
        except Exception as e:
            logger.error(f"Failed to generate response: {str(e)}")
            raise RuntimeError(f"Failed to generate response: {str(e)}")

    async def query(
        self,
        query_text: str,
        selected_text: Optional[str] = None,
        top_k: int = 5
    ) -> str:
        """Complete RAG query pipeline: search + generate."""
        search_results = await self.search_context(query_text, top_k)
        context_chunks = [result["text"] for result in search_results]
        response = await self.generate_response(
            query_text=query_text,
            context_chunks=context_chunks,
            selected_text=selected_text
        )
        return response


# Global RAG service instance
rag_service = RAGService()
