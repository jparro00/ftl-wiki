---
id: source-fandom-rebel-fight-among-federation-and-rebel-fleets
type: source
source_kind: wiki
raw: raw/wiki/rebel-fight-among-federation-and-rebel-fleets.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [last-stand, endgame, rebel, combat, fleet]
---

# Fandom — "Rebel fight among Federation and Rebel fleets"

## Summary
Community wiki page for `BOSS_FLEETS_BOTH_FIGHT`, retrieved at revision 73791. Six intro
strings and the same fight structure as
[[source-fandom-rebel-fight-among-rebel-fleet]] — because the event loads the same
`BOSS_FLEETS_REBEL` ship block.

## Key Takeaways
- Names the in-game id in Trivia: *"This event is called 'BOSS_FLEETS_BOTH_FIGHT' in the
  datafiles."*
- All six intro strings match `text_BOSS_FLEETS_BOTH_FIGHT_1` … `_6` verbatim.
- Confirms the ship is `BOSS_FLEETS_REBEL` from `events_boss.xml`, with no surrender and no
  escape.
- Confirms low `scrap_only` on a hull kill, medium `standard` on a crew kill.
- Locations box: The Last Stand, `unique=false`, long-range scanners show a ship.
- Does **not** mention that this event also sits in `BOSS_NEUTRAL` — i.e. that it can turn
  up on an ordinary neutral beacon and not only on a warning node. That comes from
  `events_boss.xml`.

## Events Covered
- [[event-rebel-fight-among-federation-and-rebel-fleets]]

## Other Pages Touched
- [[sector-the-last-stand]], [[entity-rebels]], [[event-rebel-fight-among-rebel-fleet]]

## Reliability Notes
`medium`; the mechanical claims check out. Incidentally mentioned on the
`BOSS_FLEETS_REBEL` page as well, since both events share a ship id.

## Contradictions Flagged
None.

## Links
- Source URL: https://ftl.fandom.com/wiki/Rebel_fight_among_Federation_and_Rebel_fleets
- [[source-events-boss]], [[source-text-events-xml]], [[source-sector-data-xml]]
