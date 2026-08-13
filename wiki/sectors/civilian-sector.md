---
id: sector-civilian-sector
type: sector
sector_id: CIVILIAN_SECTOR
sector_class: civilian
faction: []
min_sector: 0
unique: false
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 2
tags: []
---

# Civilian Sector

## Summary
The generic friendly sector. Its pool is Federation Space's with the store and item
allocations roughly doubled and no boarding suppression.

## Character & Hazards
More stores (2–3) and more item beacons (2–3) than any other non-home sector, and up to
8 nebula beacons — the widest nebula range in the game outside the dedicated nebula
sectors. (per [[source-sector-data-xml]])

## Event Pool

| Event list | min | max |
|---|---|---|
| `STORE` | 2 | 3 |
| `ITEMS` | 2 | 3 |
| `NEUTRAL_CIVILIAN` | 2 | 4 |
| `NOTHING` | 1 | 2 |
| `DISTRESS_BEACON` | 1 | 2 |
| `HOSTILE_CIVILIAN` | 4 | 6 |
| `NEBULA` | 0 | 8 |
| `QUESTS` | 0 | 2 |
| `HOSTILE1` | 2 | 2 |

No `startEvent` is declared for this sector.

## Chains That Run Through It
- _Not yet mapped._

## Factions & Ships
- _Unfactioned._

## Strategy Notes
- _None sourced yet._

## Open Questions
- [ ] Why no `startEvent` — does it inherit `START_BEACON`?
- [ ] Which events populate each list.

## Sources
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-text-sectorname-xml]] (per raw/gamedata/text_sectorname.xml)
