# AI-Native Textbook for Physical AI & Humanoid Robotics Course

## 1. Feature Description

This project aims to create an "AI-Native Textbook for Teaching Physical AI & Humanoid Robotics Course" for a hackathon. The textbook will be built using Docusaurus and deployed to GitHub Pages. It will feature an integrated Retrieval-Augmented Generation (RAG) chatbot for answering questions based on the book's content, including user-selected text. The project also includes several bonus features: reusable intelligence via Claude Code Subagents and Agent Skills, user signup/signin with content personalization based on user background, and Urdu translation for chapters.

## 2. User Scenarios & Testing

### User Scenarios

1.  **Student (Unauthenticated):** Accesses the Docusaurus textbook on GitHub Pages, reads content, and uses the RAG chatbot to ask questions about the book.
2.  **Student (Authenticated):** Signs in via `better-auth.com`, answers background questions, accesses personalized content, and uses the RAG chatbot. They can also translate content to Urdu.
3.  **Author/Admin:** Uses Spec-Kit Plus and Claude Code to create and update book content.
4.  **Judge:** Reviews the published book, tests the RAG chatbot and bonus features, and evaluates the demo video.

### Testing Scenarios (examples for key features)

*   **Book Display:** Verify Docusaurus renders correctly on GitHub Pages across different devices.
*   **RAG Chatbot:**
    *   Ask questions directly covered in the book content.
    *   Ask questions about specific text sections selected by the user.
    *   Test chatbot responses for accuracy and relevance.
    *   Verify the chatbot handles out-of-scope questions gracefully.
*   **Authentication:**
    *   Test user registration and login via `better-auth.com`.
    *   Verify user background questions are collected at signup.
*   **Content Personalization:**
    *   Verify content changes based on authenticated user's background (e.g., beginner vs. advanced).
    *   Test button functionality at the start of chapters for personalization.
*   **Urdu Translation:**
    *   Verify chapter content translates accurately to Urdu.
    *   Test button functionality for translation at the start of chapters.
*   **Agent Skills/Subagents:** Demonstrate usage of Claude Code Subagents/Agent Skills for content creation/management.

## 3. Functional Requirements

### Core Functionality (100 points)

1.  **AI/Spec-Driven Book Creation:**
    *   The textbook content for "Physical AI & Humanoid Robotics" course must be created using Docusaurus.
    *   The content creation process must leverage Spec-Kit Plus and Claude Code for AI/spec-driven development.
    *   The Docusaurus book must be deployable and accessible via GitHub Pages.
2.  **Integrated RAG Chatbot Development:**
    *   A RAG chatbot must be embedded within the published Docusaurus book.
    *   The chatbot must utilize OpenAI Agents/ChatKit SDKs, FastAPI for its backend API, Neon Serverless Postgres for data storage, and Qdrant Cloud Free Tier for vector search.
    *   The chatbot must accurately answer user questions about the book's content.
    *   The chatbot must be able to answer questions based on specific text selections made by the user within the book.

### Bonus Functionality

1.  **Reusable Intelligence (50 points):**
    *   The project must demonstrate the creation and use of reusable intelligence via Claude Code Subagents and Agent Skills within the book project's development workflow (e.g., for content generation, review, or management).
2.  **Signup/Signin (50 points):**
    *   User authentication (signup and signin) must be implemented using `better-auth.com`.
    *   During the signup process, the system must collect information about the user's software and hardware background.
3.  **Content Personalization (50 points):**
    *   Logged-in users must be able to personalize chapter content based on their previously provided software and hardware background.
    *   A UI element (button) must be present at the start of each chapter to trigger personalization.
4.  **Urdu Translation (50 points):**
    *   Logged-in users must be able to translate chapter content into Urdu.
    *   A UI element (button) must be present at the start of each chapter to trigger translation.

## 4. Non-Functional Requirements (NFRs)

1.  **Performance:**
    *   Book loading times should be fast (e.g., under 2 seconds for initial load).
    *   RAG chatbot response times should be efficient (e.g., under 5 seconds for most queries).
    *   Authentication and personalization operations should be responsive.
2.  **Reliability & Availability:**
    *   GitHub Pages hosting provides high availability for the book.
    *   RAG chatbot backend (FastAPI, Neon, Qdrant) should be robust and handle expected load.
3.  **Security:**
    *   `better-auth.com` integration must follow best practices for secure authentication.
    *   API endpoints (FastAPI) should be secure against common web vulnerabilities.
    *   User background data must be stored and handled securely.
4.  **Maintainability:**
    *   Codebase should be clean, well-structured, and documented (especially for hackathon judges).
    *   Docusaurus content should be easy to update and extend.
5.  **Scalability:**
    *   Neon Serverless Postgres and Qdrant Cloud Free Tier should handle initial user loads. Design should consider future scaling if project were to expand beyond hackathon scope.
6.  **Usability:**
    *   The book interface should be intuitive and easy to navigate.
    *   The RAG chatbot interface should be user-friendly.
    *   Personalization and translation features should be easily discoverable and usable.

## 5. Key Entities

*   **User:**
    *   `id` (unique identifier)
    *   `email`
    *   `password` (handled by `better-auth.com`)
    *   `software_background` (text/JSON, collected at signup)
    *   `hardware_background` (text/JSON, collected at signup)
    *   `preferences` (e.g., `default_language`, `personalization_level`)
*   **Book Content:**
    *   `chapter_id`
    *   `text_content` (original English)
    *   `personalized_content` (per user/preference)
    *   `urdu_content` (translated version)
    *   `embeddings` (vector representations for RAG)
*   **Chatbot Interaction:**
    *   `session_id`
    *   `user_query`
    *   `chatbot_response`
    *   `timestamp`
    *   `selected_text` (if applicable)

## 6. Constraints & Tradeoffs

1.  **Strict Deadline:** Sunday, Nov 30, 2025, 06:00 PM. Prioritization of core features and high-value bonuses is critical.
2.  **Mandatory Tech Stack:** Docusaurus, GitHub Pages, Spec-Kit Plus, Claude Code, OpenAI Agents/ChatKit SDKs, FastAPI, Neon Serverless Postgres, Qdrant Cloud Free Tier, `better-auth.com`. No substitutions allowed.
3.  **Demo Video Length:** Under 90 seconds. Requires careful planning for showcasing key features concisely.
4.  **Functional Specificity:** RAG chatbot must handle general questions AND selected text. Bonus features have clear requirements.
5.  **Quality & Accuracy:** Content, especially for a textbook, must be accurate and well-explained, consistent with course technical demands. This may require iterative review and refinement.
6.  **Qdrant Free Tier:** Resource limitations of the free tier must be considered in design (e.g., indexing strategy, data volume).

## 7. Success Criteria

1.  The Docusaurus book for "Physical AI & Humanoid Robotics" is publicly accessible on GitHub Pages by the deadline.
2.  The integrated RAG chatbot accurately answers at least 90% of factual questions related to the book content and selected text.
3.  The `better-auth.com` signup/signin system is fully functional, collecting user background information.
4.  Chapter-level content personalization is demonstrated for logged-in users based on their background.
5.  Chapter-level Urdu translation is demonstrated for logged-in users.
6.  Reusable intelligence via Claude Code Subagents/Agent Skills is demonstrably integrated into the content creation workflow.
7.  The demo video effectively showcases core and bonus features within 90 seconds.
8.  The textbook content demonstrates high educational clarity and technical accuracy for all modules.
9.  The overall project demonstrates an innovative and visionary approach to "AI-native textbooks."

## 8. Assumptions

1.  Existing Docusaurus project structure can be adapted or a new one created.
2.  OpenAI Agents/ChatKit SDKs can be seamlessly integrated with FastAPI and Qdrant.
3.  `better-auth.com` provides clear APIs and documentation for signup/signin and user profile management.
4.  APIs for content personalization (e.g., rewriting text based on background) and translation (e.g., Google Translate API or similar) can be integrated into the FastAPI backend.
5.  Sufficient time and resources within the hackathon timeline to implement all core and high-value bonus features.
6.  Claude Code Subagents and Agent Skills are sufficiently documented and flexible to be applied for "reusable intelligence" in content creation.
