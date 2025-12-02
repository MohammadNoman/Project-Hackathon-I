# Implementation Plan: Physical AI & Humanoid Robotics Textbook

**Branch**: `1-physical-ai-textbook` | **Date**: 2025-11-30 | **Spec**: [specs/1-physical-ai-textbook/spec.md](specs/1-physical-ai-textbook/spec.md)
**Input**: Feature specification from `/specs/1-physical-ai-textbook/spec.md`

**Note**: This template is filled in by the `/sp.plan` command. See `.specify/templates/commands/plan.md` for the execution workflow.

## Summary

The project aims to create an AI-native textbook for teaching Physical AI & Humanoid Robotics using Docusaurus, deployed on GitHub Pages. It will feature an integrated RAG chatbot with FastAPI, Neon Serverless Postgres, and Qdrant Cloud Free Tier, along with bonus features like user authentication via `better-auth.com`, personalized content, and Urdu translation. The content generation will be AI/Spec-Driven using Spec-Kit Plus and Claude Code, demonstrating reusable intelligence through Subagents and Agent Skills.

## Technical Context

**Language/Version**: Python (3.9+) for FastAPI backend and AI content generation scripts; JavaScript/TypeScript (Node.js 18+, React 18+) for Docusaurus frontend.
**Primary Dependencies**: Docusaurus, React, Python, FastAPI, OpenAI Agents/ChatKit SDKs, Neon Serverless Postgres, Qdrant Cloud Free Tier, `better-auth.com` SDK, Spec-Kit Plus, Claude Code.
**Storage**: Neon Serverless Postgres (for textbook metadata, user profiles, personalization data); Qdrant Cloud Free Tier (for vector embeddings of textbook content).
**Testing**: `pytest` for Python backend, `Jest` / `React Testing Library` for Docusaurus frontend components. End-to-end testing for core features (textbook access, RAG chatbot) and bonus features (auth, personalization, translation). Human review for content accuracy. Demo video validation.
**Target Platform**: Web (Docusaurus deployed to GitHub Pages), Backend (FastAPI deployed as a service, potentially serverless).
**Project Type**: Web application with a decoupled Docusaurus frontend and FastAPI backend.
**Performance Goals**: RAG chatbot responses within 5 seconds; personalization and translation of chapters within 5 seconds; fast page loads for Docusaurus (under 2 seconds).
**Constraints**: Strict deadline (Nov 30, 2025, 06:00 PM), mandatory tech stack (no substitutions), demo video under 90 seconds, specific functional requirements for all features, high quality and accuracy for textbook content. **Shell Environment Constraint**: All shell commands will be designed for Windows PowerShell (`powershell.exe`).
**Scale/Scope**: Comprehensive textbook covering 13 weeks/4 modules of Physical AI & Humanoid Robotics. Designed as a hackathon prototype, but with an eye towards scalability for future expansion into a full AI-native authoring/reading portal.

## Constitution Check

**GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.**

*   **I. Guiding Principles & Project Vision**: All principles are addressed by the planned phases and features.
    *   Educational Clarity: Addressed by focused content generation and presentation, and quality standards.
    *   Innovation & Experimentation: Central to AI-driven content, RAG chatbot, and bonus features.
    *   User-Centric Design: Incorporated into UI/UX design tasks and quality standards.
    *   Embodied Intelligence Focus: The core theme guiding content creation.
    *   Open Source Spirit: Addressed by documentation and GitHub repository submission.

*   **II. Core Project Requirements (Mandatory for Base Functionality)**: All core requirements are explicitly planned.
    *   Textbook Platform & Deployment (Docusaurus, GitHub Pages): Covered in Phase 0.2 and Phase 1.1.
    *   AI/Spec-Driven Content Generation (Spec-Kit Plus, Claude Code): Covered in Phase 1.2.
    *   Integrated RAG Chatbot: Covered in Phase 2.

*   **III. Recommended Development Practices (for Bonus Points)**: All recommended practices are included as bonus features.
    *   Advanced AI Automation (Claude Code Subagents/Agent Skills): Covered in Phase 3.4.
    *   User Authentication (`better-auth.com`): Covered in Phase 3.1.
    *   Personalized Content: Covered in Phase 3.2.
    *   Content Localization (Urdu): Covered in Phase 3.3.

*   **IV. Quality Standards**: All quality standards are integrated into development and testing phases.
    *   Content Accuracy & Depth: Covered in Phase 1.2 human review and Phase 4.1 content validation.
    *   Code Quality: Covered in Phase 4.1 testing and general development practices.
    *   Documentation: Covered in Phase 4.3 submission preparation.
    *   Performance & Reliability: Covered in Phase 4.2 optimization.
    *   Accessibility: Considered in UI/UX design (Phase 0.3, Phase 2.4, Phase 3.2, Phase 3.3) and quality standards.

## Project Structure

### Documentation (this feature)

```text
specs/1-physical-ai-textbook/
├── plan.md              # This file (/sp.plan command output)
├── research.md          # Phase 0 output (/sp.plan command)
├── data-model.md        # Phase 1 output (/sp.plan command)
├── quickstart.md        # Phase 1 output (/sp.plan command)
├── contracts/           # Phase 1 output (/sp.plan command)
└── tasks.md             # Phase 2 output (/sp.tasks command - NOT created by /sp.plan)
```

### Source Code (repository root)

```text
backend/
├── src/
│   ├── api/             # FastAPI endpoints for RAG, auth, personalization, translation
│   ├── services/        # Business logic for RAG, auth, content manipulation
│   ├── models/          # Data models (Pydantic for FastAPI, database schemas)
│   └── utils/           # Helper functions, embedding generation
└── tests/
    ├── unit/
    └── integration/

frontend/ (Docusaurus project root)
├── docs/                # Markdown files for textbook chapters
├── src/
│   ├── components/      # React components (Chatbot UI, Auth forms, Personalization/Translation buttons)
│   ├── pages/
│   └── theme/           # Docusaurus theme customizations
└── static/              # Static assets (images, etc.)

.specify/
├── memory/
│   ├── constitution.md
│   └── ...
├── templates/
│   ├── plan-template.md
│   ├── spec-template.md
│   ├── tasks-template.md
│   └── phr-template.prompt.md
├── scripts/
│   └── powershell/
│       ├── setup-plan.ps1
│       └── ...
└── ...

history/
├── adr/
├── prompts/
│   ├── constitution/
│   ├── spec/
│   └── plan/
└── ...

specs/1-physical-ai-textbook/
├── plan.md
├── research.md
├── data-model.md
├── quickstart.md
├── contracts/
└── tasks.md
```

**Structure Decision**: Selected a web application structure (Option 2) with a decoupled Docusaurus frontend (`frontend/`) and a FastAPI backend (`backend/`) to align with the specified technologies and modularity requirements.

## Phase 0: Ignition & Foundation

**Estimated Effort**: 15% of Total Time

### 0.1 Project Planning & Blueprinting
*   **Deliverable**: Detailed Project Plan (this `plan.md` document), refined task breakdown, initial timeline.
*   **Actions**:
    *   Finalize task assignments based on this plan (implicit for hackathon team).
    *   Create a version-controlled project board (e.g., GitHub Issues, Trello) to track tasks. (Manual action by user).
*   **UI/UX Micro-Tasks**:
    *   Define core user personas (students with varied backgrounds) for content targeting.
    *   Map critical user journeys (reading content, querying chatbot, personalizing chapters, translating content).
    *   Conduct quick internal stakeholder interviews for initial feature priority if applicable (N/A for solo hackathon).
*   **Risk Mitigation**: Proactive detailed planning mitigates scope creep and ensures clear objectives.

### 0.2 Environment & Toolchain Setup
*   **Deliverable**: Fully configured development environment, ready for coding.
*   **Actions**:
    *   Initialize Git Repository & `.gitignore` (already done by `sp.specify`).
    *   Set up Docusaurus project: `npx create-docusaurus@latest frontend classic` (assuming `frontend` as the project root).
    *   Configure GitHub Pages deployment for Docusaurus (add `deploy.js` script or similar, configure `package.json` deploy script).
    *   Install Claude Code, Spec-Kit Plus CLI tools and relevant SDKs. (Manual installation by user, ensure CLI tools are accessible in PATH).
    *   Install Node.js/npm for frontend development, Python/pip for backend development. (Manual installation by user).
    *   Set up Docker for local development of Neon/Qdrant (if cloud instances not used directly) - `docker pull neondatabase/neon` and `docker pull qdrant/qdrant` then run containers with appropriate port mappings. Alternatively, create cloud accounts and get credentials.
    *   Obtain necessary API keys (OpenAI, Claude, `better-auth.com`). Store securely in environment variables.
*   **Dependencies**: Node.js, npm, Python, pip, Docker (optional for local DBs).
*   **UI/UX Micro-Tasks**: None directly in this setup phase, but foundational for later UI/UX development.
*   **Risk Mitigation**: Early setup identifies and resolves toolchain compatibility issues; secure env var management prevents credential leaks.

### 0.3 Core UI/UX & Design System Establishment
*   **Deliverable**: Customized Docusaurus theme, initial style guide, low-fidelity wireframes for key screens.
*   **Actions**:
    *   Select and customize a Docusaurus theme (`docusaurus-theme-classic`). Modify `docusaurus.config.js` and CSS files in `frontend/src/css/`.
    *   Define core color palette, typography, spacing, and iconography (professional, clean, modern look) in global CSS or theming files.
    *   Implement responsive design principles from the outset using Docusaurus's inherent responsive capabilities and custom CSS.
*   **Dependencies**: Docusaurus project setup (0.2).
*   **UI/UX Micro-Tasks**:
    *   Create low-fidelity wireframes for key textbook pages (chapter view), chatbot widget, and authentication forms.
    *   Conduct a quick internal review of these wireframes for usability and alignment with user-centric design principles.
*   **Risk Mitigation**: Establishes a consistent visual language early, reducing rework later; early wireframing catches fundamental UX issues.

### 0.4 Risk Assessment & Prioritization Strategy
*   **Deliverable**: Identified risks with mitigation strategies; Tiered feature priority list (as defined in the master plan).
*   **Actions**:
    *   Brainstorm Risks (already done in master plan): Technical (tool integration, API limits, performance), Content (accuracy, generation quality), Time (scope creep, unexpected delays).
    *   Mitigation Planning (already done in master plan): For each high-priority risk, define a proactive step or a reactive contingency.
    *   Tiered Feature Priority (already done in master plan): Tier 1 (Must-Have for 100 points), Tier 2 (Should-Have for Bonus), Tier 3 (Could-Have for Max Bonus/Polish).
    *   Contingency: For bonus features, plan to achieve MVP first before striving for perfection. (Already integrated into planning).
*   **Dependencies**: Master plan (already provided).
*   **UI/UX Micro-Tasks**: Prioritization considers user value and critical user journeys.
*   **Risk Mitigation**: Proactive risk identification and prioritization ensures focus on core deliverables and provides fallback for bonus features under time constraints.

## Phase 1: Textbook Core & AI-Native Content Generation

**Estimated Effort**: 25% of Total Time

### 1.1 Docusaurus Structure & Navigation
*   **Deliverable**: Complete Docusaurus site structure mirroring course modules (13 weeks), navigable sidebar, basic placeholder markdown files.
*   **Actions**:
    *   Create `docs` folders in `frontend/` (if not already present from Docusaurus init).
    *   Configure `sidebar.js` in `frontend/` to define the 13-week course structure with 4 main modules (ROS 2, Digital Twin, AI-Robot Brain, VLA).
    *   Create empty markdown files (e.g., `frontend/docs/module1/week1-intro.md`, `frontend/docs/module1/week2-overview.md`, etc.) for all chapters/weeks.
*   **Dependencies**: Docusaurus project setup (0.2).
*   **UI/UX Micro-Tasks**:
    *   Optimize information architecture for clear learning progression and easy access to content.
    *   Design intuitive table of contents and navigation elements, ensuring consistency with established wireframes.
*   **Risk Mitigation**: Early structure definition prevents content disorganization and navigation issues.

### 1.2 AI-Driven Content Generation & Refinement
*   **Deliverable**: Initial drafts for all 13 weeks of content, including outlines, textual content, assessment ideas, and glossary terms. Human-reviewed and refined content.
*   **Actions**:
    *   **Detailed AI Strategy (using Claude Code/Spec-Kit Plus)**:
        *   **Module Outlining**: Prompt Claude Code (via Spec-Kit Plus) to generate detailed outlines for each of the 4 course modules based on the provided "Course Details" (e.g., `Prompt: "Generate a detailed outline for Module 1: The Robotic Nervous System (ROS 2) from the 'Physical AI & Humanoid Robotics' course, including key topics, sub-topics, and expected learning points." `).
        *   **Drafting**: For each section in the generated outlines, prompt Claude Code to generate initial textual content, focusing on explaining concepts, providing examples, and suggesting diagrams. (e.g., `Prompt: "Draft an introductory section for 'ROS 2 Fundamentals' within the Physical AI & Humanoid Robotics textbook. Explain what ROS 2 is, its architecture, and its importance in robotics, assuming a beginner to intermediate audience. Suggest a simple code example for a publisher-subscriber model." `).
        *   **Assessment Generation**: Prompt Claude Code to generate initial ideas for assessments, quizzes, or project prompts based on module learning outcomes. (e.g., `Prompt: "Generate 3 quiz questions for a section on ROS 2 topics, focusing on conceptual understanding and practical application. Provide multiple-choice options for each." `).
        *   **Glossary/Key Terms**: Use Claude Code to extract and define key terminology from generated content. (e.g., `Prompt: "Extract key technical terms from the provided textbook content on ROS 2 and provide concise definitions for each, suitable for a glossary." `).
    *   **Human Review & Editing**: Critically review all AI-generated content for technical accuracy, pedagogical clarity, depth, tone, and conciseness. This involves fact-checking, refining explanations, and ensuring pedagogical effectiveness.
    *   **Iterative Refinement**: Based on human feedback, iteratively refine content using further Claude Code prompts, focusing on areas identified for improvement.
*   **Dependencies**: Docusaurus structure (1.1), Claude Code/Spec-Kit Plus tools (0.2), API keys (0.2).
*   **UI/UX Micro-Tasks**: None directly, but content quality directly impacts the learning experience.
*   **Risk Mitigation**: Iterative AI generation with human review ensures high-quality and accurate content, mitigating risks of factual errors or poor pedagogical approach.

### 1.3 Content Presentation & Visuals
*   **Deliverable**: Well-formatted, visually appealing content within Docusaurus, including initial diagrams/images.
*   **Actions**:
    *   Integrate code blocks using Docusaurus's markdown features. Ensure proper syntax highlighting.
    *   Integrate placeholder diagrams, flowcharts, or images. If final assets are not ready, use descriptive text or basic markdown placeholders.
    *   Ensure overall readability by adjusting markdown structure, heading levels, and list formatting.
*   **Dependencies**: AI-driven content generation (1.2), Core UI/UX & Design System (0.3).
*   **UI/UX Micro-Tasks**:
    *   Ensure optimal legibility with appropriate line height, font sizes, and paragraph spacing within the Docusaurus theme.
    *   Design custom components for displaying complex concepts (e.g., ROS 2 computational graphs, NVIDIA Isaac Sim workflows) if needed, adhering to the established design system.
    *   Conduct quick internal reviews of content presentation to ensure visual appeal and ease of understanding.
*   **Risk Mitigation**: Early focus on presentation ensures a polished learning experience; placeholders prevent blocking on asset creation.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|---|---|---|
| N/A | N/A | N/A |
