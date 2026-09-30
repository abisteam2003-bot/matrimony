@echo off
title Matromani - Development Server (Auto-Reload)

echo ======================================================================
echo          MATROMANI - DEVELOPMENT SERVER (DEBUG MODE)
echo ======================================================================
echo.

if exist "venv\Scripts\activate.bat" (
    call venv\Scripts\activate.bat
)

set FLASK_ENV=development
set FLASK_DEBUG=1

start "" cmd /c "timeout /t 2 /nobreak >nul & start http://localhost:5000"

python app.py
pause
