# Project Cleanup Script
# This script safely reorganizes the Hackathon-1 project structure

Write-Host "=== Hackathon-1 Project Cleanup ===" -ForegroundColor Cyan
Write-Host ""

# Step 0: Backup
Write-Host "[Step 0] Creating backup..." -ForegroundColor Yellow
$backupName = "Hackathon-1-backup-$(Get-Date -Format 'yyyyMMdd-HHmmss')"
$backupPath = "..\$backupName"

try {
    Copy-Item -Path "." -Destination $backupPath -Recurse -Force -ErrorAction Stop
    Write-Host "✓ Backup created at: $backupPath" -ForegroundColor Green
} catch {
    Write-Host "✗ Backup failed: $_" -ForegroundColor Red
    Write-Host "ABORTING cleanup for safety." -ForegroundColor Red
    exit 1
}

Write-Host ""

# Step 1: Create frontend directory if it doesn't exist
Write-Host "[Step 1] Creating frontend/ directory..." -ForegroundColor Yellow
if (!(Test-Path "frontend")) {
    New-Item -ItemType Directory -Path "frontend" -Force | Out-Null
    Write-Host "✓ frontend/ directory created" -ForegroundColor Green
} else {
    Write-Host "⚠ frontend/ already exists - will merge content" -ForegroundColor Yellow
}

Write-Host ""

# Step 2: Move Docusaurus content
Write-Host "[Step 2] Moving Docusaurus from false/ to frontend/..." -ForegroundColor Yellow
$sourcePath = "false\001-physical-ai-textbook-docs"

if (Test-Path $sourcePath) {
    try {
        Get-ChildItem -Path $sourcePath | ForEach-Object {
            Move-Item -Path $_.FullName -Destination "frontend\" -Force -ErrorAction Stop
            Write-Host "  Moved: $($_.Name)" -ForegroundColor Gray
        }
        Write-Host "✓ Docusaurus content moved successfully" -ForegroundColor Green
    } catch {
        Write-Host "✗ Move failed: $_" -ForegroundColor Red
        Write-Host "Restore from backup: $backupPath" -ForegroundColor Red
        exit 1
    }
} else {
    Write-Host "⚠ Source path not found: $sourcePath" -ForegroundColor Yellow
}

Write-Host ""

# Step 3: Verify frontend has content
Write-Host "[Step 3] Verifying frontend/ structure..." -ForegroundColor Yellow
$requiredFiles = @("package.json", "docusaurus.config.ts", "docs")
$verification = $true

foreach ($file in $requiredFiles) {
    if (Test-Path "frontend\$file") {
        Write-Host "  ✓ Found: $file" -ForegroundColor Gray
    } else {
        Write-Host "  ✗ Missing: $file" -ForegroundColor Red
        $verification = $false
    }
}

if (!$verification) {
    Write-Host "✗ Verification failed - restore from backup!" -ForegroundColor Red
    exit 1
} else {
    Write-Host "✓ Frontend structure verified" -ForegroundColor Green
}

Write-Host ""

# Step 4: Delete junk folders
Write-Host "[Step 4] Removing empty/junk folders..." -ForegroundColor Yellow

$foldersToDelete = @(
    "false",
    "TRADERsDownloadsHackathon-1specs001-physical-ai-textbook",
    "Module_10_Robot_Human_Interaction",
    "Module_13_Humanoid_Robotics_AI",
    "Hackathon I- Physical AI & Humanoid Robotics Textbook",
    "CUsersSM"
)

foreach ($folder in $foldersToDelete) {
    if (Test-Path $folder) {
        try {
            Remove-Item -Path $folder -Recurse -Force -ErrorAction Stop
            Write-Host "  ✓ Deleted: $folder" -ForegroundColor Gray
        } catch {
            Write-Host "  ⚠ Could not delete: $folder ($_)" -ForegroundColor Yellow
        }
    } else {
        Write-Host "  - Doesn't exist: $folder" -ForegroundColor DarkGray
    }
}

Write-Host "✓ Cleanup complete" -ForegroundColor Green
Write-Host ""

# Step 5: Show final structure
Write-Host "[Step 5] Final project structure:" -ForegroundColor Yellow
Get-ChildItem -Directory | Select-Object Name, @{Name="Items";Expression={(Get-ChildItem $_.FullName -ErrorAction SilentlyContinue | Measure-Object).Count}} | Format-Table -AutoSize

Write-Host ""
Write-Host "=== Cleanup Complete ===" -ForegroundColor Cyan
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "1. Test Docusaurus: cd frontend; npm install; npm run start" -ForegroundColor White
Write-Host "2. Update GitHub workflow to use 'working-directory: ./frontend'" -ForegroundColor White
Write-Host "3. Start backend development with @chatkit-agent" -ForegroundColor White
Write-Host ""
Write-Host "Backup location: $backupPath" -ForegroundColor Cyan
