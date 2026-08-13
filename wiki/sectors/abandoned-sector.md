---
id: sector-abandoned-sector
type: sector
sector_id: LANIUS_SECTOR
sector_class: special
faction: [[[entity-lanius]]]
min_sector: 1
unique: false
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 2
tags: [advanced-edition, lanius]
---

# Abandoned Sector

## Summary
The Lanius sector, added in Advanced Edition. Display name is "Abandoned Sector" but its
in-game id is `LANIUS_SECTOR`.

> Naming trap: there is a **separate, distinct** `ABANDONED_SECTOR` entry in
> `sector_data.xml` which is *not* this sector — see [[sector-vestigial-definitions]].

## Character & Hazards
Carries `HOSTILE_ENVIRONMENT_LANIUS` (1–2), a hazard list no other sector has, and the
heaviest item allocation in the game at `ITEM_LANIUS` 2–4.
(per [[source-sector-data-xml]])

## Event Pool

| Event list | min | max |
|---|---|---|
| `STORE_LANIUS` | 2 | 2 |
| `NOTHING_LANIUS` | 1 | 2 |
| `DISTRESS_BEACON_LANIUS` | 1 | 2 |
| `HOSTILE_LANIUS` | 5 | 6 |
| `HOSTILE_ENVIRONMENT_LANIUS` | 1 | 2 |
| `BOARDERS_LANIUS` | 1 | 2 |
| `ITEM_LANIUS` | 2 | 4 |
| `QUESTS_LANIUS` | 0 | 1 |
| `NEUTRAL_LANIUS` | 5 | 6 |

Start beacon: `START_BEACON_LANIUS`.

## Chains That Run Through It
- _Not yet mapped._

## Factions & Ships
- [[entity-lanius]] — dominant faction

## Strategy Notes
- _None sourced yet._

## Open Questions
- [ ] What `HOSTILE_ENVIRONMENT_LANIUS` covers (oxygen drain is the likely theme, unsourced).
- [ ] Whether this sector requires the AE DLC to be enabled.

## Sources
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-text-sectorname-xml]] (per raw/gamedata/text_sectorname.xml)
