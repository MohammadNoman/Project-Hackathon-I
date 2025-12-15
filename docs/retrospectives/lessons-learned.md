# Lessons Learned: Token Optimization for AI-Assisted Development

## The Problem

During the Physical AI Textbook hackathon project, we consumed **79% of Claude's context window** in a single session. This was inefficient and costly.

## Root Cause Analysis

| What Happened | Tokens Used | Should Have Used |
|---------------|-------------|------------------|
| Writing demo script directly | ~15k | ~500 (delegate to Gemini) |
| Building PersonalizeButton | ~10k | ~500 (delegate to Gemini) |
| Building TranslateButton | ~10k | ~500 (delegate to Gemini) |
| Writing personalization service | ~8k | ~500 (delegate to Gemini) |
| E2E testing in main context | ~5k | ~500 (Task agent) |
| **Total Waste** | **~48k** | **~2.5k** |

**Potential Savings: 95%+**

---

## The Solution: Architect-Builder Pattern

### Claude = Architect (Expensive, Smart)
- Plans the solution
- Reviews code quality
- Integrates components
- Fixes errors
- Makes decisions

### Gemini/Qwen = Builders (Free, Fast)
- Writes implementation code
- Generates content
- Creates boilerplate
- Runs repetitive tasks

---

## Token Optimization Rules

### Rule 1: NEVER Write Code Directly
```
❌ WRONG: Claude writes 500 lines of React component
✅ RIGHT: Claude outputs dispatch command, Gemini writes code
```

### Rule 2: Use dispatch.ps1 for ALL Implementation
```powershell
# Instead of Claude writing code:
.\reusable-intelligence\dispatch.ps1 -Agent nextjs-agent -Task "Build LoginForm component with validation" -Skills visual-excellence -Execute
```

### Rule 3: Claude Only Does
- **Planning**: "Here's how we'll build this..."
- **Reviewing**: "The Gemini output has an error on line 45..."
- **Integrating**: "Place this file at src/components/..."
- **Deciding**: "We should use approach A because..."

### Rule 4: Gemini/Qwen Does
- **All code writing**
- **All content generation**
- **All boilerplate creation**
- **All documentation writing**

---

## Dispatch Command Reference

```powershell
# Syntax
.\reusable-intelligence\dispatch.ps1 -Agent <agent-name> -Task "<description>" [-Skills <skill1,skill2>] -Execute

# Examples
# Frontend component
.\reusable-intelligence\dispatch.ps1 -Agent nextjs-agent -Task "Build a modal dialog with animations" -Skills visual-excellence -Execute

# Backend API
.\reusable-intelligence\dispatch.ps1 -Agent sdk-agent -Task "Create CRUD endpoints for users" -Skills fastapi-patterns -Execute

# Documentation
.\reusable-intelligence\dispatch.ps1 -Agent content-agent -Task "Write API documentation for auth endpoints" -Execute

# Testing
.\reusable-intelligence\dispatch.ps1 -Agent testing-agent -Task "Create unit tests for RAG service" -Execute
```

---

## Available Resources

### Agents (reusable-intelligence/agents/)
| Agent | Purpose |
|-------|---------|
| `nextjs-agent` | React/Next.js/Docusaurus components |
| `better-auth-agent` | Authentication implementation |
| `chatkit-agent` | RAG chatbot, OpenAI integration |
| `content-agent` | Docs, demos, scripts, content |
| `testing-agent` | E2E and unit testing |
| `personalization-agent` | i18n, personalization features |
| `sdk-agent` | Third-party SDK integration |

### Skills (reusable-intelligence/skills/)
| Skill | Purpose |
|-------|---------|
| `visual-excellence` | Futuristic UI/UX patterns |
| `docusaurus-patterns` | Docusaurus-specific patterns |
| `fastapi-patterns` | FastAPI backend patterns |
| `gemini-delegator` | Gemini prompting optimization |
| `qwen-delegator` | Qwen prompting optimization |

---

## Workflow Example

### User Request: "Add a dark mode toggle"

### ❌ Old Way (Expensive)
```
Claude: *writes 200 lines of component code*
Claude: *writes 100 lines of CSS*
Claude: *writes 50 lines of context provider*
Total: ~10,000 tokens consumed
```

### ✅ New Way (Efficient)
```
Claude: "Run this command:"
.\reusable-intelligence\dispatch.ps1 -Agent nextjs-agent -Task "Create DarkModeToggle component with context provider and CSS" -Skills visual-excellence -Execute

User: *runs command*
Gemini: *generates all code*

Claude: "Output looks good. Place the files at:
- src/components/DarkModeToggle/index.tsx
- src/contexts/ThemeContext.tsx"

Total: ~500 tokens consumed
```

**Savings: 95%**

---

## Checklist for Every Task

- [ ] Is this an implementation task? → Delegate to Gemini
- [ ] Is this content generation? → Delegate to Gemini
- [ ] Is this code writing? → Delegate to Gemini
- [ ] Is this planning/review/decision? → Use Claude
- [ ] Did I use dispatch.ps1? → If no, reconsider

---

## Key Metrics

| Metric | Before | After | Improvement |
|--------|--------|-------|-------------|
| Tokens per feature | ~15k | ~500 | 97% reduction |
| Features per session | 3-4 | 20+ | 5x more |
| Cost per project | High | Minimal | 95%+ savings |
| Context window usage | 79% | ~10% | 8x better |

---

## Summary

**The single most important rule:**

> **Claude is the ARCHITECT. Gemini/Qwen are the BUILDERS.**
>
> Never let the architect pick up a hammer when builders are free.

---

## Action Items for Future Projects

1. **Copy `reusable-intelligence/` to every new project**
2. **Update CLAUDE.md with delegation rules**
3. **Always use dispatch.ps1 for implementation**
4. **Only use Claude for planning, review, integration**
5. **Track token usage and optimize continuously**

---

*Document created: 2024-12-11*
*Project: Physical AI & Humanoid Robotics Textbook*
