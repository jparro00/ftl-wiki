---
id: source-fandom-rebel-ship-attacking-civilians-in-last-stand
type: source
source_kind: wiki
raw: raw/wiki/rebel-ship-attacking-civilians-in-last-stand.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [last-stand, endgame, rebel, rescue, hull-repair, stuff-reward]
---

# Fandom — "Rebel ship attacking civilians in Last Stand"

## Summary
Community wiki page for `BOSS_SCOUT_RESCUE`, retrieved at revision 73812. The most detailed
of the Last Stand pages: it reconstructs the full two-level structure (fight → win branch →
hidden "Contact the survivors" choice → `BOSS_SCOUT_RESCUE_LIST`) and puts numbers on the
`stuff` reward.

## Key Takeaways
- Names the in-game id in Trivia: *"This event is called 'BOSS_SCOUT_RESCUE' in the
  datafiles."*
- Confirms both top-level choices and their outcome texts, and that declining does nothing.
- Renders the escape branch as **50% / 40–80 / 4–8**; the XML has
  `chance="0.5" min="4" max="8"`. What the "40–80" figure corresponds to is unresolved.
- Confirms `MED` `standard` on a hull kill and `HIGH` `standard` on a crew kill, both
  followed by the hidden survivors choice.
- Breaks out the three `BOSS_SCOUT_RESCUE_LIST` outcomes: nothing / 8 hull repaired /
  medium `stuff`, and **tooltips the `stuff` payload as fuel 2–4, missiles 2–4, drone parts
  1, plus some scrap** — a level of detail the game files do not carry.
- Categories: Hull Repair chance, Events with Stuff rewards.
- Locations box: The Last Stand, `unique=false`, long-range scanners show **no** ship.

## Events Covered
- [[event-rebel-ship-attacking-civilians-in-last-stand]]

## Other Pages Touched
- [[sector-the-last-stand]], [[entity-rebels]], [[entity-federation]]

## Reliability Notes
`medium`. Structure and reward levels match the files exactly. The `stuff` payload ranges
are the page's own gloss on `autoReward level="MED"` `stuff` and are not stated in
`raw/gamedata/`.

## Contradictions Flagged
- Third intro string drops a word: files read *"poised to wreak **havoc** among the
  enormous yet vulnerable transports"*, Fandom reads *"poised to wreak among…"*. Flagged on
  [[event-rebel-ship-attacking-civilians-in-last-stand]]; the files win.
- Lists the intro strings in a different order than the `textList`, and gives five where
  the list has eight entries (three of the five are duplicated in the list). Not a conflict
  — the wiki de-duplicates, which loses the weighting.

## Links
- Source URL: https://ftl.fandom.com/wiki/Rebel_ship_attacking_civilians_in_Last_Stand
- [[source-events-boss]], [[source-events-xml]], [[source-text-events-xml]],
  [[source-autoblueprints]]
