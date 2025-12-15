# Urdu Translation Feature - Integration Guide

## Overview

This document provides complete instructions for integrating the Urdu translation feature (T040-T042) into the Physical AI Textbook application.

## Files Created

### Backend Files

1. **`backend/app/core/translation.py`**
   - TranslationService class with OpenAI GPT-4 integration
   - Supports Urdu and 7 other languages (Arabic, Hindi, Spanish, French, German, Chinese, Japanese)
   - Preserves markdown formatting, code blocks, and technical terms
   - Technical terms remain in English with Urdu translation in parentheses

2. **`backend/app/api/translation.py`**
   - REST API endpoints for translation
   - `POST /api/translate/{chapter_id}` - Main translation endpoint
   - `GET /api/translate/languages` - List supported languages
   - `GET /api/translate/health` - Health check endpoint

### Backend Files Modified

3. **`backend/app/models/schemas.py`**
   - Added `TranslateRequest` schema
   - Added `TranslateResponse` schema
   - Includes metadata: tokens used, processing time, content length

4. **`backend/app/main.py`**
   - Registered translation router
   - Added to CORS configuration

### Frontend Files

5. **`frontend/src/components/TranslateButton/index.tsx`**
   - React component with translation button
   - Modal display for translated content
   - RTL (Right-to-Left) support for Urdu/Arabic
   - Markdown rendering (headings, lists, code blocks)
   - Error handling and loading states

6. **`frontend/src/components/TranslateButton/styles.module.css`**
   - Futuristic neon purple theme (#bc13fe)
   - RTL text styling for Urdu script
   - Custom Urdu font support (Noto Nastaliq Urdu)
   - Responsive design
   - Dark mode support

## Integration Steps

### Step 1: Backend Setup

The backend is already integrated. Ensure OpenAI API key is configured:

```bash
# In backend/.env
OPENAI_API_KEY=your_openai_api_key_here
```

### Step 2: Test Backend Endpoints

Start the backend server:

```bash
cd backend
python -m uvicorn app.main:app --reload
```

Test the translation endpoint:

```bash
# Check health
curl http://localhost:8000/api/translate/health

# Get supported languages
curl http://localhost:8000/api/translate/languages

# Translate a chapter to Urdu
curl -X POST http://localhost:8000/api/translate/module1 \
  -H "Content-Type: application/json" \
  -d '{
    "target_language": "ur",
    "user_id": "test_user"
  }'
```

### Step 3: Frontend Integration

#### Option A: Use in Docusaurus Pages

Add the TranslateButton to any Docusaurus page or MDX file:

```tsx
import TranslateButton from '@site/src/components/TranslateButton';

<TranslateButton
  chapterId="module1"
  onTranslated={(content, language) => {
    console.log('Translated to', language);
  }}
/>
```

#### Option B: Use in React Components

```tsx
import TranslateButton from '../components/TranslateButton';

function MyComponent() {
  return (
    <div>
      <h1>Chapter Title</h1>
      <TranslateButton
        chapterId="module1"
        content={chapterContent} // Optional: pass content directly
      />
      {/* Rest of your content */}
    </div>
  );
}
```

#### Option C: Add to All Chapter Pages

Edit your Docusaurus theme or create a wrapper component:

```tsx
// src/theme/DocItem/index.tsx
import React from 'react';
import DocItem from '@theme-original/DocItem';
import TranslateButton from '@site/src/components/TranslateButton';

export default function DocItemWrapper(props) {
  return (
    <>
      <div style={{ float: 'right', margin: '10px' }}>
        <TranslateButton chapterId={props.content.metadata.id} />
      </div>
      <DocItem {...props} />
    </>
  );
}
```

### Step 4: Add Urdu Font Support

Add Urdu font to your HTML head (in `docusaurus.config.js`):

```javascript
module.exports = {
  // ... other config
  headTags: [
    {
      tagName: 'link',
      attributes: {
        rel: 'preconnect',
        href: 'https://fonts.googleapis.com',
      },
    },
    {
      tagName: 'link',
      attributes: {
        rel: 'preconnect',
        href: 'https://fonts.gstatic.com',
        crossorigin: 'anonymous',
      },
    },
    {
      tagName: 'link',
      attributes: {
        rel: 'stylesheet',
        href: 'https://fonts.googleapis.com/css2?family=Noto+Nastaliq+Urdu:wght@400;700&display=swap',
      },
    },
  ],
};
```

Or add to `frontend/src/css/custom.css`:

```css
@import url('https://fonts.googleapis.com/css2?family=Noto+Nastaliq+Urdu:wght@400;700&display=swap');
```

## API Documentation

### POST /api/translate/{chapter_id}

Translate chapter content to target language.

**Request Body:**
```json
{
  "target_language": "ur",        // ISO 639-1 code (default: "ur")
  "content": "optional content",   // Optional: provide content directly
  "user_id": "optional_user_id"   // Optional: for tracking
}
```

**Response:**
```json
{
  "translated_content": "... translated text ...",
  "target_language": "ur",
  "language_name": "Urdu",
  "chapter_id": "module1",
  "user_id": "user123",
  "tokens_used": 1234,
  "processing_time_ms": 2500,
  "original_length": 1000,
  "translated_length": 1200
}
```

**Supported Languages:**
- `ur` - Urdu (اردو) - Primary, RTL
- `ar` - Arabic (العربية) - RTL
- `hi` - Hindi (हिन्दी)
- `es` - Spanish (Español)
- `fr` - French (Français)
- `de` - German (Deutsch)
- `zh` - Chinese (中文)
- `ja` - Japanese (日本語)

### GET /api/translate/languages

Get list of all supported languages with metadata.

**Response:**
```json
{
  "supported_languages": {
    "ur": {
      "name": "Urdu",
      "native_name": "اردو",
      "rtl": true,
      "primary": true
    },
    // ... other languages
  },
  "total_count": 8,
  "primary_language": "ur"
}
```

### GET /api/translate/health

Health check for translation service.

## Features

### Backend Features

1. **Smart Translation:**
   - Preserves technical terms in English
   - Adds translations in parentheses on first occurrence
   - Maintains code blocks in original form
   - Translates code comments only

2. **Markdown Support:**
   - Preserves all markdown formatting
   - Maintains headings, lists, bold, italic
   - Keeps code fences and syntax highlighting

3. **Multi-language:**
   - Supports 8 languages
   - Automatic RTL detection
   - Language-specific formatting

### Frontend Features

1. **Button Design:**
   - Futuristic neon purple gradient (#bc13fe)
   - Urdu text: "اردو میں پڑھیں" (Read in Urdu)
   - Hover effects and animations
   - Loading state

2. **Translation Display:**
   - Modal popup with translated content
   - RTL text support for Urdu/Arabic
   - Proper Urdu font (Noto Nastaliq Urdu)
   - Markdown rendering (headings, lists, code)

3. **User Experience:**
   - Error handling with toast notifications
   - Loading indicators
   - Translation metadata display
   - Processing time and token usage

## Usage Examples

### Example 1: Basic Usage

```tsx
<TranslateButton chapterId="module1" />
```

### Example 2: With Callback

```tsx
<TranslateButton
  chapterId="module2"
  onTranslated={(translatedContent, language) => {
    // Replace page content with translation
    document.getElementById('content').innerHTML = translatedContent;
  }}
/>
```

### Example 3: With Custom Content

```tsx
const customContent = `
# My Custom Chapter
This is some content to translate...
`;

<TranslateButton
  chapterId="custom"
  content={customContent}
/>
```

### Example 4: Multiple Buttons

```tsx
<div>
  <TranslateButton chapterId="module1" className="btn-primary" />
  <TranslateButton chapterId="module2" className="btn-secondary" />
</div>
```

## Styling Customization

### Change Button Color

Edit `styles.module.css`:

```css
.translateButton {
  background: linear-gradient(135deg, #YOUR_COLOR_1 0%, #YOUR_COLOR_2 100%);
  border: 2px solid #YOUR_COLOR_1;
  box-shadow: 0 0 15px rgba(YOUR_RGB, 0.4);
}
```

### Change Urdu Font

Update font-family in `styles.module.css`:

```css
.urduText {
  font-family: 'Your Preferred Urdu Font', 'Noto Nastaliq Urdu', serif;
}
```

### Adjust RTL Spacing

```css
.rtlText .heading1,
.rtlText .heading2,
.rtlText .paragraph {
  line-height: 2.5; /* Increase for more spacing */
}
```

## Testing

### Test Backend

```bash
# Run backend tests
cd backend
pytest tests/test_translation.py -v
```

### Test Frontend

```bash
# Run frontend in development
cd frontend
npm start

# Navigate to a page with TranslateButton
# Click the button and verify translation works
```

### Manual Testing Checklist

- [ ] Backend health check returns "healthy"
- [ ] Translation API returns translated content
- [ ] Urdu text displays correctly (RTL, proper font)
- [ ] Code blocks remain in English
- [ ] Technical terms preserved
- [ ] Modal opens and closes properly
- [ ] Loading state shows during translation
- [ ] Error handling works for invalid requests
- [ ] Responsive design works on mobile
- [ ] Dark mode styling is correct

## Troubleshooting

### Issue: Urdu text not displaying correctly

**Solution:** Ensure Urdu font is loaded:
1. Check browser console for font loading errors
2. Verify Google Fonts link in HTML head
3. Test with `font-family: 'Noto Nastaliq Urdu'` in browser DevTools

### Issue: Translation takes too long

**Solution:** Translation uses GPT-4 which can take 2-5 seconds:
1. This is normal for quality translations
2. Loading indicator keeps user informed
3. Consider caching translations in production

### Issue: RTL text alignment issues

**Solution:**
1. Verify `direction: rtl` is applied
2. Check `text-align: right` is set
3. Use browser DevTools to inspect computed styles

### Issue: API returns 503 Service Unavailable

**Solution:**
1. Check OpenAI API key is valid
2. Verify backend server is running
3. Check backend logs for detailed error
4. Test OpenAI API separately

## Production Considerations

### 1. Caching

Implement caching to avoid re-translating:

```python
# In translation.py
from functools import lru_cache

@lru_cache(maxsize=1000)
def translate_content_cached(content_hash, target_language):
    # Translation logic
    pass
```

### 2. Database Storage

Store translations in database:

```sql
CREATE TABLE translations (
    id UUID PRIMARY KEY,
    chapter_id VARCHAR,
    target_language VARCHAR(2),
    translated_content TEXT,
    created_at TIMESTAMP,
    tokens_used INTEGER
);
```

### 3. Rate Limiting

Add rate limiting to prevent abuse:

```python
from fastapi_limiter import FastAPILimiter

@router.post("/{chapter_id}")
@limiter.limit("5/minute")
async def translate_chapter(...):
    # Translation logic
    pass
```

### 4. Cost Monitoring

Monitor OpenAI API costs:

```python
# Log token usage
logger.info(f"Translation cost estimate: ${tokens_used * 0.00003:.4f}")
```

### 5. Content Security

Sanitize user-provided content:

```python
import bleach

content = bleach.clean(request.content, strip=True)
```

## Future Enhancements

1. **Offline Translation:** Use local models for common phrases
2. **Translation Memory:** Reuse previous translations
3. **User Preferences:** Save preferred language per user
4. **Batch Translation:** Translate multiple chapters at once
5. **Export:** Download translated content as PDF/DOCX
6. **Glossary:** Custom technical term translations
7. **Voice Reading:** Text-to-speech for Urdu content

## Support

For issues or questions:
- Backend issues: Check logs in `backend/logs/`
- Frontend issues: Open browser console
- API documentation: http://localhost:8000/docs
- GitHub Issues: [Create an issue](your-repo-url/issues)

## License

Same as parent project license.
