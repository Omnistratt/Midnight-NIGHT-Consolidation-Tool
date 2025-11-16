@echo off
REM Windows Batch file to start the Midnight Consolidation Tool
REM Double-click this file to start!

title Midnight Consolidation Tool

echo.
echo ============================================================
echo Starting Midnight Consolidation Tool...
echo ============================================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ERROR: Python is not installed!
    echo.
    echo Please install Python from: https://www.python.org/downloads/
    echo Make sure to check "Add Python to PATH" during installation.
    echo.
    pause
    exit /b 1
)

REM Start the tool
python START_TOOL.py

pause
