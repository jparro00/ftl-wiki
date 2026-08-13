---
id: sector-zoltan-controlled-sector
type: sector
sector_id: ZOLTAN_SECTOR
sector_class: unknown
faction: [[[entity-zoltan]]]
min_sector: 1
unique: false
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 2
tags: []
---

# Zoltan Controlled Sector

## Summary
Zoltan space. Guarantees a `ZOLTAN_CREW_STUDY` beacon even in the non-home variant —
one of only two non-unique sectors with a guaranteed named beacon.

## Character & Hazards
`minSector="1"` — never the first sector. Carries 2–6 nebula beacons.
(per [[source-sector-data-xml]])

## Event Pool

| Event list | min | max |
|---|---|---|
| `ZOLTAN_CREW_STUDY` | 1 | 1 |
| `STORE_ZOLTAN` | 2 | 2 |
| `NOTHING_ZOLTAN` | 1 | 2 |
| `DISTRESS_BEACON_ZOLTAN` | 1 | 2 |
| `NEBULA_ZOLTAN` | 2 | 6 |
| `HOSTILE_ZOLTAN` | 6 | 8 |
| `BOARDERS_ZOLTAN` | 1 | 2 |
| `ITEM_ZOLTAN` | 1 | 2 |
| `QUESTS_ZOLTAN` | 0 | 1 |
| `NEUTRAL_ZOLTAN` | 5 | 6 |

Start beacon: `START_BEACON_ZOLTAN`.

## Chains That Run Through It
- [[chain-crystal-cruiser-unlock]] — the guaranteed `ZOLTAN_CREW_STUDY` beacon is
  **step 2**, the Zoltan research facility that turns the Damaged Stasis Pod into the
  Crystal crew member Ruwen. Guaranteed here means this sector reliably serves that step.

## Factions & Ships
- [[entity-zoltan]] — dominant faction

## Strategy Notes
- Because `ZOLTAN_CREW_STUDY` is `min=1`, routing through any Zoltan sector guarantees
  step 2 of [[chain-crystal-cruiser-unlock]] if you are carrying the stasis pod.

## Open Questions
- [ ] Does `ZOLTAN_CREW_STUDY` do anything if you arrive without the stasis pod?

## Sources
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-text-sectorname-xml]] (per raw/gamedata/text_sectorname.xml)
