"""Chatbot API endpoints for RAG-powered Q&A with session support."""

import logging
import uuid
from datetime import datetime

from fastapi import APIRouter, HTTPException, status

from app.models.schemas import ChatQueryRequest, ChatQueryResponse, SourceReference
from app.core.rag import rag_service

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/chatbot", tags=["chatbot"])


@router.post("/query", response_model=ChatQueryResponse)
async def query_chatbot(request: ChatQueryRequest):
    """
    Query the RAG chatbot with a question.

    Features:
    - Retrieval-augmented generation from textbook content
    - Conversation history support via session_id
    - Source citations in responses
    - Selected text priority context
    """
    try:
        logger.info(f"Chatbot query: {request.query[:100]}...")

        # Generate session_id if not provided
        session_id = request.session_id or str(uuid.uuid4())

        # Process query through RAG service
        result = rag_service.query(
            query_text=request.query,
            selected_text=request.selected_text,
            session_id=session_id,
            max_history=5
        )

        # Convert sources to SourceReference objects
        sources = [
            SourceReference(
                file=src["file"],
                section=src["section"],
                score=src["score"],
                text_preview=src.get("text_preview")
            )
            for src in result["sources"]
        ]

        response = ChatQueryResponse(
            answer=result["answer"],
            sources=sources,
            session_id=result["session_id"],
            tokens_used=result.get("tokens_used"),
            processing_time_ms=result.get("processing_time_ms")
        )

        logger.info(
            f"Query processed. Session: {session_id}, "
            f"Sources: {len(sources)}, Tokens: {response.tokens_used}"
        )

        return response

    except RuntimeError as e:
        logger.error(f"RAG service error: {e}")
        raise HTTPException(status_code=503, detail=f"RAG service unavailable: {e}")
    except Exception as e:
        logger.error(f"Unexpected error: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal server error")


@router.post("/sessions/{session_id}/clear")
async def clear_session(session_id: str):
    """Clear conversation history for a session."""
    try:
        session = rag_service.session_manager.get_session(session_id)
        session.messages.clear()
        logger.info(f"Cleared session: {session_id}")
        return {"status": "success", "message": f"Session {session_id} cleared"}
    except Exception as e:
        logger.error(f"Error clearing session: {e}")
        raise HTTPException(status_code=500, detail="Error clearing session")


@router.get("/health")
async def chatbot_health():
    """Check chatbot service health."""
    try:
        # Check Qdrant
        qdrant_ok = False
        try:
            rag_service.qdrant_client.get_collections()
            qdrant_ok = True
        except Exception:
            pass

        # Check OpenAI (just verify client exists)
        openai_ok = rag_service.openai_client is not None

        session_count = len(rag_service.session_manager.sessions)

        return {
            "status": "healthy" if (qdrant_ok and openai_ok) else "degraded",
            "timestamp": datetime.utcnow().isoformat(),
            "components": {
                "qdrant": "ok" if qdrant_ok else "error",
                "openai": "ok" if openai_ok else "error",
                "sessions": {"status": "ok", "active": session_count}
            }
        }
    except Exception as e:
        return {"status": "error", "error": str(e)}
