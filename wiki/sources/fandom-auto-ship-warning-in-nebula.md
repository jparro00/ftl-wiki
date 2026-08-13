---
id: source-fandom-auto-ship-warning-in-nebula
type: source
source_kind: wiki
raw: raw/wiki/auto-ship-warning-in-nebula.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [nebula, rebel, auto-ship, fleet-advance, escape, unique]
---

# Fandom — "Auto-ship warning in nebula"

## Summary
The community wiki page for `NEBULA_AUTO_WARNING`. Retrieved via the MediaWiki API at
revision 74841. Short, but it is the only source here that annotates the enemy ship's
escape timer.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'NEBULA_AUTO_WARNING' in the
  datafiles."*
- Locations: Civilian Sector, Pirate Controlled Sector, Rebel Controlled Sector, Rebel
  Stronghold, Uncharted Nebula, Zoltan Controlled Sector, Zoltan Homeworlds.
  `nebula=true`, `alsooccur=nebulafiller`, `LRSmap=ship+nebula`, `unique=true`.
- Annotates the `REBEL_AUTO_WARNING` ship as **starting its escape immediately with a
  40-second timer**, citing `events_ships.xml`. That matches
  `<escape timer="40" min="22" max="22">`.
- If it escapes: *"Rebel Fleet pursuit is doubled."* This is the wiki's reading of
  `<modifyPursuit amount="1"/>`; the XML states only the amount, not "doubled".
- If destroyed: **low scrap with resources** (`autoReward level="LOW">standard`).
- Categorised `Ship escape Events`, `Rebel Fleet advancement hazard`, `Auto-ship fights`.
- Cross-references `No fuel: Auto-ship warning` and `Auto-ship warning`.

## Events Covered
- [[event-auto-ship-warning-in-nebula]]

## Other Pages Touched
- [[concept-rebel-fleet-advance]], [[concept-rebel-fleet-advance]], [[sector-uncharted-nebula]]

## Reliability Notes
`medium`. Version unstated. The "doubled" phrasing is interpretation layered on top of
`modifyPursuit`; treat the raw amount (`+1`) as the primary fact.

## Contradictions Flagged
None outright — see the `modifyPursuit` phrasing note above.

## Links
- Source URL: https://ftl.fandom.com/wiki/Auto-ship_warning_in_nebula
- [[source-events-nebula]], [[source-events-ships]], [[source-text-events-xml]]
