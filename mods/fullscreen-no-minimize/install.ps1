<#
.SYNOPSIS
    Stops FTL's fullscreen window from minimizing when it loses focus.

.DESCRIPTION
    Sets SDL_VIDEO_MINIMIZE_ON_FOCUS_LOSS=0 at user scope. FTL 1.6.x on Windows is built
    on SIL, whose should_minimize_fullscreen() reads that variable via
    GetEnvironmentVariable() and skips the ShowWindow(hwnd, SW_MINIMIZE) call in its
    WM_ACTIVATE handler when it is "0" or "false".

    See README.md for the source references.

.PARAMETER Uninstall
    Remove the variable instead of setting it.
#>
[CmdletBinding()]
param(
    [switch]$Uninstall
)

$ErrorActionPreference = 'Stop'
$name = 'SDL_VIDEO_MINIMIZE_ON_FOCUS_LOSS'
$current = [Environment]::GetEnvironmentVariable($name, 'User')

if ($Uninstall) {
    if ($null -eq $current) {
        Write-Host "$name is not set at user scope. Nothing to do."
    } else {
        [Environment]::SetEnvironmentVariable($name, $null, 'User')
        Write-Host "Removed $name (was '$current')."
        Write-Host "Restart Steam for the change to reach newly launched games."
    }
    return
}

if ($current -eq '0') {
    Write-Host "$name is already 0. Nothing to do."
} else {
    if ($null -ne $current) {
        Write-Host "$name was '$current'; overwriting with 0."
    }
    [Environment]::SetEnvironmentVariable($name, '0', 'User')
    Write-Host "Set $name=0 at user scope."
}

# Also set it for this process tree, so a game launched from this shell picks it up now.
$env:SDL_VIDEO_MINIMIZE_ON_FOCUS_LOSS = '0'

Write-Host ''
Write-Host 'Next step: restart Steam.'
Write-Host '  Steam passes its own environment to the games it launches, so a Steam that'
Write-Host '  was already running will still start FTL without this variable.'
Write-Host ''
Write-Host 'Then launch FTL normally and click a window on the other monitor:'
Write-Host '  the game should stay drawn full-screen instead of minimizing.'
