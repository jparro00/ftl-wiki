---
id: source-fandom-rebel-ship-attacking-crystal-ship
type: source
source_kind: wiki
raw: raw/wiki/rebel-ship-attacking-crystal-ship.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [crystal-sector, combat, fleet-advance, rebel]
---

# Fandom — "Rebel ship attacking Crystal ship"

## Summary
The community wiki page for `CRYSTAL_REBEL_CRYSTAL`. Retrieved via the MediaWiki API at
revision 73813. The three-way intervention: help the Crystals, turn on them, or leave.

## Key Takeaways
- Names the in-game id, under "Trivia": *"This event is called 'CRYSTAL_REBEL_CRYSTAL' in
  the datafiles"*.
- Notes that the Rebel ship *"has the same text for the ship destruction and the crew kill
  outcomes"* — confirmed in the file, where both branches point at
  `ship_REBEL_CRYSTAL_REBEL_CRYSTAL_destroyed_text` and only the reward level differs.
- Records the "Attack the Crystalline ship" branch as **pursuit doubled for 1 jump** plus a
  `CRYSTAL_SHIP_NO_SURRENDER` fight — matching `modifyPursuit amount="1"` in the file.
- Marks its own `REBEL_CRYSTAL_REBEL_CRYSTAL` surrender/escape footnote as **`verify`**,
  i.e. the wiki itself is unsure. The game file shows only `destroyed`/`deadCrew` nodes.
- The follow-up is the unexpanded `{{Crystal Ship Saved}}` template.
- Location: Hidden Crystal Worlds, `unique=false`, **no ship** on Long-Range Scanners.

## Events Covered
- [[event-rebel-ship-attacking-crystal-ship]]

## Other Pages Touched
- [[sector-hidden-crystal-worlds]], [[concept-rebel-fleet-advance]], [[entity-crystal-men]],
  [[concept-rebel-fleet-advance]]

## Reliability Notes
`medium`. No game version stated. Self-flags one unverified claim (the surrender/escape
footnote), which is recorded as an open question on the event page rather than as fact.

## Contradictions Flagged
None.

## Links
- Source URL: https://ftl.fandom.com/wiki/Rebel_ship_attacking_Crystal_ship
- [[source-events-xml]], [[source-text-events-xml]]
