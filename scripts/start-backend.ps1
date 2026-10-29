# Start InterviewAI Backend API Server
Set-Location -Path "$PSScriptRoot\..\backend"
Write-Host "Starting InterviewAI Backend on http://127.0.0.1:8000..." -ForegroundColor Cyan
.\venv\Scripts\uvicorn app.main:app --reload --host 127.0.0.1 --port 8000

