---
id: source-fandom-auto-ship-near-sensor-station
type: source
source_kind: wiki
raw: raw/wiki/auto-ship-near-sensor-station.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [rebel, auto-ship, map-reveal, blue-option]
---

# Fandom — "Auto-ship near sensor station"

## Summary
The community wiki page for `AUTO_DEFENSE_MAP`. Retrieved via the MediaWiki API at revision
73946. A complete outcome tree including both blue options.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'AUTO_DEFENSE_MAP' in the datafiles."*
- Locations: Civilian Sector, Rebel Controlled Sector, Rebel Stronghold. `LRSmap=ship`,
  `unique=true`. Omits [[sector-federation-space]], reachable via `NEUTRAL_CIVILIAN`.
- Documents both blue options with their gates: **Sensors level 3** and **Teleporter**
  (no level) — matching `req="sensors" lvl="3"` and `req="teleporter"`.
- Correctly records that the Sensors branch has **two possible results** — a free map
  reveal, or the ship activating and charging you — and that the Teleporter branch is a
  guaranteed reveal with no fight.
- Reward on the kill: **low scrap** *(scrap only)* plus the sector map revealed — matching
  `autoReward level="LOW"` `scrap_only` and `<reveal_map/>` on the `REBEL_AUTO_MAP`
  `destroyed` branch. The distinction between `scrap_only` and `standard` is preserved.
- Categorised `Random_Events`, `Unique_Events`, `Beacon Map reveal opportunity`,
  `Auto-ship fights`.

## Events Covered
- [[event-auto-ship-near-sensor-station]]

## Other Pages Touched
- [[item-sensors]], [[item-teleporter]], [[event-auto-ship-near-radar-station]],
  [[event-auto-ship-near-storage-station]], [[concept-rebel-fleet-advance]]

## Reliability Notes
`medium`. Version unstated. Structurally accurate against the game files, including the
`scrap_only` vs `standard` distinction, which many pages blur. It gives no odds for the
Sensors coin flip — neither does the file.

## Contradictions Flagged
- Sector reach — recorded on [[event-auto-ship-near-sensor-station]].

## Links
- Source URL: https://ftl.fandom.com/wiki/Auto-ship_near_sensor_station
- [[source-events-rebel]], [[source-events-ships]], [[source-text-events-xml]]
