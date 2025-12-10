<#
.SYNOPSIS
    Assembles a "Worker Prompt" by combining a specific Agent Persona, selected Skills, and a specific Task.
    Designed to generate a prompt that can be pasted into a high-context LLM (Gemini 1.5 Pro, Qwen 2.5, etc.).

.DESCRIPTION
    The script:
    1. Reads the Agent Definition (from /agents).
    2. Reads the Skill Patterns (from /skills).
    3. Wraps the User's Task with these contexts.
    4. Outputs the combined prompt to the Clipboard (default) or Console.

.PARAMETER Agent
    The name of the agent file (without extension) in the 'agents' directory. E.g., 'nextjs-agent'.

.PARAMETER Task
    The description of the work to be done.

.PARAMETER Skills
    A list of skill folder names or file paths to include. E.g., 'visual-excellence', 'docusaurus-patterns'.

.PARAMETER Print
    If set, outputs the result to the console instead of copying to clipboard.
    
.PARAMETER Execute
    If set, attempts to pipe the result to the 'gemini' CLI and output the response.

.EXAMPLE
    .\dispatch.ps1 -Agent nextjs-agent -Task "Build a login page" -Skills visual-excellence, better-auth-patterns
#>

param (
    [Parameter(Mandatory=$true)]
    [string]$Agent,

    [Parameter(Mandatory=$true)]
    [string]$Task,

    [string[]]$Skills = @(),

    [switch]$Print,
    
    [switch]$Execute
)

$ErrorActionPreference = "Stop"
$ScriptDir = Split-Path $MyInvocation.MyCommand.Path
$AgentsDir = Join-Path $ScriptDir "agents"
$SkillsDir = Join-Path $ScriptDir "skills"

# --- 1. Load Agent Persona ---
$AgentFile = Join-Path $AgentsDir "$Agent.md"
if (-not (Test-Path $AgentFile)) {
    Write-Error "Agent file not found: $AgentFile"
    exit 1
}
$AgentContent = Get-Content $AgentFile -Raw

# --- 2. Load Skills ---
$SkillsContent = ""
foreach ($Skill in $Skills) {
    # Try directory first (looking for SKILL.md or README.md inside)
    $SkillPath = Join-Path $SkillsDir $Skill
    if (Test-Path $SkillPath -PathType Container) {
        $SkillFile = Get-ChildItem -Path $SkillPath -Filter "*.md" | 
                     Where-Object { $_.Name -match "^(SKILL|README)\.md$" } | 
                     Select-Object -First 1
        
        if ($SkillFile) {
            $Content = Get-Content $SkillFile.FullName -Raw
            $SkillsContent += "`n`n--- SKILL: $Skill ---`n$Content"
        } else {
            Write-Warning "No SKILL.md or README.md found in skill folder: $Skill"
        }
    } else {
        # Try direct file
        if (-not $Skill.EndsWith(".md")) { $Skill = "$Skill.md" }
        $SkillFile = Join-Path $SkillsDir $Skill
        if (Test-Path $SkillFile) {
            $Content = Get-Content $SkillFile -Raw
            $SkillsContent += "`n`n--- SKILL: $Skill ---`n$Content"
        } else {
            Write-Warning "Skill not found: $Skill"
        }
    }
}

# --- 3. Assemble Prompt ---
$FinalPrompt = @"
<!-- WORKER PROMPT START -->
$AgentContent

# CONTEXT & SKILLS
The Architect (Claude) has provided the following skills/patterns for this task:
$SkillsContent

# YOUR TASK
$Task

# INSTRUCTIONS FOR WORKER
1. Act as the Agent described above.
2. Use the provided Skills/Patterns as your reference.
3. Generate the implementation code.
<!-- WORKER PROMPT END -->
"@

# --- 4. Output or Execution ---
if ($Print) {
    Write-Host $FinalPrompt
}
elseif ($Execute) {
    # Check for Gemini CLI
    if (Get-Command "gemini" -ErrorAction SilentlyContinue) {
    Write-Host "DELEGATING task to Gemini..." -ForegroundColor Cyan
        
        # Create a temporary file to store the prompt (safer for large prompts)
        $TempFile = [System.IO.Path]::GetTempFileName()
        $FinalPrompt | Set-Content -Path $TempFile -Encoding UTF8

        try {
            # Strategy: Pipe to gemini
            # Using -p explicitly with content
            
            # Since we can't easily pipe in all environments within PowerShell logic cleanly without complexity,
            # we will pass it as argument. If too long, this might fail, but it's the simplest start.
            
            $Output = gemini -p "$FinalPrompt" 2>&1
            
            Write-Host "`nGemini has responded:`n" -ForegroundColor Green
            Write-Output $Output
        }
        catch {
            Write-Error "Failed to execute Gemini: $_"
        }
        finally {
            Remove-Item $TempFile -ErrorAction SilentlyContinue
        }
    }
    else {
        Write-Warning "Gemini CLI ('gemini') not found. Copying to clipboard instead."
        Set-Clipboard -Value $FinalPrompt
        Write-Host "Copied prompt to clipboard."
    }
}
else {
    Set-Clipboard -Value $FinalPrompt
    Write-Host "Worker Prompt assembled and copied to CLIPBOARD." -ForegroundColor Green
    Write-Host "Paste this into Gemini 1.5 Pro or Qwen."
}
