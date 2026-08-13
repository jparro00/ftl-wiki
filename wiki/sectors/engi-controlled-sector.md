---
id: sector-engi-controlled-sector
type: sector
sector_id: ENGI_SECTOR
sector_class: unknown
faction: [[[entity-engi]]]
min_sector: 0
unique: false
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 2
tags: []
---

# Engi Controlled Sector

## Summary
Engi-flavoured sector with its own parallel set of event lists — every generic list is
replaced by an `_ENGI` variant except `ITEMS`.

## Character & Hazards
Carries both `ITEMS` (2) and `ITEMS_ENGI` (3), the heaviest item-beacon allocation of any
non-home sector. (per [[source-sector-data-xml]])

## Event Pool

| Event list | min | max |
|---|---|---|
| `STORE_ENGI` | 2 | 3 |
| `ITEMS` | 2 | 2 |
| `NOTHING_ENGI` | 1 | 2 |
| `ITEMS_ENGI` | 3 | 3 |
| `DISTRESS_BEACON_ENGI` | 1 | 3 |
| `QUESTS_ENGI` | 1 | 1 |
| `NEUTRAL_ENGI` | 4 | 6 |
| `HOSTILE_ENGI` | 5 | 7 |

Start beacon: `START_BEACON_ENGI`.

## Chains That Run Through It
- _Not yet mapped._

## Factions & Ships
- [[entity-engi]] — dominant faction

## Strategy Notes
- _None sourced yet._

## Open Questions
- [ ] Which events populate each list.
- [ ] Map colour / hostility classification — not in `sector_data.xml`.

## Sources
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-text-sectorname-xml]] (per raw/gamedata/text_sectorname.xml)
