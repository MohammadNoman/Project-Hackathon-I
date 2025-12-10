---
description: Implement RAG chatbot feature using OpenAI Agents SDK
---

Use the `@chatkit-agent` to implement the following chatbot feature:

$ARGUMENTS

The agent will:
1. Follow specs in `specs/001-physical-ai-textbook/contracts/chatbot.yaml`
2. Implement RAG core logic with Qdrant vector search
3. Create `/api/chatbot/query` endpoint with OpenAI integration
4. Support `selected_text` parameter for contextual queries
5. Index book content from Docusaurus docs/

Example usage:
```
/impl-chatbot RAG query endpoint
/impl-chatbot content indexing script
/impl-chatbot selected text support
/impl-chatbot complete chatbot integration
```

This delegates the task to the specialized chatkit-agent with isolated context, saving main conversation tokens.
