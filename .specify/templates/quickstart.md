# Quickstart Guide: AI-Native Textbook for Physical AI & Humanoid Robotics Course

**Feature**: `001-physical-ai-textbook` | **Date**: 2025-12-02 | **Spec**: [specs/001-physical-ai-textbook/spec.md](specs/001-physical-ai-textbook/spec.md)

## Overview

This guide provides a quick overview and setup instructions to get the AI-Native Textbook project running locally and to interact with its core functionalities.

## Local Development Setup

### Prerequisites

Before you begin, ensure you have the following installed:

*   **Git**
*   **Node.js** (v18 or higher) and **npm**
*   **Python** (3.9 or higher) and **pip**
*   **Docker Desktop** (optional, for local Neon/Qdrant if not using cloud services)
*   **Claude Code CLI** (`npm install -g @anthropic-ai/claude-code-cli`)
*   **Spec-Kit Plus CLI** (`npm install -g spec-kit-plus-cli`)

### 1. Clone the Repository

```bash
git clone <your-repository-url>
cd <your-repository-name>
```

### 2. Frontend (Docusaurus) Setup

Navigate to the Docusaurus project directory (e.g., `001-physical-ai-textbook-docs` if you followed the plan, or your project root if integrated).

```bash
# Assuming Docusaurus is in the root or a subdirectory named '001-physical-ai-textbook-docs'
cd 001-physical-ai-textbook-docs # or your Docusaurus root
npm install
npm start
```

This will start the Docusaurus development server, typically accessible at `http://localhost:3000`.

### 3. Backend (FastAPI) Setup

Navigate to the `backend/` directory.

```bash
cd backend
pip install -r requirements.txt
# Create a .env file based on .env.example and fill in your API keys and database credentials
# Example .env content:
# OPENAI_API_KEY=your_openai_key
# CLAUDE_API_KEY=your_claude_key
# BETTER_AUTH_API_KEY=your_better_auth_key
# NEON_DATABASE_URL=your_neon_postgres_connection_string
# QDRANT_HOST=your_qdrant_host
# QDRANT_API_KEY=your_qdrant_api_key

# Run the FastAPI application
uvicorn app.main:app --reload
```

This will start the FastAPI development server, typically accessible at `http://localhost:8000`.

### 4. Interacting with the RAG Chatbot (Postman/cURL Example)

Once the FastAPI backend is running, you can test the chatbot API.

**Endpoint**: `POST http://localhost:8000/api/chatbot/query`
**Headers**: `Content-Type: application/json`

**Body Example**:

```json
{
  "query_text": "What are the main components of ROS 2?"
}
```

## Deployment

### GitHub Pages (Docusaurus)

Configure your GitHub Actions workflow (e.g., `.github/workflows/deploy.yml`) to build and deploy your Docusaurus site to GitHub Pages on pushes to `main` or `master` branch. Refer to Docusaurus official documentation for detailed steps.

### FastAPI Backend

Deployment strategies for the FastAPI backend depend on your chosen cloud provider (e.g., Vercel, AWS Lambda, Render). Ensure your deployment environment has Python 3.9+, installs `requirements.txt`, and securely configures environment variables.
