---
id: source-fandom-auto-ship-fight-in-nebula
type: source
source_kind: wiki
raw: raw/wiki/auto-ship-fight-in-nebula.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [nebula, rebel, auto-ship, combat]
---

# Fandom — "Auto-ship fight in nebula"

## Summary
The community wiki page for `NEBULA_AUTO`. Retrieved via the MediaWiki API at revision
74838. A short page: the five intro-text variants, one outcome, and the datafile id.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'NEBULA_AUTO' in the datafiles."*
- Locations: Civilian Sector, Pirate Controlled Sector, Rebel Controlled Sector, Rebel
  Stronghold, Uncharted Nebula, Zoltan Controlled Sector, Zoltan Homeworlds.
  `nebula=true`, `alsooccur=nebulafiller`, `LRSmap=ship+nebula`, `unique=false`.
- Transcribes all five `text_NEBULA_AUTO_LIST_*` variants; they match `text_events.xml`.
- Outcome: fight an Auto-ship; on destruction *"The ship explodes, leaving behind a
  substantial collection of useful scrap material."* → **medium scrap with resources**.
  That corresponds to the `DESTROYED_DEFAULT` list's `autoReward level="MED">standard`.
- `alsooccur=nebulafiller` is the wiki's flag for events that also fill nebula beacons
  generated inside otherwise non-nebula sectors. The XML does not encode this directly.

## Events Covered
- [[event-auto-ship-fight-in-nebula]]

## Other Pages Touched
- [[concept-rebel-fleet-advance]], [[sector-uncharted-nebula]], [[sector-civilian-sector]]

## Reliability Notes
`medium`. Version unstated. Its outcome description is a paraphrase of `DESTROYED_DEFAULT`
rather than a direct reading of the event definition, which attaches no reward of its own.

## Contradictions Flagged
None.

## Links
- Source URL: https://ftl.fandom.com/wiki/Auto-ship_fight_in_nebula
- [[source-events-nebula]], [[source-events-ships]], [[source-text-events-xml]]
