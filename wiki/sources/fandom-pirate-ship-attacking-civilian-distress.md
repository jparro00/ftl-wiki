---
id: source-fandom-pirate-ship-attacking-civilian-distress
type: source
source_kind: wiki
raw: raw/wiki/pirate-ship-attacking-civilian-distress.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [distress, pirate-fight, blue-option, bugged]
---

# Fandom — "Pirate ship attacking civilian distress"

## Summary
The community wiki page for `PIRATE_CIVILIAN_BEACON`. Retrieved via the MediaWiki API at
revision 74784. Its Trivia section carries three findings that are hard to reach from the
XML alone, including a shipped bug.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'PIRATE_CIVILIAN_BEACON' in the
  datafiles."*
- **Documents a bug**: *"This event is meant to occur at a distress beacon but won't because
  the `<distressBeacon/>` tag is missing in its definition."* Confirmed — the tag is indeed
  absent in `events.xml` ([[source-events-xml]]).
- Confirms `PIRATE_CIVILIAN` **never surrenders and never escapes**, matching the absence of
  both elements in `events_ships.xml`.
- Reward split: `destroyed` → medium scrap with resources, `deadCrew` → high — i.e. boarding
  pays a tier more.
- Notes the Weapons-6 blue option is what distinguishes this event from the otherwise very
  similar [[event-pirate-ship-attacking-civilian]].
- Notes that on the scare-off branch of the blue option you get a **preview of the reward**
  if it is scrap with resources, which does not happen on the other routes into the rescue
  table. This is UI behaviour with no XML expression.
- Routes all win conditions into the shared "Save the Civilian Ship" table
  (`SAVE_CIVILIAN_LIST`), which the page transcludes rather than spells out.
- `unique=false`, `LRSmap=noship`.

## Events Covered
- [[event-pirate-ship-attacking-civilian-distress]] — choices, blue option, fight profile

## Other Pages Touched
- [[event-pirate-ship-attacking-civilian]], [[item-weapons]], [[entity-pirates]],
  [[sector-civilian-sector]], [[sector-pirate-controlled-sector]],
  [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]],
  [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]],
  [[sector-uncharted-nebula]]

## Reliability Notes
`medium`. No game version stated, so `game_version: unknown`. Everything checkable agrees
with the extracted 1.6.x files, and the bug report is independently verifiable in them.

## Contradictions Flagged
> ⚠️ **CONTRADICTION:** sector coverage — omits [[sector-federation-space]] despite
> `DISTRESS_BEACON min=1 max=2` in `STANDARD_SPACE` ([[source-sector-data-xml]]). Recorded on
> [[event-pirate-ship-attacking-civilian-distress]]; game files trusted.

## Links
- Source URL: https://ftl.fandom.com/wiki/Pirate_ship_attacking_civilian_distress
- [[source-events-xml]], [[source-events-ships]], [[source-events-pirate]],
  [[source-sector-data-xml]]
