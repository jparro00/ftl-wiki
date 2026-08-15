---
id: sector-hidden-crystal-worlds
type: sector
sector_id: CRYSTAL_HOME
sector_class: special
faction: [[[entity-crystal-men]]]
min_sector: 0
unique: true
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [hidden, crystal-route, ship-unlock]
---

# Hidden Crystal Worlds

## Summary
The hidden sector at the end of the Crystal route. Not reachable by normal map routing —
it is entered via [[chain-crystal-cruiser-unlock]].

## Character & Hazards
The most hostile pool in the game: `HOSTILE_CRYSTAL` runs 6–10, wider than any other
sector's hostile allocation. `NEUTRAL_CRYSTAL` is pinned at exactly 12 — the only fixed
double-digit allocation anywhere in `sector_data.xml`.
`minSector="0"` despite being unique, because entry is by chain rather than by depth.
(per [[source-sector-data-xml]])

## Event Pool

| Event list | min | max |
|---|---|---|
| `STORE_CRYSTAL` | 2 | 3 |
| `ITEMS_CRYSTAL` | 2 | 2 |
| `NOTHING_CRYSTAL` | 2 | 2 |
| `HOSTILE_CRYSTAL` | 6 | 10 |
| `BOARDERS_CRYSTAL` | 1 | 2 |
| `NEUTRAL_CRYSTAL` | 12 | 12 |

Start beacon: `START_BEACON_CRYSTAL`.

No quest list and no distress list — this sector is fights and neutrals only.

## Chains That Run Through It
- [[chain-crystal-cruiser-unlock]] — this sector is the destination. You arrive via the
  Crystal-crew blue option on [[event-ancient-device]] in [[sector-rock-homeworlds]];
  the payoff is [[event-crystal-unlock]] at a quest marker here.

Enemy strength here scales to the Rock Homeworlds' sector number, and on exit you do not
choose your next sector. ([[source-fandom-ancient-device]])

## Factions & Ships
- [[entity-crystal-men]] — dominant faction

## Strategy Notes
- _None sourced yet._

## Open Questions
- [ ] How the sector is entered mechanically once the chain completes.
- [ ] Whether it always replaces a normal sector or is appended.

## Sources
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-text-sectorname-xml]] (per raw/gamedata/text_sectorname.xml)
