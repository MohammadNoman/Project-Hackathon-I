"""Authentication API endpoints (placeholder for Better Auth integration)."""

from fastapi import APIRouter, HTTPException
import logging

from app.models.schemas import UserCreate, UserLogin, UserResponse, TokenResponse

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/auth", tags=["auth"])


@router.post("/signup", response_model=UserResponse)
async def signup(user: UserCreate):
    """
    Register a new user.

    NOTE: This is a placeholder endpoint. Full implementation will use Better Auth.
    """
    # TODO: Integrate with Better Auth
    raise HTTPException(
        status_code=501,
        detail="Signup not yet implemented. Better Auth integration pending."
    )


@router.post("/signin", response_model=TokenResponse)
async def signin(credentials: UserLogin):
    """
    Authenticate a user and return access token.

    NOTE: This is a placeholder endpoint. Full implementation will use Better Auth.
    """
    # TODO: Integrate with Better Auth
    raise HTTPException(
        status_code=501,
        detail="Signin not yet implemented. Better Auth integration pending."
    )


@router.post("/signout")
async def signout():
    """
    Sign out the current user.

    NOTE: This is a placeholder endpoint. Full implementation will use Better Auth.
    """
    # TODO: Integrate with Better Auth
    raise HTTPException(
        status_code=501,
        detail="Signout not yet implemented. Better Auth integration pending."
    )


@router.get("/me", response_model=UserResponse)
async def get_current_user():
    """
    Get the current authenticated user.

    NOTE: This is a placeholder endpoint. Full implementation will use Better Auth.
    """
    # TODO: Integrate with Better Auth
    raise HTTPException(
        status_code=501,
        detail="Get current user not yet implemented. Better Auth integration pending."
    )


@router.get("/health")
async def auth_health():
    """Check if auth service is healthy."""
    return {"status": "healthy", "service": "auth", "provider": "better-auth-pending"}
