# Implementation Plan - Agent & Skill Standardization

## Goal Description
Standardize all agent and skill definitions in `.claude/` with proper YAML frontmatter and unified format. This enables the AI system to correctly identify capabilities, tools, and roles for each agent.

## Proposed Changes

### Agents (.claude/agents/)
Update frontmatter for all agents. Replace existing frontmatter if present, otherwise prepend.

#### [MODIFY] [better-auth-agent.md](file:///C:/Users/SM%20TRADERs/Downloads/Hackathon-1/.claude/agents/better-auth-agent.md)
- Replace existing frontmatter with standardized definition.

#### [MODIFY] [chatkit-agent.md](file:///C:/Users/SM%20TRADERs/Downloads/Hackathon-1/.claude/agents/chatkit-agent.md)
- Add/Update frontmatter.

#### [MODIFY] [content-agent.md](file:///C:/Users/SM%20TRADERs/Downloads/Hackathon-1/.claude/agents/content-agent.md)
- Add/Update frontmatter.

#### [MODIFY] [nextjs-agent.md](file:///C:/Users/SM%20TRADERs/Downloads/Hackathon-1/.claude/agents/nextjs-agent.md)
- Add/Update frontmatter.

#### [MODIFY] [personalization-agent.md](file:///C:/Users/SM%20TRADERs/Downloads/Hackathon-1/.claude/agents/personalization-agent.md)
- Add/Update frontmatter.

#### [MODIFY] [sdk-agent.md](file:///C:/Users/SM%20TRADERs/Downloads/Hackathon-1/.claude/agents/sdk-agent.md)
- Add/Update frontmatter.

#### [MODIFY] [testing-agent.md](file:///C:/Users/SM%20TRADERs/Downloads/Hackathon-1/.claude/agents/testing-agent.md)
- Add/Update frontmatter.

#### [MODIFY] [ui-worker-gemini.md](file:///C:/Users/SM%20TRADERs/Downloads/Hackathon-1/.claude/agents/ui-worker-gemini.md)
- Prepend frontmatter.

### Skills (.claude/skills/)
Ensure all skills have `SKILL.md` with correct metadata.

#### [NEW] [visual-excellence/SKILL.md](file:///C:/Users/SM%20TRADERs/Downloads/Hackathon-1/.claude/skills/visual-excellence/SKILL.md)
- Create new SKILL.md (or rename manifest.md).

#### [NEW] [docusaurus-patterns/SKILL.md](file:///C:/Users/SM%20TRADERs/Downloads/Hackathon-1/.claude/skills/docusaurus-patterns/SKILL.md)
- Create SKILL.md.

#### [NEW] [fastapi-patterns/SKILL.md](file:///C:/Users/SM%20TRADERs/Downloads/Hackathon-1/.claude/skills/fastapi-patterns/SKILL.md)
- Create SKILL.md.

#### [NEW] [gemini-delegator/SKILL.md](file:///C:/Users/SM%20TRADERs/Downloads/Hackathon-1/.claude/skills/gemini-delegator/SKILL.md)
- Create SKILL.md.

#### [NEW] [qwen-delegator/SKILL.md](file:///C:/Users/SM%20TRADERs/Downloads/Hackathon-1/.claude/skills/qwen-delegator/SKILL.md)
- Create SKILL.md.

#### [NEW] [grok-delegator/SKILL.md](file:///C:/Users/SM%20TRADERs/Downloads/Hackathon-1/.claude/skills/grok-delegator/SKILL.md)
- Create new directory and SKILL.md.

### Commands (.claude/commands/)

#### [NEW] [token-log.md](file:///C:/Users/SM%20TRADERs/Downloads/Hackathon-1/.claude/commands/token-log.md)
- Create token tracking command.

## Verification Plan
1.  **Manual Check**: Verify that all files exist and contain the correct YAML frontmatter.
2.  **File Listing**: List all modified/created files as requested by the user.
