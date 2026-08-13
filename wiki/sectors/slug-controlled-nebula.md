---
id: sector-slug-controlled-nebula
type: sector
sector_id: SLUG_SECTOR
sector_class: nebula
faction: [[[entity-slugs]]]
min_sector: 3
unique: false
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 2
tags: [nebula]
---

# Slug Controlled Nebula

## Summary
Slug space, and a nebula sector throughout. The widest event pool in the game at 11
lists, including a dedicated ion-storm list.

## Character & Hazards
`minSector="3"` — the deepest floor of any non-unique sector, so it cannot appear early.
`STORM_SLUG` (1–3) is unique to the Slug sectors. (per [[source-sector-data-xml]])

## Event Pool

| Event list | min | max |
|---|---|---|
| `STORE` | 0 | 1 |
| `NEBULA_STORE_SLUG` | 2 | 2 |
| `ITEMS` | 0 | 2 |
| `NOTHING_SLUG` | 0 | 2 |
| `HOSTILE_SLUG` | 1 | 2 |
| `DISTRESS_BEACON_SLUG` | 3 | 4 |
| `NEBULA_NOTHING_SLUG` | 2 | 4 |
| `NEBULA_HOSTILE_SLUG` | 5 | 7 |
| `STORM_SLUG` | 1 | 3 |
| `NEBULA_NEUTRAL_SLUG` | 3 | 5 |
| `NEUTRAL` | 1 | 2 |

Start beacon: `START_BEACON_SLUG`.

## Chains That Run Through It
- _Not yet mapped._

## Factions & Ships
- [[entity-slugs]] — dominant faction

## Strategy Notes
- 3–4 guaranteed distress beacons is the heaviest distress allocation in the game — and
  Slug distress beacons are the classic trap-vs-reward decision.
  _(Allocation is sourced; the trap characterisation is not yet.)_

## Open Questions
- [ ] What `STORM_SLUG` events do mechanically.
- [ ] Which distress events are traps.

## Sources
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-text-sectorname-xml]] (per raw/gamedata/text_sectorname.xml)
