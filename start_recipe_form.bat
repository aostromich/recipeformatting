@echo off
cd /d "%~dp0"

echo Starting recipe form...
start "" http://127.0.0.1:8000

python main_web.py

pause
