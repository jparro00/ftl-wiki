---
id: source-fandom-lanius-ship-attacking-slug
type: source
source_kind: wiki
raw: raw/wiki/lanius-ship-attacking-slug.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [lanius, slug, distress, combat, advanced-edition]
---

# Fandom — "Lanius ship attacking Slug"

## Summary
Community wiki page for `LANIUS_SLUG_DISTRESS`, retrieved via the MediaWiki API at revision
74238. The Slug twin of the Rock distress page, with the same structure and the same
reward table.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'LANIUS_SLUG_DISTRESS' in the
  datafiles."*
- Location: Abandoned Sector; `distress=true`, `LRSmap=noship`, `unique=true`.
- Confirms `LANIUS_SLUG_DISTRESS_SHIP` has **no surrender and no escape**
  (`SurrenderEscape(alt)|no`), citing `dlcEvents_anaerobic.xml`.
- Shows **no outcome text under choice 1**, matching the XML, where that choice's `<event>`
  contains only the `<ship>` tag.
- Transcribes both `LANIUS_SLUG_DISTRESS_END` outcomes (Slugs flee / Slugs grudgingly pay)
  without stating odds.

## Events Covered
- [[event-lanius-ship-attacking-slug]]

## Other Pages Touched
- [[sector-abandoned-sector]], [[entity-lanius]], [[entity-slugs]]

## Reliability Notes
`medium`. Cites the source file and ship id directly.

## Contradictions Flagged
None.

## Links
- Source URL: https://ftl.fandom.com/wiki/Lanius_ship_attacking_Slug
- [[source-dlcevents-anaerobic]], [[source-text-events-xml]]
