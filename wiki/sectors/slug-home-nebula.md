---
id: sector-slug-home-nebula
type: sector
sector_id: SLUG_HOME
sector_class: nebula
faction: [[[entity-slugs]]]
min_sector: 3
unique: true
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 2
tags: [nebula, homeworld, ship-unlock]
---

# Slug Home Nebula

## Summary
Unique Slug home sector — the largest event pool in the game at 12 lists.
[[sector-slug-controlled-nebula]]'s pool plus a guaranteed `NEBULA_SLUG_FIGHT_UNLOCK`
beacon.

## Character & Hazards
`unique="true"`, `minSector="3"`. (per [[source-sector-data-xml]])

## Event Pool

| Event list | min | max |
|---|---|---|
| `NEBULA_SLUG_FIGHT_UNLOCK` | 1 | 1 |
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
- `NEBULA_SLUG_FIGHT_UNLOCK` — guaranteed; the name implies the Slug Cruiser unlock.
  _Chain page not yet created; the unlock claim is inferred from the id and not yet sourced._

## Factions & Ships
- [[entity-slugs]] — dominant faction

## Strategy Notes
- _None sourced yet._

## Open Questions
- [ ] Confirm `NEBULA_SLUG_FIGHT_UNLOCK` is the Slug Cruiser unlock.

## Sources
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-text-sectorname-xml]] (per raw/gamedata/text_sectorname.xml)
