---
id: 1
title: Initial Project Constitution
stage: constitution
date: 2025-11-30
surface: agent
model: claude-sonnet-4-5-20250929
feature: none
branch: master
user: user
command: /sp.constitution
labels: [project, constitution, hackathon]
links:
  spec: null
  ticket: null
  adr: null
  pr: null
files:
  - .specify/memory/constitution.md
tests:

---

## Prompt

""" You are an expert project manager and technical writer. I'm participating in a hackathon focused on creating a
      "Textbook for Teaching Physical AI & Humanoid Robotics Course." The goal is to bridge the gap between digital AI a
      the physical world through humanoid robots.
    2
    3 I need you to generate a comprehensive project constitution for this hackathon project. This constitution should
      serve as a foundational document, guiding our development efforts, defining key requirements, and setting quality
      standards.
    4
    5 Please structure the constitution with the following main sections, and ensure each section is detailed,
      prescriptive, and covers all relevant aspects of the project, including technologies, tools, development practices
      and project philosophy:
    6
    7 1.  **I. Guiding Principles & Project Vision**
    8 2.  **II. Core Project Requirements (Mandatory for Base Functionality)**
    9 3.  **III. Recommended Development Practices (for Bonus Points)**
   10 4.  **IV. Quality Standards**
   11 5.  **V. Technical Environment & Simulation Guidelines**
   12 6.  **VI. Project Focus & Learning Objectives (Course Overview)**
   13
   14 Here is an example of a well-structured and detailed project constitution for a similar project. Please use this a
      a reference for the expected depth, detail, and formatting, but generate a fresh constitution that addresses all
      aspects as if you were creating it from scratch based on the project description:
  Project Constitution: Physical AI & Humanoid Robotics Textbook

  I. Guiding Principles & Project Vision

   1. Educational Clarity: The primary goal is to create an accessible, effective, and engaging learning resource for
      students, fostering a deep understanding of Physical AI and Humanoid Robotics.
   2. Innovation & Experimentation: Embrace cutting-edge AI tools and approaches within the specified frameworks,
      pushing the boundaries of AI-driven textbook creation and interactive learning.
   3. User-Centric Design: Prioritize a smooth, intuitive, and visually appealing user experience for both the textbook
      content and all integrated features (e.g., chatbot, personalization, translation).
   4. Embodied Intelligence Focus: All design and implementation decisions should reinforce the core vision of "bridging
      the gap between the digital brain and the physical body" and exploring "embodied intelligence."
   5. Open Source Spirit: (If applicable) Adhere to best practices for open-source projects, including clear
      documentation and maintainable code, particularly for components that might be shared or extended.

  II. Core Project Requirements (Mandatory for Base Functionality)

   1. Textbook Platform & Deployment: The textbook must be developed using Docusaurus and deployed to GitHub Pages.
   2. AI/Spec-Driven Content Generation: All book content creation must leverage Spec-Kit Plus and Claude Code for
      efficient and structured development.
   3. Integrated RAG Chatbot: A Retrieval-Augmented Generation (RAG) chatbot must be seamlessly embedded within the
      published book.
       * Technology Stack: The chatbot will be built using OpenAI Agents/ChatKit SDKs, FastAPI, Neon Serverless Postgres
         database, and Qdrant Cloud Free Tier.
       * Functionality: The chatbot must accurately answer user questions based on the book's content, including
         providing answers from user-selected text snippets, demonstrating a deep understanding of the material.

  III. Recommended Development Practices (for Bonus Points)

   1. Advanced AI Automation: Implement and utilize Claude Code Subagents and Agent Skills to enhance the book project's
      development and content generation processes, showcasing reusable intelligence.
   2. User Authentication: Integrate robust user Signup and Signin functionality using `better-auth.com`. The signup
      process should include questions about the user's software and hardware background to enable intelligent content
      personalization.
   3. Personalized Content: Implement a feature that allows logged-in users to personalize chapter content via a
      dedicated button at the start of each chapter, adapting to their stated background.
   4. Content Localization: Provide functionality for logged-in users to translate chapter content into Urdu via a
      dedicated button at the start of each chapter, enhancing accessibility.

  IV. Quality Standards

   1. Content Accuracy & Depth: The textbook content must be technically accurate, up-to-date, comprehensive, and
      tailored to the learning outcomes of the Physical AI & Humanoid Robotics course.
   2. Code Quality: All implemented code (for the chatbot, authentication, personalization, etc.) must be clean,
      modular, maintainable, well-commented, and follow established coding standards.
   3. Documentation: Provide clear and concise documentation, including project READMEs, API documentation (if
      applicable), and explanations for complex logic.
   4. Performance & Reliability: Ensure that the chatbot and all interactive features are responsive, stable, and
      perform efficiently under typical user loads.
   5. Accessibility: Strive to make the textbook and its interactive elements accessible to a broad range of users,
      considering diverse needs.

  V. Technical Environment & Simulation Guidelines

   1. Development Workstation: For local development, prioritize high-performance workstations equipped with NVIDIA RTX
      GPUs (e.g., RTX 4070 Ti or higher with adequate VRAM), powerful CPUs (Intel Core i7 13th Gen+ or AMD Ryzen 9), and
      at least 64GB DDR5 RAM. The recommended operating system is Ubuntu 22.04 LTS for optimal compatibility with
      robotics frameworks.
   2. Edge Computing & Physical AI: Integrate NVIDIA Jetson Orin Nano/NX kits, Intel RealSense D435i/D455 cameras, and
      USB IMUs to facilitate hands-on learning, physical deployment exercises, and understanding resource constraints in
      real-world scenarios.
   3. Robotic Hardware (Lab): When demonstrating physical interactions, utilize appropriate robotic platforms such as
      Unitree Go2/G1, Robotis OP3, or Hiwonder TonyPi Pro, acknowledging their specific capabilities and limitations
      (e.g., efficiency with NVIDIA Isaac ROS) to align with course modules.
   4. Cloud-Native Simulation (Alternative): If local high-performance hardware is inaccessible, leverage cloud-based
      instances (e.g., AWS g5.2xlarge/g6e.xlarge with A10G GPU) for simulation using NVIDIA Isaac Sim on Omniverse
      Cloud. Acknowledge and mitigate latency challenges for real robot control by training models in the cloud and
      deploying weights to local edge devices.

  VI. Project Focus & Learning Objectives (Course Overview)

   1. Core Theme: The textbook will meticulously cover "AI Systems in the Physical World" and "Embodied Intelligence,"
      explicitly bridging the gap between digital AI theory and practical applications in physical robotics.
   2. Educational Goal: To equip students with the advanced knowledge and practical skills necessary to design,
      simulate, and effectively control humanoid robots in both simulated and real-world environments.
   3. Key Technologies Covered: In-depth exploration and practical application of ROS 2, Gazebo, Unity, and the NVIDIA
      Isaac platform (including Isaac Sim, Isaac ROS, and Nav2).
   4. Advanced Concepts: Detailed coverage of Vision-Language-Action (VLA) models, including the seamless integration of
      Large Language Models (LLMs) like OpenAI Whisper for voice commands and cognitive planning, to enable natural and
      intelligent human-robot interaction."""

## Response snapshot

The project constitution for the "Physical AI & Humanoid Robotics Textbook" hackathon project has been successfully generated and saved to `.specify/memory/constitution.md`.

## Outcome

- ✅ Impact: Project constitution established
- 🧪 Tests: N/A
- 📁 Files: Created .specify/memory/constitution.md
- 🔁 Next prompts: Review other templates for consistency, begin spec generation
- 🧠 Reflection: Successfully generated project constitution based on user requirements and template.

## Evaluation notes (flywheel)

- Failure modes observed: N/A
- Graders run and results (PASS/FAIL): N/A
- Prompt variant (if applicable): N/A
- Next experiment (smallest change to try): N/A
