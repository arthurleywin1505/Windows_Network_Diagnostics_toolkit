@echo off
cd /d "%~dp0.."
echo Starting Windows Network Diagnostics Toolkit...
python main.py
if errorlevel 1 (
  echo.
  echo Error starting project. Check that Python is installed and added to PATH.
  pause
)
