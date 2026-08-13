---
id: source-fandom-boarders-humans-pirate
type: source
source_kind: wiki
raw: raw/wiki/boarders-humans-pirate.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [pirate, boarding-hazard, varies-text]
---

# Fandom — "Boarders: Humans (Pirate)"

## Summary
Community wiki page for `BOARDERS`, retrieved via the MediaWiki API at revision 73958. Its
main value is transcribing **all five** intro variants of the `BOARDERS_TEXT` text list,
which the event itself only references by `load=`.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'BOARDERS' in the datafiles."*
- Locations: **Pirate Controlled Sector only**; `LRSmap=noship`, `unique=true` — matching
  `unique="true"` in the file.
- Opens with *"The intro text for this event varies, and could be any of the following"* and
  then lists five paragraphs, matching `text_BOARDERS_TEXT_1` … `_5` verbatim.
- Confirms 3–5 human boarders and **no reward** — matching a file body that is a
  `<text load>` and a `<boarders>` tag with nothing else.
- **Notably omits Federation Space**, whose only route to this event is the
  `HOSTILE_BOARDING` list that `sector_data.xml` allocates `min=0 max=0`. That omission is
  corroborating evidence the list is dead — the same argument recorded on
  [[event-boarders-asteroid]] and [[event-boarders-humans-near-sun]].

## Events Covered
- [[event-boarders-humans-pirate]]

## Other Pages Touched
- [[event-boarders-humans-jammed-sensors]], [[event-boarders-humans-near-sun]],
  [[entity-pirates]], [[sector-pirate-controlled-sector]]

## Reliability Notes
`medium`. No version stated. The event has no version-dependent tags.

## Contradictions Flagged
None. Its sector list matches the live `BOARDERS_PIRATE` allocation.

## Links
- Source URL: https://ftl.fandom.com/wiki/Boarders:_Humans_(Pirate)
- [[source-events-xml]], [[source-events-pirate]], [[source-text-events-xml]], [[source-sector-data-xml]]
