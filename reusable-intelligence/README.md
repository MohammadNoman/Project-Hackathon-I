# 🧠 Reusable Intelligence Architecture

This directory contains your **AI Assets**. It is designed to be copied into any project to instantly equip your AI Agents (Claude, etc.) with advanced capabilities while saving tokens.

## 📂 Structure

- **`skills/`**: **Building Blocks**. Reusable code patterns (e.g., `visual-excellence`, `docusaurus-patterns`).
- **`agents/`**: **Worker Prompts**. Specialized personas (Next.js Expert, Content Writer) for Gemini/Qwen.
- **`workflows/`**: **Standard Procedures**. Step-by-step guides for complex tasks (`sp.specify`, `sp.test`).
- **`CLAUDE.md`**: The **Architect's Handbook**. Configures Claude to orchestrate this system.

## 🚀 How to Use

### 1. Setup
1.  **Copy** this folder to your project root.
2.  **Copy** `CLAUDE.md` to your project root.

### 2. The "Architect Loop"
The goal is to use **Claude** as the *Architect* and **Gemini/Qwen** as the *Builders*.

1.  **Ask Claude**: "Plan a [Feature] using the [Agent Name]."
2.  **Claude Responds**: Giving you a `dispatch` command with `-Execute`.
    > `.\reusable-intelligence\dispatch.ps1 -Agent nextjs -Task "Build a dashboard" -Skills visual-excellence -Execute`
3.  **Run Command**:
    *   The script sends the prompt to **Gemini**.
    *   **Gemini** generates the code in the background.
    *   The result appears directly in your terminal.
4.  **Claude Configures**: Claude reads the output and integrates the code.

### 3. Token Savings Strategy

| Workflow | Claude Tokens | Gemini Delegation | Savings |
| :--- | :--- | :--- | :--- |
| **Full Implementation** | ~50k tokens | ~2k tokens (Planning only) | **~96%** |
| **Boilerplate Code** | ~10k tokens | ~500 tokens | **~95%** |
| **Research/Docs** | ~5k tokens | ~100 tokens | **~98%** |

## 📂 Detailed Directory Structure

```
reusable-intelligence/
├── agents/                    # 👷 WORKER PROMPTS (The Builders)
│   ├── nextjs-agent.md        # React/Next.js Specialist
│   ├── better-auth-agent.md   # Authentication Specialist
│   ├── content-agent.md       # Technical Writer
│   └── ...
├── skills/                    # 🧩 SKILLS (The Knowledge)
│   ├── visual-excellence/     # Premium UI/UX Design System
│   ├── docusaurus-patterns/   # Documentation Site Patterns
│   ├── fastapi-patterns/      # Backend API Patterns
│   └── gemini-delegator/      # Prompting logic for Gemini
├── workflows/                 # 📜 WORKFLOWS (The Procedures)
│   ├── sp.specify.md          # How to write specs
│   ├── sp.test.md             # How to run tests
│   └── ...
├── CLAUDE.md                  # 🧠 THE ARCHITECT (Configuration)
├── dispatch.ps1               # ⚡ THE AUTOMATOR (Script)
└── README.md                  # 📖 Documentation
```

## ✅ Compatibility with SDD (Spec-Driven Development)

This system is fully compatible with Spec-Kit Plus:
- **Workflows**: Use `workflows/sp.specify.md` to create specs before running agents.
- **Integration**: Start with an SDD spec -> Use Claude to plan -> Use Agents to implement.
- **History**: Use `/sp.tasks` to track progress as usual.

## 🛠️ Requirements

To use the prompt assembler (`dispatch.ps1`):
- **PowerShell 5.0+** (Windows Default) or PowerShell Core (Mac/Linux).

To use Delegation Skills (`gemini-delegator`):
- **@google/gemini-cli** (optional, if you want direct CLI access).
