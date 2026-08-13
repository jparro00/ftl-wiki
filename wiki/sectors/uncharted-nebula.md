---
id: sector-uncharted-nebula
type: sector
sector_id: NEBULA_SECTOR
sector_class: nebula
faction: []
min_sector: 0
unique: false
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 2
tags: [nebula]
---

# Uncharted Nebula

## Summary
The unfactioned nebula sector. Its pool is built from dedicated `NEBULA_*` lists rather
than the generic ones, and it carries a `NEBULA_STORE`.

## Character & Hazards
`STORE` drops to 0–1 while `NEBULA_STORE` is guaranteed at 1 — so stores exist but come
through the nebula-specific list. 4 guaranteed empty beacons (`NEBULA_EMPTY`).
(per [[source-sector-data-xml]])

## Event Pool

| Event list | min | max |
|---|---|---|
| `STORE` | 0 | 1 |
| `ITEMS` | 1 | 3 |
| `NEBULA_STORE` | 1 | 1 |
| `NEBULA_EMPTY` | 4 | 4 |
| `NEBULA_HOSTILE` | 5 | 6 |
| `NEBULA_NEUTRAL` | 7 | 8 |
| `DISTRESS_BEACON` | 1 | 3 |

Start beacon: `START_BEACON_NEBULA`.

## Chains That Run Through It
- _Not yet mapped._

## Factions & Ships
- _Unfactioned._

## Strategy Notes
- _None sourced yet._

## Open Questions
- [ ] Sensor/vision penalties are a nebula mechanic but are not declared in
      `sector_data.xml` — needs a wiki source. See [[concept-nebula-mechanics]].

## Sources
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-text-sectorname-xml]] (per raw/gamedata/text_sectorname.xml)
