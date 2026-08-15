@echo off
rem Launch FTL with fullscreen-minimize-on-focus-loss disabled, without setting the
rem variable system-wide. Steam should already be running so achievements and cloud
rem saves still work.
rem
rem If FTL lives somewhere else, point FTL_DIR at it before running this script.

setlocal
if "%FTL_DIR%"=="" set "FTL_DIR=D:\Steam\steamapps\common\FTL Faster Than Light"

if not exist "%FTL_DIR%\FTLGame.exe" (
    echo Could not find FTLGame.exe under: %FTL_DIR%
    echo Set FTL_DIR to your install folder and run this again.
    exit /b 1
)

set "SDL_VIDEO_MINIMIZE_ON_FOCUS_LOSS=0"
start "" /d "%FTL_DIR%" "%FTL_DIR%\FTLGame.exe"
endlocal
