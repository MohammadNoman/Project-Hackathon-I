# Qwen Delegator Skill

Delegate text generation and coding tasks to Alibaba's Qwen CLI to conserve Claude tokens.

## When to Use This Skill

- Alternative to Gemini for text generation
- Coding assistance tasks
- Technical documentation generation
- Multilingual content (especially Chinese/English)

## Prerequisites

Qwen CLI must be installed on the system.

## Commands

### Generate Text
```powershell
qwen -p "Your prompt here"
```

### Code Generation
```powershell
qwen --code -p "Write a FastAPI endpoint for user authentication"
```

## Integration Pattern for Claude

When delegating to Qwen:

1. **Prepare the prompt** - Format the task clearly
2. **Execute via PowerShell**:
```powershell
$result = qwen -p "Your task description" 
```
3. **Capture and use the result** in your workflow

## Example Delegation

**Task**: Generate Python code for RAG implementation

```powershell
$prompt = @"
Write a Python function that:
1. Connects to Qdrant vector database
2. Performs similarity search
3. Returns top 5 results with metadata
Use async/await patterns.
"@

$code = qwen --code -p $prompt
Write-Output $code
```

## Token Savings

Similar to Gemini delegator - significant token conservation for large generation tasks.

## Limitations

- Qwen may have different capabilities than Claude
- Results must be captured and applied manually
- Requires internet connection
