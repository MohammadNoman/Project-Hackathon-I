---
description: Auto-detect when to delegate tasks to specialized agents
---

# Auto-Delegate

This command helps Claude determine when and how to delegate tasks to specialized agents (Gemini/Qwen) to save tokens and context.

## How It Works

Claude will use this workflow to decide on delegation:

### Step 1: Task Analysis

Analyze the user's request for keywords and complexity:

**Authentication/Auth Tasks** → Delegate to `@better-auth-agent`
- Keywords: `signup`, `signin`, `login`, `auth`, `JWT`, `session`, `better-auth`, `OAuth`
- Skills: `better-auth-patterns`, `fastapi-patterns`

**RAG/Chatbot Tasks** → Delegate to `@chatkit-agent`
- Keywords: `RAG`, `chatbot`, `embedding`, `Qdrant`, `vector`, `search`, `OpenAI`
- Skills: `fastapi-patterns`

**Frontend/UI Tasks** → Delegate to `@nextjs-agent`
- Keywords: `React`, `component`, `UI`, `frontend`, `Docusaurus`, `design`, `styling`
- Skills: `visual-excellence`, `docusaurus-patterns`

**Content/Documentation Tasks** → Delegate to `@content-agent`
- Keywords: `content`, `documentation`, `write`, `docs`, `tutorial`, `guide`
- Skills: None typically

**Testing Tasks** → Delegate to `@testing-agent`
- Keywords: `test`, `verify`, `validate`, `e2e`, `unit test`, `integration`
- Skills: None typically

**Backend API Tasks** → Delegate to `@sdk-agent`
- Keywords: `API`, `endpoint`, `FastAPI`, `route`, `backend`
- Skills: `fastapi-patterns`

### Step 2: Complexity Check

**Delegate if:**
- Task requires > 500 lines of code
- Task is implementation-heavy (not planning/architecture)
- Task is repetitive/boilerplate
- Task fits a specific agent's specialty

**DON'T Delegate if:**
- Task requires understanding full project context
- Task is planning/architecture decision
- Task is quick (< 50 lines of code)
- User explicitly says "don't use agents"

### Step 3: Execute Delegation

If delegating, use this command:

```powershell
.\reusable-intelligence\dispatch.ps1 `
    -Agent <detected-agent> `
    -Task "<user's task with full context>" `
    -Skills "<relevant-skills>" `
    -Execute
```

**Important:** Provide FULL context in the task description since the agent won't have access to the conversation history.

### Step 4: Review Output

After agent completes:
1. Review the agent's output for correctness
2. Check for any errors or issues
3. Integrate the output into the project
4. Report results to the user

## Detection Examples

### Example 1: Authentication Task

**User Request:** "Implement signup and login functionality with Better Auth"

**Detection:**
- Keywords: `signup`, `login`, `Better Auth` → `@better-auth-agent`
- Complexity: High (multiple files, database, routes)
- Decision: **DELEGATE**

**Command:**
```powershell
.\reusable-intelligence\dispatch.ps1 `
    -Agent better-auth-agent `
    -Task "Implement signup and login functionality using Better Auth. Include: 1) Backend routes for /signup and /login in FastAPI, 2) Frontend React components, 3) Session management, 4) Error handling" `
    -Skills "better-auth-patterns,fastapi-patterns" `
    -Execute
```

### Example 2: UI Component

**User Request:** "Create a modern, premium button component for the textbook"

**Detection:**
- Keywords: `modern`, `premium`, `button`, `component` → `@nextjs-agent`
- Complexity: Low-Medium (single component)
- Decision: **MAYBE DELEGATE** (could do directly, but agent has design expertise)

**Command:**
```powershell
.\reusable-intelligence\dispatch.ps1 `
    -Agent nextjs-agent `
    -Task "Create a modern, premium button component for Docusaurus. Should include: 1) Multiple variants (primary, secondary, outline), 2) Hover animations, 3) Accessibility (ARIA labels, keyboard nav), 4) TypeScript definitions" `
    -Skills "visual-excellence,docusaurus-patterns" `
    -Execute
```

### Example 3: Planning Task

**User Request:** "How should we structure the personalization feature?"

**Detection:**
- Keywords: `how`, `structure`, `feature` → Planning question
- Complexity: N/A (not implementation)
- Decision: **DON'T DELEGATE** (requires project context and architectural understanding)

**Action:** Claude answers directly

## Manual Override

**User wants delegation:**
```
User: "Use the nextjs-agent to build this component"
→ Always delegate when explicitly requested
```

**User prevents delegation:**
```
User: "Do NOT use agents for this"
→ Never delegate when explicitly prevented
```

## Token Savings Estimation

**Typical Task:**
- Claude direct: ~2000 tokens (planning) + ~5000 tokens (implementation) = 7000 tokens
- With delegation: ~2000 tokens (planning + review) = 2000 tokens
- **Savings: ~70% of Claude tokens**

**Large Task:**
- Claude direct: ~10,000 tokens
- With delegation: ~3,000 tokens
- **Savings: ~70% of Claude tokens**

## Current Limitations

> [!WARNING]
> **Gemini/Qwen CLI Integration Required**
> 
> The dispatch.ps1 script is created but needs Gemini/Qwen CLI tools installed and configured.
> 
> To complete integration:
> 1. Install Gemini CLI: [Instructions needed]
> 2. Install Qwen CLI: [Instructions needed]
> 3. Configure API keys in backend/.env
> 4. Update dispatch.ps1 with CLI commands

## For Claude: When to Use This

**In your workflow:**

1. **Receive user request**
2. **Check for delegation keywords** (see Step 1 above)
3. **If keywords match and complexity is high:**
   ```
   I'll delegate this to the specialized agent to save tokens and leverage their expertise.
   ```
4. **Call dispatch.ps1** with appropriate agent and skills
5. **Wait for output** (dispatch.ps1 will create `reusable-intelligence/last-dispatch-context.txt`)
6. **Review and integrate** the agent's output
7. **Report results** to user

**Example Claude Response:**
```
I'll delegate this authentication task to @better-auth-agent with better-auth-patterns skill to efficiently implement this.

[Calls dispatch.ps1]

The agent has completed the implementation. Here's what was created:
- backend/app/routes/auth.py (signup/login endpoints)
- frontend/src/components/Auth/LoginForm.tsx
- Session management with Better Auth

All files follow best practices and are ready for integration.
```

## Integration with Claude CLI

For automatic delegation in Claude CLI, you would need to:

1. **Create a wrapper script** that intercepts Claude's responses
2. **Parse for delegation markers** (e.g., @agent-name)
3. **Call dispatch.ps1** when detected
4. **Return results** to Claude

This is advanced and requires custom setup.

---

**Version:** 1.0  
**Last Updated:** 2025-12-12  
**Status:** Framework ready, CLI integration pending
