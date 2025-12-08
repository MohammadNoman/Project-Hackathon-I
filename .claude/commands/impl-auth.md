---
description: Implement authentication feature using Better Auth
---

Use the `@better-auth-agent` to implement the following authentication feature:

$ARGUMENTS

The agent will:
1. Follow specs in `specs/001-physical-ai-textbook/contracts/auth.yaml`
2. Implement FastAPI endpoints (`/api/auth/signup`, `/api/auth/signin`)
3. Create frontend auth forms (React/Docusaurus)
4. Store user profiles with software/hardware background in Neon Postgres

Example usage:
```
/impl-auth signup endpoint with background questions
/impl-auth signin with JWT token response
/impl-auth complete authentication flow
```

This delegates the task to the specialized better-auth-agent with isolated context, saving main conversation tokens.
