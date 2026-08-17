# Event Labels — an FTL mod

Prints the name of each event above its text, so you always know which encounter you are
looking at:

```
[ Ancient device ]

An ancient device is orbiting within the crystal rings of a nearby gas giant. You can't
discern its nature or function, but it seems to have been deactivated for a very long time.
Perhaps you can get some scrap from it.
```

The names are the titles from this wiki's event cards, so what the game shows you and what
the card is called are the same string.

**Text only.** No choice, requirement, reward, ship, or probability is changed. 386 events are
labelled — the ones with a card. The rest are untouched and look exactly as they always did.

## Install

With Slipstream already set up: launch `modman.exe`, tick **event-labels**, click **Patch**.

> The original machine had Slipstream at `C:\Users\jparr\Documents\Slipstream` pointed at
> `D:\Steam\steamapps\common\FTL Faster Than Light`. Those are that machine's paths, not
> defaults — the build tools read `$SLIPSTREAM_DIR` and `$FTL_DIR` (see `SETUP.md` §6).

From scratch:

1. Get Slipstream Mod Manager — binaries are on
   [SourceForge](https://sourceforge.net/projects/slipstreammodmanager/), *not* the GitHub
   releases page, which is empty. Needs Java 1.6+.
2. Copy `event-labels.ftl` into Slipstream's `mods/` folder.
3. Launch `modman.exe`, tick **event-labels**, click **Patch**.

To uninstall, untick it and patch again. Slipstream keeps a pristine backup of the game data,
so nothing here is destructive.

## Rebuild

The mod is generated — never hand-edited:

```bash
python tools/build-mod.py --pack
```

`src/` is the file tree that goes into the archive; `event-labels.ftl` is that tree zipped and
renamed. Both come from `cards/trees/*.tree.json`. Retitle a wiki event page, rebuild its
card, rebuild the mod, and the in-game label follows.

`tools/EVENT-LABELS.md` is the specification: what the two emission mechanisms are, why the
mod avoids Slipstream's Advanced XML, and what the build verifies.

## Status

Loaded by Slipstream 1.9.1, whose own **Validate** reports `No Problems`. The vanilla files
it appends to were confirmed byte-identical to this machine's installed `ftl.dat`, so the
copied event definitions match the game exactly.

**Patched in and working**, confirmed 2026-08-15: a live save held the encounter text
`[ Start game ]` followed by the vanilla opening prose — the label rendering exactly as
designed, read back out of the game's own save file.
