---
id: sector-rebel-controlled-sector
type: sector
sector_id: REBEL_SECTOR
sector_class: unknown
faction: [[[entity-rebels]]]
min_sector: 0
unique: false
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 2
tags: []
---

# Rebel Controlled Sector

## Summary
Rebel-held space. Pool is structurally identical to the pirate sector's, swapped to
`_REBEL` lists.

## Character & Hazards
6–8 hostile beacons and a guaranteed boarding beacon.
(per [[source-sector-data-xml]])

## Event Pool

| Event list | min | max |
|---|---|---|
| `STORE_REBEL` | 1 | 2 |
| `ITEMS` | 1 | 2 |
| `HOSTILE_REBEL` | 6 | 8 |
| `BOARDERS_REBEL` | 1 | 1 |
| `DISTRESS_BEACON_REBEL` | 1 | 2 |
| `NEBULA_REBEL` | 0 | 5 |
| `NOTHING_REBEL` | 1 | 2 |
| `QUESTS_REBEL` | 0 | 2 |
| `NEUTRAL_REBEL` | 5 | 6 |

Start beacon: `START_BEACON_REBEL`.

## Chains That Run Through It
- _Not yet mapped._

## Factions & Ships
- [[entity-rebels]] — dominant faction

## Strategy Notes
- _None sourced yet._

## Open Questions
- [ ] Which events populate each list.

## Sources
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-text-sectorname-xml]] (per raw/gamedata/text_sectorname.xml)
