"""Personalization API endpoints for adaptive content delivery."""

import logging
from typing import Optional

from fastapi import APIRouter, HTTPException, status, Header

from app.models.schemas import (
    PersonalizeRequest,
    PersonalizeResponse,
    PersonalizationParams
)
from app.core.personalization import personalization_service

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/personalize", tags=["personalization"])


@router.post("/{chapter_id}", response_model=PersonalizeResponse)
async def personalize_chapter(
    chapter_id: str,
    request: PersonalizeRequest,
    authorization: Optional[str] = Header(None)
):
    """
    Personalize chapter content based on user's background.

    This endpoint adapts educational content to match the user's expertise level
    in both software and hardware domains.

    Features:
    - Automatic expertise level detection (beginner/intermediate/advanced)
    - Content adaptation using OpenAI GPT-4
    - Maintains core concepts while adjusting presentation style
    - Returns personalization parameters for transparency

    Args:
        chapter_id: Identifier for the chapter to personalize
        request: PersonalizeRequest containing user background
        authorization: Optional Bearer token for authenticated users

    Returns:
        PersonalizeResponse with adapted content and metadata
    """
    try:
        logger.info(
            f"Personalization request: chapter={chapter_id}, "
            f"user_id={request.user_id or 'anonymous'}"
        )

        # Validate inputs
        if not request.software_background and not request.hardware_background:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="At least one background field (software or hardware) must be provided"
            )

        # Get chapter content (in production, fetch from database/CMS)
        chapter_content = personalization_service.get_sample_content(chapter_id)

        if "Chapter Not Found" in chapter_content:
            logger.warning(f"Chapter not found: {chapter_id}")
            # Still personalize the placeholder for demo purposes
            # In production, raise 404

        # Personalize content
        result = personalization_service.personalize_content(
            chapter_content=chapter_content,
            software_background=request.software_background,
            hardware_background=request.hardware_background
        )

        # Build response
        response = PersonalizeResponse(
            personalized_content=result["personalized_content"],
            personalization_params=PersonalizationParams(
                software_level=result["personalization_params"]["software_level"],
                hardware_level=result["personalization_params"]["hardware_level"],
                software_background=result["personalization_params"]["software_background"],
                hardware_background=result["personalization_params"]["hardware_background"]
            ),
            chapter_id=chapter_id,
            user_id=request.user_id,
            tokens_used=result.get("tokens_used"),
            processing_time_ms=result.get("processing_time_ms")
        )

        logger.info(
            f"Personalization successful: chapter={chapter_id}, "
            f"SW={response.personalization_params.software_level}, "
            f"HW={response.personalization_params.hardware_level}"
        )

        return response

    except HTTPException:
        raise
    except RuntimeError as e:
        logger.error(f"Personalization service error: {e}")
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Personalization service unavailable: {e}"
        )
    except Exception as e:
        logger.error(f"Unexpected error in personalize_chapter: {e}", exc_info=True)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error during personalization"
        )


@router.get("/levels/detect")
async def detect_background_levels(
    software_background: str = "",
    hardware_background: str = ""
):
    """
    Detect expertise levels without personalizing content.

    Useful for UI previews or user profile setup.

    Args:
        software_background: User's software background description
        hardware_background: User's hardware background description

    Returns:
        Detected expertise levels for both domains
    """
    try:
        software_level = (
            personalization_service.get_background_level(software_background)
            if software_background else "not_specified"
        )
        hardware_level = (
            personalization_service.get_background_level(hardware_background)
            if hardware_background else "not_specified"
        )

        return {
            "software_level": software_level,
            "hardware_level": hardware_level,
            "software_background": software_background,
            "hardware_background": hardware_background
        }
    except Exception as e:
        logger.error(f"Error detecting levels: {e}")
        raise HTTPException(status_code=500, detail="Error detecting expertise levels")


@router.get("/health")
async def personalization_health():
    """Check personalization service health."""
    try:
        # Verify OpenAI client
        openai_ok = personalization_service.openai_client is not None

        return {
            "status": "healthy" if openai_ok else "degraded",
            "service": "personalization",
            "components": {
                "openai": "ok" if openai_ok else "error"
            }
        }
    except Exception as e:
        return {
            "status": "error",
            "service": "personalization",
            "error": str(e)
        }
