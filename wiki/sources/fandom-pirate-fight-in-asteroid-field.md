---
id: source-fandom-pirate-fight-in-asteroid-field
type: source
source_kind: wiki
raw: raw/wiki/pirate-fight-in-asteroid-field.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [pirate, hostile, asteroid-field, cut-content]
---

# Fandom — "Pirate fight in asteroid field"

## Summary
Community wiki page for `PIRATE_ASTEROID`, retrieved via the MediaWiki API at revision
73767. Short page: one intro text, one choice, default rewards — plus a useful note about
cut content.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'PIRATE_ASTEROID' in the datafiles."*
- Locations: Civilian Sector, Engi Controlled Sector, Engi Homeworlds, Pirate Controlled
  Sector; `asteroidfield=true`, `LRSmap=ship+asteroidfield`, `unique=false`.
- **Independently confirms the cut Piloting blue option**, citing TCRF's
  "Partially Unused Events" page: *"the game code contains a commented out level 2+
  piloting system blue option for attempt to escape the asteroid field environment."*
  This matches the commented-out `<choice req="pilot" lvl="2">` and
  `PIRATE_ASTEROID_PILOTING` list in `raw/gamedata/events_pirate.xml`.
- Intro text matches `event_PIRATE_ASTEROID_text` exactly.

## Events Covered
- [[event-pirate-fight-in-asteroid-field]]

## Other Pages Touched
- [[event-pirate-fight]], [[entity-pirates]], [[sector-pirate-controlled-sector]]

## Reliability Notes
`medium`. No version stated. Location list omits [[sector-federation-space]], which the
event reaches via `HOSTILE_CIVILIAN`.

## Contradictions Flagged
- Sector list omits Federation Space — recorded on the event page, not resolved.

## Links
- Source URL: https://ftl.fandom.com/wiki/Pirate_fight_in_asteroid_field
- [[source-events-pirate]], [[source-newevents]]
