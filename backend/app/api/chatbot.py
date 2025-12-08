"""Chatbot API endpoints for RAG-powered Q&A."""

from fastapi import APIRouter, HTTPException
import logging

from app.models.schemas import ChatQueryRequest, ChatQueryResponse, ContextChunk
from app.core.rag import rag_service

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/chatbot", tags=["chatbot"])


@router.post("/query", response_model=ChatQueryResponse)
async def query_chatbot(request: ChatQueryRequest):
    """
    Query the RAG chatbot with a question.

    Optionally include selected_text from the textbook for context-aware responses.
    """
    try:
        # Get context from vector search
        search_results = await rag_service.search_context(
            query_text=request.query,
            top_k=request.top_k
        )

        # Extract context chunks
        context_chunks = [
            ContextChunk(
                text=result["text"],
                file=result["file"],
                score=result["score"]
            )
            for result in search_results
        ]

        # Generate response using RAG
        answer = await rag_service.generate_response(
            query_text=request.query,
            context_chunks=[chunk.text for chunk in context_chunks],
            selected_text=request.selected_text
        )

        return ChatQueryResponse(
            answer=answer,
            context_chunks=context_chunks,
            query=request.query
        )

    except RuntimeError as e:
        logger.error(f"RAG service error: {str(e)}")
        raise HTTPException(status_code=503, detail=f"RAG service unavailable: {str(e)}")
    except Exception as e:
        logger.error(f"Unexpected error in chatbot query: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")


@router.get("/health")
async def chatbot_health():
    """Check if chatbot service is healthy."""
    return {"status": "healthy", "service": "chatbot"}
