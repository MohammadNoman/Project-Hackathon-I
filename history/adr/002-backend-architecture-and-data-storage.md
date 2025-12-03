---
id: 002
title: Backend Architecture and Data Storage
status: Accepted
date: 2025-12-02
context: The project requires a robust backend to power the RAG chatbot, user authentication, content personalization, and Urdu translation. This involves handling API requests, interacting with a database for user data and content metadata, and a vector store for embeddings.
decision: The backend will be implemented using FastAPI for API services. Neon Serverless Postgres will be used for relational data (user profiles, content metadata), and Qdrant Cloud Free Tier for vector embeddings to support RAG.
consequences:
  - Positive: FastAPI provides a high-performance, asynchronous framework suitable for AI services. Neon Serverless Postgres offers a scalable and cost-effective relational database solution. Qdrant Cloud Free Tier provides specialized vector search capabilities, crucial for RAG, without initial cost.
  - Negative: Managing two distinct data storage solutions (relational DB and vector store) adds complexity. The Qdrant Free Tier has resource limitations that need to be considered for scalability. Integration between FastAPI, Neon, and Qdrant requires careful implementation.
alternatives:
  - name: Monolithic application with a single database (e.g., PostgreSQL with pgvector extension)
    consequences: Simpler deployment and data management with a single database. However, pgvector might not offer the same performance or specialized features as Qdrant for advanced vector search, potentially impacting RAG quality. Scalability for vector search might be less efficient.
  - name: Other backend frameworks (e.g., Flask, Django, Node.js with Express)
    consequences: Flask/Django are also viable Python options, but FastAPI offers superior performance for I/O-bound tasks and built-in Pydantic validation, which is beneficial for API development. Node.js would introduce another language stack, increasing complexity for a Python-heavy AI project.
references:
  - specs/001-physical-ai-textbook/plan.md
  - specs/001-physical-ai-textbook/spec.md
  - specs/001-physical-ai-textbook/data-model.md
  - specs/001-physical-ai-textbook/contracts/chatbot.yaml
  - specs/001-physical-ai-textbook/contracts/auth.yaml
  - specs/001-physical-ai-textbook/contracts/personalization.yaml
  - specs/001-physical-ai-textbook/contracts/translation.yaml
---

## Decision: Backend Architecture and Data Storage

The backend of the AI-Native Textbook project will be architected around **FastAPI** to provide high-performance API services for the RAG chatbot, user authentication, content personalization, and Urdu translation. FastAPI's asynchronous capabilities and automatic data validation (via Pydantic) are well-suited for the dynamic and data-intensive nature of these AI-driven features.

For data storage, **Neon Serverless Postgres** has been chosen for all relational data, including user profiles, their software and hardware backgrounds, content metadata, and chatbot interaction logs. Neon provides a scalable, cloud-native PostgreSQL solution that aligns with the project's need for a robust and cost-effective database.

To power the Retrieval-Augmented Generation (RAG) chatbot, **Qdrant Cloud Free Tier** will serve as the dedicated vector store. This decision allows for efficient storage and retrieval of vector embeddings generated from the textbook content, enabling semantic search and contextual answers for user queries. The choice of Qdrant specifically addresses the need for advanced vector search capabilities that are critical for the RAG functionality.

This integrated backend architecture leverages the strengths of each component to meet the project's functional and non-functional requirements, as detailed in `specs/001-physical-ai-textbook/spec.md` and `specs/001-physical-ai-textbook/plan.md`.