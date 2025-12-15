---
description: Initialize environment files from examples
---

# Setup Environment

Initialize `.env` files for backend and frontend from example templates.

## Quick Setup

```bash
# Backend
cp backend/.env.example backend/.env

# Frontend (if exists)
cp frontend/.env.example frontend/.env
```

Then edit the files with your actual values.

## Backend Environment Variables

Edit `backend/.env`:

```bash
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
# Or for Neon: postgresql://user:password@ep-xxx.neon.tech/dbname

# OpenAI
OPENAI_API_KEY=sk-your-key-here

# Qdrant
QDRANT_URL=https://your-cluster.qdrant.io
QDRANT_API_KEY=your-qdrant-key

# Better Auth (optional)
BETTER_AUTH_SECRET=your-secret-key
GOOGLE_CLIENT_ID=your-google-client-id
GOOGLE_CLIENT_SECRET=your-google-client-secret
```

## Frontend Environment Variables

Edit `frontend/.env`:

```bash
REACT_APP_API_URL=http://localhost:8000
REACT_APP_BETTER_AUTH_URL=http://localhost:8000/api/auth
```

## Verification

```bash
# Test backend env
cd backend
python -c "from dotenv import load_dotenv; load_dotenv(); import os; print(os.getenv('DATABASE_URL'))"

# Test frontend env
cd frontend
npm run start # Should load with correct API URL
```

## Security Notes

- Never commit `.env` files to Git
- Use different values for development/production
- Rotate secrets regularly
- Use environment-specific .env files (`.env.local`, `.env.production`)
