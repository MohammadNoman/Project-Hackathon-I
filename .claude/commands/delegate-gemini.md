---
description: Delegate a task to Gemini CLI to save Claude tokens
---

Execute the following task using Gemini CLI and return the result:

$ARGUMENTS

Steps:
1. Use the gemini-delegator skill to properly format the command
2. Execute via PowerShell: `gemini -p "task description"`
3. Capture and return the result

This command is useful for:
- Large text generation tasks
- Content summarization
- Research tasks
- Bulk content creation

Example usage:
```
/delegate-gemini Generate a 1000-word summary of ROS2 architecture
```
