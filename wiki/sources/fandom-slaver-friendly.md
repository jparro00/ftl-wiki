---
id: source-fandom-slaver-friendly
type: source
source_kind: wiki
raw: raw/wiki/slaver-friendly.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [pirate, slaver, crew-purchase, blue-option]
---

# Fandom — "Slaver (friendly)"

## Summary
Community wiki page for `FRIENDLY_SLAVER`, retrieved via the MediaWiki API at revision
73863. Documents the four choices including the Teleporter blue option, and adds a UI
detail the game files do not encode.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'FRIENDLY_SLAVER' in the datafiles."*
- Locations: Abandoned Sector, Civilian Sector, Pirate Controlled Sector, Rock Controlled
  Sector, Rock Homeworlds, Slug Controlled Nebula, Slug Home Nebula, Zoltan Controlled
  Sector, Zoltan Homeworlds; `alsooccur=exitandfiller`, `LRSmap=ship`, `unique=true`.
- **Adds a detail absent from the game files**: *"the crew race and crew skills are shown
  prior to the trade"* — choice 1 is an informed purchase, not a blind one. Nothing in
  `events_pirate.xml` says this, so it is a UI observation.
- Confirms the purchase price as 25–45 scrap, matching
  `<item type="scrap" min="-45" max="-25"/>`.
- Marks the first two `FRIENDLY_SLAVER_TELEPORTER` entries with a duplicate-event notice —
  the same observation behind the derived **2/3 crew + fight, 1/3 fight** split.
- Notes that *"Crew Teleporter blue option does not prevent receiving another crew by
  accepting a surrender offer or killing enemy crew (in 2 out of 3 outcomes)"* — i.e. the
  crew rewards stack.
- The "Slaver Fight" section is a `{{Slaver Fight}}` template transclusion that did not
  come through in the API dump, so this page carries no ship numbers.

## Events Covered
- [[event-slaver-friendly]]

## Other Pages Touched
- [[event-slaver-hostile]], [[item-teleporter]], [[entity-pirates]],
  [[sector-pirate-controlled-sector]], [[sector-rock-controlled-sector]],
  [[sector-zoltan-controlled-sector]]

## Reliability Notes
`medium`. No version stated. Incomplete on the fight itself (unexpanded template).

## Contradictions Flagged
- Trivial: Fandom renders the intro as *"well known slave trader"*; the file has
  *"well-known"*. Not recorded as a substantive conflict.
- Sector list omits [[sector-federation-space]], reachable via the `NEUTRAL` filler list.

## Links
- Source URL: https://ftl.fandom.com/wiki/Slaver_(friendly)
- [[source-events-pirate]], [[source-events-ships]], [[source-events-xml]]
