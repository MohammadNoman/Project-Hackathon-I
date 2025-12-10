"""Translation API endpoints for multilingual content delivery."""

import logging
from typing import Optional

from fastapi import APIRouter, HTTPException, status, Header

from app.models.schemas import (
    TranslateRequest,
    TranslateResponse
)
from app.core.translation import translation_service

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/translate", tags=["translation"])


@router.post("/{chapter_id}", response_model=TranslateResponse)
async def translate_chapter(
    chapter_id: str,
    request: TranslateRequest,
    authorization: Optional[str] = Header(None)
):
    """
    Translate chapter content to target language (default: Urdu).

    This endpoint translates educational content while preserving technical accuracy,
    code blocks, markdown formatting, and mathematical notation.

    Features:
    - Supports multiple languages (primary: Urdu)
    - Preserves technical terms in English with translations
    - Maintains code blocks and markdown structure
    - Right-to-left (RTL) text support for Urdu/Arabic
    - Technical term transliteration

    Args:
        chapter_id: Identifier for the chapter to translate
        request: TranslateRequest containing target language and optional content
        authorization: Optional Bearer token for authenticated users

    Returns:
        TranslateResponse with translated content and metadata
    """
    try:
        logger.info(
            f"Translation request: chapter={chapter_id}, "
            f"language={request.target_language}, "
            f"user_id={request.user_id or 'anonymous'}"
        )

        # Validate language code
        supported_languages = ["ur", "ar", "hi", "es", "fr", "de", "zh", "ja"]
        if request.target_language not in supported_languages:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Unsupported language code: {request.target_language}. "
                       f"Supported: {', '.join(supported_languages)}"
            )

        # Get chapter content
        # If content is provided in request, use it; otherwise fetch from sample
        if request.content:
            chapter_content = request.content
        else:
            chapter_content = translation_service.get_sample_content(chapter_id)

            if "Chapter Not Found" in chapter_content:
                logger.warning(f"Chapter not found: {chapter_id}")
                # Still translate the placeholder for demo purposes
                # In production, raise 404

        # Translate content
        result = translation_service.translate_content(
            chapter_content=chapter_content,
            target_language=request.target_language
        )

        # Build response
        response = TranslateResponse(
            translated_content=result["translated_content"],
            target_language=result["target_language"],
            language_name=result["language_name"],
            chapter_id=chapter_id,
            user_id=request.user_id,
            tokens_used=result.get("tokens_used"),
            processing_time_ms=result.get("processing_time_ms"),
            original_length=result.get("original_length"),
            translated_length=result.get("translated_length")
        )

        logger.info(
            f"Translation successful: chapter={chapter_id}, "
            f"language={response.language_name} ({response.target_language}), "
            f"tokens={response.tokens_used}"
        )

        return response

    except HTTPException:
        raise
    except RuntimeError as e:
        logger.error(f"Translation service error: {e}")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Translation service unavailable: {e}"
        )
    except Exception as e:
        logger.error(f"Unexpected error in translate_chapter: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error during translation"
        )


@router.get("/languages")
async def get_supported_languages():
    """
    Get list of supported translation languages.

    Returns:
        Dictionary of supported language codes and their names
    """
    try:
        languages = {
            "ur": {
                "name": "Urdu",
                "native_name": "اردو",
                "rtl": True,
                "primary": True
            },
            "ar": {
                "name": "Arabic",
                "native_name": "العربية",
                "rtl": True,
                "primary": False
            },
            "hi": {
                "name": "Hindi",
                "native_name": "हिन्दी",
                "rtl": False,
                "primary": False
            },
            "es": {
                "name": "Spanish",
                "native_name": "Español",
                "rtl": False,
                "primary": False
            },
            "fr": {
                "name": "French",
                "native_name": "Français",
                "rtl": False,
                "primary": False
            },
            "de": {
                "name": "German",
                "native_name": "Deutsch",
                "rtl": False,
                "primary": False
            },
            "zh": {
                "name": "Chinese",
                "native_name": "中文",
                "rtl": False,
                "primary": False
            },
            "ja": {
                "name": "Japanese",
                "native_name": "日本語",
                "rtl": False,
                "primary": False
            }
        }

        return {
            "supported_languages": languages,
            "total_count": len(languages),
            "primary_language": "ur"
        }

    except Exception as e:
        logger.error(f"Error retrieving languages: {e}")
        raise HTTPException(
            status_code=500,
            detail="Error retrieving supported languages"
        )


@router.get("/health")
async def translation_health():
    """Check translation service health."""
    try:
        # Verify OpenAI client
        openai_ok = translation_service.openai_client is not None

        return {
            "status": "healthy" if openai_ok else "degraded",
            "service": "translation",
            "components": {
                "openai": "ok" if openai_ok else "error"
            },
            "supported_languages": 8
        }
    except Exception as e:
        return {
            "status": "error",
            "service": "translation",
            "error": str(e)
        }
