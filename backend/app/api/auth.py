"""Authentication API endpoints using JWT tokens."""

import os
import logging
from datetime import datetime, timedelta
from typing import Optional

from fastapi import APIRouter, HTTPException, status, Depends
from pydantic import BaseModel, EmailStr, validator
from passlib.context import CryptContext
import jwt

from app.core.config import settings

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/api/auth", tags=["auth"])

# Configuration
SECRET_KEY = settings.better_auth_secret
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24  # 24 hours

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# In-memory user store (replace with database in production)
users_db = {}


# Request/Response Models
class SignupRequest(BaseModel):
    email: EmailStr
    password: str
    software_background: str = ""
    hardware_background: str = ""

    @validator('password')
    def password_strength(cls, v):
        if len(v) < 8:
            raise ValueError('Password must be at least 8 characters')
        return v


class SigninRequest(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: str
    email: str
    software_background: str
    hardware_background: str
    created_at: datetime


class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"
    user: UserResponse


# Helper Functions
def hash_password(password: str) -> str:
    return pwd_context.hash(password)


def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


@router.post("/signup", response_model=TokenResponse, status_code=status.HTTP_201_CREATED)
async def signup(request: SignupRequest):
    """Register a new user."""
    logger.info(f"Signup attempt for: {request.email}")

    # Check if user exists
    if request.email in users_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    # Create user
    user_id = str(len(users_db) + 1)
    hashed_password = hash_password(request.password)
    created_at = datetime.utcnow()

    users_db[request.email] = {
        "id": user_id,
        "email": request.email,
        "hashed_password": hashed_password,
        "software_background": request.software_background,
        "hardware_background": request.hardware_background,
        "created_at": created_at
    }

    # Create token
    access_token = create_access_token(data={"sub": request.email, "user_id": user_id})

    user_response = UserResponse(
        id=user_id,
        email=request.email,
        software_background=request.software_background,
        hardware_background=request.hardware_background,
        created_at=created_at
    )

    logger.info(f"User created: {request.email}")

    return TokenResponse(
        access_token=access_token,
        token_type="bearer",
        user=user_response
    )


@router.post("/signin", response_model=TokenResponse)
async def signin(request: SigninRequest):
    """Authenticate existing user."""
    logger.info(f"Signin attempt for: {request.email}")

    # Find user
    user = users_db.get(request.email)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    # Verify password
    if not verify_password(request.password, user["hashed_password"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password"
        )

    # Create token
    access_token = create_access_token(data={"sub": user["email"], "user_id": user["id"]})

    user_response = UserResponse(
        id=user["id"],
        email=user["email"],
        software_background=user["software_background"],
        hardware_background=user["hardware_background"],
        created_at=user["created_at"]
    )

    logger.info(f"User signed in: {request.email}")

    return TokenResponse(
        access_token=access_token,
        token_type="bearer",
        user=user_response
    )


@router.get("/me", response_model=UserResponse)
async def get_current_user(token: str):
    """Get current user from token."""
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if not email:
            raise HTTPException(status_code=401, detail="Invalid token")

        user = users_db.get(email)
        if not user:
            raise HTTPException(status_code=401, detail="User not found")

        return UserResponse(
            id=user["id"],
            email=user["email"],
            software_background=user["software_background"],
            hardware_background=user["hardware_background"],
            created_at=user["created_at"]
        )
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")


@router.get("/health")
async def auth_health():
    """Check auth service health."""
    return {"status": "healthy", "service": "auth", "users_count": len(users_db)}
