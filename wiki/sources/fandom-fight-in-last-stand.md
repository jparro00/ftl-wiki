---
id: source-fandom-fight-in-last-stand
type: source
source_kind: wiki
raw: raw/wiki/fight-in-last-stand.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [last-stand, endgame, rebel, auto-ship, combat]
---

# Fandom — "Fight in Last Stand"

## Summary
Community wiki page for `BOSS_SCOUT`, retrieved at revision 74064. Short page: six intro
strings, one fight, default rewards — plus the one thing the raw event XML does not make
readable, a breakdown of which enemy hulls the `REBEL_AND_AUTO` pool actually produces.

## Key Takeaways
- Names the in-game id in Notes: *"This event is called 'BOSS_SCOUT' in the datafiles."*
- All six intro strings match `text_BOSS_SCOUT_1` … `_6` verbatim.
- Confirms the enemy is either a Rebel ship or an auto-ship, both on default rewards, and
  that the ship neither surrenders nor escapes.
- **Derives the hull weighting from `dlcBlueprintsOverwrite.xml`** and states it in
  readable names: 2× Auto-Scout, 1× Auto-Surveyor, 2× Auto-Assault, 1× Auto-Hacker,
  2× Rebel Rigger, 1× Rebel Disruptor, 2× Rebel Fighter, 1× Rebel Invader. This matches
  `OVERRIDE_SHPS_REBEL_AND_AUTO` entry-for-entry (base hulls twice, `_DLC` hulls once).
- Locations box: The Last Stand, `unique=false`, long-range scanners show a ship.
- Categories: Fights with Default Rewards, Auto-ship fights.

## Events Covered
- [[event-fight-in-last-stand]]

## Other Pages Touched
- [[sector-the-last-stand]], [[entity-rebels]]

## Reliability Notes
`medium`. Everything it states checks out against the files, and the ship-pool breakdown is
explicitly sourced to `dlcBlueprintsOverwrite.xml` — which makes it an **AE-only** reading
even though the page does not say so. The vanilla pool (`SHPS_REBEL_AND_AUTO`, four
entries) is not mentioned.

## Contradictions Flagged
None against the game files.

## Links
- Source URL: https://ftl.fandom.com/wiki/Fight_in_Last_Stand
- [[source-events-boss]], [[source-events-ships]], [[source-autoblueprints]],
  [[source-text-events-xml]]
