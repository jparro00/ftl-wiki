---
id: source-fandom-abandoned-station
type: source
source_kind: wiki
raw: raw/wiki/abandoned-station.md
game_version: ae
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [filler, boarding-risk, pds, clone-bay, blue-option, ae]
---

# Fandom — "Abandoned station"

## Summary
The community wiki page for `EMPTY_STATION2`. Retrieved via the MediaWiki API at revision
74022. Transcribes all six outcomes of the examine branch and explains the odd event id.

## Key Takeaways
- **Names the in-game id explicitly:** *"This event is called 'EMPTY_STATION2' in the
  datafiles."*
- Explains the `2` suffix: *"There are no 'EMPTY_STATION' or 'EMPTY_STATION1' events in
  the datafiles."* The name is a notation marking that the event is **also reused as a
  sub-event of the Space station under construction event** — which is
  `QUEST_CONSTRUCTIONYARD` in `newEvents.xml`, and does load `EMPTY_STATION2_LIST`
  directly.
- Uses a `{{DuplicateEvent|2}}` marker on the two low-scrap outcomes and on the two
  successful clone outcomes — i.e. the wiki independently observed the same duplication
  the event lists encode.
- Locations template: Slug Controlled Nebula, Slug Home Nebula, `alsooccur=exitandfiller`,
  `unique=true`, Long-Range Scanners `noship`.
- Categorised `Advanced Edition Content Events`, `Filler Events`, `Fights with Default
  Rewards`, `Anti-Ship Battery hazard risk`, `Boarding risk`, `Pirate ship fights`. The
  AE category corroborates the `dlcEventsOverwrite.xml`-only list membership.
- Gives `PIRATE` surrender/escape numbers via a template: escape+surrender, 50%/20–40/2–4
  and 50%/30–40/3–4.

## Events Covered
- [[event-abandoned-station]]

## Other Pages Touched
- [[entity-pirates]], [[item-clone-bay]], [[concept-anti-ship-battery]],
  [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]

## Reliability Notes
`medium`. The `Advanced Edition Content Events` category is an explicit version statement
and agrees with the game files. The claim about reuse inside Space station under
construction is directly verifiable in `newEvents.xml`.

## Contradictions Flagged
None.

## Links
- Source URL: https://ftl.fandom.com/wiki/Abandoned_station
- [[source-newevents]], [[source-dlceventsoverwrite]], [[source-text-events-xml]],
  [[source-events-ships]]
