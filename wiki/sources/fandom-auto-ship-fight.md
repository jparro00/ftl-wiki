---
id: source-fandom-auto-ship-fight
type: source
source_kind: wiki
raw: raw/wiki/auto-ship-fight.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [rebel, auto-ship, combat]
---

# Fandom — "Auto-ship fight"

## Summary
The community wiki page for `REBEL_AUTO`, the baseline auto-ship encounter. Retrieved via
the MediaWiki API at revision 73938. A transcription of the nine-string `REBEL_AUTO` text
list plus the win condition.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'REBEL_AUTO' in the datafiles."*
- Locations: Abandoned Sector, Civilian Sector, Pirate Controlled Sector, Rebel Controlled
  Sector, Rebel Stronghold, Zoltan Controlled Sector, Zoltan Homeworlds. `LRSmap=ship`,
  `unique=false`. It omits [[sector-federation-space]], reachable via `HOSTILE1`.
- Transcribes all **nine** `text_REBEL_AUTO_*` variants; they match `text_events.xml`.
- Outcome: destroy the auto-ship → *"The ship explodes, leaving behind a substantial
  collection of useful scrap material."* → medium scrap with resources. This matches the
  `DESTROYED_DEFAULT` `autoReward level="MED"` `standard` in the game files.
- **Notes the shared text list:** *"This event shares its intro texts with the Auto-ship
  warning event, but the fight is slightly different."* — useful confirmation that
  `REBEL_AUTO`, `AUTO_WARNING` and the unreachable `AUTO_BAIT` are indistinguishable at the
  beacon.
- Categorised `Random_Events`, `Auto-ship fights`.

## Events Covered
- [[event-auto-ship-fight]]

## Other Pages Touched
- [[event-auto-ship-warning]], [[concept-rebel-fleet-advance]]

## Reliability Notes
`medium`. Version unstated. Accurate and consistent with the game files on everything it
covers; its location list is narrower than the event lists imply.

## Contradictions Flagged
None outright. Sector reach is narrower than [[source-newevents]] /
[[source-dlceventsoverwrite]] support.

## Links
- Source URL: https://ftl.fandom.com/wiki/Auto-ship_fight
- [[source-events-rebel]], [[source-events-ships]], [[source-text-events-xml]]
