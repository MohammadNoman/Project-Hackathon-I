# Making Reusable Intelligence Portable Across Projects

**Date:** 2025-12-12  
**Goal:** Use agents, skills, and commands in ANY project

---

## What You Built (Project Automation)

Your current project has:
- ✅ 10 specialized agents
- ✅ 5 comprehensive skill sets
- ✅ 22 workflow commands
- ✅ Dispatch system (dispatch.ps1)
- ✅ Auto-detection rules

**Current location:** `Hackathon-1/.claude/`

**Problem:** This is inside ONE project. You want to use it everywhere!

---

## Solution: Two Approaches

### Approach 1: Centralized Reusable Intelligence (Recommended)

Create a SINGLE location for all reusable components that ALL projects can access.

#### Structure:

```
C:\Users\SM TRADERs\
├── reusable-intelligence\          ← CENTRAL HUB
│   ├── agents\                     ← All agents
│   ├── skills\                     ← All skills
│   ├── commands\                   ← Generic commands
│   └── dispatch.ps1                ← Dispatch script
│
└── Projects\
    ├── Hackathon-1\
    │   ├── .claude\
    │   │   ├── agents\             ← Project-specific agents (optional)
    │   │   └── commands\           ← Project-specific commands
    │   └── .claude-config.json     ← Points to central hub
    │
    ├── Hackathon-2\
    │   └── .claude-config.json     ← Points to central hub
    │
    └── MyApp\
        └── .claude-config.json     ← Points to central hub
```

#### Benefits:
- ✅ Update agents once, affects all projects
- ✅ No duplication
- ✅ Easy maintenance
- ✅ Can still have project-specific overrides

### Approach 2: Copy Template Per Project

Copy the entire `.claude/` folder to each new project.

#### Benefits:
- ✅ Each project is self-contained
- ✅ Can customize per project
- ✅ No dependencies between projects

#### Drawbacks:
- ❌ Updates require changing multiple projects
- ❌ Duplication of files

---

## Implementation: Approach 1 (Centralized)

### Step 1: Create Central Hub

```powershell
# Create central directory
New-Item -ItemType Directory -Path "C:\Users\SM TRADERs\reusable-intelligence" -Force

# Move current agents/skills there
Move-Item ".\Hackathon-1\.claude\agents" "C:\Users\SM TRADERs\reusable-intelligence\agents"
Move-Item ".\Hackathon-1\.claude\skills" "C:\Users\SM TRADERs\reusable-intelligence\skills"

# Move dispatch.ps1
Move-Item ".\Hackathon-1\reusable-intelligence\dispatch.ps1" "C:\Users\SM TRADERs\reusable-intelligence\dispatch.ps1"

# Create commands directory (generic only)
New-Item -ItemType Directory -Path "C:\Users\SM TRADERs\reusable-intelligence\commands" -Force

# Move generic commands
Move-Item ".\Hackathon-1\.claude\commands\auto-delegate.md" "C:\Users\SM TRADERs\reusable-intelligence\commands\"
Move-Item ".\Hackathon-1\.claude\commands\setup-env.md" "C:\Users\SM TRADERs\reusable-intelligence\commands\"
# Keep project-specific commands in project (.claude/commands/)
```

### Step 2: Update dispatch.ps1 for Central Location

```powershell
# C:\Users\SM TRADERs\reusable-intelligence\dispatch.ps1

param(
    [Parameter(Mandatory=$true)][string]$Agent,
    [Parameter(Mandatory=$true)][string]$Task,
    [string]$Skills = "",
    [string]$ProjectRoot = (Get-Location).Path,  # NEW: Accept project root
    [switch]$Execute
)

# Use central hub for agents/skills
$HubRoot = "C:\Users\SM TRADERs\reusable-intelligence"

# Check central agents first
$agentPath = Join-Path $HubRoot "agents" "$Agent.md"

# If not found, check project-specific
if (!(Test-Path $agentPath)) {
    $agentPath = Join-Path $ProjectRoot ".claude" "agents" "$Agent.md"
}

# Similar logic for skills...
```

### Step 3: Create Config for Each Project

```json
// Hackathon-1/.claude-config.json
{
  "reusable_intelligence_hub": "C:\\Users\\SM TRADERs\\reusable-intelligence",
  "project_name": "Hackathon-1",
  "enabled_agents": [
    "nextjs-agent",
    "better-auth-agent",
    "chatkit-agent",
    "deployment-agent"
  ],
  "custom_skills": [],
  "dispatch_script": "C:\\Users\\SM TRADERs\\reusable-intelligence\\dispatch.ps1"
}
```

### Step 4: Use in Any Project

```powershell
# From ANY project directory
C:\Users\SM TRADERs\reusable-intelligence\dispatch.ps1 `
    -Agent nextjs-agent `
    -Task "Build login form" `
    -Skills "visual-excellence" `
    -ProjectRoot (Get-Location).Path `
    -Execute
```

---

## Implementation: Approach 2 (Template)

### Step 1: Create Template

```powershell
# Create template directory
New-Item -ItemType Directory -Path "C:\Users\SM TRADERs\claude-template" -Force

# Copy everything
Copy-Item ".\Hackathon-1\.claude\*" "C:\Users\SM TRADERs\claude-template\" -Recurse
Copy-Item ".\Hackathon-1\reusable-intelligence" "C:\Users\SM TRADERs\claude-template\reusable-intelligence" -Recurse
```

### Step 2: For Each New Project

```powershell
# In new project
cd MyNewProject
Copy-Item "C:\Users\SM TRADERs\claude-template\.claude" ".\" -Recurse
Copy-Item "C:\Users\SM TRADERs\claude-template\reusable-intelligence" ".\" -Recurse

# Customize CLAUDE.md for project
# Update commands for project-specific needs
```

---

## Generic vs Project-Specific Components

### Always Generic (Reusable Everywhere):

**Agents:**
- ✅ nextjs-agent
- ✅ better-auth-agent
- ✅ qwen-agent
- ✅ deployment-agent
- ✅ testing-agent
- ✅ content-agent

**Skills:**
- ✅ visual-excellence
- ✅ gemini-delegator
- ✅ qwen-delegator
- ✅ better-auth-patterns
- ✅ fastapi-patterns (mostly)

**Commands:**
- ✅ auto-delegate
- ✅ setup-env (generic version)

### Project-Specific:

**Agents:**
- ❓ chatkit-agent (if RAG is specific to this project)
- ❓ personalization-agent (specific feature)
- ❓ sdk-agent (project-specific SDK)

**Skills:**
- ❓ docusaurus-patterns (only if using Docusaurus)
- ❓ Project-specific patterns

**Commands:**
- ❌ deploy-frontend (deployment target varies)
- ❌ deploy-backend (deployment target varies)
- ❌ index-content (specific to this project's content)

---

## Recommended Hybrid Setup

```
C:\Users\SM TRADERs\
├── reusable-intelligence\              # CENTRAL HUB
│   ├── agents\
│   │   ├── nextjs-agent.md            # Generic agents
│   │   ├── better-auth-agent.md
│   │   ├── qwen-agent.md
│   │   ├── deployment-agent.md
│   │   └── testing-agent.md
│   │
│   ├── skills\
│   │   ├── visual-excellence\         # Generic skills
│   │   ├── gemini-delegator\
│   │   ├── qwen-delegator\
│   │   └── better-auth-patterns\
│   │
│   ├── commands\
│   │   ├── auto-delegate.md           # Generic commands
│   │   └── setup-env.md
│   │
│   └── dispatch.ps1                   # Central dispatch
│
└── Projects\
    └── Hackathon-1\
        ├── .claude\
        │   ├── agents\                # Project-specific agents
        │   │   ├── chatkit-agent.md
        │   │   └── personalization-agent.md
        │   │
        │   ├── skills\                # Project-specific skills
        │   │   └── docusaurus-patterns\
        │   │
        │   └── commands\              # Project-specific commands
        │       ├── deploy-frontend.md
        │       ├── deploy-backend.md
        │       └── index-content.md
        │
        ├── .claude-config.json        # Points to hub
        └── CLAUDE.md                  # Project instructions
```

---

## Quick Start for New Projects

### Template Checklist:

When starting a new project:

1. **Copy CLAUDE.md** to new project
2. **Create `.claude-config.json`** pointing to hub
3. **Add project-specific agents** (if needed) to `.claude/agents/`
4. **Add project-specific commands** to `.claude/commands/`
5. **Update CLAUDE.md** with project context

### Example: Starting "Hackathon-2"

```powershell
# Navigate to new project
cd C:\Users\SM TRADERs\Downloads\Hackathon-2

# Create .claude directory
New-Item -ItemType Directory -Path ".claude\agents" -Force
New-Item -ItemType Directory -Path ".claude\commands" -Force

# Create config pointing to hub
@"
{
  "reusable_intelligence_hub": "C:\\Users\\SM TRADERs\\reusable-intelligence",
  "project_name": "Hackathon-2",
  "enabled_agents": ["nextjs-agent", "deployment-agent"]
}
"@ | Set-Content ".claude-config.json"

# Copy CLAUDE.md template
Copy-Item "C:\Users\SM TRADERs\Downloads\Hackathon-1\CLAUDE.md" "."

# Use agents immediately!
C:\Users\SM TRADERs\reusable-intelligence\dispatch.ps1 `
    -Agent nextjs-agent `
    -Task "Build dashboard" `
    -ProjectRoot (Get-Location).Path `
    -Execute
```

---

## Benefits of This Setup

### For Reusability:
✅ Write agents/skills once, use everywhere
✅ Update centrally, affects all projects
✅ Can still customize per-project
✅ Easy to add new agents

### For Token Savings:
✅ Same delegation system works in all projects
✅ Gemini/Qwen do heavy lifting
✅ Claude only plans and reviews
✅ 70-85% token reduction

---

## Next Steps

1. **Decide:** Centralized hub vs template copy
2. **Reorganize:** Move generic components to central location
3. **Test:** Try dispatch from another project
4. **Document:** Update CLAUDE.md template
5. **Scale:** Use across all your projects!

---

**Recommended:** Start with centralized hub, keep project-specific overrides in each project's `.claude/` folder.
