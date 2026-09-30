@echo off
title Matromani - Stop Server

echo ======================================================================
echo          Stopping Matromani Server on Port 5000...
echo ======================================================================
echo.

for /f "tokens=5" %%a in ('netstat -aon ^| findstr :5000 ^| findstr LISTENING') do (
    echo [*] Found process %%a on port 5000. Terminating...
    taskkill /f /pid %%a >nul 2>&1
    echo [OK] Process %%a terminated.
)

echo.
echo [OK] Matromani server stopped successfully.
pause
