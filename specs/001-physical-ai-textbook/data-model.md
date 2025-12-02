# Data Model: AI-Native Textbook for Physical AI & Humanoid Robotics Course

**Feature**: `001-physical-ai-textbook` | **Date**: 2025-12-02 | **Spec**: [specs/001-physical-ai-textbook/spec.md](specs/001-physical-ai-textbook/spec.md)
**Input**: Feature specification from `/specs/001-physical-ai-textbook/spec.md`

## 1. Entities and Attributes

### User
*   **id**: Unique identifier (UUID or similar)
*   **email**: User's email address (string, unique)
*   **password**: Hashed password (handled by `better-auth.com`)
*   **software_background**: User's software expertise/experience (JSON or text, e.g., `{"languages": ["Python", "JavaScript"], "frameworks": ["React", "ROS 2"]}`)
*   **hardware_background**: User's hardware familiarity (JSON or text, e.g., `{"robot_platforms": ["Unitree Go2", "Jetson Orin"], "sensors": ["Intel RealSense"]}`)
*   **preferences**: User-specific settings (JSON, e.g., `{"default_language": "en", "personalization_level": "intermediate"}`)

### Book Content
*   **chapter_id**: Unique identifier for each chapter/section (string)
*   **text_content_en**: Original English text content of the chapter (string)
*   **text_content_ur**: Urdu translated text content of the chapter (string, nullable)
*   **embeddings**: Vector embeddings of the `text_content_en` for RAG (array of floats, stored in Qdrant)
*   **metadata**: Additional chapter metadata (JSON, e.g., `{"module": "Module 1", "week": "Week 1-2", "title": "Intro to Physical AI"}`)

### Personalized Content
*   **user_id**: Foreign key referencing User.id
*   **chapter_id**: Foreign key referencing Book Content.chapter_id
*   **personalized_text**: Personalized version of the chapter content for a specific user (string)
*   **personalization_params**: Parameters used for personalization (JSON, e.g., `{"target_level": "advanced", "focus_area": "ROS 2"}`)

### Chatbot Interaction
*   **session_id**: Unique identifier for a chat session (UUID)
*   **user_id**: Foreign key referencing User.id (nullable, for unauthenticated users)
*   **query_text**: User's question to the chatbot (string)
*   **response_text**: Chatbot's generated answer (string)
*   **timestamp**: Timestamp of the interaction (datetime)
*   **selected_text_context**: User-selected text used as additional context for the query (string, nullable)

## 2. Relationships

*   **User to Personalized Content**: One-to-many (`User` can have many `Personalized Content` entries, `Personalized Content` belongs to one `User`)
*   **Book Content to Personalized Content**: One-to-many (`Book Content` can have many `Personalized Content` entries, `Personalized Content` belongs to one `Book Content`)
*   **User to Chatbot Interaction**: One-to-many (`User` can have many `Chatbot Interaction` entries, `Chatbot Interaction` belongs to one `User` if authenticated)
*   **Book Content Embeddings**: `Book Content` entries will have their `text_content_en` processed into vector `embeddings` and stored in Qdrant, with a reference (e.g., `chapter_id`) to link back to the original content.
