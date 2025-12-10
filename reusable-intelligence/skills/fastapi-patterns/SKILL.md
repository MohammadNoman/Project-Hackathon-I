# FastAPI Patterns Skill

Common FastAPI development patterns, boilerplate, and best practices for rapid backend development.

## Router Endpoint Template

```python
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import schemas

router = APIRouter(prefix="/api/resource", tags=["resource"])

@router.post("/", response_model=schemas.ResourceResponse, status_code=status.HTTP_201_CREATED)
async def create_resource(
    request: schemas.ResourceCreate,
    db: Session = Depends(get_db)
) -> schemas.ResourceResponse:
    """Create a new resource"""
    try:
        # Implementation
        resource = create_resource_in_db(db, request)
        return resource
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
```

## Database Session Pattern

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

## Pydantic Schema Pattern

```python
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class ResourceBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = None

class ResourceCreate(ResourceBase):
    pass

class ResourceResponse(ResourceBase):
    id: int
    created_at: datetime
    
    class Config:
        from_attributes = True
```

## Error Handling Pattern

```python
from fastapi import HTTPException, status

def handle_not_found(resource_type: str, resource_id: int):
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"{resource_type} with id {resource_id} not found"
    )

def handle_validation_error(message: str):
    raise HTTPException(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        detail=message
    )
```

## CORS Configuration

```python
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Frontend URL
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

## Environment Variables Pattern

```python
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str
    OPENAI_API_KEY: str
    QDRANT_HOST: str
    QDRANT_API_KEY: str
    
    class Config:
        env_file = ".env"

settings = Settings()
```

## Use These Patterns

When implementing FastAPI endpoints, use these patterns as templates to maintain consistency and reduce boilerplate.
