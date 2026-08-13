---
id: source-fandom-free-drone-schematic
type: source
source_kind: wiki
raw: raw/wiki/free-drone-schematic.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [free-item, drone, no-choice]
---

# Fandom — "Free drone schematic"

## Summary
The community wiki page for the event the game files call `FIND_DRONE`. Retrieved via the
MediaWiki API at revision 74066. A pure reward event with no choices — the page is
essentially a transcription of the six intro strings plus the payout.

## Key Takeaways
- **Names the in-game id explicitly**: *"This event is called 'FIND_DRONE' in the
  datafiles."* This is the join key.
- Lists all **six** intro variants, including `text_FIND_DRONE_6` (*"Free schematic
  samples! … sector XR1-45!"*), which the files mark `<!--DLC! Added text-->`. The page
  presents all six without distinguishing the Advanced Edition addition — see the
  contradiction below.
- Reads `<autoReward level="LOW">drone</autoReward>` as *"a drone schematic with low
  scrap"*, which is the join between the payload type `drone` and what the player actually
  receives.
- Confirms availability in sixteen sectors including **Hidden Crystal Worlds**, plus
  `alsooccur=exit`, `LRSmap=noship`, `unique=false` (repeatable within a run).
- Categorised `Random_Events`, `Drone Schematics reward`.

## Events Covered
- [[event-free-drone-schematic]]

## Other Pages Touched
- [[event-free-weapon]], [[event-free-scrap-with-resources]], [[concept-autoreward-tiers]]

## Reliability Notes
`medium`. No game version stated — and this page is a case where that matters, because it
silently merges vanilla and AE text pools.

## Contradictions Flagged
> ⚠️ **Version gap, not an error.** The sixth intro string is flagged `<!--DLC! Added
> text-->` in `events.xml` ([[source-events-xml]]). Vanilla therefore draws from five
> strings, Advanced Edition from six. Fandom lists six with no version note.
> Recorded on [[event-free-drone-schematic]].

## Links
- Source URL: https://ftl.fandom.com/wiki/Free_drone_schematic
- [[source-events-xml]], [[source-text-events-xml]]
