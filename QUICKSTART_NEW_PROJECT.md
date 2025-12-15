# Quick Start: Add Reusable Intelligence to New Project

**Time:** 5 minutes  
**Result:** Full agent delegation in any project

---

## Step 1: Copy This File Structure

```powershell
# In your new project root
New-Item -ItemType Directory -Path ".claude" -Force
```

Create `.claude-config.json`:
```json
{
  "reusable_intelligence_hub": "C:\\Users\\SM TRADERs\\Downloads\\Hackathon-1\\reusable-intelligence",
  "project_name": "YOUR_PROJECT_NAME",
  "enabled_agents": [
    "nextjs-agent",
    "better-auth-agent",
    "chatkit-agent",
    "deployment-agent",
    "testing-agent"
  ]
}
```

---

## Step 2: Add to CLAUDE.md (or create it)

```markdown
# PROJECT_NAME - Claude Instructions

## Delegation System

This project uses agent delegation to save Claude tokens.

### When to Delegate

Run dispatch.ps1 for:
- Auth tasks (better-auth-agent)
- UI components (nextjs-agent)
- Backend APIs (sdk-agent)
- Testing (testing-agent)
- Deployment (deployment-agent)

### Command:

```powershell
C:\Users\SM TRADERs\Downloads\Hackathon-1\reusable-intelligence\dispatch.ps1 `
    -Agent <agent-name> `
    -Task "<detailed task>" `
    -Skills "<relevant-skills>" `
    -ProjectRoot "<this-project-path>" `
    -Execute
```

### Detection Rules

See: `.claude/commands/auto-delegate.md` (if using central hub)

---

## Step 3: Use It!

### From Terminal:
```powershell
# Navigate to your project
cd C:\path\to\your\project

# Run dispatch
C:\Users\SM TRADERs\Downloads\Hackathon-1\reusable-intelligence\dispatch.ps1 `
    -Agent nextjs-agent `
    -Task "Build a login form component" `
    -Skills "visual-excellence" `
    -ProjectRoot (Get-Location).Path `
    -Execute
```

### With Claude:
```
You: "Claude, use the nextjs-agent to build a dashboard component"

Claude: "I'll delegate this. Please run:
[command provided]

Then share the output."

You: [Run → Copy output → Paste back to Claude]

Claude: [Reviews and helps integrate]
```

---

## That's It!

You now have:
- ✅ Access to all 10 agents
- ✅ Access to all 5 skills
- ✅ 70-85% token savings
- ✅ Consistent across all projects

---

## Project-Specific Customization (Optional)

If this project needs unique agents/skills:

```powershell
# Create project-specific directories
New-Item -ItemType Directory -Path ".claude\agents" -Force
New-Item -ItemType Directory -Path ".claude\skills" -Force
New-Item -ItemType Directory -Path ".claude\commands" -Force

# Add custom agent (example)
# .claude/agents/my-custom-agent.md

# Add custom skill (example)
# .claude/skills/my-framework-patterns/patterns.md
```

Dispatch will check project-specific locations first, then fall back to the central hub.

---

## Quick Reference

### All Available Agents:
1. nextjs-agent (React/UI)
2. better-auth-agent (Authentication)
3. chatkit-agent (RAG/Chatbot)
4. sdk-agent (Backend APIs)
5. testing-agent (Tests)
6. content-agent (Documentation)
7. personalization-agent (User customization)
8. ui-worker-gemini (Gemini-specific UI)
9. qwen-agent (Qwen AI tasks)
10. deployment-agent (DevOps/Deploy)

### All Available Skills:
1. visual-excellence (Modern UI design)
2. gemini-delegator (Gemini patterns)
3. qwen-delegator (Qwen patterns)
4. better-auth-patterns (Auth implementation)
5. fastapi-patterns (Backend development)
6. docusaurus-patterns (Docusaurus sites)

### Common Commands:
- auto-delegate (detection rules)
- setup-env (environment setup)
- deploy-frontend (generic)
- deploy-backend (generic)

---

**Done! Your project now has reusable intelligence!** 🎉
