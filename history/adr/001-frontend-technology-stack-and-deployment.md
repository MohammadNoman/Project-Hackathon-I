---
id: 001
title: Frontend Technology Stack and Deployment
status: Accepted
date: 2025-12-02
context: The project requires a robust and easily deployable platform for an AI-Native Textbook. Key considerations include ease of content creation, documentation-focused features, and cost-effective hosting for a hackathon.
decision: The frontend will be built using Docusaurus, a static site generator, and deployed to GitHub Pages.
consequences:
  - Positive: Leverages Docusaurus's built-in documentation features (markdown support, search, versioning), simplifying content management. GitHub Pages provides free, highly available hosting, reducing infrastructure overhead. Aligns with mandatory tech stack constraints.
  - Negative: Customization beyond Docusaurus's intended use cases might require more effort. Relying on GitHub Pages ties deployment to GitHub.
alternatives:
  - name: Other Static Site Generators (e.g., Next.js, Gatsby)
    consequences: While flexible, these would require more effort to implement documentation-specific features already present in Docusaurus. Deployment might be more complex for a static site.
  - name: Dynamic Web Frameworks (e.g., React with custom backend)
    consequences: Overkill for the static textbook portion, significantly increasing complexity and deployment overhead for a hackathon project. Does not align with the documentation-centric nature of a textbook.
references:
  - specs/001-physical-ai-textbook/plan.md
  - specs/001-physical-ai-textbook/spec.md
---

## Decision: Frontend Technology Stack and Deployment

The AI-Native Textbook project will utilize **Docusaurus** as its frontend technology stack due to its specialized features for documentation-focused websites, including robust markdown support, built-in search capabilities, and content versioning. This choice aligns directly with the project's core requirement to function as a textbook.

For deployment, the Docusaurus site will be hosted on **GitHub Pages**. This provides a cost-effective, highly available, and straightforward deployment solution for a static website, which is particularly advantageous given the hackathon's time constraints and focus on rapid iteration and demonstration.

This decision is in direct accordance with the mandatory technology stack requirements outlined in the project specification (specs/001-physical-ai-textbook/spec.md) and the implementation plan (specs/001-physical-ai-textbook/plan.md).