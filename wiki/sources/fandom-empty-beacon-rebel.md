---
id: source-fandom-empty-beacon-rebel
type: source
source_kind: wiki
raw: raw/wiki/empty-beacon-rebel.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [rebel, structural, empty-beacon]
---

# Fandom — "Empty beacon (Rebel)"

## Summary
The community wiki page for `NOTHING_REBEL`, the Rebel sector's empty beacon. Retrieved via
the MediaWiki API at revision 73663. A transcription of the five-string text list and
nothing else — which is all the event contains.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'NOTHING_REBEL' in the datafiles."*
- Locations: Rebel Controlled Sector, Rebel Stronghold. `LRSmap=noship`, `unique=false`.
  Matches the sector definitions, which allocate `NOTHING_REBEL` at `min=1 max=2` in both.
- Transcribes all **five** `text_NOTHING_REBEL_*` variants verbatim; they match
  `text_events.xml`.
- Outcome: *"Nothing happens."*
- **Does not record the `planet=` gates.** In the game file, variant 4 requires
  `planet="NONE"` and variant 5 requires `planet="PLANET_POPULATED_SMALL"`, so those two
  only appear with the matching beacon backdrop.
- Categorised `Random_Events`.

## Events Covered
- [[event-empty-beacon-rebel]]

## Other Pages Touched
- [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]]

## Reliability Notes
`medium`. Version unstated. Accurate as a transcription; omits the backdrop gating, which is
a detail only visible in the XML.

## Contradictions Flagged
None. The `planet=` gating is an omission, not a disagreement — recorded on
[[event-empty-beacon-rebel]].

## Links
- Source URL: https://ftl.fandom.com/wiki/Empty_beacon_(Rebel)
- [[source-events-rebel]], [[source-text-events-xml]], [[source-sector-data-xml]]
