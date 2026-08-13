---
id: sector-federation-space
type: sector
sector_id: STANDARD_SPACE
sector_class: special
faction: []
min_sector: 0
unique: false
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 2
tags: [starting-sector]
---

# Federation Space

## Summary
The sector every run begins in. Its event pool is the generic, faction-neutral one —
the baseline against which every other sector's pool is a variation.

## Character & Hazards
Draws from the unfactioned lists. Notably the only sector whose `HOSTILE_BOARDING`
allocation is `min=0 max=0` — boarding events are switched off here, which is
consistent with it being the tutorializing first sector.
(per [[source-sector-data-xml]])

## Event Pool
Beacon allocation per `sector_data.xml`. `min`/`max` are how many beacons of that
list the sector generator places.

| Event list | min | max |
|---|---|---|
| `STORE` | 1 | 2 |
| `ITEMS` | 1 | 1 |
| `NEUTRAL_CIVILIAN` | 2 | 4 |
| `NOTHING` | 1 | 2 |
| `DISTRESS_BEACON` | 1 | 2 |
| `HOSTILE_CIVILIAN` | 4 | 6 |
| `NEBULA` | 0 | 4 |
| `QUESTS` | 1 | 1 |
| `HOSTILE1` | 2 | 2 |
| `HOSTILE_BOARDING` | 0 | 0 |

Start beacon: `START_BEACON`.

## Chains That Run Through It
- _Not yet mapped._

## Factions & Ships
- _Unfactioned / civilian. Rebel presence is the fleet pursuit, not the event pool._

## Strategy Notes
- _None sourced yet._

## Open Questions
- [ ] Which events populate each of these lists (needs the events-file ingest).
- [ ] Map colour / hostility classification is not in `sector_data.xml` — needs a wiki source.

## Sources
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-text-sectorname-xml]] (per raw/gamedata/text_sectorname.xml)
