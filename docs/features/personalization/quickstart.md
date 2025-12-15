# Content Personalization - Quick Start Guide

## What Was Built

A complete content personalization system that adapts textbook chapters to each user's software and hardware background using AI (OpenAI GPT-4).

## Key Features

- 🎯 Automatic expertise detection (beginner/intermediate/advanced)
- 🤖 AI-powered content adaptation
- 💾 User background persistence
- 🎨 Futuristic neon cyan UI (#00f3ff)
- 📊 Real-time metrics (tokens used, processing time)
- 🌓 Dark mode support
- 📱 Fully responsive

## Quick Test (5 minutes)

### 1. Start Backend
```bash
cd backend
# Make sure .env has: OPENAI_API_KEY=your-key-here
uvicorn app.main:app --reload
```

### 2. Test API
```bash
curl -X POST http://localhost:8000/api/personalize/module1 \
  -H "Content-Type: application/json" \
  -d '{
    "software_background": "Beginner in Python, no ML experience",
    "hardware_background": "Never worked with robots"
  }'
```

### 3. Start Frontend
```bash
cd frontend
npm start
```

### 4. Add to Page
```tsx
import PersonalizeButton from '@site/src/components/PersonalizeButton';

<PersonalizeButton chapterId="module1" />
```

## Files Created

### Backend (4 files)
```
backend/
├── app/
│   ├── core/
│   │   └── personalization.py          [NEW - 237 lines]
│   ├── api/
│   │   └── personalization.py          [NEW - 165 lines]
│   ├── models/
│   │   └── schemas.py                  [UPDATED - +24 lines]
│   └── main.py                         [UPDATED - +2 lines]
```

### Frontend (2 files)
```
frontend/
└── src/
    └── components/
        └── PersonalizeButton/
            ├── index.tsx               [NEW - 285 lines]
            └── styles.module.css       [NEW - 346 lines]
```

### Documentation (2 files)
```
PERSONALIZATION_INTEGRATION.md          [NEW - 450+ lines]
PERSONALIZATION_QUICKSTART.md           [THIS FILE]
```

## API Endpoints

### Main Endpoint
**POST** `/api/personalize/{chapter_id}`

Request:
```json
{
  "user_id": "optional",
  "software_background": "Your programming experience...",
  "hardware_background": "Your robotics experience..."
}
```

Response:
```json
{
  "personalized_content": "Adapted chapter text...",
  "personalization_params": {
    "software_level": "beginner|intermediate|advanced",
    "hardware_level": "beginner|intermediate|advanced",
    "software_background": "...",
    "hardware_background": "..."
  },
  "tokens_used": 2547,
  "processing_time_ms": 3421.5
}
```

### Helper Endpoints
- **GET** `/api/personalize/levels/detect?software_background=...&hardware_background=...`
- **GET** `/api/personalize/health`

## Component Usage

### Basic
```tsx
<PersonalizeButton chapterId="module1" />
```

### With Callback
```tsx
const handlePersonalized = (content, params) => {
  console.log('SW Level:', params.software_level);
  console.log('HW Level:', params.hardware_level);
  // Update your UI with personalized content
};

<PersonalizeButton
  chapterId="module1"
  onPersonalized={handlePersonalized}
/>
```

### In MDX Files
```mdx
---
title: Chapter 1
---

import PersonalizeButton from '@site/src/components/PersonalizeButton';

<PersonalizeButton chapterId="module1" />

# Chapter 1 Content

Your markdown content here...
```

## Expertise Level Detection

The system automatically detects levels using keywords:

**Advanced**: expert, professional, senior, lead, architect, phd, research, master, specialist

**Beginner**: new, beginner, learning, student, no experience, basic, fundamental

**Intermediate**: Everything else (default)

## Cost & Performance

- **Tokens per request**: 2,000-3,000
- **Cost**: ~$0.02-$0.04 per personalization
- **Processing time**: 2-5 seconds
- **Recommendation**: Implement caching for production

## Sample Chapters Included

- `module1`: Introduction to Physical AI
- `module2`: Sensors and Perception

To add more chapters, edit `get_sample_content()` in `backend/app/core/personalization.py`

## Common Issues

**"OpenAI API Error"**
→ Check `.env` file has valid `OPENAI_API_KEY`

**"CORS Error"**
→ Verify backend CORS settings include your frontend URL

**"Chapter Not Found"**
→ Add your chapter to `get_sample_content()` or integrate with database

## Next Steps

1. **Add Real Content**: Replace `get_sample_content()` with database queries
2. **Add Caching**: Implement Redis/in-memory cache
3. **User Profiles**: Store backgrounds in user profile DB
4. **Analytics**: Track usage and effectiveness

## Full Documentation

See `PERSONALIZATION_INTEGRATION.md` for:
- Detailed architecture
- Customization guide
- Performance optimization
- Security considerations
- Troubleshooting

## Visual Preview

**Button**: Neon cyan gradient with glow effect
**Modal**: Dark overlay with cyan-bordered form
**Results**: Expertise badges (green/yellow/red) with formatted content

---

**Status**: ✅ Complete and Ready for Integration
**Tasks**: T037, T038, T039 (All Complete)
**Agent**: @personalization-agent
