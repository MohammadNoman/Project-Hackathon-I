---
feature: AI-Native Physical AI & Humanoid Robotics Textbook
---

# Tasks: AI-Native Physical AI & Humanoid Robotics Textbook (V3 - Enhanced Execution Plan)

This document outlines the detailed, executable tasks for developing the AI-Native Physical AI & Humanoid Robotics Textbook, adhering to TDD, Context7 MCP usage, CLI automation, and easy rollback principles.

## Phase 0: Ignition & Foundation

**Objective**: Establish a robust, verified development environment, foundational UI/UX, and core project management.

### 0.1 Project Planning & Blueprinting

- [ ] T001 Review the Enhanced Project Master Plan (V2).
- [ ] T002 Set up a GitHub Project Board and populate it with initial high-level tasks, assigning initial priorities.
  *Traceability*: Initial Git commit: Feat: Initialize project structure and planning documents.
  *Deliverable*: Live GitHub Project Board with prioritized tasks.

### 0.2 Environment & Toolchain Setup

- [ ] T003 Create `Tests/EnvSetup/verify_env.ps1` to check Node.js, npm, Python, pip, Docker, claude, adk, Docusaurus CLI, Python packages from `requirements-base.txt`, and Node.js packages from `package.json`.
- [ ] T004 Initialize Git Repository: `git init`
- [ ] T005 Install Node.js & npm (if not present).
- [ ] T006 Install Python (if not present, version 3.10).
- [ ] T007 Install Docker Desktop (if not present).
- [ ] T008 Setup Docusaurus Project: `npx create-docusaurus@latest my-textbook classic`, `cd my-textbook`, `npm install`, `cd ..`
- [ ] T009 Install claude and adk CLIs as per official instructions.
- [ ] T010 Run initial login: `claude login`, `adk login` (follow prompts).
- [ ] T011 Register Spec-Kit Plus with Claude Code (specific command depends on Spec-Kit implementation, e.g., `claude mcp add --transport stdio spec-kit-plus "adk run <path_to_spec_kit_plus_server_script>"`).
- [ ] T012 Create backend folder: `New-Item -ItemType Directory -Path "my-textbook/backend" -Force`.
- [ ] T013 Change directory to `my-textbook/backend`: `Push-Location "my-textbook/backend"`.
- [ ] T014 Create Python virtual environment: `python -m venv .venv`.
- [ ] T015 Activate virtual environment: `.venv/Scripts/Activate.ps1`.
- [ ] T016 Create `requirements-base.txt` with: `fastapi`, `uvicorn`, `qdrant-client`, `psycopg2-binary`, `openai`, `litellm` in `my-textbook/backend/requirements-base.txt`.
- [ ] T017 Install Python packages: `pip install -r requirements-base.txt`.
- [ ] T018 Return to previous directory: `Pop-Location`.
- [ ] T019 Create `Tests/Context7/test_context7_mcp_connection.ps1` to test Context7 MCP connection.
- [ ] T020 Install Context7 MCP implementation: `npm install -g @upstash/context7-mcp`.
- [ ] T021 Register the MCP server with Claude Code: `claude mcp add --transport stdio context7 "npx @upstash/context7-mcp"`.
- [ ] T022 Develop a PowerShell script `Scripts/Context7/populate_context7.ps1` to ingest key documentation into Context7 MCP server.
- [ ] T023 Run the population script: `.\Scripts\Context7\populate_context7.ps1`.
- [ ] T024 Create `.env` files in `my-textbook` and `my-textbook/backend` for API keys.
- [ ] T025 Verify Environment: Run the TDD script: `.\Tests\EnvSetup\verify_env.ps1`. Debug and resolve any failures.
  *Traceability*:
    * Commit after Docusaurus setup: Feat: Initialize Docusaurus project.
    * Commit after Python backend setup: Feat: Setup Python backend environment and dependencies.
    * Commit after Claude/Spec-Kit setup: Feat: Configure Claude Code and Spec-Kit Plus CLIs.
    * Commit after Context7 setup and population: Feat: Setup and populate Context7 MCP for documentation lookups.
  *Deliverable*: Fully functional local development environment, all required tools installed, and Context7 MCP server running/populated.

### 0.3 Core UI/UX & Design System Establishment

- [ ] T026 Create `Tests/UIUX/test_theme_visual_regression.spec.js` (using Playwright/Cypress) for visual regression testing.
- [ ] T027 Create low-fidelity wireframes for key textbook pages, chatbot widget, and authentication forms. Conduct a quick internal review of these wireframes.
- [ ] T028 Modify `docusaurus.config.js` (site title, favicon, custom CSS paths) in `my-textbook/docusaurus.config.js`.
- [ ] T029 Create `src/css/custom.css` and define core color palette, typography variables, and global styles in `my-textbook/src/css/custom.css`.
- [ ] T030 Modify `src/theme/Navbar` components and `src/pages/index.js` for custom landing page layout in `my-textbook/src/theme/Navbar.js` (example) and `my-textbook/src/pages/index.js`.
- [ ] T031 Implement responsive design rules in CSS in `my-textbook/src/css/custom.css`.
- [ ] T032 Verify UI/UX: Run `npx playwright test --update-snapshots` (or similar) or `npx playwright test` to check for regressions.
  *Traceability*: Commit theme changes: Feat: Establish core Docusaurus theme and visual identity.
  *Deliverable*: Docusaurus site with custom branding and a defined style guide, passing visual regression tests.

### 0.4 Risk Assessment & Prioritization Strategy

- [ ] T033 Regularly review and update the "Tiered Feature Priority" (from the master plan).
- [ ] T034 Update risk log with new findings or resolved risks.
  *Traceability*: Updates to the risk log or priority list are committed to Git.
  *Deliverable*: Updated project documentation on risks and priorities.

## Phase 1: Textbook Core & AI-Native Content Generation

**Objective**: Construct the foundational textbook structure and generate initial AI-assisted content, ensuring quality and accuracy.

### 1.1 Docusaurus Structure & Navigation

- [ ] T035 Create `Tests/Docusaurus/test_navigation_structure.spec.js` (using Playwright/Cypress) to verify the 13-week module structure.
- [ ] T036 Create `docs` subdirectories for each of the 13 weeks/modules (e.g., `my-textbook/docs/week1-intro`, `my-textbook/docs/week2-ros`).
- [ ] T037 Create placeholder `_category_.json` and `index.md` files within each module directory (e.g., `my-textbook/docs/week1-intro/_category_.json`, `my-textbook/docs/week1-intro/index.md`).
- [ ] T038 Edit `my-textbook/sidebars.js` to define the 13-week course structure, linking to the newly created markdown files.
- [ ] T039 Verify Docusaurus Structure: Run `npx playwright test` to ensure navigation tests pass.
  *Traceability*: Commit after each module's structure is added: Feat: Add structure for Module X: Module Name.
  *Deliverable*: Complete Docusaurus site structure with a navigable sidebar for all 13 weeks, passing navigation tests.

### 1.2 AI-Driven Content Generation & Refinement

- [ ] T040 Create `Tests/Content/test_module1_content_quality.ps1` to test content quality for Module 1.
- [ ] T041 Generate a detailed outline for Module 1 using Claude Code: `claude ask "Generate a detailed outline for Module 1: The Robotic Nervous System (ROS 2) from the Physical AI & Humanoid Robotics course..." | Out-File -FilePath "my-textbook/docs/week1-intro/outline.md"`.
- [ ] T042 Draft content for the 'ROS 2 Nodes, Topics, and Services' section of Module 1 using Claude Code: `claude ask "Draft content for the 'ROS 2 Nodes, Topics, and Services' section of Module 1..." | Out-File -FilePath "my-textbook/docs/week1-intro/1.1-nodes-topics-services.md"`.
- [ ] T043 Repeat CLI commands for other sections and modules, progressively filling `my-textbook/docs`.
- [ ] T044 Generate initial assessment questions for Module 1 using Claude Code.
- [ ] T045 Generate glossary for Module 1 using Claude Code.
- [ ] T046 Manually review and edit `my-textbook/docs/week1-intro/index.md`, `my-textbook/docs/week1-intro/1.1-nodes-topics-services.md`, and other generated files for accuracy, clarity, depth, and tone.
- [ ] T047 Verify Content: Rerun `Tests/Content/test_module1_content_quality.ps1`. Debug and refine content until tests pass.
  *Traceability*:
    * Commit outlines: Feat: Generate AI outlines for all 13 modules.
    * Commit after AI drafting of Module 1: Feat: AI-draft content for Module 1: Intro to Physical AI.
    * Commit after Human review/refinement of Module 1: Chore: Human review and refinement of Module 1 content.
  *Deliverable*: Initial drafts of all 13 modules' content, passing basic content quality tests.

### 1.3 Content Presentation & Visuals

- [ ] T048 Rerun `Tests/UIUX/test_theme_visual_regression.spec.js` after integrating content to ensure no unintended visual changes caused by content styling.
- [ ] T049 Integrate diagrams, images, and tables into markdown files (e.g., `my-textbook/docs/week1-intro/index.md`). Use placeholder images (`/static/img/placeholder.png`) or simple Mermaid diagrams initially.
- [ ] T050 Ensure consistent use of Docusaurus markdown features (admonitions, code blocks, tabs) for rich content.
  *Traceability*: Commit content styling/image integration: Feat: Integrate initial visuals and formatting for Module 1.
  *Deliverable*: Content for Module 1 (and eventually all modules) is formatted and visually clean, ready for later high-fidelity asset integration, and passes visual regression tests.

## Dependencies

- Phase 0 must be completed before Phase 1.
- Within Phase 0 and Phase 1, tasks can be executed in parallel where indicated by `[P]` if no direct file dependencies exist.

## Parallel Execution Examples

- **Environment Setup**:
    - T005, T006, T007 (Installing Node.js, Python, Docker) can be done in parallel.
    - T009, T010, T011 (Installing/configuring Claude Code & Spec-Kit) can be done in parallel with Python backend setup steps (T012-T018) after initial folder creation.
- **UI/UX Design**: T028, T029, T030, T031 (Docusaurus theme customization) can be done in parallel after wireframing (T027).
- **Content Generation**: T041, T042, T043, T044, T045 can be done for different modules/sections in parallel once the Docusaurus structure is in place.

## Implementation Strategy

The implementation will follow an MVP-first approach, iteratively delivering features. We will prioritize foundational setup and core textbook structure before diving deep into advanced AI-native content generation and refinement for all modules. Each phase is designed to be a shippable increment, allowing for continuous feedback and validation.
