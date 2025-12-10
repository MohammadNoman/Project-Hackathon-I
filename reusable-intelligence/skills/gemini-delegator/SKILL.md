# Gemini Delegator Skill

Delegate text generation and research tasks to Google Gemini CLI to conserve Claude tokens.

## When to Use This Skill

- Large text generation (content writing, summaries)
- Research and web search tasks
- Bulk content processing
- Tasks that don't require Claude's precise coding capabilities

## Prerequisites

Gemini CLI must be installed on the system.

## Commands

### Generate Text
```powershell
gemini -p "Your prompt here"
```

### Interactive Chat
```powershell
gemini chat
```

## Integration Pattern for Claude

When delegating to Gemini:

1. **Prepare the prompt** - Format the task clearly
2. **Execute via PowerShell**:
```powershell
$result = gemini -p "Summarize the following text about ROS2..." 
```
3. **Capture and use the result** in your workflow

## Example Delegation

**Task**: Generate module outline for Physical AI textbook

```powershell
$prompt = @"
Generate a detailed outline for a textbook module on ROS2.
Include: learning objectives, key concepts, code examples, assessments.
"@

$outline = gemini -p $prompt
Write-Output $outline
```

## Token Savings

| Task Type | Claude Tokens | Gemini Delegation |
|-----------|---------------|-------------------|
| 1000-word summary | ~2000 tokens | ~50 tokens |
| Research task | ~5000 tokens | ~100 tokens |
| Bulk content | ~10000 tokens | ~200 tokens |
