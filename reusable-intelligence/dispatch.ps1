# Agent Dispatch Script
# Purpose: Delegate tasks to Gemini/Qwen agents with skill context
# Usage: .\reusable-intelligence\dispatch.ps1 -Agent <agent> -Task "<task>" [-Skills <skills>] [-Execute]

param(
    [Parameter(Mandatory=$true)]
    [string]$Agent,
    
    [Parameter(Mandatory=$true)]
    [string]$Task,
    
    [string]$Skills = "",
    
    [switch]$Execute
)

# Color output function
function Write-ColorOutput {
    param([string]$Message, [string]$Color = "White")
    Write-Host $Message -ForegroundColor $Color
}

# Main execution
Write-ColorOutput "`n========================================" "Cyan"
Write-ColorOutput "  Agent Dispatch System v1.0" "Cyan"
Write-ColorOutput "========================================`n" "Cyan"

# Determine script directory
$ScriptDir = if ($PSScriptRoot) { $PSScriptRoot } else { Split-Path -Parent $MyInvocation.MyCommand.Path }
$ProjectRoot = Split-Path -Parent $ScriptDir

Write-ColorOutput "Script directory: $ScriptDir" "DarkGray"
Write-ColorOutput "Project root: $ProjectRoot`n" "DarkGray"

# Step 1: Validate agent exists
$agentsDir = Join-Path -Path $ProjectRoot -ChildPath ".claude"
$agentsDir = Join-Path -Path $agentsDir -ChildPath "agents"
$agentPath = Join-Path -Path $agentsDir -ChildPath "$Agent.md"

Write-ColorOutput "DEBUG: Agent path = $agentPath" "DarkGray"
Write-ColorOutput "DEBUG: Testing path..." "DarkGray"

if (!(Test-Path -Path $agentPath -PathType Leaf)) {
    Write-ColorOutput "[X] ERROR: Agent not found: $Agent" "Red"
    Write-ColorOutput "   Expected location: $agentPath" "Gray"
    Write-ColorOutput "`nAvailable agents:" "Yellow"
    
    if (Test-Path -Path $agentsDir -PathType Container) {
        Get-ChildItem -Path $agentsDir -Filter "*.md" | ForEach-Object {
            Write-ColorOutput "  - $($_.BaseName)" "Gray"
        }
    } else {
        Write-ColorOutput "  [X] Agents directory not found: $agentsDir" "Red"
    }
    exit 1
}

Write-ColorOutput "[OK] Agent found: $Agent" "Green"
Write-ColorOutput "  Location: $agentPath`n" "Gray"

# Step 2: Load agent instructions
try {
    if ([string]::IsNullOrWhiteSpace($agentPath)) {
        throw "Agent path is null or empty"
    }
    
    Write-ColorOutput "DEBUG: Loading agent from: $agentPath" "DarkGray"
    
    $agentInstructions = Get-Content -Path $agentPath -Raw
    
    if ([string]::IsNullOrWhiteSpace($agentInstructions)) {
        throw "Agent instructions are empty"
    }
    
    $instructionLength = $agentInstructions.Length
    Write-ColorOutput "[OK] Agent instructions loaded ($instructionLength characters)" "Green"
} catch {
    Write-ColorOutput "[X] ERROR: Failed to load agent instructions" "Red"
    Write-ColorOutput "  Error: $($_.Exception.Message)" "Gray"
    Write-ColorOutput "  Path attempted: $agentPath" "Gray"
    exit 1
}

# Step 3: Load skills if specified
$skillContext = ""
if ($Skills) {
    $skillsBaseDir = Join-Path -Path $ProjectRoot -ChildPath ".claude"
    $skillsBaseDir = Join-Path -Path $skillsBaseDir -ChildPath "skills"
    $skillPath = Join-Path -Path $skillsBaseDir -ChildPath $Skills
    
    if (Test-Path -Path $skillPath -PathType Container) {
        Write-ColorOutput "[OK] Loading skill: $Skills" "Green"
        
        # Load all .md files in the skill directory
        $skillFiles = Get-ChildItem -Path $skillPath -Recurse -Filter "*.md"
        
        if ($skillFiles.Count -eq 0) {
            Write-ColorOutput "  [!] Warning: Skill directory is empty" "Yellow"
        } else {
            $skillContext = $skillFiles | ForEach-Object {
                $fileName = $_.Name
                $content = Get-Content -Path $_.FullName -Raw
                Write-ColorOutput "  - Loaded: $fileName ($($content.Length) chars)" "Gray"
                "## Skill: $fileName`n$content"
            } | Join-String -Separator "`n`n"
            
            Write-ColorOutput "[OK] Skill context assembled ($($skillContext.Length) characters)`n" "Green"
        }
    } else {
        Write-ColorOutput "[!] Warning: Skill not found: $Skills" "Yellow"
        Write-ColorOutput "  Expected location: $skillPath`n" "Gray"
    }
}

# Step 4: Build delegation context
Write-ColorOutput "[TASK] Task Details:" "Cyan"
Write-ColorOutput "  Agent: $Agent" "White"
Write-ColorOutput "  Task: $Task" "White"
if ($Skills) {
    Write-ColorOutput "  Skills: $Skills" "White"
}
Write-ColorOutput ""

# Step 5: Execute or dry-run
if ($Execute) {
    Write-ColorOutput "[RUN] EXECUTION MODE" "Cyan"
    Write-ColorOutput "========================================`n" "Cyan"
    
    # TODO: Integrate with Gemini/Qwen CLI
    # This is where you would call the actual CLI tool
    # Example integrations:
    
    # For Gemini:
    # $prompt = "$agentInstructions`n`n## Task`n$Task`n`n## Available Skills`n$skillContext"
    # & gemini-cli --prompt $prompt
    
    # For Qwen:
    # $prompt = "$agentInstructions`n`n## Task`n$Task`n`n## Available Skills`n$skillContext"
    # & qwen-cli --prompt $prompt
    
    Write-ColorOutput "[!] Gemini/Qwen CLI integration not yet implemented" "Yellow"
    Write-ColorOutput "`nTo complete integration:" "Cyan"
    Write-ColorOutput "  1. Install Gemini or Qwen CLI tool" "Gray"
    Write-ColorOutput "  2. Configure API keys in backend/.env" "Gray"
    Write-ColorOutput "  3. Uncomment and customize CLI call above" "Gray"
    Write-ColorOutput "`nAgent file ready at: $agentPath" "Gray"
    
    # Save context to temp file for manual testing
    $tempFile = Join-Path $ScriptDir "last-dispatch-context.txt"
    @"
AGENT: $Agent
TASK: $Task
SKILLS: $Skills

========================================
AGENT INSTRUCTIONS
========================================
$agentInstructions

========================================
SKILL CONTEXT
========================================
$skillContext
"@ | Set-Content $tempFile
    
    Write-ColorOutput "`nContext saved to: $tempFile" "Green"
    
} else {
    Write-ColorOutput "[DRY RUN] DRY RUN MODE (use -Execute to run)" "DarkGray"
    Write-ColorOutput "========================================`n" "DarkGray"
    
    Write-ColorOutput "Would execute with Gemini/Qwen CLI:" "DarkGray"
    Write-ColorOutput "  - Agent context: $instructionLength characters" "DarkGray"
    if ($skillContext) {
        Write-ColorOutput "  - Skill context: $($skillContext.Length) characters" "DarkGray"
    }
    Write-ColorOutput "  - Task: $Task" "DarkGray"
}

Write-ColorOutput "`n========================================" "Cyan"
Write-ColorOutput "  Dispatch Complete" "Cyan"
Write-ColorOutput "========================================`n" "Cyan"
