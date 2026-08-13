---
id: source-fandom-empty-beacon-zoltan
type: source
source_kind: wiki
raw: raw/wiki/empty-beacon-zoltan.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [zoltan, empty, varies-text, flavour]
---

# Fandom — "Empty beacon (Zoltan)"

## Summary
The community wiki page for `NOTHING_ZOLTAN`. Retrieved via the MediaWiki API at revision
73666 — the oldest revision in this batch. Its sole content is the seven flavour text
variants, and it transcribes all seven correctly.

## Key Takeaways
- **Names the in-game id explicitly**: *"This event is called 'NOTHING_ZOLTAN' in the
  datafiles."*
- Lists **seven** intro variants, matching the seven ids
  (`text_NOTHING_ZOLTAN_1` … `_7`) the game file references — **and in the same order**.
  Verified string by string against `text_events.xml`; a complete and accurate
  transcription, unlike [[source-fandom-pirate-fight-zoltan]].
- Confirms `unique=false` (repeatable) and that nothing happens.
- Long-Ranged Scanners `noship`.
- Preserves the in-game strategy hint carried by variant 4: *"Their Energy Shields are
  impressive, but you note how quickly beam and ion weaponry take them down."*

## Events Covered
- [[event-empty-beacon-zoltan]]

## Other Pages Touched
- [[item-zoltan-shield]] — variant 4 is the game's own counter-play hint

## Reliability Notes
`medium`. States no game version. Because every claim was checkable against the game
files and all seven checked out, this page is at the high end of its reliability band.

## Contradictions Flagged
None. All seven strings match `text_events.xml` verbatim.

## Links
- Source URL: https://ftl.fandom.com/wiki/Empty_beacon_(Zoltan)
- [[source-events-zoltan]], [[source-text-events-xml]]
