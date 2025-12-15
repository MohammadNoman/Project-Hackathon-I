# Gemini Delegator Patterns

## Overview

This skill provides patterns and best practices for delegating tasks to Google Gemini AI models efficiently and effectively.

## Task Formatting for Gemini

### Structure

```markdown
**Context:**
[Brief overview of the project/system]

**Task:**
[Clear, specific task description]

**Constraints:**
- Constraint 1
- Constraint 2

**Expected Output:**
[Description of expected format/content]

**Files to Consider:**
- `path/to/file1.ext`
- `path/to/file2.ext`
```

### Best Practices

1. **Be Specific** - Clearly define what you want
2. **Provide Context** - Include relevant background information
3. **Set Boundaries** - Specify what NOT to do
4. **Request Confirmation** - Ask for verification before execution
5. **Include Examples** - Show desired output format

## Context Limits

### Gemini Pro
- **Token Limit:** ~30,000 tokens (~22,500 words)
- **Best Practice:** Keep prompts under 20,000 tokens for safety
- **Optimization:** Summarize large files rather than including full content

### Gemini 1.5 Pro
- **Token Limit:** 1M tokens for input
- **Best Practice:** Still aim for concise prompts when possible
- **Use Case:** Ideal for analyzing entire codebases

## Error Handling Patterns

### Retry with Clarification
```powershell
# If Gemini returns unclear result:
.\\reusable-intelligence\\dispatch.ps1 `
    -Agent gemini-agent `
    -Task "Previous response was unclear. Please [specific clarification]" `
    -Execute
```

### Progressive Refinement
```powershell
# Start broad, then refine
Task 1: "Analyze file structure"
Task 2: "Based on analysis, suggest improvements"
Task 3: "Implement top 3 improvements"
```

## Common Task Templates

### Code Generation
````
Generate a [language] [component type] that:
- Requirement 1
- Requirement 2
- Requirement 3

Follow these patterns:
- Pattern 1
- Pattern 2

File should be: path/to/new/file.ext
````

### Code Review
````
Review the following code for:
1. Security vulnerabilities
2. Performance issues
3. Code style compliance
4. Best practice violations

Code:
```[language]
[code here]
```

Provide specific line numbers and fix suggestions.
````

### Documentation
````
Create documentation for [component]:

Include:
- Purpose and overview
- API/Interface reference
- Usage examples
- Configuration options

Format: Markdown with code examples
````

## Integration with dispatch.ps1

### Basic Delegation
```powershell
.\\reusable-intelligence\\dispatch.ps1 `
    -Agent gemini-agent `
    -Task "Your task here" `
    -Skills "gemini-delegator" `
    -Execute
```

### With Multiple Skills
```powershell
.\\reusable-intelligence\\dispatch.ps1 `
    -Agent gemini-agent `
    -Task "Build React component" `
    -Skills "gemini-delegator,visual-excellence" `
    -Execute
```

## Response Validation

### Checklist
- [ ] Response addresses the task completely
- [ ] Code (if generated) is syntactically correct
- [ ] Explanations are clear and accurate
- [ ] No hallucinated information
- [ ] Follows project conventions

### If Response is Inadequate
1. Identify specific issues
2. Provide clearer constraints
3. Include examples of desired output
4. Re-delegate with refined prompt

## Performance Optimization

### Reduce Token Usage
1. **Summarize context** - Don't include entire files
2. **Use references** - Point to files instead of including content
3. **Break down tasks** - Multiple small tasks vs. one large task
4. **Cache context** - Reuse context across related tasks

### Improve Response Quality
1. **Provide examples** - Show desired output format
2. **Set explicit constraints** - Define boundaries clearly
3. **Request step-by-step** - Ask for reasoning process
4. **Specify format** - JSON, Markdown, Code, etc.

## Troubleshooting

### Issue: Response Too Generic
**Solution:** Add specific examples and constraints

### Issue: Wrong Technology/Pattern Used
**Solution:** Explicitly list allowed technologies/patterns

### Issue: Incomplete Implementation
**Solution:** Break task into smaller, sequential sub-tasks

### Issue: Hallucinated Information
**Solution:** Request citation of sources, verify factual claims

## Meta-Prompting

For complex tasks, consider using meta-prompting:

```
You are an expert [role]. Your task is to:
1. Analyze the requirements
2. Break down into sub-tasks
3. Prioritize sub-tasks
4. Generate implementation plan
5. Implement each sub-task

Requirements:
[Your requirements]

For each implementation, provide:
- File path
- Complete code
- Brief explanation
```

---

**Version:** 1.0  
**Last Updated:** 2025-12-12  
**Compatibility:** Gemini Pro, Gemini 1.5 Pro, Gemini 2.0
