---
id: 001
title: Generated Tasks for AI-Native Physical AI Textbook
stage: tasks
date: 2025-11-30
surface: agent
model: claude-opus-4-5-20251101
feature: ai-native-physical-ai-humanoid-robotics-textbook
branch: master
user: user
command: /sp.tasks Project Tasks: AI-Native Physical AI & Humanoid Robotics Textbook (V3 - Enhanced Execution Plan)

  This plan details tasks for Phase 0: Ignition & Foundation and Phase 1: Textbook Core & AI-Native Content Generation.
  Each task adheres to the following principles:

   * TDD (Test-Driven Development): Write the test before the code.
   * Context7 MCP Usage: Leverage Context7 for documentation, best practices, and knowledge lookup.
   * CLI Automation: Prioritize powershell.exe compatible commands for efficiency and consistency.
   * Easy Rollback & Traceability: Frequent, atomic Git commits with clear messages.

  ---

  🚀 Phase 0: Ignition & Foundation

  Objective: Establish a robust, verified development environment, foundational UI/UX, and core project management.

  0.1 Project Planning & Blueprinting
   * Objective: Solidify the project plan and task management.
   * TDD Step: N/A (planning activity).
   * Action Steps:
       * Review the Enhanced Project Master Plan (V2).
       * Set up a GitHub Project Board and populate it with initial high-level tasks derived from this plan. Assign
         initial priorities.
   * Context7 Usage: N/A.
   * Traceability: Initial Git commit: Feat: Initialize project structure and planning documents.
   * Deliverable: Live GitHub Project Board with prioritized tasks.

  0.2 Environment & Toolchain Setup
   * Objective: Have a fully configured and verified development environment.
   * TDD Step (Pre-Code):
       * Test Script: Create Tests\EnvSetup\verify_env.ps1. This PowerShell script will:
           * Check for Node.js (node -v) and npm (npm -v) presence.
           * Check for Python (python -V) and pip (pip -V) presence.
           * Check for Docker (docker -v) presence and ensure docker-compose is available.
           * Verify the presence of claude and adk CLI tools (e.g., using Get-Command claude).
           * Verify Docusaurus CLI (npx docusaurus -v) presence.
           * Verify Python packages from requirements-base.txt are installed in the active virtual environment.
           * Verify Node.js packages from package.json are installed in node_modules.
           * The script should exit 1 (or throw an error) if any critical check fails.
   * Action Steps:
       1. Initialize Git Repository:

   1         git init
       2. Install Essential Tools:
           * Node.js & npm: (If not installed, user guides to official installer or choco install nodejs-lts).
           * Python: (If not installed, user guides to official installer or choco install python --version=3.10).
           * Docker Desktop: (If not installed, user guides to official installer).
       3. Setup Docusaurus Project:

   1         npx create-docusaurus@latest my-textbook classic
   2         Push-Location my-textbook # Equivalent to cd my-textbook
   3         npm install
   4         Pop-Location # Equivalent to cd ..
       4. Setup Claude Code & Spec-Kit Plus CLIs:
           * Install claude and adk CLIs as per official instructions.
           * Run initial login: claude login, adk login (follow prompts).
           * Register Spec-Kit Plus with Claude Code (specific command depends on Spec-Kit implementation, e.g., claude
             mcp add --transport stdio spec-kit-plus "adk run <path_to_spec_kit_plus_server_script>").
       5. Setup Python Virtual Environment & Dependencies:

   1         New-Item -ItemType Directory -Path "my-textbook\backend" -Force # Create backend folder
   2         Push-Location "my-textbook\backend"
   3         python -m venv .venv
   4         .venv\Scripts\Activate.ps1 # Activate virtual environment
   5         # Create 'requirements-base.txt' with: fastapi, uvicorn, qdrant-client, psycopg2-binary, openai, litellm
   6         pip install -r requirements-base.txt
   7         Pop-Location
       6. Context7 MCP Server Setup:
           * TDD (Pre-Code): Create Tests\Context7\test_context7_mcp_connection.ps1. This script will use claude call or
             a direct client to attempt a simple interaction with the Context7 MCP server and assert a successful,
             expected response.
           * Action Steps:
               * Install Context7 MCP implementation (e.g., @upstash/context7-mcp if Node.js-based): npm install -g
                 @upstash/context7-mcp.
               * Register the MCP server with Claude Code:
   1                 claude mcp add --transport stdio context7 "npx @upstash/context7-mcp"
               * Populate Context7: Develop a PowerShell script (Scripts\Context7\populate_context7.ps1) that
                 programmatically ingests key documentation (Docusaurus docs, FastAPI docs, Spec-Kit Plus docs, Claude
                 Code CLI reference) into the Context7 MCP server.
               * Run the population script: .\Scripts\Context7\populate_context7.ps1
       7. Secure API Keys: Create .env files in appropriate project root directories (my-textbook, my-textbook\backend)
          for storing API keys.
       8. Verify Environment: Run the TDD script: .\Tests\EnvSetup\verify_env.ps1. Debug and resolve any failures.
   * Context7 Usage: N/A (this task is setting up Context7).
   * Traceability:
       * Commit after Docusaurus setup: Feat: Initialize Docusaurus project.
       * Commit after Python backend setup: Feat: Setup Python backend environment and dependencies.
       * Commit after Claude/Spec-Kit setup: Feat: Configure Claude Code and Spec-Kit Plus CLIs.
       * Commit after Context7 setup and population: Feat: Setup and populate Context7 MCP for documentation lookups.
   * Deliverable: Fully functional local development environment, all required tools installed, and Context7 MCP server
     running/populated.

  0.3 Core UI/UX & Design System Establishment
   * Objective: Define the visual identity and user experience for the textbook, with verified consistency.
   * TDD Step (Pre-Code):
       * Test: Create Tests\UIUX\test_theme_visual_regression.spec.js (using Playwright/Cypress). This script will
         navigate to the Docusaurus homepage, take a screenshot, and establish a baseline for visual regression testing.
   * Action Steps:
       1. UI/UX Role: Create low-fidelity wireframes for key textbook pages, chatbot widget, and authentication forms.
          Conduct a quick internal review of these wireframes.
       2. Code: Docusaurus Theme Customization:
           * Modify docusaurus.config.js (site title, favicon, custom CSS paths).
           * Create src/css/custom.css and define core color palette, typography variables, and global styles for a
             professional, clean, modern look.
           * Modify src/theme/Navbar components and src/pages/index.js for custom landing page layout.
           * Implement responsive design rules in CSS.
       3. Verify: Run npx playwright test --update-snapshots (or similar) to capture new baselines if changes are
          intentional, or npx playwright test to check for regressions.
   * Context7 Usage: Consult Context7 MCP for Docusaurus theming best practices, general UI/UX principles, and
     accessibility guidelines.
   * Traceability: Commit theme changes: Feat: Establish core Docusaurus theme and visual identity.
   * Deliverable: Docusaurus site with custom branding and a defined style guide, passing visual regression tests.

  0.4 Risk Assessment & Prioritization Strategy
   * Objective: Maintain an active risk log and feature priority, guiding development.
   * TDD Step: N/A (planning/management activity).
   * Action Steps:
       * Regularly review and update the "Tiered Feature Priority" (from the master plan).
       * Update risk log with new findings or resolved risks.
   * Context7 Usage: N/A.
   * Traceability: Updates to the risk log or priority list are committed to Git.
   * Deliverable: Updated project documentation on risks and priorities.

  ---

  📚 Phase 1: Textbook Core & AI-Native Content Generation

  Objective: Construct the foundational textbook structure and generate initial AI-assisted content, ensuring quality
  and accuracy.

  1.1 Docusaurus Structure & Navigation
   * Objective: Establish the full 13-week course structure in Docusaurus.
   * TDD Step (Pre-Code):
       * Test: Create Tests\Docusaurus\test_navigation_structure.spec.js (using Playwright/Cypress). This script will:
           * Navigate to the Docusaurus homepage.
           * Verify that all 13 modules (weeks) are listed in the sidebar navigation.
           * Click on a sample module link and assert that its corresponding page loads (even if empty).
   * Action Steps:
       1. CLI Automation:
           * Create docs subdirectories for each of the 13 weeks/modules (e.g., my-textbook\docs\week1-intro,
             my-textbook\docs\week2-ros).
           * Create placeholder _category_.json and index.md files within each module directory.
           * Edit my-textbook\sidebars.js to define the 13-week course structure, linking to the newly created markdown
             files.
   * Context7 Usage: Consult Context7 MCP for Docusaurus navigation best practices and sidebars.js configuration
     examples.
   * Traceability: Commit after each module's structure is added: Feat: Add structure for Module X: Module Name.
   * Deliverable: Complete Docusaurus site structure with a navigable sidebar for all 13 weeks, passing navigation
     tests.

  1.2 AI-Driven Content Generation & Refinement
   * Objective: Generate initial drafts for the textbook content using AI, then refine them for accuracy and clarity.
   * TDD Step (Pre-Code):
       * Test: Create Tests\Content\test_module1_content_quality.ps1. This PowerShell script will:
           * Read the generated content for Module 1 (e.g., my-textbook\docs\week1-intro\index.md).
           * Use simple text processing (e.g., regex, string comparisons) to assert the presence of key terms from the
             module's learning outcomes (e.g., "Physical AI", "embodied intelligence", "ROS 2 fundamentals").
           * Assert a minimum word count and check for basic markdown formatting (e.g., headings, code blocks).
           * Optionally, integrate an LLM API call (via Python invoked from PowerShell) to perform a higher-level
             coherence or factual check against a trusted source.
   * Action Steps:
       1. CLI Automation (AI Strategy):
           * Module Outlining (Example for Module 1):

   1             $prompt = "Generate a detailed outline for Module 1: The Robotic Nervous System (ROS 2) from the Physic
     AI & Humanoid Robotics course, ensuring all learning objectives from the provided hackathon brief are covered.
     Structure it logically for a beginner's textbook."
   2             claude ask "$prompt" | Out-File -FilePath "my-textbook\docs\week1-intro\outline.md"
           * Drafting Section Content (Example for Module 1, Section 1.1):

   1             $prompt = "Draft content for the 'ROS 2 Nodes, Topics, and Services' section of Module 1, explaining
     concepts clearly for beginners, including Python code examples for publisher and subscriber. Emphasize the
     communication paradigm (nodes, topics, messages)."
   2             claude ask "$prompt" | Out-File -FilePath "my-textbook\docs\week1-intro\1.1-nodes-topics-services.md"
           * Repeat similar CLI commands for other sections and modules, progressively filling my-textbook\docs.
           * Assessment Generation (CLI): Use Claude Code to generate initial assessment questions for Module 1.
           * Glossary Generation (CLI): Use Claude Code to extract key terms from Module 1 content and define them.
       2. Human Review & Editing: Manually review my-textbook\docs\week1-intro\index.md,
          my-textbook\docs\week1-intro\1.1-nodes-topics-services.md, and other generated files for accuracy, clarity,
          depth, and tone. Make necessary corrections directly in the markdown.
       3. Verify: After human edits, rerun Tests\Content\test_module1_content_quality.ps1. Debug and refine content
          until tests pass.
   * Context7 Usage: Continuously consult Context7 MCP for Claude Code prompting best practices, Spec-Kit schema
     examples, pedagogical guidelines, and existing documentation on specific robotics concepts (ROS 2, Gazebo, etc.) to
     inform human editing and refine prompts.
   * Traceability:
       * Commit outlines: Feat: Generate AI outlines for all 13 modules.
       * Commit after AI drafting of Module 1: Feat: AI-draft content for Module 1: Intro to Physical AI.
       * Commit after Human review/refinement of Module 1: Chore: Human review and refinement of Module 1 content.
   * Deliverable: Initial drafts of all 13 modules' content, passing basic content quality tests.

  1.3 Content Presentation & Visuals
   * Objective: Ensure content is well-formatted and visually engaging.
   * TDD Step (Pre-Code):
       * Test: Rerun Tests\UIUX\test_theme_visual_regression.spec.js after integrating content to ensure no unintended
         visual changes caused by content styling.
   * Action Steps:
       1. Integrate diagrams, images, and tables into markdown files. Use placeholder images
          (/static/img/placeholder.png) or simple Mermaid diagrams initially.
       2. Ensure consistent use of Docusaurus markdown features (admonitions, code blocks, tabs) for rich content.
   * Context7 Usage: Consult Context7 MCP for Docusaurus features for rich content, image optimization tips, and Mermaid
     diagram syntax.
   * Traceability: Commit content styling/image integration: Feat: Integrate initial visuals and formatting for Module
     1.
   * Deliverable: Content for Module 1 (and eventually all modules) is formatted and visually clean, ready for later
     high-fidelity asset integration, and passes visual regression tests.
labels: [tasks, spec-driven-development, ai-native, robotics, textbook]
links:
  spec: specs/ai-native-physical-ai-humanoid-robotics-textbook/spec.md
  ticket: null
  adr: null
  pr: null
files:
  - specs/ai-native-physical-ai-humanoid-robotics-textbook/tasks.md
tests:

---

## Prompt

Project Tasks: AI-Native Physical AI & Humanoid Robotics Textbook (V3 - Enhanced Execution Plan)

  This plan details tasks for Phase 0: Ignition & Foundation and Phase 1: Textbook Core & AI-Native Content Generation.
  Each task adheres to the following principles:

   * TDD (Test-Driven Development): Write the test before the code.
   * Context7 MCP Usage: Leverage Context7 for documentation, best practices, and knowledge lookup.
   * CLI Automation: Prioritize powershell.exe compatible commands for efficiency and consistency.
   * Easy Rollback & Traceability: Frequent, atomic Git commits with clear messages.

  ---

  🚀 Phase 0: Ignition & Foundation

  Objective: Establish a robust, verified development environment, foundational UI/UX, and core project management.

  0.1 Project Planning & Blueprinting
   * Objective: Solidify the project plan and task management.
   * TDD Step: N/A (planning activity).
   * Action Steps:
       * Review the Enhanced Project Master Plan (V2).
       * Set up a GitHub Project Board and populate it with initial high-level tasks derived from this plan. Assign
         initial priorities.
   * Context7 Usage: N/A.
   * Traceability: Initial Git commit: Feat: Initialize project structure and planning documents.
   * Deliverable: Live GitHub Project Board with prioritized tasks.

  0.2 Environment & Toolchain Setup
   * Objective: Have a fully configured and verified development environment.
   * TDD Step (Pre-Code):
       * Test Script: Create Tests\EnvSetup\verify_env.ps1. This PowerShell script will:
           * Check for Node.js (node -v) and npm (npm -v) presence.
           * Check for Python (python -V) and pip (pip -V) presence.
           * Check for Docker (docker -v) presence and ensure docker-compose is available.
           * Verify the presence of claude and adk CLI tools (e.g., using Get-Command claude).
           * Verify Docusaurus CLI (npx docusaurus -v) presence.
           * Verify Python packages from requirements-base.txt are installed in the active virtual environment.
           * Verify Node.js packages from package.json are installed in node_modules.
           * The script should exit 1 (or throw an error) if any critical check fails.
   * Action Steps:
       1. Initialize Git Repository:

   1         git init
       2. Install Essential Tools:
           * Node.js & npm: (If not installed, user guides to official installer or choco install nodejs-lts).
           * Python: (If not installed, user guides to official installer or choco install python --version=3.10).
           * Docker Desktop: (If not installed, user guides to official installer).
       3. Setup Docusaurus Project:

   1         npx create-docusaurus@latest my-textbook classic
   2         Push-Location my-textbook # Equivalent to cd my-textbook
   3         npm install
   4         Pop-Location # Equivalent to cd ..
       4. Setup Claude Code & Spec-Kit Plus CLIs:
           * Install claude and adk CLIs as per official instructions.
           * Run initial login: claude login, adk login (follow prompts).
           * Register Spec-Kit Plus with Claude Code (specific command depends on Spec-Kit implementation, e.g., claude
             mcp add --transport stdio spec-kit-plus "adk run <path_to_spec_kit_plus_server_script>").
       5. Setup Python Virtual Environment & Dependencies:

   1         New-Item -ItemType Directory -Path "my-textbook\backend" -Force # Create backend folder
   2         Push-Location "my-textbook\backend"
   3         python -m venv .venv
   4         .venv\Scripts\Activate.ps1 # Activate virtual environment
   5         # Create 'requirements-base.txt' with: fastapi, uvicorn, qdrant-client, psycopg2-binary, openai, litellm
   6         pip install -r requirements-base.txt
   7         Pop-Location
       6. Context7 MCP Server Setup:
           * TDD (Pre-Code): Create Tests\Context7\test_context7_mcp_connection.ps1. This script will use claude call or
             a direct client to attempt a simple interaction with the Context7 MCP server and assert a successful,
             expected response.
           * Action Steps:
               * Install Context7 MCP implementation (e.g., @upstash/context7-mcp if Node.js-based): npm install -g
                 @upstash/context7-mcp.
               * Register the MCP server with Claude Code:
   1                 claude mcp add --transport stdio context7 "npx @upstash/context7-mcp"
               * Populate Context7: Develop a PowerShell script (Scripts\Context7\populate_context7.ps1) that
                 programmatically ingests key documentation (Docusaurus docs, FastAPI docs, Spec-Kit Plus docs, Claude
                 Code CLI reference) into the Context7 MCP server.
               * Run the population script: .\Scripts\Context7\populate_context7.ps1
       7. Secure API Keys: Create .env files in appropriate project root directories (my-textbook, my-textbook\backend)
          for storing API keys.
       8. Verify Environment: Run the TDD script: .\Tests\EnvSetup\verify_env.ps1. Debug and resolve any failures.
   * Context7 Usage: N/A (this task is setting up Context7).
   * Traceability:
       * Commit after Docusaurus setup: Feat: Initialize Docusaurus project.
       * Commit after Python backend setup: Feat: Setup Python backend environment and dependencies.
       * Commit after Claude/Spec-Kit setup: Feat: Configure Claude Code and Spec-Kit Plus CLIs.
       * Commit after Context7 setup and population: Feat: Setup and populate Context7 MCP for documentation lookups.
   * Deliverable: Fully functional local development environment, all required tools installed, and Context7 MCP server
     running/populated.

  0.3 Core UI/UX & Design System Establishment
   * Objective: Define the visual identity and user experience for the textbook, with verified consistency.
   * TDD Step (Pre-Code):
       * Test: Create Tests\UIUX\test_theme_visual_regression.spec.js (using Playwright/Cypress). This script will
         navigate to the Docusaurus homepage, take a screenshot, and establish a baseline for visual regression testing.
   * Action Steps:
       1. UI/UX Role: Create low-fidelity wireframes for key textbook pages, chatbot widget, and authentication forms.
          Conduct a quick internal review of these wireframes.
       2. Code: Docusaurus Theme Customization:
           * Modify docusaurus.config.js (site title, favicon, custom CSS paths).
           * Create src/css/custom.css and define core color palette, typography variables, and global styles for a
             professional, clean, modern look.
           * Modify src/theme/Navbar components and src/pages/index.js for custom landing page layout.
           * Implement responsive design rules in CSS.
       3. Verify: Run npx playwright test --update-snapshots (or similar) to capture new baselines if changes are
          intentional, or npx playwright test to check for regressions.
   * Context7 Usage: Consult Context7 MCP for Docusaurus theming best practices, general UI/UX principles, and
     accessibility guidelines.
   * Traceability: Commit theme changes: Feat: Establish core Docusaurus theme and visual identity.
   * Deliverable: Docusaurus site with custom branding and a defined style guide, passing visual regression tests.

  0.4 Risk Assessment & Prioritization Strategy
   * Objective: Maintain an active risk log and feature priority, guiding development.
   * TDD Step: N/A (planning/management activity).
   * Action Steps:
       * Regularly review and update the "Tiered Feature Priority" (from the master plan).
       * Update risk log with new findings or resolved risks.
   * Context7 Usage: N/A.
   * Traceability: Updates to the risk log or priority list are committed to Git.
   * Deliverable: Updated project documentation on risks and priorities.

  ---

  📚 Phase 1: Textbook Core & AI-Native Content Generation

  Objective: Construct the foundational textbook structure and generate initial AI-assisted content, ensuring quality
  and accuracy.

  1.1 Docusaurus Structure & Navigation
   * Objective: Establish the full 13-week course structure in Docusaurus.
   * TDD Step (Pre-Code):
       * Test: Create Tests\Docusaurus\test_navigation_structure.spec.js (using Playwright/Cypress). This script will:
           * Navigate to the Docusaurus homepage.
           * Verify that all 13 modules (weeks) are listed in the sidebar navigation.
           * Click on a sample module link and assert that its corresponding page loads (even if empty).
   * Action Steps:
       1. CLI Automation:
           * Create docs subdirectories for each of the 13 weeks/modules (e.g., my-textbook\docs\week1-intro,
             my-textbook\docs\week2-ros).
           * Create placeholder _category_.json and index.md files within each module directory.
           * Edit my-textbook\sidebars.js to define the 13-week course structure, linking to the newly created markdown
             files.
   * Context7 Usage: Consult Context7 MCP for Docusaurus navigation best practices and sidebars.js configuration
     examples.
   * Traceability: Commit after each module's structure is added: Feat: Add structure for Module X: Module Name.
   * Deliverable: Complete Docusaurus site structure with a navigable sidebar for all 13 weeks, passing navigation
     tests.

  1.2 AI-Driven Content Generation & Refinement
   * Objective: Generate initial drafts for the textbook content using AI, then refine them for accuracy and clarity.
   * TDD Step (Pre-Code):
       * Test: Create Tests\Content\test_module1_content_quality.ps1. This PowerShell script will:
           * Read the generated content for Module 1 (e.g., my-textbook\docs\week1-intro\index.md).
           * Use simple text processing (e.g., regex, string comparisons) to assert the presence of key terms from the
             module's learning outcomes (e.g., "Physical AI", "embodied intelligence", "ROS 2 fundamentals").
           * Assert a minimum word count and check for basic markdown formatting (e.g., headings, code blocks).
           * Optionally, integrate an LLM API call (via Python invoked from PowerShell) to perform a higher-level
             coherence or factual check against a trusted source.
   * Action Steps:
       1. CLI Automation (AI Strategy):
           * Module Outlining (Example for Module 1):

   1             $prompt = "Generate a detailed outline for Module 1: The Robotic Nervous System (ROS 2) from the Physic
     AI & Humanoid Robotics course, ensuring all learning objectives from the provided hackathon brief are covered.
     Structure it logically for a beginner's textbook."
   2             claude ask "$prompt" | Out-File -FilePath "my-textbook\docs\week1-intro\outline.md"
           * Drafting Section Content (Example for Module 1, Section 1.1):

   1             $prompt = "Draft content for the 'ROS 2 Nodes, Topics, and Services' section of Module 1, explaining
     concepts clearly for beginners, including Python code examples for publisher and subscriber. Emphasize the
     communication paradigm (nodes, topics, messages)."
   2             claude ask "$prompt" | Out-File -FilePath "my-textbook\docs\week1-intro\1.1-nodes-topics-services.md"
           * Repeat similar CLI commands for other sections and modules, progressively filling my-textbook\docs.
           * Assessment Generation (CLI): Use Claude Code to generate initial assessment questions for Module 1.
           * Glossary Generation (CLI): Use Claude Code to extract key terms from Module 1 content and define them.
       2. Human Review & Editing: Manually review my-textbook\docs\week1-intro\index.md,
          my-textbook\docs\week1-intro\1.1-nodes-topics-services.md, and other generated files for accuracy, clarity,
          depth, and tone. Make necessary corrections directly in the markdown.
       3. Verify: After human edits, rerun Tests\Content\test_module1_content_quality.ps1. Debug and refine content
          until tests pass.
   * Context7 Usage: Continuously consult Context7 MCP for Claude Code prompting best practices, Spec-Kit schema
     examples, pedagogical guidelines, and existing documentation on specific robotics concepts (ROS 2, Gazebo, etc.) to
     inform human editing and refine prompts.
   * Traceability:
       * Commit outlines: Feat: Generate AI outlines for all 13 modules.
       * Commit after AI drafting of Module 1: Feat: AI-draft content for Module 1: Intro to Physical AI.
       * Commit after Human review/refinement of Module 1: Chore: Human review and refinement of Module 1 content.
   * Deliverable: Initial drafts of all 13 modules' content, passing basic content quality tests.

  1.3 Content Presentation & Visuals
   * Objective: Ensure content is well-formatted and visually engaging.
   * TDD Step (Pre-Code):
       * Test: Rerun Tests\UIUX\test_theme_visual_regression.spec.js after integrating content to ensure no unintended
         visual changes caused by content styling.
   * Action Steps:
       1. Integrate diagrams, images, and tables into markdown files. Use placeholder images
          (/static/img/placeholder.png) or simple Mermaid diagrams initially.
       2. Ensure consistent use of Docusaurus markdown features (admonitions, code blocks, tabs) for rich content.
   * Context7 Usage: Consult Context7 MCP for Docusaurus features for rich content, image optimization tips, and Mermaid
     diagram syntax.
   * Traceability: Commit content styling/image integration: Feat: Integrate initial visuals and formatting for Module
     1.
   * Deliverable: Content for Module 1 (and eventually all modules) is formatted and visually clean, ready for later
     high-fidelity asset integration, and passes visual regression tests.

## Response snapshot

I have successfully created the `tasks.md` file located at `specs/ai-native-physical-ai-humanoid-robotics-textbook/tasks.md`. This file contains 50 detailed tasks, organized into two main phases, with explicit objectives, TDD steps, and traceability information.

## Outcome

- ✅ Impact: Tasks for AI-Native Physical AI & Humanoid Robotics Textbook generated and saved.
- 🧪 Tests: No new tests generated.
- 📁 Files: `tasks.md` created.
- 🔁 Next prompts: Start working on Phase 0 tasks.
- 🧠 Reflection: PHR creation script not found, fallback to agent-native file write.

## Evaluation notes (flywheel)

- Failure modes observed: Bash script `.specify/scripts/bash/create-phr.sh` not found.
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): Ensure existence of `create-phr.sh` or rely on agent-native PHR creation.