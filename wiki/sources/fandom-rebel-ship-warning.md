---
id: source-fandom-rebel-ship-warning
type: source
source_kind: wiki
raw: raw/wiki/rebel-ship-warning.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [rebel, timed-escape, fleet-advance-risk]
---

# Fandom — "Rebel ship warning"

## Summary
The community wiki page for `SQUAT_WARNING`, the crewed timed-escape Rebel scout. Retrieved
via the MediaWiki API at revision 73817. Short, accurate, and explicit about the ship's
behaviour.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'SQUAT_WARNING' in the datafiles."*
- Locations: Civilian Sector, Engi Controlled Sector, Engi Homeworlds, Rebel Controlled
  Sector, Rebel Stronghold. `LRSmap=ship`, `unique=true`. Omits
  [[sector-federation-space]].
- Cites the enemy ship as `SQUAT_WARNING` in `events_ships.xml`, gives the escape timer as
  **40**, and states **no surrender** — all matching the file.
- Transcribes the single intro text, the escape text, the `gotaway` text, and **both**
  win texts (`destroyed` and `deadCrew`) verbatim; they match `text_events.xml`.
- Reward: **medium** scrap with resources on either kill — matches `autoReward level="MED"`
  `standard` on both branches.
- Describes the `gotaway` penalty as *"Rebel Fleet pursuit is **doubled**"*, where the file
  states `<modifyPursuit amount="1"/>`.
- Categorised `Random_Events`, `Unique_Events`, `Ship escape Events`,
  `Rebel Fleet advancement hazard`.

## Events Covered
- [[event-rebel-ship-warning]]

## Other Pages Touched
- [[event-auto-ship-warning]], [[concept-rebel-fleet-advance]], [[concept-rebel-fleet-advance]]

## Reliability Notes
`medium`. Version unstated. Everything it asserts about the ship matches
`events_ships.xml`; the only divergence is the pursuit wording.

## Contradictions Flagged
- "pursuit is doubled" vs `<modifyPursuit amount="1"/>` — recorded on
  [[event-rebel-ship-warning]].

## Links
- Source URL: https://ftl.fandom.com/wiki/Rebel_ship_warning
- [[source-events-rebel]], [[source-events-ships]], [[source-text-events-xml]]
