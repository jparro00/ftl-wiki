---
id: source-events-slug
type: source
source_kind: gamedata
raw: raw/gamedata/events_slug.xml
game_version: ae
ingested: 2026-08-09
reliability: high
tags: [partial-ingest]
---

# events_slug.xml

## Summary
Slug faction events, including the nebula and ion-storm lists.

Contains **38 event definitions**, **24 event lists**, 40 KB.

## Key Takeaways
- Extracted from the user's installed 1.6.x Advanced Edition build; see
  `raw/gamedata/_PROVENANCE.md`.
- Event prose is not stored here - it is referenced by id and resolved through
  [[source-text-events-xml]].
- Reliability `high`: this is the game's own data, and it outranks the community wiki
  wherever the two disagree.

## Events Covered
_Ingested incrementally as individual event pages are built. See `index.md` for which
events currently have pages._

## Contradictions Flagged
_None recorded at file level. Cross-source conflicts are flagged on the individual event
pages that carry them._

## Links
- [[source-text-events-xml]] - the string table every event depends on
- [[source-sector-data-xml]] - which sectors draw on these lists
