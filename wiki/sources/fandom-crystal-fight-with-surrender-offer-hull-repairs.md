---
id: source-fandom-crystal-fight-with-surrender-offer-hull-repairs
type: source
source_kind: wiki
raw: raw/wiki/crystal-fight-with-surrender-offer-hull-repairs.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [crystal-sector, combat, surrender, hull-repair]
---

# Fandom — "Crystal fight with surrender offer (hull repairs)"

## Summary
The community wiki page for `CRYSTAL_CONVOY`. Retrieved via the MediaWiki API at revision
74027. Documents the convoy-escort fight and its unusually generous truce branch.

## Key Takeaways
- Names the in-game id: *"This event is called 'CRYSTAL_CONVOY' in the datafiles"*.
- The surrender branch: stop the fight → **1–3 fuel and scrap + 8 hull repairs**. The
  8 repairs correspond to `<damage amount="-8"/>` in the game file; the "1–3 fuel" is the
  page's quantification of `autoReward level="LOW">fuel`.
- Win outright (destroyed or dead crew) → medium scrap with resources.
- Its `SurrenderEscape` footnote is flagged `surrenderofferchance100`, i.e. the surrender
  offer is claimed to be guaranteed — against `chance="0"` in the game file.
- Location: Hidden Crystal Worlds, `unique=true`, **ship** on Long-Range Scanners.

## Events Covered
- [[event-crystal-fight-with-surrender-offer-hull-repairs]]

## Other Pages Touched
- [[sector-hidden-crystal-worlds]], [[entity-crystal-men]], [[concept-surrender-offers]]

## Reliability Notes
`medium`. No game version stated. Its numeric reward quantifications (1–3 fuel) come from
wiki convention for `autoReward LOW fuel` rather than from the event file, so they inherit
the wiki's reliability rather than the files'.

## Contradictions Flagged
> ⚠️ **CONTRADICTION:** `CRYSTAL_CONVOY` surrender-offer chance.
> Fandom: guaranteed (`surrenderofferchance100`). Game files:
> `<surrender chance="0" min="3" max="4">` ([[source-events-xml]], per
> raw/gamedata/events_ships.xml).
> Recorded on [[event-crystal-fight-with-surrender-offer-hull-repairs]]. Unresolved: read
> literally the file says "never", which cannot be reconciled with the page existing and
> being titled for the offer. The likeliest reading is an engine special case for
> `chance="0"`, but no ingested source states it.

## Links
- Source URL: https://ftl.fandom.com/wiki/Crystal_fight_with_surrender_offer_(hull_repairs)
- [[source-events-xml]], [[source-text-events-xml]]
