---
id: source-fandom-rebel-fight-among-rebel-fleet
type: source
source_kind: wiki
raw: raw/wiki/rebel-fight-among-rebel-fleet.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [last-stand, endgame, rebel, combat, fleet]
---

# Fandom — "Rebel fight among Rebel fleet"

## Summary
Community wiki page for `BOSS_FLEETS_REBEL`, retrieved at revision 73792. Seven intro
strings, one unavoidable fight, and the two win branches with their reward levels.

## Key Takeaways
- Names the in-game id in Trivia: *"This event is called 'BOSS_FLEETS_REBEL' in the
  datafiles."*
- Confirms no surrender and no escape branch on the `BOSS_FLEETS_REBEL` ship
  (`surrenderno+escapeno`).
- Confirms the reward asymmetry: hull kill → **low scrap only**; crew kill → **medium
  scrap with resources**. Both match the `autoReward` levels in `events_boss.xml`.
- Quotes both win texts verbatim.
- Locations box: The Last Stand, `unique=false`, long-range scanners show a ship.

## Events Covered
- [[event-rebel-fight-among-rebel-fleet]]

## Other Pages Touched
- [[sector-the-last-stand]], [[entity-rebels]],
  [[event-rebel-fight-among-federation-and-rebel-fleets]] (it links the same ship block)

## Reliability Notes
`medium`; every mechanical claim checks out against `events_boss.xml`.

## Contradictions Flagged
- One-word transcription difference in the first intro string: the files read *"**You**
  scanners can hardly register them all"*, Fandom reads *"**Your** scanners"*. Flagged on
  [[event-rebel-fight-among-rebel-fleet]]; the files win.

## Links
- Source URL: https://ftl.fandom.com/wiki/Rebel_fight_among_Rebel_fleet
- [[source-events-boss]], [[source-text-events-xml]], [[source-autoblueprints]]
