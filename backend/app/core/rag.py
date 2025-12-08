"""RAG (Retrieval-Augmented Generation) service with conversation support."""

import logging
import uuid
from typing import List, Optional, Dict, Any, Tuple
from datetime import datetime, timedelta
from collections import defaultdict

logger = logging.getLogger(__name__)


class ConversationSession:
    """In-memory conversation session storage."""

    def __init__(self, session_id: str):
        self.session_id = session_id
        self.messages: List[Dict[str, Any]] = []
        self.created_at = datetime.utcnow()
        self.last_accessed = datetime.utcnow()

    def add_message(self, role: str, content: str):
        self.messages.append({
            "role": role,
            "content": content,
            "timestamp": datetime.utcnow()
        })
        self.last_accessed = datetime.utcnow()

    def get_recent_messages(self, max_messages: int = 5) -> List[Dict[str, str]]:
        recent = self.messages[-max_messages * 2:] if self.messages else []
        return [{"role": msg["role"], "content": msg["content"]} for msg in recent]

    def is_expired(self, ttl_minutes: int = 60) -> bool:
        return (datetime.utcnow() - self.last_accessed) > timedelta(minutes=ttl_minutes)


class SessionManager:
    """Manages conversation sessions."""

    def __init__(self, ttl_minutes: int = 60):
        self.sessions: Dict[str, ConversationSession] = {}
        self.ttl_minutes = ttl_minutes

    def get_session(self, session_id: str) -> ConversationSession:
        if session_id not in self.sessions:
            self.sessions[session_id] = ConversationSession(session_id)
        else:
            self.sessions[session_id].last_accessed = datetime.utcnow()
        return self.sessions[session_id]

    def cleanup_expired(self):
        expired = [sid for sid, s in self.sessions.items() if s.is_expired(self.ttl_minutes)]
        for sid in expired:
            del self.sessions[sid]
            logger.info(f"Cleaned up expired session: {sid}")


class RAGService:
    """Production-ready RAG service with conversation history and source citations."""

    def __init__(self):
        self.collection_name = "physical_ai_textbook"
        self.embedding_model = "text-embedding-3-small"
        self.chat_model = "gpt-4-turbo-preview"
        self._openai_client = None
        self._qdrant_client = None
        self.session_manager = SessionManager(ttl_minutes=60)

    @property
    def openai_client(self):
        if self._openai_client is None:
            from openai import OpenAI
            from app.core.config import settings
            self._openai_client = OpenAI(api_key=settings.openai_api_key)
        return self._openai_client

    @property
    def qdrant_client(self):
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
        """Generate embedding vector for text."""
        try:
            response = self.openai_client.embeddings.create(
                model=self.embedding_model,
                input=text
            )
            return response.data[0].embedding
        except Exception as e:
            logger.error(f"Failed to generate embedding: {e}")
            raise RuntimeError(f"Embedding generation failed: {e}")

    def search_context(self, query_text: str, top_k: int = 5) -> List[Dict[str, Any]]:
        """Search for relevant context in Qdrant."""
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
                    "section": hit.payload.get("section", f"chunk_{hit.payload.get('chunk_index', 0)}"),
                    "score": hit.score,
                }
                for hit in search_results
            ]
        except Exception as e:
            logger.error(f"Context search failed: {e}")
            return []

    def format_context_with_citations(
        self,
        search_results: List[Dict[str, Any]],
        selected_text: Optional[str] = None
    ) -> Tuple[str, List[Dict[str, Any]]]:
        """Format search results into context with source tracking."""
        sources = []
        context_parts = []

        if selected_text:
            context_parts.append(f"SELECTED TEXT (User Highlighted):\n{selected_text}\n")

        if search_results:
            context_parts.append("RELATED CONTENT FROM TEXTBOOK:\n")
            for idx, result in enumerate(search_results, 1):
                context_parts.append(
                    f"\n[Source {idx}] {result['file']} - {result['section']}\n{result['text']}\n"
                )
                sources.append({
                    "file": result["file"],
                    "section": result["section"],
                    "score": result["score"],
                    "text_preview": result["text"][:200] + "..." if len(result["text"]) > 200 else result["text"]
                })

        return "\n".join(context_parts), sources

    def generate_response(
        self,
        query_text: str,
        context: str,
        conversation_history: Optional[List[Dict[str, str]]] = None
    ) -> Tuple[str, int]:
        """Generate response using OpenAI with conversation history."""
        try:
            messages = [
                {
                    "role": "system",
                    "content": (
                        "You are a helpful AI assistant for the Physical AI Textbook. "
                        "Answer questions based on the provided context. "
                        "If the context doesn't contain relevant information, say so clearly. "
                        "Cite sources using [Source N] notation when referencing the context. "
                        "Be concise but thorough."
                    )
                }
            ]

            if conversation_history:
                messages.extend(conversation_history)

            messages.append({
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion: {query_text}"
            })

            response = self.openai_client.chat.completions.create(
                model=self.chat_model,
                messages=messages,
                temperature=0.7,
                max_tokens=1000
            )

            return response.choices[0].message.content, response.usage.total_tokens
        except Exception as e:
            logger.error(f"Response generation failed: {e}")
            raise RuntimeError(f"Response generation failed: {e}")

    def query(
        self,
        query_text: str,
        selected_text: Optional[str] = None,
        session_id: Optional[str] = None,
        max_history: int = 5
    ) -> Dict[str, Any]:
        """Main RAG query method with conversation support."""
        start_time = datetime.utcnow()

        # Get or create session
        if not session_id:
            session_id = str(uuid.uuid4())
        session = self.session_manager.get_session(session_id)

        # Search for context
        search_results = self.search_context(query_text)

        # Format context with citations
        context, sources = self.format_context_with_citations(search_results, selected_text)

        # Get conversation history
        conversation_history = session.get_recent_messages(max_history) if max_history > 0 else None

        # Generate response
        answer, tokens_used = self.generate_response(query_text, context, conversation_history)

        # Store in session
        session.add_message("user", query_text)
        session.add_message("assistant", answer)

        processing_time = (datetime.utcnow() - start_time).total_seconds() * 1000

        return {
            "answer": answer,
            "sources": sources,
            "session_id": session_id,
            "tokens_used": tokens_used,
            "processing_time_ms": processing_time
        }


# Global RAG service instance
rag_service = RAGService()
