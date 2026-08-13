---
id: source-fandom-slaver-hostile
type: source
source_kind: wiki
raw: raw/wiki/slaver-hostile.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [pirate, slaver, crew-loss-risk, blue-option]
---

# Fandom — "Slaver (hostile)"

## Summary
Community wiki page for `PIRATE_SLAVER`, retrieved via the MediaWiki API at revision
73864. Documents the three choices, the Clone Bay interaction, and the Engines-6 escape.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'PIRATE_SLAVER' in the datafiles."*
- Locations: Civilian Sector, Pirate Controlled Sector; `LRSmap=ship`, `unique=false`.
- **Confirms the Clone Bay does not save the surrendered crew member**, quoting the
  `<clone>false</clone>` message verbatim, and categorises the page under
  "Clone Bay failed revival".
- Marks the two "get away" texts of `PIRATE_SLAVER_RUN` with a duplicate-event notice —
  the same observation behind the derived **2/3 escape, 1/3 fight** split.
- The "Slaver Fight" section is a MediaWiki template transclusion (`{{Slaver Fight}}`)
  that did **not** come through in the API dump, so this page carries **no** numbers for
  the `PIRATE_SLAVER` ship's surrender/escape/destroyed branches. Those come from
  `events_ships.xml` only.

## Events Covered
- [[event-slaver-hostile]]

## Other Pages Touched
- [[event-slaver-friendly]], [[item-clone-bay]], [[entity-pirates]],
  [[sector-pirate-controlled-sector]], [[sector-civilian-sector]]

## Reliability Notes
`medium`. No version stated. Incomplete on the fight itself (unexpanded template).

## Contradictions Flagged
- **Intro text wording.** Fandom: *"Hand over one of your crew and the rest can go
  unharmed."* Game files: *"Hand over one of your crew-members and the rest of you can go
  free unharmed."* Recorded on [[event-slaver-hostile]]; game files trusted.
- Sector list omits [[sector-federation-space]], reachable via `HOSTILE_CIVILIAN`.

## Links
- Source URL: https://ftl.fandom.com/wiki/Slaver_(hostile)
- [[source-events-pirate]], [[source-events-ships]], [[source-events-xml]]
