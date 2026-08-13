---
id: sector-engi-homeworlds
type: sector
sector_id: ENGI_HOME
sector_class: unknown
faction: [[[entity-engi]]]
min_sector: 2
unique: true
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 2
tags: [homeworld, ship-unlock]
---

# Engi Homeworlds

## Summary
The unique Engi home sector. Identical to [[sector-engi-controlled-sector]] except it
guarantees one `ENGI_UNLOCK_1` beacon and shifts `NEUTRAL_ENGI` up by one.

## Character & Hazards
`unique="true"` — at most one per run, and never before sector 2.
(per [[source-sector-data-xml]])

## Event Pool

| Event list | min | max |
|---|---|---|
| `ENGI_UNLOCK_1` | 1 | 1 |
| `STORE_ENGI` | 2 | 3 |
| `ITEMS` | 2 | 2 |
| `NOTHING_ENGI` | 1 | 2 |
| `ITEMS_ENGI` | 3 | 3 |
| `DISTRESS_BEACON_ENGI` | 1 | 3 |
| `QUESTS_ENGI` | 1 | 1 |
| `NEUTRAL_ENGI` | 5 | 7 |
| `HOSTILE_ENGI` | 5 | 7 |

Start beacon: `START_BEACON_ENGI`.

## Chains That Run Through It
- `ENGI_UNLOCK_1` is a guaranteed beacon here — the ship-unlock chain entry point.
  _Chain page not yet created._

## Factions & Ships
- [[entity-engi]] — dominant faction

## Strategy Notes
- _None sourced yet._

## Open Questions
- [ ] Which ship does `ENGI_UNLOCK_1` unlock, and what are its steps?
- [ ] Which events populate each list.

## Sources
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-text-sectorname-xml]] (per raw/gamedata/text_sectorname.xml)
