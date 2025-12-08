"""Application configuration management using Pydantic Settings."""

from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""

    # Database Configuration
    database_url: str = "postgresql://localhost/physical_ai"

    # Qdrant Configuration
    qdrant_host: str = "localhost"
    qdrant_api_key: Optional[str] = None

    # OpenAI Configuration
    openai_api_key: str = ""

    # Better Auth Configuration
    better_auth_secret: str = "dev-secret-change-in-production"
    better_auth_url: str = "http://localhost:8000"

    # Application Configuration
    environment: str = "development"
    api_port: int = 8000
    frontend_url: str = "http://localhost:3000"

    # Application Metadata
    app_name: str = "Physical AI Textbook API"
    app_version: str = "0.1.0"
    debug: bool = True

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
        extra="ignore"
    )


# Global settings instance
settings = Settings()
