---
id: source-fandom-rock-atheists
type: source
source_kind: wiki
raw: raw/wiki/rock-atheists.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [rock, crew-reward, blue-option]
---

# Fandom — "Rock atheists"

## Summary
Community wiki page for `ROCK_ATHIEST`, retrieved via the MediaWiki API at revision 73844.
Full choice tree with outcomes, including the Sensors blue option and its level gate.

## Key Takeaways
- **Names the in-game id, with the developers' typo intact**: *"This event is called
  'ROCK_ATHIEST' [sic] in the datafiles."*
- Locations: Rock Controlled Sector, Rock Homeworlds; `LRSmap=ship`, `unique=true`.
- Renders the blue option as **`Improved Sensors … level=2+`**, matching
  `req="sensors" lvl="2"` in the game files — and making explicit that Sensors level 1 is
  insufficient, which the raw attribute alone does not spell out.
- Tags the "they close frequencies and jump away" outcome with `{{DuplicateEvent|2}}`,
  i.e. it occupies **two** of the three slots in `eventList ROCK_ATHIEST_GOOD`. This is
  independent confirmation of the 1/3-crew, 2/3-nothing weighting derived from the XML.
- Categorised `Fights with Default Rewards` and `Crew reward opportunity`.

## Events Covered
- [[event-rock-atheists]]

## Other Pages Touched
- [[item-sensors]], [[item-rock-crew]], [[entity-rock-men]], [[event-rock-fight]]

## Reliability Notes
`medium`. No version stated. The `{{DuplicateEvent}}` convention makes this page unusually
useful — it encodes list weighting that the game files only imply.

## Contradictions Flagged
None.

## Links
- Source URL: https://ftl.fandom.com/wiki/Rock_atheists
- [[source-events-rock]], [[source-text-events-xml]]
