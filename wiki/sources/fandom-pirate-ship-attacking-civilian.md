---
id: source-fandom-pirate-ship-attacking-civilian
type: source
source_kind: wiki
raw: raw/wiki/pirate-ship-attacking-civilian.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [pirate, moral-choice, save-civilian-list]
---

# Fandom — "Pirate ship attacking civilian"

## Summary
Community wiki page for `PIRATE_CIVILIAN`, retrieved via the MediaWiki API at revision
73771. Transcribes six intro variants and both choices, and confirms the enemy ship's two
win branches.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'PIRATE_CIVILIAN' in the datafiles."*
- Locations: Civilian Sector, Pirate Controlled Sector, Rock Controlled Sector, Rock
  Homeworlds, Slug Controlled Nebula, Slug Home Nebula; `alsooccur=exitandfiller`,
  `LRSmap=noship`, `unique=false`.
- **Confirms the enemy ship neither surrenders nor escapes** (`surrenderno+escapeno` on
  `PIRATE_CIVILIAN` in `events_ships.xml`) and that destroyed pays **medium** while a crew
  kill pays **high** `standard` — matching the file exactly.
- Notes the event is *"very similar to the Civilian ship chased by Pirate (distress)
  event, but lacks the Improved Weapons blue option."* Confirmed in the files: the
  distress variant has `event_PIRATE_CIVILIAN_BEACON_c3_choice` and this one has no
  equivalent.
- The "Contact the civilian ship" section is a `{{Save the Civilian Ship}}` template
  transclusion that did **not** expand in the API dump, so this page carries no detail on
  `SAVE_CIVILIAN_LIST` — that comes from `events_pirate.xml` only.

## Events Covered
- [[event-pirate-ship-attacking-civilian]]

## Other Pages Touched
- [[event-pirate-ship-attacking-civilian-distress]],
  [[event-mantis-ship-attacking-civilian]], [[entity-pirates]],
  [[sector-pirate-controlled-sector]], [[sector-rock-controlled-sector]]

## Reliability Notes
`medium`. No version stated. Incomplete on the reward tree (unexpanded template).

## Contradictions Flagged
- Trivial wording in intro variant 5: Fandom *"only to immediately be hailed"* vs game
  files *"only to be immediately hailed"*. Recorded on the event page; game files trusted.
- Sector list omits [[sector-federation-space]], reachable via the `NEUTRAL` filler list.

## Links
- Source URL: https://ftl.fandom.com/wiki/Pirate_ship_attacking_civilian
- [[source-events-pirate]], [[source-events-ships]], [[source-text-events-xml]]
