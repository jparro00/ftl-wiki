---
id: source-fandom-crystal-fight
type: source
source_kind: wiki
raw: raw/wiki/crystal-fight.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [crystal-sector, combat, surrender, crew-reward]
---

# Fandom — "Crystal fight"

## Summary
The community wiki page for `CRYSTAL_FIGHT`, the most common encounter in the Crystal
sector. Retrieved via the MediaWiki API at revision 74033. The bulk of the page is the
`CRYSTAL_SHIP` surrender tree, which is where all the decision-making lives.

## Key Takeaways
- Names the in-game id: *"This event is called 'CRYSTAL_FIGHT' in the datafiles"*.
- Transcribes all seven intro-text variants.
- Maps the full surrender tree, including the branch where a young Crystal soldier asks to
  join — the crew reward — and notes *"the surrender options are unique to this event
  only"*.
- Its `SurrenderEscape` footnote passes **40** as the `CRYSTAL_SHIP` surrender-offer
  percentage, against `chance="0.6"` in the game files.
- Raises its own **Verification needed** item: is the surrender reward shown before you
  accept the offer?
- Location: Hidden Crystal Worlds, `unique=false`, **ship** on Long-Range Scanners.

## Events Covered
- [[event-crystal-fight]]

## Other Pages Touched
- [[sector-hidden-crystal-worlds]], [[entity-crystal-men]], [[concept-surrender-offers]]

## Reliability Notes
`medium`. No game version stated. Its surrender-tree transcription matches the game files
entry for entry; only the numeric offer chance disagrees.

## Contradictions Flagged
> ⚠️ **CONTRADICTION:** `CRYSTAL_SHIP` surrender-offer chance.
> Fandom: **40%**. Game files: `<surrender chance="0.6">` = **60%**
> ([[source-events-xml]], per raw/gamedata/events_ships.xml).
> Recorded on [[event-crystal-fight]]. Game files trusted. Notably the same template
> parameter is **correct** for `CRYSTAL_HUNTER` (50 vs `chance="0.5"`), so this reads as a
> wiki error rather than a version difference.

## Links
- Source URL: https://ftl.fandom.com/wiki/Crystal_fight
- [[source-events-xml]], [[source-text-events-xml]]
