---
id: source-fandom-pirate-toll
type: source
source_kind: wiki
raw: raw/wiki/pirate-toll.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [pirate, scrap-cost, optional-fight]
---

# Fandom — "Pirate toll"

## Summary
Community wiki page for `PIRATE_CHOICE`, retrieved via the MediaWiki API at revision
73782. Two choices — pay 15–25 scrap, or fight a standard pirate ship.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'PIRATE_CHOICE' in the datafiles."*
- Locations: Civilian Sector, Engi Controlled Sector, Engi Homeworlds, Pirate Controlled
  Sector; `LRSmap=ship`, `unique=false`.
- Scrap cost 15–25 matches `<item type="scrap" min="-25" max="-15"/>` in the game files.
- **This is the page that annotates the `PIRATE` enemy ship's surrender/escape numbers**:
  *"can offer a surrender (50% chance at 30-40% hull) and/or try to escape (50% chance at
  20-40% hull)"*. That makes it the reference point for the `chance`-attribute
  contradiction documented on [[event-pirate-fight]].
- All prose matches `text_events.xml`.

## Events Covered
- [[event-pirate-toll]]

## Other Pages Touched
- [[event-pirate-fight]], [[entity-pirates]], [[sector-pirate-controlled-sector]]

## Reliability Notes
`medium`. No version stated. Location list omits [[sector-federation-space]].

## Contradictions Flagged
- **The `chance` attribute reading.** Fandom's "50%" happens to match `chance="0.5"`, but
  its numbers on other pirate ships are consistently `1 − chance`
  ([[source-fandom-pirate-briber]], [[source-fandom-destroyed-cargo-ship]]). Recorded on
  [[event-pirate-fight]].
- Also renders `min`/`max` hull **points** as hull **percentages**, with its own tooltip
  conceding the underlying value may be "3-4 hull".
- Sector list omits Federation Space.

## Links
- Source URL: https://ftl.fandom.com/wiki/Pirate_toll
- [[source-events-pirate]], [[source-events-ships]], [[source-newevents]]
