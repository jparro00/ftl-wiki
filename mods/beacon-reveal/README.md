# Beacon Reveal — an FTL mod

Labels every beacon on the sector map, **whether or not you have explored it**. A map spoiler,
on purpose.

Each beacon gets a boxed label in the game's own style, showing the **category** it was rolled
from — `DISTRESS_BEACON_ENGI`, `STORE_ENGI`, `HOSTILE_ENGI` — colour-coded like the vanilla
`STORE` and `EXIT` tags. **Hover a beacon** and the game's own tooltip — the one that normally
says *"An unvisited location."* — tells you the event instead: `Pirate ship distress trap`.

```
   ┌──────────────────────┐        ┌────────────┐
   │ DISTRESS_BEACON_ENGI │        │ STORE_ENGI │
   └──────────┬───────────┘        └─────┬──────┘
              ( o )────────────────────( o )
                 ↖ cursor
                  ┌────────────────────────────┐
                  │ Pirate ship distress trap  │  <- the game's own tooltip
                  └────────────────────────────┘
```

The categories are the sector event pools from `sector_data.xml`, scoped to the sector you are
in. The event names are the titles from this wiki's event cards — the same strings the
[event-labels](../event-labels/) mod prints above the event text. An event with no card shows
its raw id instead; the mod never invents a name.

**Draws only.** No event, choice, requirement, reward, ship or probability is changed, and
nothing is written to your save. 386 events are named.

## Requires Hyperspace

The sector map is drawn by compiled code, so no ordinary FTL mod can put text above a beacon.
This one runs as a Lua script under [FTL Hyperspace](https://ftl-hyperspace.github.io/FTL-Hyperspace/),
which exposes the star map to scripts.

Hyperspace only runs on **FTL 1.6.9**, and its installer downgrades 1.6.14 for you. The
versions in between add only a Japanese translation and Steam achievements, so the game itself
is unchanged — but Steam achievements stop unlocking while you are downgraded.

## Install

Already installed on this machine. Hyperspace 1.22.2 is in the game folder, and all three mods
are patched in. To re-patch after a rebuild:

```powershell
cd C:\Users\jparr\Documents\Slipstream
java -jar modman.jar --patch Hyperspace.ftl event-labels.ftl beacon-reveal.ftl
```

Hyperspace must come first — this mod adds itself to Hyperspace's script list, which has to
exist already.

From scratch elsewhere: install Hyperspace per its own guide, drop `beacon-reveal.ftl` into
Slipstream's `mods/` folder, and patch it after `Hyperspace.ftl`.

## Uninstall

Untick it and patch again. To remove Hyperspace as well, delete `Hyperspace.dll` from the game
folder, then delete `FTLGame.exe` and rename `FTLGame_orig.exe` back — that restores 1.6.14.

## Rebuild

Generated, never hand-edited:

```bash
python tools/build-beacon-mod.py --pack
```

`tools/beacon-reveal.lua.tmpl` is the code; the label table is generated from
`cards/trees/*.tree.json`. `tools/BEACON-REVEAL.md` is the specification.

## Status

**Working, confirmed on screen 2026-08-15.** Every beacon in a Civilian Sector map was named
and each label sat above its own beacon — including beacons whose own tooltip still read
*"An unvisited location."*, which is the whole point.

`FTL_HS.log` corroborates it each run:

```
Loading Lua file: data/beacon-reveal.lua
[Lua]: beacon-reveal: loaded, 386 names
[Lua]: beacon-reveal: vector index base = 0
[Lua]: beacon-reveal: sector 1: named 21 beacons, 20 of them unvisited -- e.g. Mantis fight / ...
```

Cosmetic, not yet fixed: long names on a crowded map overlap each other and can sit on top of
the vanilla `STORE` / `EXIT` tags.

## Rebuilding, without the trap

Use `--install`. A rebuilt `.ftl` that never gets patched into `ftl.dat` is invisible — the game
just keeps running the previous build, and the only symptom is that your fix "didn't work". That
happened once during development and cost a debugging round.

```bash
python tools/build-beacon-mod.py --install    # pack, copy to Slipstream, patch (close FTL first)
```

Then restart FTL: the Lua is read from `ftl.dat` at startup.
