"""Pydantic schemas for API request/response models."""

from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


# Chatbot Schemas
class ChatQueryRequest(BaseModel):
    """Request model for chatbot query endpoint."""
    query: str = Field(..., min_length=1, max_length=2000, description="User's question")
    selected_text: Optional[str] = Field(None, max_length=5000, description="Text selected from textbook")
    top_k: int = Field(5, ge=1, le=20, description="Number of context chunks to retrieve")


class ContextChunk(BaseModel):
    """A single context chunk from vector search."""
    text: str
    file: str
    score: float


class ChatQueryResponse(BaseModel):
    """Response model for chatbot query endpoint."""
    answer: str
    context_chunks: List[ContextChunk]
    query: str


# Auth Schemas (placeholders for Better Auth integration)
class UserCreate(BaseModel):
    """Request model for user signup."""
    email: str = Field(..., description="User email address")
    password: str = Field(..., min_length=8, description="User password")
    name: Optional[str] = Field(None, description="User display name")


class UserLogin(BaseModel):
    """Request model for user login."""
    email: str = Field(..., description="User email address")
    password: str = Field(..., description="User password")


class UserResponse(BaseModel):
    """Response model for user data."""
    id: str
    email: str
    name: Optional[str]
    created_at: datetime


class TokenResponse(BaseModel):
    """Response model for authentication tokens."""
    access_token: str
    token_type: str = "bearer"
    expires_in: int


# Health Check
class HealthCheckResponse(BaseModel):
    """Response model for health check endpoint."""
    status: str
    version: str
    environment: str
