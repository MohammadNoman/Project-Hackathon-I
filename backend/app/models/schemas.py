"""Pydantic schemas for API request/response models."""

from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime


# Source Reference for RAG responses
class SourceReference(BaseModel):
    """Source citation for RAG response."""
    file: str = Field(..., description="Source file path")
    section: str = Field(..., description="Section identifier")
    score: float = Field(..., ge=0, le=1, description="Relevance score")
    text_preview: Optional[str] = Field(None, description="Preview of matched text")


# Chatbot Schemas
class ChatQueryRequest(BaseModel):
    """Request model for chatbot query endpoint."""
    query: str = Field(..., min_length=1, max_length=2000, description="User's question")
    selected_text: Optional[str] = Field(None, max_length=5000, description="Text selected from textbook")
    session_id: Optional[str] = Field(None, description="Session ID for conversation continuity")
    top_k: int = Field(5, ge=1, le=20, description="Number of context chunks to retrieve")


class ChatQueryResponse(BaseModel):
    """Response model for chatbot query endpoint."""
    answer: str
    sources: List[SourceReference]
    session_id: str
    tokens_used: Optional[int] = None
    processing_time_ms: Optional[float] = None


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


# Personalization Schemas
class PersonalizeRequest(BaseModel):
    """Request model for content personalization."""
    user_id: Optional[str] = Field(None, description="User ID for personalization tracking")
    software_background: str = Field("", description="User's software/programming background")
    hardware_background: str = Field("", description="User's hardware/robotics background")


class PersonalizationParams(BaseModel):
    """Parameters used for content personalization."""
    software_level: str = Field(..., description="Detected software expertise: beginner/intermediate/advanced")
    hardware_level: str = Field(..., description="Detected hardware expertise: beginner/intermediate/advanced")
    software_background: str = Field(..., description="Original software background description")
    hardware_background: str = Field(..., description="Original hardware background description")


class PersonalizeResponse(BaseModel):
    """Response model for personalized content."""
    personalized_content: str = Field(..., description="Content adapted to user's background")
    personalization_params: PersonalizationParams
    chapter_id: str = Field(..., description="Chapter identifier")
    user_id: Optional[str] = Field(None, description="User ID if provided")
    tokens_used: Optional[int] = Field(None, description="OpenAI tokens consumed")
    processing_time_ms: Optional[float] = Field(None, description="Processing time in milliseconds")


# Translation Schemas
class TranslateRequest(BaseModel):
    """Request model for content translation."""
    target_language: str = Field("ur", description="Target language code (ISO 639-1, default: 'ur' for Urdu)")
    content: Optional[str] = Field(None, description="Optional content to translate (if not provided, fetches chapter)")
    user_id: Optional[str] = Field(None, description="User ID for translation tracking")


class TranslateResponse(BaseModel):
    """Response model for translated content."""
    translated_content: str = Field(..., description="Content translated to target language")
    target_language: str = Field(..., description="Target language code")
    language_name: str = Field(..., description="Full name of target language")
    chapter_id: str = Field(..., description="Chapter identifier")
    user_id: Optional[str] = Field(None, description="User ID if provided")
    tokens_used: Optional[int] = Field(None, description="OpenAI tokens consumed")
    processing_time_ms: Optional[float] = Field(None, description="Processing time in milliseconds")
    original_length: Optional[int] = Field(None, description="Length of original content")
    translated_length: Optional[int] = Field(None, description="Length of translated content")


# Health Check
class HealthCheckResponse(BaseModel):
    """Response model for health check endpoint."""
    status: str
    version: str
    environment: str
