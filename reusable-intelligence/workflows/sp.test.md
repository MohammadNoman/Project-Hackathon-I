---
description: Run end-to-end tests for the full-stack application (frontend + backend + integration)
---

# End-to-End Testing Command

Execute comprehensive testing of the application using the @testing-agent.

## Usage

```
/sp.test [component]
```

**Components:**
- `all` - Run all tests (default)
- `frontend` - Frontend only (build, typecheck)
- `backend` - Backend only (API, database)
- `integration` - Integration tests only
- `quick` - Quick health checks only

## Test Sequence

### 1. Environment Verification
- [ ] Check Node.js version (18+)
- [ ] Check Python version (3.9+)
- [ ] Verify .env files exist
- [ ] Check dependencies installed

### 2. Frontend Tests
- [ ] Run `npm run build` in frontend/
- [ ] Check for build errors
- [ ] Verify all 13 modules render
- [ ] Check chatbot widget loads
- [ ] Verify responsive design

### 3. Backend Tests
- [ ] Start FastAPI server
- [ ] Test `/health` endpoint
- [ ] Test `/api/chatbot/query` endpoint
- [ ] Test `/api/auth/signup` endpoint
- [ ] Test `/api/auth/signin` endpoint
- [ ] Verify Qdrant connection
- [ ] Check CORS headers

### 4. Integration Tests
- [ ] Frontend can reach backend API
- [ ] Chatbot returns responses
- [ ] Auth flow works end-to-end
- [ ] Text selection + chatbot works

## Quick Commands

```powershell
# Frontend build test
cd frontend && npm run build

# Backend start
cd backend && uvicorn app.main:app --reload --port 8000

# API health check
curl http://localhost:8000/health

# Chatbot test
curl -X POST http://localhost:8000/api/chatbot/query -H "Content-Type: application/json" -d "{\"query\": \"What is ROS2?\"}"
```

## Expected Output

Provide a clear test report:
- ✅ Passed tests
- ❌ Failed tests with error + fix
- 📊 Summary statistics

## Delegation

This command delegates to `@testing-agent` for execution. The agent will:
1. Run tests in isolated context (saves tokens)
2. Return summarized results
3. Provide actionable fixes for any failures
