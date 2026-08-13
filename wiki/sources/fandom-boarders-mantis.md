---
id: source-fandom-boarders-mantis
type: source
source_kind: wiki
raw: raw/wiki/boarders-mantis.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [mantis, boarding-hazard]
---

# Fandom — "Boarders: Mantis"

## Summary
The community wiki page for the event the game files call `MANTIS_BOARDERS`. Retrieved via
the MediaWiki API at revision 73963. A short page: three intro-text variants, the boarder
count, and the sector list.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'MANTIS_BOARDERS' in the datafiles."*
  This is the join key to [[source-events-xml]].
- Locations template gives Mantis Controlled Sector and Mantis Homeworlds, `unique=true`,
  and `LRSmap=noship` — long-range scanners show no ship at the beacon. The
  no-ship detail is **not** derivable from the game files.
- States **2–4 Mantis boarders**, matching `<boarders min="2" max="4" class="mantis"/>` in
  `events_mantis.xml` exactly.
- Transcribes all three `MANTIS_BOARDERS` text-list variants verbatim; they match
  `text_events.xml` word for word.
- Categorised `Random_Events`, `Unique_Events`, `Boarding hazard`.

## Events Covered
- [[event-boarders-mantis]]

## Other Pages Touched
- [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]], [[entity-mantis]]

## Reliability Notes
`medium`. The page states no game version, so `game_version` is `unknown` — not `ae`.
Everything it asserts that *can* be checked against the 1.6.x AE files checks out, which
is a point in its favour but not a version claim.

## Contradictions Flagged
None. The page agrees with the game files on every checkable point.

## Links
- Source URL: https://ftl.fandom.com/wiki/Boarders:_Mantis
- [[source-events-xml]], [[source-text-events-xml]], [[source-sector-data-xml]]
