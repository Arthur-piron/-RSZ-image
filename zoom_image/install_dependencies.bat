@echo off
setlocal

echo ----------------------------------------
echo   RESIZE IMAGE - Dependency Installer
echo ----------------------------------------

REM Check if Python is installed
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [INFO] Python is not installed. Starting download...

    REM Download the latest Python installer silently
    powershell -Command "Invoke-WebRequest -Uri 'https://www.python.org/ftp/python/3.12.3/python-3.12.3-amd64.exe' -OutFile 'python-installer.exe'"

    echo [INFO] Installing Python silently...
    start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1 Include_test=0

    del python-installer.exe

    REM Re-check if Python is installed
    python --version >nul 2>&1
    if %errorlevel% neq 0 (
        echo [ERROR] Python installation failed. Please install it manually from:
        echo         https://www.python.org/downloads/
        pause
        exit /b 1
    )
)

REM Check pip
python -m pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [INFO] Pip not found. Installing pip...
    python -m ensurepip --upgrade
)

REM Upgrade pip to the latest version
echo [INFO] Upgrading pip...
python -m pip install --upgrade pip

REM Check if install.txt exists
if not exist install.txt (
    echo [ERROR] install.txt not found! Please create a file called install.txt in the same directory as this script.
    pause
    exit /b 1
)

REM Install required packages from install.txt
echo [INFO] Installing dependencies from install.txt...
pip install -r install.txt

REM Check for tkinter (used by easygui)
python -c "import tkinter" >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo [WARNING] tkinter is not available on your system.
    echo You must install it manually:
    echo - On Windows: Reinstall Python with tkinter enabled
    pause
) else (
    echo [INFO] tkinter is available.
)

echo.
echo ✅ All dependencies installed successfully!
pause
endlocal
