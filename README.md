<div align="center">

# Physical AI & Humanoid Robotics Textbook

### An AI-Native Interactive Learning Platform

[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen?style=for-the-badge&logo=github)](https://mohammadnoman.github.io/Project-Hackathon-I/)
[![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Docusaurus](https://img.shields.io/badge/Docusaurus-3ECC5F?style=for-the-badge&logo=docusaurus&logoColor=white)](https://docusaurus.io/)
[![Python](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)
[![TypeScript](https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white)](https://www.typescriptlang.org/)

---

**A comprehensive, AI-powered educational platform for learning Physical AI and Humanoid Robotics**

[Explore the Textbook](https://mohammadnoman.github.io/Project-Hackathon-I/) | [View API Docs](http://localhost:8000/docs) | [Report Bug](https://github.com/MohammadNoman/Project-Hackathon-I/issues)

</div>

---

## Overview

This project delivers an **AI-native interactive textbook** covering Physical AI and Humanoid Robotics across 13 comprehensive modules. It features a **RAG-powered chatbot** that answers questions using the textbook content, with support for contextual queries based on selected text.

### Key Features

| Feature | Description |
|---------|-------------|
| **Interactive Textbook** | 13 modules covering ROS2, perception, kinematics, RL, SLAM, ethics & more |
| **AI Chatbot** | RAG-powered assistant using Qdrant vector search + OpenAI |
| **Contextual Queries** | Select text and ask questions about specific content |
| **User Authentication** | JWT-based signup/signin with background questions |
| **Modern UI** | Responsive Docusaurus site with dark/light mode |
| **Session Memory** | Chatbot remembers conversation history |

---

## Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         FRONTEND                                 │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐  │
│  │   Docusaurus    │  │  ChatbotWidget  │  │   AuthForms     │  │
│  │   (13 Modules)  │  │  (React + CSS)  │  │  (JWT Auth)     │  │
│  └────────┬────────┘  └────────┬────────┘  └────────┬────────┘  │
└───────────┼─────────────────────┼─────────────────────┼─────────┘
            │                     │                     │
            ▼                     ▼                     ▼
┌─────────────────────────────────────────────────────────────────┐
│                        FASTAPI BACKEND                           │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐  │
│  │  /api/chatbot   │  │   /api/auth     │  │   RAG Service   │  │
│  │  query endpoint │  │  signup/signin  │  │  (OpenAI+Qdrant)│  │
│  └────────┬────────┘  └────────┬────────┘  └────────┬────────┘  │
└───────────┼─────────────────────┼─────────────────────┼─────────┘
            │                     │                     │
            ▼                     ▼                     ▼
┌─────────────────────────────────────────────────────────────────┐
│                        DATA LAYER                                │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐  │
│  │     Qdrant      │  │  Neon Postgres  │  │   OpenAI API    │  │
│  │  Vector Store   │  │  (User Data)    │  │  (Embeddings)   │  │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Course Modules

| # | Module | Topics |
|---|--------|--------|
| 1 | **ROS2 Nervous System** | Nodes, Topics, Services, Actions, Parameters |
| 2 | **Robot Sensing & Perception** | Cameras, Lidar, IMU, Sensor Fusion |
| 3 | **Kinematics & Dynamics** | Forward/Inverse Kinematics, Dynamics |
| 4 | **Motion Planning & Control** | RRT, PRM, PID, Trajectory Planning |
| 5 | **Robot Learning & Adaptation** | ML for Robotics, Transfer Learning |
| 6 | **Humanoid Design & Locomotion** | Bipedal Walking, Balance Control |
| 7 | **Manipulation & Interaction** | Grasping, Force Control, Dexterity |
| 8 | **Reinforcement Learning** | DRL, Policy Gradients, Sim-to-Real |
| 9 | **SLAM** | Mapping, Localization, Visual SLAM |
| 10 | **Human-Robot Interaction** | HRI Design, Safety, Collaboration |
| 11 | **Ethics & Safety** | Robot Ethics, Safety Standards, LAWS |
| 12 | **Advanced Topics** | Soft Robotics, Swarms, Foundation Models |
| 13 | **Future of Robotics** | Trends, Challenges, Opportunities |

---

## Quick Start

### Prerequisites

- **Node.js** 18+ and npm
- **Python** 3.9+
- **Git**

### 1. Clone the Repository

```bash
git clone https://github.com/MohammadNoman/Project-Hackathon-I.git
cd Project-Hackathon-I
```

### 2. Setup Frontend (Docusaurus)

```bash
cd frontend
npm install
npm start
```

The textbook will be available at `http://localhost:3000`

### 3. Setup Backend (FastAPI)

```bash
cd backend
pip install -r requirements.txt

# Create .env file with your API keys
cp .env.example .env
# Edit .env with your keys:
# - OPENAI_API_KEY
# - QDRANT_HOST
# - QDRANT_API_KEY

# Run the server
uvicorn app.main:app --reload
```

API docs available at `http://localhost:8000/docs`

### 4. Index Content (Optional)

```bash
cd scripts
python index_content.py
```

---

## API Endpoints

### Chatbot API

```http
POST /api/chatbot/query
Content-Type: application/json

{
  "query": "What is ROS2?",
  "selected_text": "optional context from textbook",
  "session_id": "optional-session-id"
}
```

**Response:**
```json
{
  "answer": "ROS2 (Robot Operating System 2) is...",
  "sources": [
    {"file": "module1/index.md", "section": "Introduction", "score": 0.95}
  ],
  "session_id": "uuid-session-id"
}
```

### Authentication API

```http
POST /api/auth/signup
{
  "email": "user@example.com",
  "password": "securepassword",
  "software_background": "intermediate",
  "hardware_background": "beginner"
}

POST /api/auth/signin
{
  "email": "user@example.com",
  "password": "securepassword"
}
```

---

## Tech Stack

### Frontend
- **Docusaurus 3** - Static site generator with MDX support
- **React 18** - UI components (ChatbotWidget, AuthForms)
- **TypeScript** - Type-safe development
- **CSS Modules** - Scoped styling

### Backend
- **FastAPI** - High-performance Python API framework
- **Pydantic** - Data validation and settings
- **OpenAI API** - Embeddings and completions
- **Qdrant** - Vector similarity search
- **JWT** - Token-based authentication
- **bcrypt** - Password hashing

### Infrastructure
- **GitHub Pages** - Frontend hosting
- **GitHub Actions** - CI/CD pipeline
- **Qdrant Cloud** - Managed vector database

---

## Project Structure

```
Project-Hackathon-I/
├── frontend/                 # Docusaurus site
│   ├── docs/                 # 13 course modules
│   │   ├── module1-ros2-nervous-system/
│   │   ├── module2-robot-sensing-and-perception/
│   │   └── ...
│   ├── src/
│   │   ├── components/
│   │   │   ├── ChatbotWidget/   # AI chatbot UI
│   │   │   └── AuthForms/       # Login/signup forms
│   │   └── theme/
│   ├── docusaurus.config.ts
│   └── sidebars.ts
├── backend/                  # FastAPI server
│   ├── app/
│   │   ├── api/
│   │   │   ├── chatbot.py    # RAG query endpoint
│   │   │   └── auth.py       # JWT authentication
│   │   ├── core/
│   │   │   ├── rag.py        # RAG service + sessions
│   │   │   └── config.py     # Settings
│   │   └── models/
│   │       └── schemas.py    # Pydantic models
│   └── requirements.txt
├── scripts/                  # Utility scripts
│   └── index_content.py      # Qdrant indexing
├── specs/                    # Project specifications
└── .github/
    └── workflows/
        └── deploy.yml        # CI/CD pipeline
```

---

## Features Showcase

### RAG Chatbot
The chatbot uses Retrieval-Augmented Generation to answer questions:
1. User query is embedded using OpenAI
2. Similar content is retrieved from Qdrant
3. Context + query sent to LLM for response
4. Sources are cited with relevance scores

### Contextual Queries
Users can:
1. Select text in the textbook
2. Click the chatbot
3. Ask questions with the selection as context
4. Get highly relevant, focused answers

### Session Memory
- Conversations are tracked per session
- Context from previous messages is included
- Sessions persist across page refreshes

---

## Development

### Run Tests
```bash
# Backend tests
cd backend
pytest

# Frontend type checking
cd frontend
npm run typecheck
```

### Build for Production
```bash
# Frontend
cd frontend
npm run build

# The build output is in frontend/build/
```

---

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **Anthropic Claude** - AI-assisted development
- **OpenAI** - Embeddings and language models
- **Qdrant** - Vector search infrastructure
- **Docusaurus** - Documentation framework

---

<div align="center">

**Built with passion for the future of robotics education**

Made by [Mohammad Noman](https://github.com/MohammadNoman)

</div>
