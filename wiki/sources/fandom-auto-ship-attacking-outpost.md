---
id: source-fandom-auto-ship-attacking-outpost
type: source
source_kind: wiki
raw: raw/wiki/auto-ship-attacking-outpost.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [rebel, auto-ship, filler, optional-fight]
---

# Fandom — "Auto-ship attacking outpost"

## Summary
The community wiki page for `AUTO_REFUEL_STATION`. Retrieved via the MediaWiki API at
revision 73936. A complete transcription of a short, deterministic event.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'AUTO_REFUEL_STATION' in the
  datafiles."*
- Locations: Civilian Sector, Slug Controlled Nebula, Slug Home Nebula, with
  `alsooccur=exitandfiller`, `LRSmap=ship`, `unique=true`. The `exitandfiller` flag matches
  the event's membership in the hardcoded `NEUTRAL` / `NEUTRAL_EXIT` lists. Omits
  [[sector-federation-space]], reachable via `HOSTILE1` / `OVERRIDE_HOSTILE1`.
- Transcribes intro, both choice outcomes, the ship-destroyed text and the outpost hail —
  all match `text_events.xml`.
- Records the **stacked reward** correctly: low scrap with resources on the kill, then
  medium scrap with resources from the grateful outpost — matching `autoReward level="LOW"`
  `standard` followed by `autoReward level="MED"` `standard`.
- Categorised `Random_Events`, `Unique_Events`, `Filler_Events`, `Auto-ship fights`.

## Events Covered
- [[event-auto-ship-attacking-outpost]]

## Other Pages Touched
- [[event-rebel-ship-attacking-refueling-outpost]], [[concept-rebel-fleet-advance]]

## Reliability Notes
`medium`. Version unstated. Accurate and complete on mechanics; only the location list is
narrower than the event lists support.

## Contradictions Flagged
- Sector reach — recorded on [[event-auto-ship-attacking-outpost]].

## Links
- Source URL: https://ftl.fandom.com/wiki/Auto-ship_attacking_outpost
- [[source-events-rebel]], [[source-events-ships]], [[source-text-events-xml]]
