---
id: sector-mantis-homeworlds
type: sector
sector_id: MANTIS_HOME
sector_class: unknown
faction: [[[entity-mantis]]]
min_sector: 2
unique: true
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 2
tags: [homeworld, ship-unlock]
---

# Mantis Homeworlds

## Summary
Unique Mantis home sector. [[sector-mantis-controlled-sector]]'s pool plus a guaranteed
`MANTIS_NAMED_THIEF` beacon.

## Character & Hazards
`unique="true"`, `minSector="2"`. (per [[source-sector-data-xml]])

## Event Pool

| Event list | min | max |
|---|---|---|
| `MANTIS_NAMED_THIEF` | 1 | 1 |
| `STORE_MANTIS` | 1 | 2 |
| `NOTHING_MANTIS` | 2 | 3 |
| `DISTRESS_BEACON_MANTIS` | 1 | 3 |
| `HOSTILE_MANTIS` | 6 | 7 |
| `BOARDERS_MANTIS` | 1 | 2 |
| `ITEMS` | 1 | 2 |
| `NEUTRAL_MANTIS` | 6 | 7 |

Start beacon: `START_BEACON_MANTIS`.

## Chains That Run Through It
- `MANTIS_NAMED_THIEF` — guaranteed. _Chain page not yet created._

## Factions & Ships
- [[entity-mantis]] — dominant faction

## Strategy Notes
- _None sourced yet._

## Open Questions
- [ ] Is `MANTIS_NAMED_THIEF` the Mantis Cruiser unlock step?

## Sources
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-text-sectorname-xml]] (per raw/gamedata/text_sectorname.xml)
