---
id: source-fandom-auto-ship-warning
type: source
source_kind: wiki
raw: raw/wiki/auto-ship-warning.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [rebel, auto-ship, timed-escape, fleet-advance-risk]
---

# Fandom — "Auto-ship warning"

## Summary
The community wiki page for `AUTO_WARNING`, the timed auto-ship fight. Retrieved via the
MediaWiki API at revision 74037. Transcribes the shared nine-string intro list and then
documents the escape/gotaway/destroyed branches of the `REBEL_AUTO_WARNING` ship.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'AUTO_WARNING' in the datafiles."*
- Locations: Civilian Sector, Mantis Controlled Sector, Mantis Homeworlds, Rebel Controlled
  Sector, Rebel Stronghold. `LRSmap=ship`, `unique=true`. Omits
  [[sector-federation-space]] (reachable via `HOSTILE1` / `OVERRIDE_HOSTILE1`).
- Cites `events_ships.xml` directly for the escape behaviour and gives the escape timer as
  **40**, matching `<escape timer="40" min="22" max="22">`.
- Reward on the kill: **low** scrap with resources — matches `autoReward level="LOW"`
  `standard`.
- Describes the `gotaway` penalty as *"Rebel Fleet pursuit is **doubled**"*, where the file
  states `<modifyPursuit amount="1"/>`.
- Notes the shared intro texts with [[event-auto-ship-fight]] and the similarity to
  `No fuel: Auto-ship warning` and `Auto-ship warning in nebula`.
- Categorised `Random_Events`, `Unique_Events`, `Ship escape Events`,
  `Rebel Fleet advancement hazard`, `Auto-ship fights`.

## Events Covered
- [[event-auto-ship-warning]]

## Other Pages Touched
- [[event-auto-ship-fight]], [[event-auto-bait]], [[concept-rebel-fleet-advance]],
  [[concept-rebel-fleet-advance]]

## Reliability Notes
`medium`. Version unstated. Unusually well-sourced for a Fandom page — it cites the ship
definition and its timer values — but renders `modifyPursuit` in gameplay terms rather than
file terms.

## Contradictions Flagged
- "pursuit is doubled" vs `<modifyPursuit amount="1"/>` — recorded on
  [[event-auto-ship-warning]].
- Sector reach narrower than the event lists support.

## Links
- Source URL: https://ftl.fandom.com/wiki/Auto-ship_warning
- [[source-events-rebel]], [[source-events-ships]], [[source-text-events-xml]]
