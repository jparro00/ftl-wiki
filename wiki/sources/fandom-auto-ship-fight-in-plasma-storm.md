---
id: source-fandom-auto-ship-fight-in-plasma-storm
type: source
source_kind: wiki
raw: raw/wiki/auto-ship-fight-in-plasma-storm.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [plasma-storm, rebel, auto-ship, blue-option, engines, cloaking, unique]
---

# Fandom — "Auto-ship fight in plasma storm"

## Summary
The community wiki page for `STORM_AUTO`. Retrieved via the MediaWiki API at revision
74839. Four choices — a forced fight plus three escape routes at different tiers.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'STORM_AUTO' in the datafiles."*
- Locations: Civilian Sector, Pirate Controlled Sector, Rebel Controlled Sector, Rebel
  Stronghold, Uncharted Nebula, Zoltan Controlled Sector, Zoltan Homeworlds.
  `plasmastorm=true`, `alsooccur=nebulafiller`, `LRSmap=noship+plasmastorm`, `unique=true`.
- Records the **Engines tier split precisely**: level **3-5** is the coin-flip escape
  (`STORM_AUTO_ESCAPE`), level **6+** is the guaranteed escape. Matches `lvl="3"` and
  `lvl="6"` on two separate choices with `max_group="0"`.
- **Cloaking** is a guaranteed escape with no level requirement.
- Fighting yields **medium scrap with resources** (`DESTROYED_DEFAULT`).
- Categorised `Auto-ship fights`.

## Events Covered
- [[event-auto-ship-fight-in-plasma-storm]]

## Other Pages Touched
- [[item-engines]], [[item-cloaking]], [[concept-rebel-fleet-advance]],
  [[sector-uncharted-nebula]], [[concept-blue-options]]

## Reliability Notes
`medium`. Version unstated. The tier split (3-5 vs 6+) is a correct reading of how two
`req="engines"` choices with different `lvl` values behave together — useful, and not
stated anywhere in the XML.

## Contradictions Flagged
None.

## Links
- Source URL: https://ftl.fandom.com/wiki/Auto-ship_fight_in_plasma_storm
- [[source-events-nebula]], [[source-events-ships]], [[source-text-events-xml]]
