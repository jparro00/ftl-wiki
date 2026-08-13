---
id: source-fandom-boarders-humans-abandoned
type: source
source_kind: wiki
raw: raw/wiki/boarders-humans-abandoned.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [lanius, boarding, human, hazard]
---

# Fandom — "Boarders: Humans (Abandoned)"

## Summary
The community wiki page for `LANIUS_PIRATE_BOARDERS`, the Abandoned Sector's boarding
event. Retrieved at revision 73957.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'LANIUS_PIRATE_BOARDERS' in the
  datafiles."*
- Locations: Abandoned Sector, `LRSmap=noship`, `unique=false`.
- Outcome: **3-4 human boarders** beam aboard — matching
  `<boarders breach="false" min="3" max="4" class="human"/>`.
- **Engine-behaviour claim not in the XML:** *"If this event happens after a fight against
  a Lanius ship, the human boarders will have the Emergency Respirators augmentation. If
  this event repeats sequentially, the human boarders will still have the augmentation."*
- Category: `Boarding hazard`. Notably it does **not** carry the
  `Advanced Edition Content Events` category, despite living in an AE-only file.

## Events Covered
- [[event-boarders-humans-abandoned]]

## Other Pages Touched
- [[sector-abandoned-sector]], [[item-emergency-respirators]]

## Reliability Notes
`medium`. Boarder count and species match the XML. The Emergency Respirators claim is an
observed engine quirk with no support anywhere in `raw/gamedata/` — treat it as community
observation, and useful because it changes how the boarders fight in vented rooms.

## Contradictions Flagged
None on the data; one unverifiable engine claim, recorded on
[[event-boarders-humans-abandoned]].

## Links
- Source URL: https://ftl.fandom.com/wiki/Boarders:_Humans_(Abandoned)
- [[source-dlcevents-anaerobic]], [[source-text-events-xml]]
