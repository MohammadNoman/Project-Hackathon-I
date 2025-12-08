# Claude Code Agents, Skills & Commands

This directory contains **reusable intelligence** for Claude Code CLI to reduce token consumption and enable specialized task delegation.

## Directory Structure

```
.claude/
├── agents/                    # Subagents with isolated context
│   ├── better-auth-agent.md   # Better Auth integration specialist
│   ├── chatkit-agent.md       # RAG chatbot & OpenAI Agents specialist
│   ├── nextjs-agent.md        # Next.js & React development specialist
│   └── sdk-agent.md           # General SDK integration specialist
├── skills/                    # Skills that load in main context
│   ├── gemini-delegator/      # Delegate tasks to Gemini CLI
│   ├── qwen-delegator/        # Delegate tasks to Qwen CLI
│   ├── fastapi-patterns/      # FastAPI code patterns
│   └── docusaurus-patterns/   # Docusaurus component patterns
├── commands/                  # Quick command shortcuts
│   ├── delegate-gemini.md     # /delegate-gemini <task>
│   ├── delegate-qwen.md       # /delegate-qwen <task>
│   ├── impl-auth.md           # /impl-auth <feature>
│   ├── impl-chatbot.md        # /impl-chatbot <feature>
│   ├── sp.adr.md              # Existing SDD command
│   ├── sp.plan.md             # Existing SDD command
│   └── ...                    # Other SDD commands
└── settings.local.json        # Permissions & configuration
```

## How to Use

### 1. Invoke Subagents (Isolated Context)

Subagents operate in **separate context windows** - perfect for large, focused tasks that would otherwise consume many tokens.

```bash
# In Claude CLI terminal
@better-auth-agent implement signup endpoint with background questions
@chatkit-agent implement RAG query with Qdrant
@nextjs-agent create chatbot widget component
@sdk-agent integrate OpenAI Agents SDK
```

**When to use subagents:**
- Large implementation tasks (complete endpoint, full component)
- Tasks that need deep focus without main conversation noise
- Bonus features (auth, personalization, translation)

### 2. Use Skills (Main Context)

Skills are **automatically loaded** when Claude detects relevant context. They provide patterns and examples.

**Skills activate automatically when you:**
- Talk about FastAPI → `fastapi-patterns` skill loads
- Mention Docusaurus → `docusaurus-patterns` skill loads
- Want to delegate → `gemini-delegator` or `qwen-delegator` skills load

### 3. Quick Commands

Use `/command-name` for instant workflows:

```bash
/delegate-gemini Generate a 1000-word outline for Module 3
/delegate-qwen Write Python code for vector similarity search
/impl-auth complete authentication flow
/impl-chatbot RAG query endpoint with selected_text support
```

## Token Savings Strategy

| Without Agents/Skills | With Agents/Skills | Token Savings |
|----------------------|-------------------|---------------|
| Full context + implementation | Agent handles in isolation | ~60-70% |
| Repeat boilerplate code | Load skill patterns | ~30-40% |
| Claude generates bulk content | Delegate to Gemini/Qwen | ~80-90% |

**Example:**
- **Before**: "Claude, implement entire auth system" → 50K tokens
- **After**: `@better-auth-agent implement complete auth flow` → 15K tokens
- **Delegation**: `/delegate-gemini write module outlines` → 2K tokens

## Reusability Across Projects

### Option 1: Copy `.claude` folder
```powershell
# Copy to new project
Copy-Item -Path ".\. claude" -Destination "C:\path\to\new-project\.claude" -Recurse
```

### Option 2: Global shared folder (recommended)
```powershell
# Create global location
New-Item -ItemType Directory -Path "$HOME\.claude-shared" -Force

# Copy agents/skills to global
Copy-Item -Path ".\.claude\*" -Destination "$HOME\.claude-shared" -Recurse

# In new projects, symlink to shared
New-Item -ItemType SymbolicLink -Path ".\.claude\skills" -Target "$HOME\.claude-shared\skills"
New-Item -ItemType SymbolicLink -Path ".\.claude\agents" -Target "$HOME\.claude-shared\agents"
```

## Compatibility with SDD

✅ **This agent architecture is fully compatible with Spec-Driven Development (SDD):**

- All agents reference specs in `specs/001-physical-ai-textbook/`
- Agents follow contracts in `specs/001-physical-ai-textbook/contracts/`
- Commands like `/sp.plan`, `/sp.tasks`, `/sp.adr` continue to work
- PHR (Prompt History Records) are still created
- Agents can call `/sp.*` commands when needed

**Agent + SDD workflow:**
1. Use `/sp.specify` to create spec
2. Use `/sp.plan` to create plan
3. Use `/sp.tasks` to break down tasks
4. Use `@chatkit-agent` to implement T028-T030 (RAG tasks)
5. Agents automatically reference the specs you created!

## External CLI Requirements

For delegation features to work:

### Gemini CLI
```powershell
# Install (example - verify actual installation method)
npm install -g @google/gemini-cli
# OR follow official Google AI CLI installation
```

### Qwen CLI
```powershell
# Install (example - verify actual installation method)
pip install qwen-cli
# OR follow official Alibaba Qwen CLI installation
```

**Note:** If you don't have these installed, delegation commands won't work, but all other agents/skills will function normally.

## Testing the Setup

### Test 1: List Agents
```bash
claude
/agents
```
You should see: better-auth-agent, chatkit-agent, nextjs-agent, sdk-agent

### Test 2: List Commands
```bash
/
```
Tab-complete to see all commands including `delegate-gemini`, `impl-auth`, etc.

### Test 3: Invoke an Agent
```bash
@better-auth-agent what can you help with?
```

### Test 4: Use a Skill
```bash
Show me FastAPI endpoint patterns
```
Claude should reference `fastapi-patterns` skill.

## Troubleshooting

**Agents not appearing:**
- Ensure `.md` files are in `.claude/agents/`
- Check YAML frontmatter has `name:` field
- Restart Claude CLI

**Commands not working:**
- Ensure `.md` files are in `.claude/commands/`
- Commands must have `---` frontmatter with `description:`
- Use `$ARGUMENTS` placeholder for dynamic input

**Gemini/Qwen delegation fails:**
- Check if CLI is installed: `gemini --version` or `qwen --version`
- Verify permissions in `.claude/settings.local.json`
- Check API keys if required by the CLIs

## Contributing

When adding new agents/skills:
1. Follow existing file naming conventions
2. Include clear frontmatter metadata
3. Provide code examples and patterns
4. Document when to use the agent/skill
5. Update this README

---

**Created for**: Hackathon I - Physical AI Textbook Project  
**Compatible with**: Spec-Kit Plus, Claude Code CLI, SDD workflow  
**Reusable in**: Any Python/JavaScript/Next.js/FastAPI project
