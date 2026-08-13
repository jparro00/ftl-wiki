---
id: sector-rebel-stronghold
type: sector
sector_id: REBEL_SECTOR_MINIBOSS
sector_class: unknown
faction: [[[entity-rebels]]]
min_sector: 4
unique: true
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 2
tags: [unique, flagship]
---

# Rebel Stronghold

## Summary
The unique rebel sector that houses the Flagship construction beacon. Identical to
[[sector-rebel-controlled-sector]] plus one guaranteed `FLAGSHIP_CONSTRUCTION` beacon.

## Character & Hazards
`unique="true"`, `minSector="4"` — one per run at most, never before sector 4.
(per [[source-sector-data-xml]])

## Event Pool

| Event list | min | max |
|---|---|---|
| `FLAGSHIP_CONSTRUCTION` | 1 | 1 |
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
- `FLAGSHIP_CONSTRUCTION` — guaranteed. _Chain page not yet created._

## Factions & Ships
- [[entity-rebels]] — dominant faction
- [[entity-flagship]] — previewed here

## Strategy Notes
- _None sourced yet._

## Open Questions
- [ ] What `FLAGSHIP_CONSTRUCTION` actually offers, and whether it is skippable.

## Sources
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-text-sectorname-xml]] (per raw/gamedata/text_sectorname.xml)
