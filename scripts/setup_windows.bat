@echo off
echo ================================================
echo   AI Photo Tagger v3.0 - Windows Setup Script
echo ================================================
echo.

:: Check Python installation
echo [1/6] Checking Python installation...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Python not found! Please install Python 3.9+ from python.org
    echo    Download from: https://www.python.org/downloads/
    pause
    exit /b 1
)
echo ✅ Python is installed

:: Check pip
echo [2/6] Checking pip...
pip --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ pip not found! Please reinstall Python with pip
    pause
    exit /b 1
)
echo ✅ pip is available

:: Install Python dependencies
echo [3/6] Installing Python dependencies...
echo    This may take several minutes...
pip install ollama pillow opencv-python rawpy numpy
if %errorlevel% neq 0 (
    echo ❌ Failed to install Python dependencies
    echo    Try running as administrator or check internet connection
    pause
    exit /b 1
)
echo ✅ Python dependencies installed

:: Check/Install Ollama
echo [4/6] Checking Ollama installation...
ollama --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ⚠️  Ollama not found
    echo    Installing Ollama for Windows...
    
    :: Try winget first
    winget install Ollama.Ollama >nul 2>&1
    if %errorlevel% neq 0 (
        echo ❌ Could not install Ollama automatically
        echo    Please install manually from: https://ollama.ai/download
        echo    Then run this script again
        pause
        exit /b 1
    )
    
    :: Refresh PATH
    call RefreshEnv.cmd >nul 2>&1
)
echo ✅ Ollama is installed

:: Check/Install ExifTool
echo [5/6] Checking ExifTool...
exiftool -ver >nul 2>&1
if %errorlevel% neq 0 (
    echo ⚠️  ExifTool not found
    echo    Please install ExifTool manually:
    echo    1. Download from: https://exiftool.org/install.html#Windows
    echo    2. Extract exiftool.exe to a folder
    echo    3. Add that folder to your PATH
    echo    4. Or place exiftool.exe in the same folder as this script
    echo.
    echo    ExifTool is optional but recommended for DNG embedding
    set /p continue="Continue without ExifTool? (y/n): "
    if /i not "%continue%"=="y" (
        echo Setup cancelled
        pause
        exit /b 1
    )
) else (
    echo ✅ ExifTool is installed
)

:: Download AI model
echo [6/6] Setting up AI model...
echo    Starting Ollama service...
start /b ollama serve

:: Wait for service to start
echo    Waiting for Ollama to start...
timeout /t 5 /nobreak >nul

echo    Downloading AI model (this may take 10-15 minutes)...
ollama pull llava:7b
if %errorlevel% neq 0 (
    echo ❌ Failed to download AI model
    echo    Make sure you have internet connection
    echo    You can try manually: ollama pull llava:7b
    pause
    exit /b 1
)
echo ✅ AI model downloaded

:: Create example batch file
echo [BONUS] Creating example batch file...
(
echo @echo off
echo :: AI Photo Tagger v3.0 - Concert Mode Example
echo echo Starting AI Photo Tagger v3.0 in Concert Mode...
echo echo.
echo :: Make sure Ollama is running
echo start /b ollama serve
echo timeout /t 3 /nobreak ^>nul
echo.
echo :: Run the enhanced tagger
echo python AI_Photo_Tagger_v3_Enhanced.py ^
echo     --folder "C:\Users\%USERNAME%\Pictures" ^
echo     --concert-mode ^
echo     --quality-check ^
echo     --blur-threshold 150
echo.
echo pause
) > "Run_Concert_Mode.bat"

echo ✅ Created Run_Concert_Mode.bat

echo.
echo ================================================
echo   🎉 SETUP COMPLETE!
echo ================================================
echo.
echo Next steps:
echo 1. Place AI_Photo_Tagger_v3_Enhanced.py in this folder
echo 2. Run: python AI_Photo_Tagger_v3_Enhanced.py --help
echo 3. Or use: Run_Concert_Mode.bat for concert photography
echo.
echo For concert photography:
echo   Run_Concert_Mode.bat
echo.
echo For regular use:
echo   python AI_Photo_Tagger_v3_Enhanced.py --folder "C:\Path\To\Photos"
echo.
echo ✅ Setup successful! Happy photo tagging!
pause
