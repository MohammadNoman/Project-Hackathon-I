---
description: Deploy FastAPI backend to Render or other cloud platforms
---

# Deploy Backend

Deploy the FastAPI backend application.

## Option 1: Render (Recommended)

### Prerequisites
- GitHub repository connected to Render
- Environment variables configured

### Steps

1. **Create`render.yaml` (if not exists):**

```yaml
services:
  - type: web
    name: physical-ai-textbook-api
    env: python
    buildCommand: "cd backend && pip install -r requirements.txt"
    startCommand: "cd backend && uvicorn app.main:app --host 0.0.0.0 --port $PORT"
    envVars:
      - key: PYTHON_VERSION
        value: 3.11
      - key: DATABASE_URL
        sync: false
      - key: OPENAI_API_KEY
        sync: false
      - key: QDRANT_URL
        sync: false
```

2. **Push to GitHub:**

```bash
git add render.yaml
git commit -m "Add backend deployment config"
git push
```

3. **Deploy on Render:**
- Go to Render Dashboard
- New + → Web Service
- Connect repository
- Render auto-detects configuration
- Add environment variables
- Deploy

## Option 2: Manual uvicorn

```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## Environment Variables

Required:
- `DATABASE_URL` - PostgreSQL connection string
- `OPENAI_API_KEY` - OpenAI API key
- `QDRANT_URL` - Qdrant cloud URL
- `QDRANT_API_KEY` - Qdrant API key

## Verification

After deployment:
- Test `/docs` endpoint (FastAPI Swagger UI)
- Test `/health` endpoint
- Verify database connection
- Test RAG endpoints

## Troubleshooting

**Build fails:** Check Python version (3.11+)
**Database errors:** Verify DATABASE_URL format
**Import errors:** Ensure all dependencies in requirements.txt
