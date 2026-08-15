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

**In the game's environment** is the whole difficulty. A process environment is fixed when
the process is created and inherited from whoever created it. Setting the variable at user
scope does not reach a process that is already running — including whatever will later
launch the game. So the question is never "is the variable set?" but "did it reach
`FTLGame.exe`?", and those two answers come apart silently: the game runs perfectly and
just minimizes again. `verify-env.py` answers the second question directly, by reading the
running game's own environment block.

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

## Files

| File | What it does |
|------|--------------|
| `install.ps1` | Sets the variable at user scope, permanently (`-Uninstall` removes it) |
| `launch-ftl.cmd` | Launches FTL with the variable set in the command — the reliable path |
| `verify-env.py` | Reads the **running** game's environment and says PASS/FAIL |

---

## Install

```powershell
powershell -ExecutionPolicy Bypass -File mods\fullscreen-no-minimize\install.ps1
```

Sets the variable at **user** scope, permanently. Then **restart Steam** — Steam hands its
own environment to the games it launches, so a Steam that was already running when you
installed will still start FTL with the old environment. After that, launch FTL normally.

Or skip the ambient environment entirely and launch through
`mods\fullscreen-no-minimize\launch-ftl.cmd`, which needs no install and no Steam restart.
Either way, `verify-env.py` is what tells you it took.

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

## Hyperspace

Hyperspace does not break this fix and cannot: it never touches the code path.

- It replaces `FTLGame.exe` (retail 1.6.22, 5.5 MB) with the downgraded-and-patched 1.6.14
  build it needs (125 MB), keeping the original as `FTLGame_orig.exe`, and injects itself
  through `xinput1_4.dll` in the game folder. So `FTLGame.exe` is a **different binary**
  than the one this mod was written against — worth re-checking, and it checks out:
  `SDL_VIDEO_MINIMIZE_ON_FOCUS_LOSS` and `fullscreen_minimize_on_focus_loss` are both still
  in its string table, i.e. the same SIL backend with the same switch.
- `Hyperspace.dll` contains neither string. Its hook log (`zhl.log`) resolves
  `CApp::OnInputFocus`, `CApp::UpdateFullScreen` and `CApp::UpdateWindowSettings` but
  installs hooks on none of them — of 1118 hooks, not one is on focus or fullscreen
  handling.

What Hyperspace does change is **how the game gets launched**, and that is the whole story
of why the fix appears to stop working. Any launch path other than "a process that already
had the variable" produces a game that minimizes. Confirmed failing paths:

- Launched from a shell that started before the variable was installed — including a
  Claude Code Bash/PowerShell tool call, which inherits the agent's own stale environment.
  This is how it broke on 2026-08-15: the running game's environment held `CLAUDECODE=1`
  and no SDL variable, while Steam's environment two processes away held the variable fine.
- Launched by a Steam that has been running since before the install.

`launch-ftl.cmd` is immune to all of them, because it sets the variable in the command
rather than inheriting it. **Use it for every launch, including agent-driven ones.**

---

## Smoke test

**Check the process, not the setting.** With FTL running:

```powershell
python mods\fullscreen-no-minimize\verify-env.py
```

It reads the running `FTLGame.exe`'s environment block out of its PEB (read-only; it never
writes to the game) and prints PASS or FAIL, and on FAIL it names the launcher that is
responsible. Exit code 0 = the game will not minimize.

Then confirm by hand:

1. Launch FTL, confirm fullscreen.
2. Click a window on the other monitor.
3. FTL should stay drawn full-screen on its monitor; the taskbar should not show it as
   minimized.

If `verify-env.py` says PASS and it still minimizes, that is the one remaining unknown
below — the engine, not the launch path.

---

## Still unverified

Whether FTL itself ever calls `graphics_set_display_attr("fullscreen_minimize_on_focus_loss", …)`.
If it does, `minimize_fullscreen` is pinned `>= 0` and the environment variable is inert no
matter how cleanly it is delivered. Nothing in either binary settles it. The proof is a
launch that `verify-env.py` reports as PASS which still minimizes on focus loss — every
failure observed so far has been a FAIL, i.e. the delivery, not the engine.

---

## Sources

- SIL, `src/sysdep/windows/graphics.c` — https://achurch.org/SIL/current/src/sysdep/windows/graphics.c
- SIL, `src/sysdep/windows/util.c` — https://achurch.org/SIL/current/src/sysdep/windows/util.c
- SIL project page — https://achurch.org/SIL/
- `FTLGame.exe` 1.6.14 (Steam build) — string table contains
  `SDL_VIDEO_MINIMIZE_ON_FOCUS_LOSS`, `fullscreen_minimize_on_focus_loss`, `SILWindowClass`
