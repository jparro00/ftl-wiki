---
id: source-beacon-name-labels-mod-research
type: source
source_kind: research
raw: raw/modding/2026-08-15-beacon-name-labels-mod.md
game_version: both
date: 2026-08-15
ingested: 2026-08-15
reliability: medium
tags: [modding, hyperspace, lua, sector-map, beacons]
---

# Naming every beacon on the sector map — feasibility research

## Summary
A synthesis, written into `raw/` by instruction, answering whether a mod can print each
beacon's event name on the sector map *before* the beacon is revealed. It can — but only
through FTL Hyperspace, whose Lua API exposes `StarMap.locations`, each `Location.event`, and
that event's `eventName`, together with text-drawing calls and a render hook. Vanilla
Slipstream modding cannot reach the map renderer at all, and the save file does not store
unvisited beacons' events, so no external tool can recover them either.

## Key Takeaways
- **The engine decides every beacon's event when it generates the sector.** Confirmed three
  ways: `StarMap::AddQuest` filters *unvisited* beacons on store/distress properties
  ([[source-xftl-sector-map]]); markers are withheld until one jump away
  ([[source-fandom-beacons]]); and the save stores only `sectorLayoutSeed`, from which
  "environment hazards … and events" are regenerated. The cheat is a reveal, not a computation.
- **Hyperspace exposes exactly what is needed.** `StarMap.locations` (read-only vector),
  `FocusWindow.bOpen`, `Location.loc/.known/.visited/.event`, and `LocationEvent.eventName`,
  `.text`, `.store`, `.distressBeacon`, `.quest`. `Location.event` reads fine on an unvisited
  beacon — that one fact is the whole mod.
- **There is no star-map render layer** in `Defines.RenderEvents`; `MOUSE_CONTROL` is the hook
  that fires over the map, and `Graphics.freetype.easy_printCenter` draws the text. Its first
  argument is a font **id**, not a point size.
- **`<beaconType>` is a real per-event map label** with `req` equipment gating, a colour, and
  separate undiscovered / unvisited / visited tooltips — but its label is taken from the
  **first** declaration of an event, the opposite of every other tag, so the `.append`
  override trick behind [[concept-modding-and-the-append-convention]] does not work for it.
- **The save leaks ships and stores, never the event.** `readBeacon` stores `seen`,
  `enemyPresent` + `shipEventId`, `fleetPresence`, `underAttack` and a store's full inventory —
  a partial spoiler map with no game modification, which is worth measuring first.
- **Hyperspace downgrades FTL 1.6.14 to 1.6.9**, requires uninstalling other mods, and extends
  the save format — so it collides with `raw/gamedata/` provenance, the `event-labels` patch,
  and the save watcher (`tools/SAVE-WATCH.md` §6).

## Events Covered
None. This source is about tooling, not game content.

## Other Pages Touched
- [[concept-modding-and-the-append-convention]] — the first-declaration rule for beacon labels
  is a documented exception to the last-one-wins rule that page rests on.
- [[source-fandom-beacons]] / [[concept-quest-beacon-placement]] — what the map reveals and
  when, which is precisely what this mod would override.
- [[source-xftl-sector-map]] — the engine-side generation order this relies on.
- [[source-modding-research]] — the Slipstream/Hyperspace groundwork this extends.

## Contradictions Flagged
> ⚠️ **CONTRADICTION (resolved as a scope difference, not an error):** Slipstream's
> `readme_modders.txt` states that "whenever multiple tags share the same name, only the last
> one counts", and `tools/EVENT-LABELS.md` §4 is built on it. FTL-Hyperspace issue #216 reports
> that **beacon labels are set by the first instance of an event rather than the last**. Both
> hold: the Slipstream rule governs which event *definition* wins, while Hyperspace's own
> `<beaconType>` parse keeps the first label it sees. The practical consequence is that beacon
> labels must be inserted with Advanced XML, not appended as a redefinition.

## Links
- `raw/modding/2026-08-15-beacon-name-labels-mod.md` — the full synthesis, with every URL and
  the date each was read.
- Hyperspace Lua API: <https://github.com/FTL-Hyperspace/FTL-Hyperspace/wiki/Lua-Hyperspace-Module>
- Issue #216 (beacon-label load order): <https://github.com/FTL-Hyperspace/FTL-Hyperspace/issues/216>
- Install guide (the 1.6.14 → 1.6.9 downgrade):
  <https://ftl-hyperspace.github.io/FTL-Hyperspace/install-guides/windows/steam-install/>
