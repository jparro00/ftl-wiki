---
id: sector-vestigial-definitions
type: sector
sector_id: DEEP_SPACE_SECTOR, ABANDONED_SECTOR
sector_class: unknown
faction: []
min_sector: 0
unique: false
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 1
tags: [oddity, unused]
---

# Vestigial sector definitions — `DEEP_SPACE_SECTOR` and `ABANDONED_SECTOR`

## Summary
Two `<sectorDescription>` entries in `sector_data.xml` that appear to be dead stubs.
Grouped on one page because neither warrants its own and neither is a playable sector as
far as the data shows.

## Character & Hazards
Both are structurally incomplete compared to every other sector:

- **No `<nameList>`** — so no display name exists for either. Every real sector has one
  pointing into `text_sectorname.xml`.
- **A single event list**, `STORE` at `min=2 max=4`, and nothing else. No hostiles, no
  neutrals, no start beacon.

That combination cannot generate a playable sector map.

> Naming trap: `ABANDONED_SECTOR` here is **not** the Advanced Edition Lanius sector.
> That one is [[sector-abandoned-sector]], whose in-game id is `LANIUS_SECTOR` and whose
> *display name* happens to be "Abandoned Sector". Anything matching on the string
> "abandoned" will conflate the two.

## Event Pool

| Event list | min | max |
|---|---|---|
| `STORE` | 2 | 4 |

## Chains That Run Through It
- _None._

## Factions & Ships
- _None declared._

## Strategy Notes
- Not applicable — these do not appear to be reachable.

## Open Questions
- [ ] Are these leftovers from development, or reachable through some mechanism not
      visible in `sector_data.xml`?
- [ ] Does the community wiki document either? Neither name appeared in the 291 pages
      pulled in this ingest.

## Sources
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
