# Quickstart Guide

## Physical AI & Humanoid Robotics Textbook

Get the project running in under 5 minutes!

---

## Prerequisites

| Tool | Version | Download |
|------|---------|----------|
| Node.js | 18+ | [nodejs.org](https://nodejs.org/) |
| Python | 3.9+ | [python.org](https://python.org/) |
| Git | Latest | [git-scm.com](https://git-scm.com/) |

---

## Step 1: Clone & Enter Project

```bash
git clone https://github.com/MohammadNoman/Project-Hackathon-I.git
cd Project-Hackathon-I
```

---

## Step 2: Run Frontend (Textbook)

```bash
cd frontend
npm install
npm start
```

**Open:** http://localhost:3000

You should see the interactive textbook with 13 modules!

---

## Step 3: Run Backend (API)

Open a **new terminal**:

```bash
cd backend
pip install -r requirements.txt
```

### Configure Environment

Create `backend/.env`:

```env
# Required for RAG chatbot
OPENAI_API_KEY=sk-your-openai-key
QDRANT_HOST=your-qdrant-cluster.qdrant.io
QDRANT_API_KEY=your-qdrant-api-key

# Required for auth
BETTER_AUTH_SECRET=your-secret-key-min-32-chars

# Optional
DEBUG=true
ENVIRONMENT=development
```

### Start Server

```bash
uvicorn app.main:app --reload
```

**API Docs:** http://localhost:8000/docs

---

## Step 4: Test the Chatbot

### Option A: Use the UI
1. Go to http://localhost:3000
2. Click the chat button (bottom-right)
3. Ask: "What is ROS2?"

### Option B: Use cURL
```bash
curl -X POST http://localhost:8000/api/chatbot/query \
  -H "Content-Type: application/json" \
  -d '{"query": "What is ROS2?"}'
```

### Option C: Use the API Docs
1. Go to http://localhost:8000/docs
2. Find `POST /api/chatbot/query`
3. Click "Try it out"
4. Enter a query and execute

---

## Step 5: Test Authentication

### Sign Up
```bash
curl -X POST http://localhost:8000/api/auth/signup \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "password123",
    "software_background": "intermediate",
    "hardware_background": "beginner"
  }'
```

### Sign In
```bash
curl -X POST http://localhost:8000/api/auth/signin \
  -H "Content-Type: application/json" \
  -d '{
    "email": "test@example.com",
    "password": "password123"
  }'
```

---

## Project Structure Overview

```
Project-Hackathon-I/
├── frontend/           # Docusaurus textbook
│   ├── docs/           # 13 course modules
│   ├── src/components/ # ChatbotWidget, AuthForms
│   └── package.json
├── backend/            # FastAPI server
│   ├── app/
│   │   ├── api/        # Endpoints (chatbot, auth)
│   │   ├── core/       # RAG service, config
│   │   └── models/     # Pydantic schemas
│   └── requirements.txt
└── scripts/            # Utility scripts
```

---

## Common Issues

### "Module not found" in frontend
```bash
cd frontend
rm -rf node_modules
npm install
```

### "No module named 'app'" in backend
```bash
cd backend
pip install -r requirements.txt
# Make sure you're in the backend directory when running uvicorn
```

### Chatbot returns error
- Check that `OPENAI_API_KEY` is set in `.env`
- Check that Qdrant is accessible
- Run `python scripts/index_content.py` to index content

### Port already in use
```bash
# Frontend (change port)
npm start -- --port 3001

# Backend (change port)
uvicorn app.main:app --reload --port 8001
```

---

## API Quick Reference

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/chatbot/query` | POST | Ask the RAG chatbot |
| `/api/chatbot/health` | GET | Check chatbot service |
| `/api/auth/signup` | POST | Register new user |
| `/api/auth/signin` | POST | Login existing user |
| `/api/auth/me` | GET | Get current user |
| `/health` | GET | Check API health |

---

## Next Steps

1. **Explore the textbook** - Browse all 13 modules
2. **Try the chatbot** - Ask questions about robotics
3. **Select text** - Highlight text and ask contextual questions
4. **Create an account** - Test the authentication flow
5. **Check API docs** - Explore all endpoints at `/docs`

---

## Live Demo

**Textbook:** https://mohammadnoman.github.io/Project-Hackathon-I/

---

## Need Help?

- **Issues:** [GitHub Issues](https://github.com/MohammadNoman/Project-Hackathon-I/issues)
- **Docs:** Check `specs/` folder for detailed specifications

---

Happy Learning!
