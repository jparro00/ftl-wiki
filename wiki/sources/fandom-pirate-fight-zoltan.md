---
id: source-fandom-pirate-fight-zoltan
type: source
source_kind: wiki
raw: raw/wiki/pirate-fight-zoltan.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [zoltan, filler-fight, pirate, incomplete-transcription]
---

# Fandom — "Pirate fight (Zoltan)"

## Summary
The community wiki page for `ZOLTAN_PIRATE`. Retrieved via the MediaWiki API at revision
73765 — the oldest revision in this Zoltan batch. It adds little beyond the game files
and is **demonstrably incomplete** on the one thing it exists to record: the intro text
variants.

## Key Takeaways
- **Names the in-game id explicitly**: *"This event is called 'ZOLTAN_PIRATE' in the
  datafiles."*
- Confirms the event is `unique=false` (repeatable within a sector) and that a ship shows
  on Long-Ranged Scanners.
- Confirms **default rewards** and no choices.
- Lists **five** intro text variants, which correspond to game strings 1, 6, 3, 7 and 5 —
  exactly the second half of the ten-entry `textList`.
- Categorised `Fights with Default Rewards`, `Pirate ship fights`.

## Events Covered
- [[event-pirate-fight-zoltan]]

## Other Pages Touched
- [[entity-pirates]]

## Reliability Notes
`medium`, and lower than usual in practice — the page's only substantive content is a
text list that is missing two of seven entries. States no game version.

## Contradictions Flagged
> ⚠️ **CONTRADICTION:** number of intro variants.
> Fandom lists **five**. The game files reference **seven** distinct strings
> (`text_ZOLTAN_PIRATE_1` … `_7`) across a ten-entry list, with 1, 3 and 5 duplicated
> ([[source-events-zoltan]], [[source-text-events-xml]]).
> The two missing strings — `_2` and `_4` — are near-identical rewrites of `_6` and `_7`,
> which suggests the wiki editor deduplicated by eye rather than by id.
> Recorded on [[event-pirate-fight-zoltan]]. Game files trusted.

## Links
- Source URL: https://ftl.fandom.com/wiki/Pirate_fight_(Zoltan)
- [[source-events-zoltan]], [[source-text-events-xml]]
