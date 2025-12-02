# Implementation Plan: AI-Native Textbook for Physical AI & Humanoid Robotics Course

**Branch**: `001-physical-ai-textbook` | **Date**: 2025-12-02 | **Spec**: [specs/001-physical-ai-textbook/spec.md](specs/001-physical-ai-textbook/spec.md)
**Input**: Feature specification from `/specs/001-physical-ai-textbook/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

This project aims to create an AI-Native Textbook for Physical AI & Humanoid Robotics using Docusaurus, deployed to GitHub Pages. It will feature an integrated RAG chatbot powered by FastAPI, OpenAI Agents/ChatKit SDKs, Neon Serverless Postgres, and Qdrant. Bonus features include user authentication with `better-auth.com` for personalized content and Urdu translation, along with leveraging Claude Code Subagents and Agent Skills for reusable intelligence in content creation. The technical approach involves a modern web application architecture with a static site generator frontend and a Python backend for AI services.

## Technical Context

**Language/Version**: Python 3.9+ (for FastAPI, RAG), Node.js (for Docusaurus), JavaScript/TypeScript (for Docusaurus frontend interaction)
**Primary Dependencies**: Docusaurus, OpenAI Agents/ChatKit SDKs, FastAPI, Neon Serverless Postgres, Qdrant Cloud Free Tier, `better-auth.com`
**Storage**: Neon Serverless Postgres (for user profiles, content personalization data, potentially core book metadata), Qdrant Cloud Free Tier (for vector embeddings of book content for RAG)
**Testing**: Pytest (for FastAPI backend), Jest/React Testing Library (for Docusaurus frontend components)
**Target Platform**: GitHub Pages (for Docusaurus static site), Cloud/Serverless environment (for FastAPI backend API, e.g., Vercel, AWS Lambda, or a simple PythonAnywhere deployment for hackathon scope).
**Project Type**: Web application (static site generator frontend + RESTful API backend)
**Performance Goals**: Book loading <2 seconds, RAG chatbot response <5 seconds, Authentication & personalization operations responsive.
**Constraints**: Strict deadline (Nov 30, 2025), mandatory tech stack (Docusaurus, GitHub Pages, Spec-Kit Plus, Claude Code, OpenAI Agents/ChatKit SDKs, FastAPI, Neon, Qdrant, `better-auth.com`), demo video <90 seconds, functional specificity for RAG and bonus features, quality & accuracy of textbook content, Qdrant Free Tier limitations.
**Scale/Scope**: Initial target for hackathon submission, single user access for RAG/personalization/translation features. Designed for future extensibility beyond hackathon.

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- [X] **Educational Clarity**: The project's core is an educational textbook, aligning perfectly with this principle.
- [X] **Innovation & Experimentation**: The use of AI-native tools (Claude Code, OpenAI Agents, RAG, personalization) demonstrates strong alignment.
- [X] **User-Centric Design**: Focus on interactive chatbot, personalization, and translation directly addresses user experience.
- [X] **Embodied Intelligence Focus**: The textbook's content directly targets "Physical AI & Humanoid Robotics", maintaining theme alignment.
- [ ] **Open Source Spirit**: While not explicitly open-source in the spec, adherence to maintainable code and clear documentation aligns. This will be an implicit goal.
- [X] **Textbook Platform & Deployment**: Docusaurus on GitHub Pages is a direct requirement.
- [X] **AI/Spec-Driven Content Generation**: Spec-Kit Plus and Claude Code are mandatory tools.
- [X] **Integrated RAG Chatbot**: Core functionality with specified tech stack.
- [X] **Advanced AI Automation**: Claude Code Subagents/Agent Skills are a bonus point item.
- [X] **User Authentication**: `better-auth.com` integration is a bonus point item.
- [X] **Personalized Content**: Chapter-level personalization is a bonus point item.
- [X] **Content Localization**: Urdu translation is a bonus point item.
- [X] **Content Accuracy & Depth**: Explicitly called out in NFRs and success criteria.
- [X] **Code Quality**: Explicitly called out in NFRs.
- [X] **Documentation**: Explicitly called out in NFRs and for hackathon judges.
- [X] **Performance & Reliability**: Explicitly called out in NFRs.
- [X] **Accessibility**: Strived for in NFRs.
- [X] **Technical Environment & Simulation Guidelines**: These are for the *content* of the textbook, not the project's development environment. The project will reflect these topics.

**Constitution Check Status**: PASS. All principles are either directly addressed, aligned, or will be implicitly pursued (Open Source Spirit for maintainability).

## Project Structure

### Documentation (this feature)

```text
specs/001-physical-ai-textbook/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
.
├── docs/                # Docusaurus content (chapters, images, assets)
├── blog/                # Docusaurus blog (if needed for updates/announcements)
├── src/                 # Docusaurus custom components, pages, styling
├── docusaurus.config.js # Docusaurus configuration
├── package.json         # Node.js dependencies for Docusaurus
├── sidebar.js           # Docusaurus sidebar configuration
├── static/              # Docusaurus static assets

├── backend/             # FastAPI application for RAG, Auth, Personalization, Translation
│   ├── app/
│   │   ├── main.py      # FastAPI application entry point
│   │   ├── api/         # API endpoints (auth, chatbot, personalization, translation)
│   │   ├── core/        # Core logic (RAG engine, personalization algorithms, translation service)
│   │   ├── models/      # Pydantic models for data (User, Content, ChatRequest)
│   │   └── database/    # DB connection, ORM models (Neon Postgres)
│   ├── tests/           # Pytest tests for backend
│   ├── requirements.txt # Python dependencies
│   └── .env.example     # Environment variable template

├── scripts/             # Utility scripts (e.g., for Qdrant indexing, content processing)
├── .github/             # GitHub Actions for CI/CD (Docusaurus deploy, backend deploy)
├── .env.example         # Root environment variables
├── .gitignore           # Git ignore file
└── README.md            # Project README
```

**Structure Decision**: The project will use a monorepo-like structure with Docusaurus handling the frontend (book content, UI) and a separate `backend/` directory for the FastAPI application. This separation allows independent development and deployment of the static site and the dynamic API services. It aligns with the "Web application" option and is expanded to include Docusaurus specific structure.

## Complexity Tracking

> **Fill ONLY if Constitution Check has violations that must be justified**

No constitution check violations were detected that require justification.

---

## Sub-Plan for Phase 0: Ignition & Foundation

**Estimated Effort: 15% of Total Time**

### 0.1 Project Planning & Blueprinting
*   **Deliverable**: Detailed Project Plan (this document), refined task breakdown, and initial timeline.
*   **Actions**:
    *   Finalize task assignments, create a version-controlled project board (e.g., GitHub Issues, Trello).
    *   **UI/UX Role**: Define core user personas (students with varied backgrounds), map critical user journeys (reading, querying, personalizing). Conduct quick internal stakeholder interviews for initial feature priority if applicable.
*   **Risk Mitigation**: Proactive planning addresses scope creep and unexpected delays by clearly defining tasks and priorities.

### 0.2 Environment & Toolchain Setup
*   **Deliverable**: Fully configured development environment.
*   **Actions**:
    *   **T001**: Initialize Git Repository & `.gitignore`.
        *   **Specific Commands/Actions (PowerShell)**: `git init; Set-Content -Path .gitignore -Value "*`n`.env`n`node_modules`n`__pycache__`n`venv`n`dist`n`build`n`*.log" -Force`
        *   **Estimated Effort**: Low
        *   **Dependencies**: Git installed
        *   **Risk Mitigation**: Early git init ensures version control from start; comprehensive .gitignore prevents sensitive files from being committed.
    *   **T002**: Install Node.js/npm for frontend, Python/pip for backend (FastAPI).
        *   **Specific Commands/Actions (PowerShell)**: `Write-Host "Ensure Node.js (v18+) and Python (3.9+) are installed. Verify with: node -v; python --version; pip --version"`
        *   **Estimated Effort**: Low
        *   **Dependencies**: OS installation of Node.js and Python
    *   **T003**: Install Claude Code and Spec-Kit Plus CLI tools and relevant SDKs.
        *   **Specific Commands/Actions (PowerShell)**: `npm install -g @anthropic-ai/claude-code-cli; npm install -g spec-kit-plus-cli` (Assuming Spec-Kit Plus CLI is also distributed via npm)
        *   **Estimated Effort**: Low
        *   **Dependencies**: Node.js/npm
    *   **T004**: Set up Docusaurus project.
        *   **Specific Commands/Actions (PowerShell)**: `npx create-docusaurus@latest 001-physical-ai-textbook-docs classic` (This will create a new directory `001-physical-ai-textbook-docs`. You may want to integrate this directly into the root or move its contents to the `docs` and `src` directories after creation.)
        *   **Estimated Effort**: Medium
        *   **Dependencies**: Node.js/npm
        *   **Risk Mitigation**: Using `@latest` ensures current version, reducing compatibility issues.
    *   **T005**: Configure GitHub Pages deployment for Docusaurus.
        *   **Specific Commands/Actions (PowerShell)**: `Write-Host "Follow Docusaurus deployment guide for GitHub Pages. This involves adding Docusaurus build script to package.json and configuring a GitHub Actions workflow (e.g., .github/workflows/deploy.yml)."`
        *   **Estimated Effort**: Medium
        *   **Dependencies**: Docusaurus project setup, GitHub repository
    *   **T006**: Set up Docker for local development of Neon/Qdrant substitutes (if not using cloud instances directly).
        *   **Specific Commands/Actions (PowerShell)**: `Write-Host "Install Docker Desktop: https://docs.docker.com/desktop/install/windows-install/"`
        *   **Estimated Effort**: Low
        *   **Dependencies**: Windows OS
    *   **T007**: Obtain necessary API keys (OpenAI, Claude, `better-auth.com`).
        *   **Specific Commands/Actions (PowerShell)**: `Write-Host "Register for accounts and obtain API keys. Securely store these in environment variables (e.g., in a .env file, loaded by python-dotenv for FastAPI)."`
        *   **Estimated Effort**: Low
        *   **Dependencies**: External service accounts
        *   **Risk Mitigation**: Storing API keys in `.env` and not committing them to git prevents credential leakage.
    *   **Technical Considerations**: Ensure all tools are compatible and properly authenticated. Implement secure environment variable management.

### 0.3 Core UI/UX & Design System Establishment
*   **Deliverable**: Docusaurus theme customized for branding, initial style guide, low-fidelity wireframes for key screens.
*   **Actions**:
    *   **T008**: Select and customize a Docusaurus theme (`docusaurus-theme-classic`).
        *   **Specific Commands/Actions (PowerShell)**: `Write-Host "Modify docusaurus.config.js and custom CSS files (e.g., src/css/custom.css) for branding."`
        *   **Estimated Effort**: Medium
        *   **Dependencies**: Docusaurus project setup
    *   **T009**: Define core color palette, typography, spacing, and iconography (professional, clean, modern look).
        *   **UI/UX Role**: Create a small design system document or update Docusaurus CSS variables.
        *   **Estimated Effort**: Medium
        *   **Dependencies**: Docusaurus theme customization
    *   **T010**: Implement responsive design principles from the outset.
        *   **Specific Commands/Actions (PowerShell)**: `Write-Host "Ensure Docusaurus layout and custom components are responsive by using CSS media queries and flexible layouts."`
        *   **Estimated Effort**: Medium
        *   **Dependencies**: Docusaurus theme customization
    *   **UI/UX Role**: Create low-fidelity wireframes for key textbook pages, chatbot widget, and authentication forms. Conduct a quick internal review of these wireframes.

### 0.4 Risk Assessment & Prioritization Strategy
*   **Deliverable**: Identified risks with mitigation strategies; Tiered feature priority list. (Already documented in Master Plan).

## Sub-Plan for Phase 1: Textbook Core & AI-Native Content Generation

**Estimated Effort: 25% of Total Time**

### 1.1 Docusaurus Structure & Navigation
*   **Deliverable**: Complete Docusaurus site structure mirroring course modules (13 weeks), navigable sidebar.
*   **Actions**:
    *   **T011**: Create docs folders, `sidebar.js`, and basic markdown files for all chapters/weeks.
        *   **Specific Commands/Actions (PowerShell - illustrative, adapt for actual structure)**:
            `New-Item -ItemType Directory -Path "docs/module1-ros2-nervous-system" -Force | Out-Null`
            `New-Item -ItemType File -Path "docs/module1-ros2-nervous-system/index.md" -Value "# Module 1: The Robotic Nervous System (ROS 2)`n`Content for Week 1 goes here." -Force | Out-Null`
            `# ... repeat similar structure for all 13 weeks/modules`
            `# Update sidebar.js to reflect the new structure`
        *   **Estimated Effort**: High (repetitive, but foundational)
        *   **Dependencies**: Docusaurus project setup
    *   **T012**: Optimize information architecture for clear learning progression; design intuitive table of contents and navigation elements. Ensure consistency with wireframes from Phase 0.
        *   **UI/UX Role**: Review and refine `sidebar.js` and overall navigation flow. Consider user testing for navigation clarity.
        *   **Estimated Effort**: Medium
        *   **Dependencies**: Basic Docusaurus structure

### 1.2 AI-Driven Content Generation & Refinement
*   **Deliverable**: Initial drafts for all 13 weeks of content, with clear AI-human collaboration.
*   **Actions**:
    *   **Detailed AI Strategy (using Claude Code via Spec-Kit Plus)**:
        *   **T013**: Module Outlining: Use Claude Code to generate detailed outlines for each course module based on the "Course Details" in the Master Plan.
            *   **Specific Commands/Actions (PowerShell)**: `Write-Host "Prompt Claude Code with specific module details for outlines. E.g., Ask Claude Code to generate a detailed outline for \"Module 1: The Robotic Nervous System (ROS 2)\" based on the course details in spec.md, focusing on learning outcomes and weekly breakdown."`
            *   **Estimated Effort**: Medium
            *   **Dependencies**: Access to Claude Code
        *   **T014**: Drafting: For each section, prompt Claude Code to generate initial textual content, explaining concepts, providing examples, and suggesting diagrams.
            *   **Specific Commands/Actions (PowerShell)**: `Write-Host "Iteratively prompt Claude Code, saving output to respective markdown files (e.g., docs/module1-ros2-nervous-system/week1-intro.md)."`
            *   **Estimated Effort**: High
            *   **Dependencies**: Module outlines, Claude Code
        *   **T015**: Assessment Generation: Prompt Claude Code to generate initial ideas for assessments, quizzes, or project prompts based on module learning outcomes.
            *   **Specific Commands/Actions (PowerShell)**: `Write-Host "Prompt Claude Code for assessment ideas, saving to docs/assessments/moduleX-assessments.md."`
            *   **Estimated Effort**: Medium
            *   **Dependencies**: Module content, Claude Code
        *   **T016**: Glossary/Key Terms: Use Claude Code to extract and define key terminology from generated content.
            *   **Specific Commands/Actions (PowerShell)**: `Write-Host "Prompt Claude Code to identify and define terms from generated content, saving to a glossary file (e.g., docs/glossary.md)."`
            *   **Estimated Effort**: Medium
            *   **Dependencies**: Generated content, Claude Code
    *   **T017**: Human Review & Editing: Critically review AI-generated content for technical accuracy, pedagogical clarity, depth, tone, and conciseness.
        *   **Specific Commands/Actions**: Manual review and editing of all markdown content. Fact-checking against authoritative sources (e.g., ROS 2, NVIDIA Isaac documentation).
        *   **Estimated Effort**: Very High
        *   **Dependencies**: All AI-generated content
        *   **Risk Mitigation**: Human review is critical for accuracy and quality in a textbook, mitigating the risk of AI-generated factual errors or outdated information.
    *   **T018**: Iteratively refine content based on human feedback and further Claude Code prompts.
        *   **Specific Commands/Actions**: Repeat T014-T017 as needed, focusing on improving clarity, accuracy, and completeness.
        *   **Estimated Effort**: High (ongoing)
        *   **Risk Mitigation**: Iterative refinement helps address content quality risks, ensuring the final textbook is world-class.
*   **Technical Considerations**: Develop a clear prompt engineering strategy for Claude Code to ensure consistent and high-quality outputs. Maintain version control of prompts and generated content.

### 1.3 Content Presentation & Visuals
*   **Deliverable**: Well-formatted, visually appealing content.
*   **Actions**:
    *   **T019**: Integrate code blocks, diagrams, images, and tables. Ensure readability. Start with placeholder images if final assets are not ready.
        *   **Specific Commands/Actions**: Embed code snippets using markdown syntax. Create/source diagrams/images (e.g., using Mermaid.js for diagrams in Docusaurus, or external tools). Add tables for structured data.
        *   **Estimated Effort**: High
        *   **Dependencies**: Content drafts, Docusaurus capabilities
    *   **T020**: Ensure optimal legibility with appropriate line height, font sizes; design custom components for complex concepts (e.g., ROS 2 graphs, Isaac Sim workflows) if needed. Conduct quick internal reviews of content presentation.
        *   **UI/UX Role**: CSS adjustments in `src/css/custom.css`. Development of custom React components (e.g., `src/components/RosGraphViewer.js`) if highly interactive or complex visualizations are required.
        *   **Estimated Effort**: Medium
        *   **Dependencies**: Docusaurus project, content needs