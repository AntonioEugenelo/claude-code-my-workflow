@echo off
REM sync-overleaf-scheduled.bat — Wrapper for Windows Task Scheduler
REM Runs the Overleaf sync script via Git Bash
"C:\Program Files\Git\bin\bash.exe" -c "C:/CustomTools/claude-code-my-workflow/scripts/sync-overleaf.sh sync"
