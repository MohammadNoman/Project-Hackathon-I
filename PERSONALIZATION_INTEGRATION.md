# Content Personalization Feature - Integration Guide

## Overview

The content personalization feature (T037-T039) enables adaptive learning by tailoring textbook chapters to each user's software and hardware background. The system automatically detects expertise levels (beginner/intermediate/advanced) and uses OpenAI GPT-4 to adapt content presentation while maintaining core concepts.

## Architecture

### Backend Components

#### 1. PersonalizationService (`backend/app/core/personalization.py`)
- **Class**: `PersonalizationService`
- **Methods**:
  - `get_background_level(background: str) -> str`: Detects expertise level from description
  - `create_personalization_prompt(...)`: Builds prompts for GPT-4
  - `personalize_content(...)`: Main method for content adaptation
  - `get_sample_content(chapter_id: str)`: Retrieves chapter content (demo implementation)

#### 2. API Endpoint (`backend/app/api/personalization.py`)
- **Route**: `/api/personalize/{chapter_id}`
- **Method**: POST
- **Request Body**:
```json
{
  "user_id": "optional-user-id",
  "software_background": "Senior Python engineer with 5 years ML experience",
  "hardware_background": "Built Arduino projects, learning robotics"
}
```
- **Response**:
```json
{
  "personalized_content": "Adapted chapter text...",
  "personalization_params": {
    "software_level": "advanced",
    "hardware_level": "intermediate",
    "software_background": "...",
    "hardware_background": "..."
  },
  "chapter_id": "module1",
  "user_id": "optional-user-id",
  "tokens_used": 2547,
  "processing_time_ms": 3421.5
}
```

#### 3. Additional Endpoints
- **GET** `/api/personalize/levels/detect`: Preview expertise level detection
- **GET** `/api/personalize/health`: Service health check

#### 4. Data Models (`backend/app/models/schemas.py`)
- `PersonalizeRequest`: Request validation model
- `PersonalizeResponse`: Response model
- `PersonalizationParams`: Expertise level parameters

### Frontend Component

#### PersonalizeButton (`frontend/src/components/PersonalizeButton/`)

**Features**:
- Futuristic neon cyan design (#00f3ff)
- Modal form for background input
- LocalStorage persistence for user backgrounds
- Result display with expertise level badges
- Responsive design with dark mode support
- Smooth animations and transitions

**Props**:
```typescript
interface PersonalizeButtonProps {
  chapterId: string;                    // Required: Chapter to personalize
  onPersonalized?: (                     // Optional: Callback on success
    content: string,
    params: PersonalizationParams
  ) => void;
  className?: string;                    // Optional: Additional CSS classes
}
```

## Integration Steps

### 1. Backend Setup

The personalization router is already included in `backend/app/main.py`:

```python
from app.api import chatbot, auth, personalization

app.include_router(personalization.router)
```

Ensure OpenAI API key is configured in `.env`:
```
OPENAI_API_KEY=your-openai-api-key-here
```

### 2. Frontend Integration

#### Basic Usage

```tsx
import PersonalizeButton from '@site/src/components/PersonalizeButton';

export default function ChapterPage() {
  const handlePersonalized = (content: string, params: PersonalizationParams) => {
    console.log('Content personalized!', params);
    // Update your chapter display with personalized content
  };

  return (
    <div>
      <h1>Chapter Title</h1>
      <PersonalizeButton
        chapterId="module1"
        onPersonalized={handlePersonalized}
      />
      {/* Chapter content here */}
    </div>
  );
}
```

#### Advanced Usage with State Management

```tsx
import React, { useState } from 'react';
import PersonalizeButton from '@site/src/components/PersonalizeButton';

export default function ChapterPage() {
  const [chapterContent, setChapterContent] = useState(originalContent);
  const [isPersonalized, setIsPersonalized] = useState(false);
  const [expertiseLevels, setExpertiseLevels] = useState(null);

  const handlePersonalized = (content, params) => {
    setChapterContent(content);
    setIsPersonalized(true);
    setExpertiseLevels(params);
  };

  const resetToOriginal = () => {
    setChapterContent(originalContent);
    setIsPersonalized(false);
  };

  return (
    <div>
      <div style={{ display: 'flex', gap: '12px', marginBottom: '20px' }}>
        <PersonalizeButton
          chapterId="module1"
          onPersonalized={handlePersonalized}
        />
        {isPersonalized && (
          <button onClick={resetToOriginal}>
            Reset to Original
          </button>
        )}
      </div>

      {expertiseLevels && (
        <div className="expertise-indicator">
          <span>Software: {expertiseLevels.software_level}</span>
          <span>Hardware: {expertiseLevels.hardware_level}</span>
        </div>
      )}

      <div dangerouslySetInnerHTML={{ __html: chapterContent }} />
    </div>
  );
}
```

#### Integration with Docusaurus MDX

Create a wrapper component in your MDX files:

```mdx
---
title: Introduction to Physical AI
---

import PersonalizeButton from '@site/src/components/PersonalizeButton';

<PersonalizeButton chapterId="module1" />

# Introduction to Physical AI

Your chapter content here...
```

### 3. Testing

#### Backend Testing

```bash
# Navigate to backend directory
cd backend

# Start the server
uvicorn app.main:app --reload

# Test personalization endpoint
curl -X POST http://localhost:8000/api/personalize/module1 \
  -H "Content-Type: application/json" \
  -d '{
    "software_background": "Beginner learning Python",
    "hardware_background": "No robotics experience"
  }'

# Test level detection
curl "http://localhost:8000/api/personalize/levels/detect?software_background=Expert%20in%20Python&hardware_background=Built%20robots"
```

#### Frontend Testing

```bash
# Navigate to frontend directory
cd frontend

# Start Docusaurus dev server
npm start

# Navigate to a page with PersonalizeButton
# Click "Personalize" and test the workflow
```

## Expertise Level Detection

The system uses keyword matching to determine expertise levels:

### Advanced Keywords
- expert, professional, senior, lead, architect
- phd, research, extensive experience
- advanced, master, specialist

### Beginner Keywords
- new, beginner, learning, student
- no experience, starting, basic
- fundamental, introductory

### Default
- If neither advanced nor beginner keywords are found: **intermediate**

## Customization

### 1. Modify Expertise Detection

Edit `backend/app/core/personalization.py`:

```python
def get_background_level(self, background: str) -> str:
    # Add your custom keywords
    advanced_keywords = [...]
    beginner_keywords = [...]
    # Custom logic
```

### 2. Adjust Personalization Prompts

Modify `create_personalization_prompt()` method:

```python
def create_personalization_prompt(self, ...):
    return f"""
    Your custom prompt template here...
    """
```

### 3. Customize UI Theme

Edit `frontend/src/components/PersonalizeButton/styles.module.css`:

```css
.personalizeButton {
  background: linear-gradient(135deg, #your-color 0%, #your-color-2 100%);
  border-color: #your-border-color;
  box-shadow: 0 0 15px rgba(your, colors, here, 0.3);
}
```

### 4. Add Chapter Content Source

Replace `get_sample_content()` with database/CMS integration:

```python
def get_sample_content(self, chapter_id: str) -> str:
    # Fetch from database
    chapter = db.query(Chapter).filter_by(id=chapter_id).first()
    return chapter.content if chapter else "Not found"
```

## Performance Considerations

### Token Usage
- Average: 2,000-3,000 tokens per personalization
- Cost: ~$0.02-$0.04 per request (GPT-4 Turbo)
- Processing time: 2-5 seconds

### Optimization Strategies
1. **Caching**: Cache personalized content per user/chapter/background combination
2. **Background Processing**: Queue personalization requests for async processing
3. **Batch Processing**: Pre-generate personalized versions for common backgrounds
4. **Model Selection**: Use GPT-3.5 for faster/cheaper processing if quality is acceptable

### Implementation Example (Caching)

```python
from functools import lru_cache
import hashlib

class PersonalizationService:
    def __init__(self):
        self.cache = {}

    def _cache_key(self, chapter_id, sw_bg, hw_bg):
        combined = f"{chapter_id}:{sw_bg}:{hw_bg}"
        return hashlib.md5(combined.encode()).hexdigest()

    def personalize_content(self, chapter_content, software_background, hardware_background):
        cache_key = self._cache_key(chapter_id, software_background, hardware_background)

        if cache_key in self.cache:
            logger.info(f"Returning cached personalization: {cache_key}")
            return self.cache[cache_key]

        # Generate personalization
        result = # ... existing logic ...

        # Cache result
        self.cache[cache_key] = result
        return result
```

## Security Considerations

1. **Rate Limiting**: Implement rate limits to prevent API abuse
2. **Input Validation**: Background text is validated (max length in schema)
3. **Authentication**: Optional Bearer token support in endpoint
4. **Content Sanitization**: Ensure personalized content is sanitized before rendering

## Troubleshooting

### Common Issues

**1. "OpenAI API Error"**
- Check `.env` file has valid `OPENAI_API_KEY`
- Verify API key has sufficient credits
- Check OpenAI service status

**2. "Chapter Not Found"**
- Update `get_sample_content()` with your chapter IDs
- Integrate with actual content source (database/CMS)

**3. "CORS Error in Frontend"**
- Verify backend CORS settings in `backend/app/main.py`
- Check `frontend_url` in settings matches your dev server

**4. "Personalization Too Slow"**
- Implement caching (see Performance section)
- Consider using GPT-3.5 instead of GPT-4
- Add loading indicators in UI

## Future Enhancements

1. **User Profiles**: Store backgrounds in database, auto-populate from profile
2. **Learning Path Tracking**: Track how expertise evolves over time
3. **A/B Testing**: Compare personalized vs. original content effectiveness
4. **Multi-language Support**: Personalize and translate simultaneously
5. **Difficulty Slider**: Allow manual adjustment of technical depth
6. **Feedback Loop**: Let users rate personalization quality
7. **Collaborative Filtering**: Suggest backgrounds based on similar users

## API Documentation

Once integrated, view interactive API docs at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## Support

For issues or questions:
1. Check backend logs: `backend/logs/` (if configured)
2. Check browser console for frontend errors
3. Verify all dependencies are installed
4. Ensure OpenAI API key is valid

## Files Modified/Created

### Backend
- ✅ `backend/app/core/personalization.py` (new)
- ✅ `backend/app/api/personalization.py` (new)
- ✅ `backend/app/models/schemas.py` (updated)
- ✅ `backend/app/main.py` (updated)

### Frontend
- ✅ `frontend/src/components/PersonalizeButton/index.tsx` (new)
- ✅ `frontend/src/components/PersonalizeButton/styles.module.css` (new)

### Documentation
- ✅ `PERSONALIZATION_INTEGRATION.md` (this file)
