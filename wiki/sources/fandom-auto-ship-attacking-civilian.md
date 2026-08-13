---
id: source-fandom-auto-ship-attacking-civilian
type: source
source_kind: wiki
raw: raw/wiki/auto-ship-attacking-civilian.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [rebel, auto-ship, save-civilian, optional-fight]
---

# Fandom — "Auto-ship attacking civilian"

## Summary
The community wiki page for `AUTO_CIVILIAN`. Retrieved via the MediaWiki API at revision
73984. Short, because it delegates the rescue outcomes to a shared
`{{Save the Civilian Ship}}` template rather than transcribing them.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'AUTO_CIVILIAN' in the datafiles."*
- Locations: Civilian Sector, Rebel Controlled Sector, Rebel Stronghold. `LRSmap=noship`,
  `unique=false` — the `unique=false` matches the file's explicit
  `unique="false"` attribute. Omits [[sector-federation-space]], reachable via `HOSTILE1` /
  `OVERRIDE_HOSTILE1`.
- Transcribes the intro text and both choice/outcome texts; all match `text_events.xml`.
- Reward on the kill: **low** scrap with resources — matches
  `autoReward level="LOW"` `standard` on the `REBEL_AUTO_CIVILIAN` `destroyed` branch.
  It does not mention the `deadCrew` branch (which is unreachable — auto-ships have no
  crew).
- Records the follow-up as *"Contact the civilian ship"* → the shared
  `{{Save the Civilian Ship}}` table, i.e. `SAVE_CIVILIAN_LIST`.
- Categorised `Random_Events`, `Auto-ship fights`.

## Events Covered
- [[event-auto-ship-attacking-civilian]]

## Other Pages Touched
- [[event-mantis-ship-attacking-civilian]] (same `SAVE_CIVILIAN_LIST` table),
  [[concept-rebel-fleet-advance]]

## Reliability Notes
`medium`. Version unstated. Accurate on what it covers; the rescue table lives behind a
template, so this page is not a transcription source for those six outcomes —
[[source-events-pirate]] is.

## Contradictions Flagged
- Sector reach narrower than the event lists support — recorded on
  [[event-auto-ship-attacking-civilian]].

## Links
- Source URL: https://ftl.fandom.com/wiki/Auto-ship_attacking_civilian
- [[source-events-rebel]], [[source-events-ships]], [[source-events-pirate]],
  [[source-text-events-xml]]
