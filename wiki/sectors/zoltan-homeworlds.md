---
id: sector-zoltan-homeworlds
type: sector
sector_id: ZOLTAN_HOME
sector_class: unknown
faction: [[[entity-zoltan]]]
min_sector: 2
unique: true
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 2
tags: [homeworld, ship-unlock]
---

# Zoltan Homeworlds

## Summary
Unique Zoltan home sector. [[sector-zoltan-controlled-sector]]'s pool plus a guaranteed
`ZOLTAN_PEACE_QUEST` beacon.

## Character & Hazards
`unique="true"`, `minSector="2"`. Two guaranteed named beacons — `ZOLTAN_CREW_STUDY`
and `ZOLTAN_PEACE_QUEST`. (per [[source-sector-data-xml]])

## Event Pool

| Event list | min | max |
|---|---|---|
| `ZOLTAN_CREW_STUDY` | 1 | 1 |
| `ZOLTAN_PEACE_QUEST` | 1 | 1 |
| `STORE_ZOLTAN` | 2 | 2 |
| `NOTHING_ZOLTAN` | 1 | 2 |
| `DISTRESS_BEACON_ZOLTAN` | 1 | 2 |
| `NEBULA_ZOLTAN` | 2 | 6 |
| `HOSTILE_ZOLTAN` | 6 | 8 |
| `BOARDERS_ZOLTAN` | 1 | 2 |
| `ITEM_ZOLTAN` | 1 | 2 |
| `QUESTS_ZOLTAN` | 0 | 1 |
| `NEUTRAL_ZOLTAN` | 5 | 6 |

Start beacon: `START_BEACON_ZOLTAN`.

## Chains That Run Through It
- [[chain-crystal-cruiser-unlock]] — the guaranteed `ZOLTAN_CREW_STUDY` beacon is
  **step 2** (the Zoltan research facility).
- `ZOLTAN_PEACE_QUEST` — guaranteed. _Chain page not yet created._

## Factions & Ships
- [[entity-zoltan]] — dominant faction

## Strategy Notes
- _None sourced yet._

## Open Questions
- [ ] Does `ZOLTAN_PEACE_QUEST` gate the Zoltan Cruiser unlock?

## Sources
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-text-sectorname-xml]] (per raw/gamedata/text_sectorname.xml)
