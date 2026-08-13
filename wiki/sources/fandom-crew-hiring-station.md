---
id: source-fandom-crew-hiring-station
type: source
source_kind: wiki
raw: raw/wiki/crew-hiring-station.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [crew, trading, items-pool]
---

# Fandom — "Crew hiring station"

## Summary
Community wiki page for `TAVERN_HIRE`, retrieved at revision 73989. Confirms the two
hire prices and adds one piece of engine behaviour the game files do not encode: the
crew's race and skills are shown before you pay.

## Key Takeaways
- Names the in-game id in Notes: *"This event is called 'TAVERN_HIRE' in the
  datafiles."*
- Locations: the 14 sectors that allocate `ITEMS`, plus `alsooccur=exit` — consistent
  with `ITEMS` being half of `EXIT_LIST`.
- Prices rendered as **25–45** and **25–55** scrap, matching the two `item_modify` bands
  exactly.
- Footnote (used on both hire options): *"The crew race and their skills are shown prior
  to the trade."* Nothing in `newEvents.xml` encodes this — treated as Fandom's account
  of engine behaviour.
- `unique=true`, matching the files.
- Categorised under "Crew purchase opportunity".

## Events Covered
- [[event-crew-hiring-station]]

## Other Pages Touched
- [[event-trade-scrap-for-upgrades]], [[event-improve-reactor-for-supplies]],
  [[concept-event-list-weighting]]

## Reliability Notes
`medium`. Numbers match the files. The "shown prior to the trade" claim is unverifiable
from data and is attributed rather than asserted.

## Contradictions Flagged
- Trivial: text variant 3 is transcribed as *"a meeting place"* where the game string
  reads *"meeting place"*, and the three variants are listed in a different order.
  Recorded on [[event-crew-hiring-station]].

## Links
- Source URL: https://ftl.fandom.com/wiki/Crew_hiring_station
- [[source-newevents]], [[source-text-events-xml]], [[source-dlceventsoverwrite]]
