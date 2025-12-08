---
description: Delegate a task to Qwen CLI to save Claude tokens
---

Execute the following task using Qwen CLI and return the result:

$ARGUMENTS

Steps:
1. Use the qwen-delegator skill to properly format the command
2. Execute via PowerShell: `qwen -p "task description"`
3. Capture and return the result

This command is useful for:
- Code generation tasks
- Technical documentation
- Alternative to Gemini for text generation
- Multilingual content (especially Chinese/English)

Example usage:
```
/delegate-qwen Write a Python function for vector similarity search with Qdrant
```
