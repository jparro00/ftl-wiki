---
id: source-fandom-lanius-ship-attacking-rock
type: source
source_kind: wiki
raw: raw/wiki/lanius-ship-attacking-rock.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [lanius, rock, distress, combat, advanced-edition]
---

# Fandom — "Lanius ship attacking Rock"

## Summary
Community wiki page for `LANIUS_ROCK_DISTRESS`, retrieved via the MediaWiki API at revision
74237. Documents the distress-beacon fight, both winning texts, and the two-way aftermath
roll when you contact the Rockmen.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'LANIUS_ROCK_DISTRESS' in the
  datafiles."*
- Location: Abandoned Sector; `distress=true`, `LRSmap=noship`, `unique=true`.
- Confirms the enemy ship block has **no surrender and no escape** — its
  `SurrenderEscape(alt)` template is rendered with `no`, and it names the ship
  `LANIUS_ROCK_DISTRESS_SHIP` and the file `dlcEvents_anaerobic.xml`.
- Both `destroyed` and `deadCrew` are shown paying medium scrap with resources, matching the
  XML's `autoReward level="MED">standard`.
- Transcribes both `LANIUS_ROCK_DISTRESS_END` outcomes (gratitude / salvage) but states no
  odds for the split.

## Events Covered
- [[event-lanius-ship-attacking-rock]]

## Other Pages Touched
- [[sector-abandoned-sector]], [[entity-lanius]], [[entity-rock-men]]

## Reliability Notes
`medium`. Notably it cites the source file and ship id directly, which makes it easy to
cross-check.

## Contradictions Flagged
None.

## Links
- Source URL: https://ftl.fandom.com/wiki/Lanius_ship_attacking_Rock
- [[source-dlcevents-anaerobic]], [[source-text-events-xml]]
