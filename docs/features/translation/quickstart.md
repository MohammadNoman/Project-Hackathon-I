# Urdu Translation Feature - Quick Start Guide

## 🚀 Quick Setup (5 Minutes)

### Step 1: Backend Setup (2 minutes)

```bash
# 1. Add OpenAI API key to environment
cd backend
echo "OPENAI_API_KEY=your_key_here" >> .env

# 2. Start backend server
python -m uvicorn app.main:app --reload
```

Backend will be available at: http://localhost:8000

### Step 2: Verify Backend (30 seconds)

```bash
# Test translation endpoint
curl -X POST http://localhost:8000/api/translate/module1 \
  -H "Content-Type: application/json" \
  -d '{"target_language": "ur"}'
```

### Step 3: Frontend Setup (2 minutes)

```bash
# 1. Add Urdu font support
cd frontend

# Edit docusaurus.config.js and add to headTags:
# {
#   tagName: 'link',
#   attributes: {
#     rel: 'stylesheet',
#     href: 'https://fonts.googleapis.com/css2?family=Noto+Nastaliq+Urdu:wght@400;700&display=swap',
#   },
# },

# 2. Start frontend
npm start
```

Frontend will be available at: http://localhost:3000

### Step 4: Add Button to Page (30 seconds)

In any `.mdx` or `.tsx` file:

```tsx
import TranslateButton from '@site/src/components/TranslateButton';

<TranslateButton chapterId="module1" />
```

### Step 5: Test Translation (10 seconds)

1. Open page with TranslateButton
2. Click "اردو میں پڑھیں" button
3. See translated content in modal

## ✅ That's It!

Translation feature is now fully functional.

## 📁 Files Created

### Backend
- `backend/app/core/translation.py` (new)
- `backend/app/api/translation.py` (new)
- `backend/app/models/schemas.py` (modified)
- `backend/app/main.py` (modified)

### Frontend
- `frontend/src/components/TranslateButton/index.tsx` (new)
- `frontend/src/components/TranslateButton/styles.module.css` (new)

## 🎨 Button Preview

```
┌─────────────────────────────┐
│  🌐  اردو میں پڑھیں        │  ← Neon purple gradient
└─────────────────────────────┘
```

When clicked → Modal with translated Urdu content (RTL support)

## 🔧 Configuration Options

### Change Target Language

```tsx
<TranslateButton
  chapterId="module1"
  targetLanguage="ar"  // Arabic instead of Urdu
/>
```

### Pass Custom Content

```tsx
<TranslateButton
  chapterId="custom"
  content="Your content here..."
/>
```

### Handle Translation Result

```tsx
<TranslateButton
  chapterId="module1"
  onTranslated={(content, language) => {
    console.log('Translated:', content);
    // Do something with translated content
  }}
/>
```

## 🌐 Supported Languages

- **ur** - Urdu (اردو) ✅ Primary
- **ar** - Arabic (العربية)
- **hi** - Hindi (हिन्दी)
- **es** - Spanish (Español)
- **fr** - French (Français)
- **de** - German (Deutsch)
- **zh** - Chinese (中文)
- **ja** - Japanese (日本語)

## 📊 API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/api/translate/{chapter_id}` | POST | Translate content |
| `/api/translate/languages` | GET | List languages |
| `/api/translate/health` | GET | Health check |

## 💰 Cost Estimate

- ~$0.03-$0.09 per translation (GPT-4 pricing)
- ~2-5 seconds processing time
- ~1000-3000 tokens per chapter

## 🐛 Troubleshooting

### Button not showing
✅ Check import path: `@site/src/components/TranslateButton`

### Urdu text broken
✅ Add font link to `docusaurus.config.js`

### API returns 503
✅ Verify `OPENAI_API_KEY` in `.env`

### Translation takes too long
✅ Normal - GPT-4 takes 2-5 seconds

## 📖 Full Documentation

- **Integration Guide:** `URDU_TRANSLATION_INTEGRATION.md`
- **Feature Summary:** `TRANSLATION_FEATURE_SUMMARY.md`
- **API Docs:** http://localhost:8000/docs

## 🎯 Example Usage

### Basic (Minimal)
```tsx
<TranslateButton chapterId="module1" />
```

### Advanced (With Options)
```tsx
<TranslateButton
  chapterId="module1"
  content={myContent}
  onTranslated={(content) => updatePage(content)}
  className="my-custom-class"
/>
```

### In Docusaurus Page
```mdx
---
title: My Chapter
---

import TranslateButton from '@site/src/components/TranslateButton';

# Chapter Title

<TranslateButton chapterId="my-chapter" />

Your chapter content here...
```

## ✨ Features at a Glance

✅ One-click translation to Urdu
✅ Neon purple futuristic design
✅ RTL (right-to-left) support
✅ Technical terms preserved
✅ Code blocks unchanged
✅ Markdown formatting maintained
✅ Responsive & mobile-friendly
✅ Dark mode support
✅ Loading indicators
✅ Error handling
✅ Translation metadata
✅ 8 languages supported

## 🚀 Production Deployment

### Backend
1. Set `OPENAI_API_KEY` in production environment
2. Enable CORS for production frontend URL
3. Consider adding caching for translations
4. Monitor API costs

### Frontend
1. Update `API_URL` in `index.tsx` to production backend
2. Ensure Urdu font loads in production
3. Test on various devices/browsers
4. Enable analytics for translation usage

## 📝 Notes

- **Translation Quality:** Uses GPT-4 for high accuracy
- **Technical Terms:** Kept in English with Urdu translation
- **Code Blocks:** Always remain in English
- **Right-to-Left:** Automatic for Urdu/Arabic
- **Font:** Noto Nastaliq Urdu (Google Fonts)

## 🆘 Need Help?

1. Check API docs: http://localhost:8000/docs
2. Review full guide: `URDU_TRANSLATION_INTEGRATION.md`
3. Inspect browser console for errors
4. Check backend logs: `backend/logs/`

---

**Ready to translate? Click the purple button and enjoy Urdu content! 🎉**

اردو میں پڑھنے کا مزہ لیں!
