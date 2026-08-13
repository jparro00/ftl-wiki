---
id: source-sector-data-xml
type: source
source_kind: gamedata
raw: raw/gamedata/sector_data.xml
game_version: ae
ingested: 2026-08-09
reliability: high
tags: [structural]
---

# sector_data.xml

## Summary
The sector definition file: every sector type, its display-name reference, its depth
floor, whether it is unique, and — the payload — which event lists it draws from and how
many beacons of each it places. This is the structural backbone the whole wiki hangs off.

## Key Takeaways
- **21 `<sectorDescription>` entries**, of which 19 are playable and 2 are stubs
  (see [[sector-vestigial-definitions]]).
- Each sector declares `<event name="LIST" min="n" max="m"/>` entries. `min`/`max` are
  **beacon counts**, not probabilities — a `min=1` list is guaranteed to appear.
- `minSector` sets the earliest map depth a sector can appear at; `unique="true"` caps it
  at one per run.
- The file references **173 event lists** in total.
- Sector display names are not here — they are ids into `text_sectorname.xml`
  ([[source-text-sectorname-xml]]).
- The sector generator accepts a **single event name** where an event list is expected:
  `ROCK_CRYSTAL_BEACON` and `ROCK_UNLOCK1` are `<event>` definitions, not `<eventList>`s,
  yet appear in [[sector-rock-homeworlds]]'s allocation table.
- **No hostility / map-colour flag exists in this file.** The red-vs-blue sector
  distinction players use is not represented here and must come from another source.

## Pages Created From This Source
All 20 sector pages: [[sector-federation-space]], [[sector-civilian-sector]],
[[sector-engi-controlled-sector]], [[sector-engi-homeworlds]],
[[sector-pirate-controlled-sector]], [[sector-rebel-controlled-sector]],
[[sector-rebel-stronghold]], [[sector-mantis-controlled-sector]],
[[sector-mantis-homeworlds]], [[sector-rock-controlled-sector]],
[[sector-rock-homeworlds]], [[sector-zoltan-controlled-sector]],
[[sector-zoltan-homeworlds]], [[sector-uncharted-nebula]],
[[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]],
[[sector-hidden-crystal-worlds]], [[sector-abandoned-sector]],
[[sector-the-last-stand]], [[sector-vestigial-definitions]].

## Contradictions Flagged
None internal to this file.

Worth recording as an oddity rather than a contradiction: `ABANDONED_SECTOR` (a stub with
no name list) and `LANIUS_SECTOR` (display name "Abandoned Sector") are different
entries. Any lookup by the string "abandoned" will conflate them.

## Links
- [[source-text-sectorname-xml]]
