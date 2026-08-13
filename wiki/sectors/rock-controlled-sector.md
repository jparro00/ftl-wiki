---
id: sector-rock-controlled-sector
type: sector
sector_id: ROCK_SECTOR
sector_class: unknown
faction: [[[entity-rock-men]]]
min_sector: 1
unique: false
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 2
tags: []
---

# Rock Controlled Sector

## Summary
Rock space. Never appears as the first sector (`minSector="1"`), and carries the
game's largest neutral allocation at 7–8 beacons.

## Character & Hazards
Guaranteed 2 stores and 1–2 boarding beacons.
(per [[source-sector-data-xml]])

## Event Pool

| Event list | min | max |
|---|---|---|
| `STORE_ROCK` | 2 | 2 |
| `NOTHING_ROCK` | 2 | 3 |
| `DISTRESS_BEACON_ROCK` | 1 | 2 |
| `HOSTILE_ROCK` | 6 | 8 |
| `BOARDERS_ROCK` | 1 | 2 |
| `ITEMS` | 1 | 2 |
| `QUESTS_ROCK` | 0 | 1 |
| `NEUTRAL_ROCK` | 7 | 8 |

Start beacon: `START_BEACON_ROCK`.

## Chains That Run Through It
- _Not yet mapped._

## Factions & Ships
- [[entity-rock-men]] — dominant faction

## Strategy Notes
- _None sourced yet._

## Open Questions
- [ ] Which events populate each list.

## Sources
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-text-sectorname-xml]] (per raw/gamedata/text_sectorname.xml)
