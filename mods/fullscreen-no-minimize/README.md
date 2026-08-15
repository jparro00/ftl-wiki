# fullscreen-no-minimize

Keeps FTL's fullscreen window up on one 4K monitor while you click around on the other,
instead of minimizing the moment the game loses focus.

**This is not a Slipstream `.ftl` mod.** Window behaviour lives in the engine, not in
`ftl.dat`, so no data mod can touch it. What this *is*: a documented runtime switch the
engine already reads, plus the scripts to set it.

---

## The mechanism

FTL 1.6.x on Windows is built on **SIL** (System Interface Library, by Andrew Church —
who did the 1.6 ports). SIL's Windows video backend handles `WM_ACTIVATE` like this:

```c
if (!window_focused && window_fullscreen && should_minimize_fullscreen()) {
    ShowWindow(hwnd, SW_MINIMIZE);
}
```

— `src/sysdep/windows/graphics.c:2656-2660`

So the minimize is **deliberate engine behaviour**, not Windows reclaiming an exclusive
display mode. That matters, because it means no resolution you pick will avoid it. And
`should_minimize_fullscreen()` is:

```c
static int should_minimize_fullscreen(void)
{
    if (minimize_fullscreen >= 0) {
        return minimize_fullscreen;
    }

    /* If the SDL hint variable is present, use it to override default
     * behavior. */
    const char *sdl_hint = windows_getenv("SDL_VIDEO_MINIMIZE_ON_FOCUS_LOSS");
    if (sdl_hint && *sdl_hint) {
        return strcmp(sdl_hint, "0") != 0 && stricmp(sdl_hint, "false") != 0;
    }

    /* Otherwise, always minimize. */
    return 1;
}
```

— `src/sysdep/windows/graphics.c:3069-3084`

`windows_getenv()` is a thin wrapper over `GetEnvironmentVariable()`
(`src/sysdep/windows/util.c:165`), so an ordinary process environment variable is all it
takes. SIL borrows SDL's variable name for compatibility even though FTL doesn't use SDL
on Windows — the string `SDL_VIDEO_MINIMIZE_ON_FOCUS_LOSS` is present verbatim in
`FTLGame.exe`, confirming this code path shipped in the retail build.

**The switch:** `SDL_VIDEO_MINIMIZE_ON_FOCUS_LOSS=0` in the game's environment.

`minimize_fullscreen` starts at `-1` ("client hasn't specified"), which is why the
environment variable gets a say at all. If FTL itself ever called
`graphics_set_display_attr("fullscreen_minimize_on_focus_loss", …)` the variable would be
ignored — the smoke test below is what proves it doesn't.

---

## What you get

The fullscreen window is `WS_POPUP | WS_VISIBLE` and is placed `HWND_TOPMOST`
(`graphics.c:1221`). With the minimize suppressed, clicking the other monitor moves focus
there and leaves FTL drawn full-screen on its own monitor — which is the behaviour you'd
expect from borderless fullscreen, without running the game windowed.

---

## Install

```powershell
powershell -ExecutionPolicy Bypass -File mods\fullscreen-no-minimize\install.ps1
```

Sets the variable at **user** scope, permanently. Then **restart Steam** — Steam hands its
own environment to the games it launches, so a Steam that was already running when you
installed will still start FTL with the old environment. After that, launch FTL normally.

To undo:

```powershell
powershell -ExecutionPolicy Bypass -File mods\fullscreen-no-minimize\install.ps1 -Uninstall
```

### Scope note

The variable is SDL's, so it also applies to any SDL game you launch afterwards — the
effect there is identical: fullscreen stops minimizing on focus loss. On a two-monitor
desktop that's generally what you want. If you'd rather keep it to FTL alone, use
`launch-ftl.cmd` instead of installing: it sets the variable for one process and starts
the game directly (Steam must already be running for achievements and cloud saves).

---

## Optional: avoid the display-mode switch too

Separate from the minimize, SIL calls `ChangeDisplaySettingsEx(…, CDS_FULLSCREEN)` whenever
the requested fullscreen size differs from the monitor's current mode. It skips that
entirely when the sizes match:

```c
if (refresh_rate==0 && width==device_width && height==device_height) {
    fullscreen_mode = -1;   /* no ChangeDisplaySettingsEx call */
}
```

— `graphics.c:1106-1112`

Your monitors run 3840×2160, so picking **3840×2160** in FTL's options means no real mode
change happens — the game is then just a topmost popup window at desktop size. That avoids
the window-shuffling other apps do when a mode switch fires. It is not required for the
minimize fix; it's polish.

If the in-game list doesn't offer it, force it in
`%APPDATA%\FasterThanLight\settings.ini`:

```ini
manual=1
screen_x=3840
screen_y=2160
windowed=0
stretched=0
```

(That block is the game's own escape hatch — the file says so: *"Set manual to 1 and then
change the resolution. Does not check if values are valid."*)

---

## Smoke test

1. Launch FTL, confirm fullscreen.
2. Click a window on the other monitor.
3. FTL should stay drawn full-screen on its monitor; the taskbar should not show it as
   minimized.

If it still minimizes, the variable didn't reach the process. Confirm it's set:

```powershell
[Environment]::GetEnvironmentVariable('SDL_VIDEO_MINIMIZE_ON_FOCUS_LOSS','User')
```

and confirm Steam was restarted after install — that's the usual culprit, since FTL
inherits Steam's environment, not the one you edited afterwards.

---

## Sources

- SIL, `src/sysdep/windows/graphics.c` — https://achurch.org/SIL/current/src/sysdep/windows/graphics.c
- SIL, `src/sysdep/windows/util.c` — https://achurch.org/SIL/current/src/sysdep/windows/util.c
- SIL project page — https://achurch.org/SIL/
- `FTLGame.exe` 1.6.14 (Steam build) — string table contains
  `SDL_VIDEO_MINIMIZE_ON_FOCUS_LOSS`, `fullscreen_minimize_on_focus_loss`, `SILWindowClass`
