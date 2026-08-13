---
id: sector-rock-homeworlds
type: sector
sector_id: ROCK_HOME
sector_class: unknown
faction: [[[entity-rock-men]]]
min_sector: 4
unique: true
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 2
tags: [homeworld, ship-unlock, crystal-route]
---

# Rock Homeworlds

## Summary
Unique Rock home sector, and the gateway to the Crystal route: it guarantees both the
`ROCK_CRYSTAL_BEACON` beacon ([[event-ancient-device]]) and a `ROCK_UNLOCK1` beacon.

## Character & Hazards
`unique="true"`, `minSector="4"` — at most one per run, never before sector 4. That
depth floor is what makes the Crystal Cruiser route a late-run commitment.
(per [[source-sector-data-xml]])

## Event Pool

| Event list | min | max |
|---|---|---|
| `ROCK_CRYSTAL_BEACON` | 1 | 1 |
| `ROCK_UNLOCK1` | 1 | 1 |
| `STORE_ROCK` | 2 | 2 |
| `NOTHING_ROCK` | 2 | 3 |
| `DISTRESS_BEACON_ROCK` | 1 | 2 |
| `HOSTILE_ROCK` | 6 | 8 |
| `BOARDERS_ROCK` | 1 | 2 |
| `ITEMS` | 1 | 2 |
| `QUESTS_ROCK` | 0 | 1 |
| `NEUTRAL_ROCK` | 7 | 8 |

Start beacon: `START_BEACON_ROCK`.

> Note: `ROCK_CRYSTAL_BEACON` and `ROCK_UNLOCK1` are referenced here as if they were
> event lists, but both are defined as single `<event name=...>` entries, not
> `<eventList>`s — the sector generator accepts either.

## Chains That Run Through It
- [[chain-crystal-cruiser-unlock]] — [[event-ancient-device]] is the step that happens here.
- `ROCK_UNLOCK1` — Rock Cruiser unlock line. _Chain page not yet created._

## Factions & Ships
- [[entity-rock-men]] — dominant faction

## Strategy Notes
- Both guaranteed beacons are unique-per-run quest steps, so this sector is worth
  routing into if either chain is live. _(Derived from the allocation table, not from a
  strategy source.)_

## Open Questions
- [ ] What does `ROCK_UNLOCK1` lead to after the initial encounter?
- [ ] Which events populate the ordinary lists.

## Sources
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-text-sectorname-xml]] (per raw/gamedata/text_sectorname.xml)
