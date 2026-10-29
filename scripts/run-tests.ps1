# Run InterviewAI Backend Automated Tests
Set-Location -Path "$PSScriptRoot\..\backend"
Write-Host "Running Backend Automated Test Suite..." -ForegroundColor Cyan
.\venv\Scripts\python -m pytest -v

