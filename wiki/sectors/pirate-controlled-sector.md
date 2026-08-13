---
id: sector-pirate-controlled-sector
type: sector
sector_id: PIRATE_SECTOR
sector_class: unknown
faction: [[[entity-pirates]]]
min_sector: 0
unique: false
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 2
tags: []
---

# Pirate Controlled Sector

## Summary
Pirate sector. Heaviest hostile allocation of the early-available sectors (6–8) plus a
guaranteed boarding beacon.

## Character & Hazards
`BOARDERS_PIRATE` is `min=1` — a boarding encounter is guaranteed, unlike in
Federation Space where boarding is disabled entirely. (per [[source-sector-data-xml]])

## Event Pool

| Event list | min | max |
|---|---|---|
| `STORE_PIRATE` | 1 | 2 |
| `ITEMS` | 1 | 2 |
| `HOSTILE_PIRATE` | 6 | 8 |
| `BOARDERS_PIRATE` | 1 | 1 |
| `DISTRESS_BEACON_PIRATE` | 1 | 2 |
| `NEBULA_PIRATE` | 0 | 5 |
| `NOTHING_PIRATE` | 1 | 2 |
| `QUESTS_PIRATE` | 0 | 1 |
| `NEUTRAL_PIRATE` | 5 | 6 |

Start beacon: `START_BEACON_PIRATE`.

## Chains That Run Through It
- _Not yet mapped._

## Factions & Ships
- [[entity-pirates]] — dominant faction

## Strategy Notes
- _None sourced yet._

## Open Questions
- [ ] Which events populate each list.
- [ ] Map colour / hostility classification — not in `sector_data.xml`.

## Sources
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-text-sectorname-xml]] (per raw/gamedata/text_sectorname.xml)
