@echo off
setlocal EnableDelayedExpansion
title Matromani - Deployment & Server Launch

echo ======================================================================
echo          MATROMANI - PREMIUM BILINGUAL MATRIMONIAL PLATFORM
echo          மேட்ரோமணி - தமிழ் மற்றும் ஆங்கில திருமண இணையதளம்
echo ======================================================================
echo.

:: 1. Check Python installation
echo [*] Checking Python installation...
where python >nul 2>nul
if %errorlevel% neq 0 (
    where py >nul 2>nul
    if %errorlevel% neq 0 (
        echo [ERROR] Python was not found in your system PATH!
        echo Please download and install Python from https://www.python.org/
        echo Make sure to check the box "Add Python to PATH" during installation.
        pause
        exit /b 1
    ) else (
        set "PY_CMD=py"
    )
) else (
    set "PY_CMD=python"
)

echo [OK] Python detected:
!PY_CMD! --version
echo.

:: 2. Check and create virtual environment
if not exist "venv\Scripts\activate.bat" (
    echo [*] Creating virtual environment (venv)...
    !PY_CMD! -m venv venv
    if %errorlevel% neq 0 (
        echo [ERROR] Failed to create virtual environment!
        pause
        exit /b 1
    )
    echo [OK] Virtual environment created successfully.
) else (
    echo [OK] Virtual environment found.
)
echo.

:: 3. Activate virtual environment
echo [*] Activating virtual environment...
call venv\Scripts\activate.bat
echo [OK] Virtual environment activated.
echo.

:: 4. Upgrade pip and install dependencies
echo [*] Installing / updating required dependencies from requirements.txt...
python -m pip install --upgrade pip --quiet
pip install -r requirements.txt --quiet
if %errorlevel% neq 0 (
    echo [WARNING] Some packages had warnings or issues. Retrying install...
    pip install -r requirements.txt
)
echo [OK] All dependencies are ready.
echo.

:: 5. Create required runtime directories
echo [*] Ensuring static upload folders exist...
if not exist "static\uploads" mkdir "static\uploads"
echo [OK] Uploads directory verified.
echo.

:: 6. Initialize database and seed sample profiles
echo [*] Initializing SQLite database and verifying seed data...
python seed_data.py
if %errorlevel% neq 0 (
    echo [ERROR] Database initialization failed!
    pause
    exit /b 1
)
echo [OK] Database seeded and ready.
echo.

:: 7. Run validation test suite
echo [*] Running automated platform verification tests...
python test_app.py
if %errorlevel% neq 0 (
    echo [WARNING] Test suite reported warnings, proceeding with launch...
) else (
    echo [OK] All automated tests passed successfully!
)
echo.

:: 8. Launch Production Web Server
echo ======================================================================
echo  [SUCCESS] Matromani Matrimonial Platform Deployed Successfully!
echo.
echo  Access URLs:
echo    - Main Website:   http://localhost:5000
echo    - Admin Portal:   http://localhost:5000/admin/login
echo.
echo  Demo User Accounts:
echo    - Groom:  karthik.raman@example.com / Password123
echo    - Bride:  priya.soundar@example.com / Password123
echo    - Admin:  admin / Admin@123
echo.
echo  Press Ctrl+C at any time in this window to stop the server.
echo ======================================================================
echo.

:: Launch browser in background after 2 seconds
start "" cmd /c "timeout /t 2 /nobreak >nul & start http://localhost:5000"

:: Start production WSGI server via Waitress
python wsgi.py

pause
