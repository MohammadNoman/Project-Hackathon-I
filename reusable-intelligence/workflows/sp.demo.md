---
description: Generate demo video script and preparation materials for project showcase
---

# Demo Preparation Command

Generate comprehensive demo materials using the @content-agent.

## Usage

```
/sp.demo [duration] [audience]
```

**Parameters:**
- `duration` - Video length: `30s`, `60s`, `90s` (default: 90s)
- `audience` - Target: `judges`, `developers`, `students`, `general`

## What This Command Creates

### 1. Demo Script
- Timestamped narration
- Visual cues for each segment
- Key talking points
- Transitions

### 2. Storyboard Outline
- Scene-by-scene breakdown
- Screen captures needed
- Feature demonstration order

### 3. Recording Checklist
- Environment setup
- Browser/app state preparation
- Test data to have ready
- Equipment checklist

### 4. Key Messages
- Elevator pitch (10 seconds)
- Problem statement
- Solution highlights
- Unique value proposition

## Demo Structure (90 seconds)

```
[0:00-0:05]  HOOK - Grab attention
[0:05-0:15]  PROBLEM - Why this matters
[0:15-0:25]  SOLUTION - What we built
[0:25-0:70]  DEMO - Show key features
[0:70-0:85]  HIGHLIGHTS - Tech stack, achievements
[0:85-0:90]  CTA - Call to action
```

## Best Practices

### DO:
- Start with your most impressive feature
- Show, don't tell
- Use real interactions (not mockups)
- Keep transitions smooth
- End with clear next step

### DON'T:
- Don't show loading screens
- Don't read code line by line
- Don't rush through features
- Don't use placeholder content
- Don't exceed time limit

## Delegation

This command delegates to `@content-agent` for:
- Script writing (isolated context)
- Storyboard creation
- Checklist generation
- Marketing copy

Saves tokens by running content generation in agent context.
