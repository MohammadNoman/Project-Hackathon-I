<!--
Sync Impact Report:
Version change: Initial creation (N/A -> 1.0.0)
Modified principles: N/A (newly defined)
Added sections: I. Guiding Principles & Project Vision, II. Core Project Requirements (Mandatory for Base Functionality), III. Recommended Development Practices (for Bonus Points), IV. Quality Standards, V. Technical Environment & Simulation Guidelines, VI. Project Focus & Learning Objectives (Course Overview)
Removed sections: N/A
Templates requiring updates:
  - .specify/templates/plan-template.md: ⚠ pending
  - .specify/templates/spec-template.md: ⚠ pending
  - .specify/templates/tasks-template.md: ⚠ pending
  - .specify/templates/commands/*.md: ⚠ pending
  - README.md: ⚠ pending
  - docs/quickstart.md: ⚠ pending
  - agent-specific guidance files: ⚠ pending
Follow-up TODOs: None
-->
# Physical AI & Humanoid Robotics Textbook Constitution

## I. Guiding Principles & Project Vision

### Educational Clarity
The primary goal is to create an accessible, effective, and engaging learning resource for students, fostering a deep understanding of Physical AI and Humanoid Robotics.

### Innovation & Experimentation
Embrace cutting-edge AI tools and approaches within the specified frameworks, pushing the boundaries of AI-driven textbook creation and interactive learning.

### User-Centric Design
Prioritize a smooth, intuitive, and visually appealing user experience for both the textbook content and all integrated features (e.g., chatbot, personalization, translation).

### Embodied Intelligence Focus
All design and implementation decisions should reinforce the core vision of "bridging the gap between the digital brain and the physical body" and exploring "embodied intelligence."

### Open Source Spirit
(If applicable) Adhere to best practices for open-source projects, including clear documentation and maintainable code, particularly for components that might be shared or extended.

## II. Core Project Requirements (Mandatory for Base Functionality)

### Textbook Platform & Deployment
The textbook must be developed using Docusaurus and deployed to GitHub Pages.

### AI/Spec-Driven Content Generation
All book content creation must leverage Spec-Kit Plus and Claude Code for efficient and structured development.

### Integrated RAG Chatbot
A Retrieval-Augmented Generation (RAG) chatbot must be seamlessly embedded within the published book.
*   Technology Stack: The chatbot will be built using OpenAI Agents/ChatKit SDKs, FastAPI, Neon Serverless Postgres database, and Qdrant Cloud Free Tier.
*   Functionality: The chatbot must accurately answer user questions based on the book's content, including providing answers from user-selected text snippets, demonstrating a deep understanding of the material.

## III. Recommended Development Practices (for Bonus Points)

### Advanced AI Automation
Implement and utilize Claude Code Subagents and Agent Skills to enhance the book project's development and content generation processes, showcasing reusable intelligence.

### User Authentication
Integrate robust user Signup and Signin functionality using `better-auth.com`. The signup process should include questions about the user's software and hardware background to enable intelligent content personalization.

### Personalized Content
Implement a feature that allows logged-in users to personalize chapter content via a dedicated button at the start of each chapter, adapting to their stated background.

### Content Localization
Provide functionality for logged-in users to translate chapter content into Urdu via a dedicated button at the start of each chapter, enhancing accessibility.

## IV. Quality Standards

### Content Accuracy & Depth
The textbook content must be technically accurate, up-to-date, comprehensive, and tailored to the learning outcomes of the Physical AI & Humanoid Robotics course.

### Code Quality
All implemented code (for the chatbot, authentication, personalization, etc.) must be clean, modular, maintainable, well-commented, and follow established coding standards.

### Documentation
Provide clear and concise documentation, including project READMEs, API documentation (if applicable), and explanations for complex logic.

### Performance & Reliability
Ensure that the chatbot and all interactive features are responsive, stable, and perform efficiently under typical user loads.

### Accessibility
Strive to make the textbook and its interactive elements accessible to a broad range of users, considering diverse needs.

## V. Technical Environment & Simulation Guidelines

### Development Workstation
For local development, prioritize high-performance workstations equipped with NVIDIA RTX GPUs (e.g., RTX 4070 Ti or higher with adequate VRAM), powerful CPUs (Intel Core i7 13th Gen+ or AMD Ryzen 9), and at least 64GB DDR5 RAM. The recommended operating system is Ubuntu 22.04 LTS for optimal compatibility with robotics frameworks.

### Edge Computing & Physical AI
Integrate NVIDIA Jetson Orin Nano/NX kits, Intel RealSense D435i/D455 cameras, and USB IMUs to facilitate hands-on learning, physical deployment exercises, and understanding resource constraints in real-world scenarios.

### Robotic Hardware (Lab)
When demonstrating physical interactions, utilize appropriate robotic platforms such as Unitree Go2/G1, Robotis OP3, or Hiwonder TonyPi Pro, acknowledging their specific capabilities and limitations (e.g., efficiency with NVIDIA Isaac ROS) to align with course modules.

### Cloud-Native Simulation (Alternative)
If local high-performance hardware is inaccessible, leverage cloud-based instances (e.g., AWS g5.2xlarge/g6e.xlarge with A10G GPU) for simulation using NVIDIA Isaac Sim on Omniverse Cloud. Acknowledge and mitigate latency challenges for real robot control by training models in the cloud and deploying weights to local edge devices.

## VI. Project Focus & Learning Objectives (Course Overview)

### Core Theme
The textbook will meticulously cover "AI Systems in the Physical World" and "Embodied Intelligence," explicitly bridging the gap between digital AI theory and practical applications in physical robotics.

### Educational Goal
To equip students with the advanced knowledge and practical skills necessary to design, simulate, and effectively control humanoid robots in both simulated and real-world environments.

### Key Technologies Covered
In-depth exploration and practical application of ROS 2, Gazebo, Unity, and the NVIDIA Isaac platform (including Isaac Sim, Isaac ROS, and Nav2).

### Advanced Concepts
Detailed coverage of Vision-Language-Action (VLA) models, including the seamless integration of Large Language Models (LLMs) like OpenAI Whisper for voice commands and cognitive planning, to enable natural and intelligent human-robot interaction.

## Governance
All amendments to this constitution require documentation, explicit approval from project leads, and a clear migration plan for any affected components. All team members must verify compliance during code reviews and development activities.

**Version**: 1.0.0 | **Ratified**: 2025-11-30 | **Last Amended**: 2025-11-30
