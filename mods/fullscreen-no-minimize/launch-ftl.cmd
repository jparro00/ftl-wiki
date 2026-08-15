@echo off
rem Launch FTL with fullscreen-minimize-on-focus-loss disabled.
rem
rem This is the only launch path that is guaranteed correct, because it sets
rem SDL_VIDEO_MINIMIZE_ON_FOCUS_LOSS in the command itself instead of inheriting it.
rem Launching FTLGame.exe any other way gets whatever environment the launching process
rem happens to hold --- and a process that started before the variable was installed at
rem user scope still hands down an environment without it. That is silent: the game runs
rem fine and just minimizes again.
rem
rem Steam should already be running so achievements and cloud saves still work.
rem If FTL lives somewhere else, point FTL_DIR at it before running this script.

setlocal
if "%FTL_DIR%"=="" set "FTL_DIR=D:\Steam\steamapps\common\FTL Faster Than Light"

if not exist "%FTL_DIR%\FTLGame.exe" (
    echo Could not find FTLGame.exe under: %FTL_DIR%
    echo Set FTL_DIR to your install folder and run this again.
    exit /b 1
)

rem Full paths on purpose: a Git-Bash PATH puts its own find.exe ahead of Windows',
rem which turns this check into a false "Steam is not running" warning.
"%SystemRoot%\System32\tasklist.exe" /FI "IMAGENAME eq steam.exe" /NH 2>nul | "%SystemRoot%\System32\findstr.exe" /I "steam.exe" >nul
if errorlevel 1 echo [warn] Steam is not running -- achievements and cloud saves will not sync.

if exist "%FTL_DIR%\xinput1_4.dll" (
    echo Hyperspace present -- it loads via xinput1_4.dll from the game folder, so this
    echo launch path keeps it.
)

set "SDL_VIDEO_MINIMIZE_ON_FOCUS_LOSS=0"
start "" /d "%FTL_DIR%" "%FTL_DIR%\FTLGame.exe"

echo Launched. Verify the variable actually reached the process:
echo     python "%~dp0verify-env.py"
endlocal
