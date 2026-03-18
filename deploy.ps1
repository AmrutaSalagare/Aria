#requires -Version 5.0
<#
.SYNOPSIS
Aria Job Search - Full GitHub Deployment Script
.DESCRIPTION
This script automates the GitHub setup process
#>

$ErrorActionPreference = "Stop"

Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "Aria Job Search - GitHub Deployment" -ForegroundColor Yellow
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host ""

$GITHUB_USERNAME = "AmrutaSalagare"
$REPO_NAME = "aria-job-search"
$BOT_TOKEN = "8649568407:AAEFvjsHUR20LtFnAjeb0A1C69ZBoSv3Hvg"
$CHAT_ID = "5201142003"
$REPO_URL = "https://github.com/$GITHUB_USERNAME/$REPO_NAME.git"

Write-Host "Your GitHub Setup Information:" -ForegroundColor Green
Write-Host "  GitHub Username: $GITHUB_USERNAME"
Write-Host "  Repository: $REPO_NAME"
Write-Host "  Full URL: $REPO_URL"
Write-Host ""

Write-Host "IMPORTANT: Before continuing, you MUST:" -ForegroundColor Yellow
Write-Host ""
Write-Host "1. Create GitHub Repository:"
Write-Host "   → Go to https://github.com/new"
Write-Host "   → Name: $REPO_NAME"
Write-Host "   → Visibility: Public"
Write-Host "   → Click 'Create repository'"
Write-Host ""
Write-Host "2. Add GitHub Secrets:"
Write-Host "   → Go to: https://github.com/$GITHUB_USERNAME/$REPO_NAME/settings/secrets/actions"
Write-Host "   → Click 'New repository secret'"
Write-Host "   → Name: TELEGRAM_BOT_TOKEN"
Write-Host "   → Value: $BOT_TOKEN"
Write-Host "   → Click 'Add secret'"
Write-Host ""
Write-Host "   → Click 'New repository secret' again"
Write-Host "   → Name: TELEGRAM_CHAT_ID"
Write-Host "   → Value: $CHAT_ID"
Write-Host "   → Click 'Add secret'"
Write-Host ""

$confirm = Read-Host "Have you completed steps 1 and 2 above? (yes/no)"

if ($confirm -ne "yes" -and $confirm -ne "y") {
    Write-Host "Please complete the setup manually first. Exiting." -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "Proceeding with code push..." -ForegroundColor Green
Write-Host ""

$projectPath = "d:\openclaw-amruta"
Set-Location $projectPath

# Configure git with GitHub credentials
Write-Host "Configuring git repository..." -ForegroundColor Cyan

try {
    git remote add origin $REPO_URL
    Write-Host "✓ Remote added" -ForegroundColor Green
} catch {
    Write-Host "⚠ Remote might already exist, trying to update..." -ForegroundColor Yellow
    git remote set-url origin $REPO_URL
    Write-Host "✓ Remote updated" -ForegroundColor Green
}

# Ensure main branch
Write-Host "Setting up main branch..." -ForegroundColor Cyan
git branch -M main
Write-Host "✓ Branch set to main" -ForegroundColor Green

# Push code
Write-Host ""
Write-Host "Pushing code to GitHub..." -ForegroundColor Cyan
Write-Host "(You may be asked to authenticate with GitHub)" -ForegroundColor Yellow
Write-Host ""

try {
    git push -u origin main
    Write-Host ""
    Write-Host "✓ Code pushed successfully!" -ForegroundColor Green
} catch {
    Write-Host "ERROR: Failed to push code" -ForegroundColor Red
    Write-Host "Please ensure:" -ForegroundColor Yellow
    Write-Host "  1. Git is installed"
    Write-Host "  2. GitHub repo exists at: $REPO_URL"
    Write-Host "  3. You're authenticated with GitHub"
    exit 1
}

Write-Host ""
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host "✓ DEPLOYMENT COMPLETE!" -ForegroundColor Green
Write-Host "=========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "Your automation is now LIVE!" -ForegroundColor Green
Write-Host ""
Write-Host "Next steps:" -ForegroundColor Yellow
Write-Host "1. View your repo: $REPO_URL"
Write-Host "2. Go to 'Actions' tab"
Write-Host "3. Click 'Run workflow' to test (optional)"
Write-Host "4. Tomorrow at 6 AM IST, automation runs automatically"
Write-Host "5. Check Telegram for daily job reports"
Write-Host ""
Write-Host "Your automation runs daily at: 6:00 AM IST (00:30 UTC)" -ForegroundColor Cyan
Write-Host ""
