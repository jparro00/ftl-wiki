---
id: source-fandom-auto-ship-fight-in-asteroid-field
type: source
source_kind: wiki
raw: raw/wiki/auto-ship-fight-in-asteroid-field.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [rebel, auto-ship, asteroid-field]
---

# Fandom — "Auto-ship fight in asteroid field"

## Summary
Community wiki page for `AUTO_ASTEROID`, retrieved via the MediaWiki API at revision 73940.
Very short — one text, one fight, one reward.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'AUTO_ASTEROID' in the datafiles."*
- Locations: Civilian Sector, Mantis Controlled Sector, Mantis Homeworlds, Pirate Controlled
  Sector, Rebel Controlled Sector, Rebel Stronghold; `asteroidfield=true`,
  `LRSmap=ship+asteroidfield`, **`unique=false`** — matching the absence of a `unique`
  attribute in the file, so the event can recur.
- Confirms the reward as *medium scrap with resources*, i.e. `autoReward level="MED"`
  `standard` via `DESTROYED_DEFAULT`.
- Intro text matches `event_AUTO_ASTEROID_text` exactly.

## Events Covered
- [[event-auto-ship-fight-in-asteroid-field]]

## Other Pages Touched
- [[event-auto-ship-fight]], [[concept-rebel-fleet-advance]]

## Reliability Notes
`medium`. No version stated. The event has no version-dependent tags, so nothing here turns
on it.

## Contradictions Flagged
One, recorded on [[event-auto-ship-fight-in-asteroid-field]]: the location list omits
[[sector-federation-space]], although `HOSTILE1` — which contains this event — is allocated
`min=2 max=2` in `STANDARD_SPACE`. Same systematic omission as the other generic-hostile
pages.

## Links
- Source URL: https://ftl.fandom.com/wiki/Auto-ship_fight_in_asteroid_field
- [[source-events-xml]], [[source-newevents]], [[source-events-ships]]
