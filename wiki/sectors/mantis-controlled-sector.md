---
id: sector-mantis-controlled-sector
type: sector
sector_id: MANTIS_SECTOR
sector_class: unknown
faction: [[[entity-mantis]]]
min_sector: 0
unique: false
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 2
tags: []
---

# Mantis Controlled Sector

## Summary
Mantis space. The narrowest event pool of any faction sector — 7 lists, with no quest
list and no dedicated nebula list.

## Character & Hazards
Up to 2 boarding beacons (`BOARDERS_MANTIS` 1–2), the highest guaranteed-boarding range
in the game, which fits the Mantis boarding threat.
(per [[source-sector-data-xml]])

## Event Pool

| Event list | min | max |
|---|---|---|
| `STORE_MANTIS` | 1 | 2 |
| `NOTHING_MANTIS` | 2 | 3 |
| `DISTRESS_BEACON_MANTIS` | 1 | 3 |
| `HOSTILE_MANTIS` | 6 | 7 |
| `BOARDERS_MANTIS` | 1 | 2 |
| `ITEMS` | 1 | 2 |
| `NEUTRAL_MANTIS` | 6 | 7 |

Start beacon: `START_BEACON_MANTIS`.

## Chains That Run Through It
- _Not yet mapped._

## Factions & Ships
- [[entity-mantis]] — dominant faction

## Strategy Notes
- _None sourced yet._

## Open Questions
- [ ] No `QUESTS_MANTIS` list exists — are Mantis-sector quests really absent?

## Sources
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-text-sectorname-xml]] (per raw/gamedata/text_sectorname.xml)
