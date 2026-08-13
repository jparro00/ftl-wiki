---
id: source-fandom-space-station-under-construction
type: source
source_kind: wiki
raw: raw/wiki/space-station-under-construction.md
game_version: ae
ingested: 2026-08-09
date: 2026-08-09
reliability: medium
tags: [quest, blue-option, lanius]
---

# Fandom — "Space station under construction"

## Summary
Documents the AE-only construction-yard quest: the intro beacon, the Lanius blue option,
and all three quest-marker follow-up beacons. Declares the datafile id:
**"This event is called `QUEST_CONSTRUCTIONYARD` in the datafiles."** Tagged
`Advanced Edition Content Events`.

## Key Takeaways
- Accepting gives 2–4 fuel, 0–4 missiles, 0–2 drone parts and a quest marker.
- The Lanius blue option can trade the crew member for an augment plus high scrap, or
  refuse and take medium scrap. Clone Bay does not revive the traded crew member.
- The quest beacon resolves to one of three sub-events; the "empty space station" one is
  the [[event-abandoned-station]] event reused with a different intro.
- Confirms `QUEST_CONSTRUCTIONYARD_SHIP` neither surrenders nor escapes.

## Events Covered
- [[event-space-station-under-construction]] (`QUEST_CONSTRUCTIONYARD`)

## Other Pages Touched
- [[event-abandoned-station]], [[sector-civilian-sector]], [[entity-lanius]]

## Contradictions Flagged
- Sector scope: page says Civilian Sector; the `QUESTS` slot that `OVERRIDE_QUESTS` fills
  is allocated in `STANDARD_SPACE` as well ([[source-sector-data-xml]]). Recorded on the
  event page.

## Links
- https://ftl.fandom.com/wiki/Space_station_under_construction (revision 74321, retrieved 2026-08-09)
