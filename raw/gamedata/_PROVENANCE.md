# Provenance — raw/gamedata/

These XML files were extracted from the user's own installed copy of the game.

- **Source archive:** `D:\Steam\steamapps\common\FTL Faster Than Light\ftl.dat` (267.6 MB)
- **Archive format:** `PKG\n` — the FTL **1.6.x Advanced Edition** package format
  (pre-1.6 builds shipped `data.dat` + `resource.dat` in a different, uncompressed format)
- **Extracted:** 2026-08-09, 33 of 3,219 archive entries
- **Tool:** `tools/ftlpkg.py` in this repo — a read-only parser written against
  [`PkgPack.java`](https://github.com/Vhati/Slipstream-Mod-Manager/blob/master/src/main/java/net/vhati/ftldat/PkgPack.java)
  from Vhati's Slipstream Mod Manager. The game install was not modified.
- **Reliability:** `high`. This is the game's own data for the exact build being played.

### What `version:` to record

These files are the **AE build**, but that is not the same as the content being AE-only.
Superseded guidance: an earlier draft of this file said to record `ae` for everything
sourced here. That is wrong per `CLAUDE.md` §2.0, where `ae` means *Advanced Edition only*.
Use:

| Defining file / evidence | `version:` |
|---|---|
| `dlcEvents*.xml`, or reachable only via an `OVERRIDE_*` list | `ae` |
| A base file (`events*.xml`, `newEvents.xml`) with no DLC markers | `both` |
| A base-file event whose *tags* are `<!--DLC-->`-wrapped | `both`, with the vanilla difference documented in-body |
| A list replaced by `OVERRIDE_*`, where the base entry is gone in AE | `vanilla` for the dropped content |

We hold only AE files, so `both` is an inference: base files predate AE and the content is
present in this build unmarked. It is not a direct observation of a vanilla install.

## Re-extracting after a game update

```
python tools/ftlpkg.py list    "<path>\ftl.dat" ".xml"
python tools/ftlpkg.py extract-list "<path>\ftl.dat" raw/gamedata <paths-file> --flat
```

## How these files fit together

**Event text is not stored with the events.** Events reference it by id:

```xml
<text id="text_START_BEACON_ROCK_1"/>
```

and the prose lives in `text_events.xml`:

```xml
<text name="event_ROCK_CRYSTAL_BEACON_text">An ancient device is orbiting ...</text>
```

So `events_*.xml` and `text_events.xml` must be read together — neither is usable alone.

| File(s) | Role |
|---|---|
| `events.xml`, `events_<faction>.xml` | Base event and event-list definitions (342 events, 213 lists) |
| `newEvents.xml` | Advanced Edition additions (83 events, 41 lists) |
| `dlcEvents.xml`, `dlcEvents_anaerobic.xml` | AE events, incl. Lanius/anaerobic sectors (48 events) |
| `dlcEventsOverwrite.xml` | **AE overrides** — replaces base event lists when AE is enabled |
| `events_ships.xml` | Enemy ship encounter definitions referenced by events |
| `events_imageList.xml`, `nameEvents.xml` | Background art pools, generated names |
| `sector_data.xml` | Sector definitions and which event lists each sector draws from (173 refs) |
| `blueprints.xml`, `dlc*Blueprints*.xml`, `autoBlueprints.xml` | Weapons, drones, augments, systems, ships |
| `bosses.xml` | Flagship |
| `achievements.xml` | Achievements, incl. ship-unlock conditions |
| `text_*.xml` | English strings referenced by id from all of the above |

`dlcEventsOverwrite.xml` and `dlcBlueprintsOverwrite.xml` are the mechanical basis of the
`version: ae | vanilla` distinction — they are what AE swaps in over the base files.

## Copyright

This is Subset Games' copyrighted game content, extracted from a legitimately owned copy
for personal reference. Keep it out of any public repository.
