---
id: source-fandom-auto-ship-near-storage-station
type: source
source_kind: wiki
raw: raw/wiki/auto-ship-near-storage-station.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [rebel, auto-ship, filler, blue-option, item-reward]
---

# Fandom — "Auto-ship near storage station"

## Summary
The community wiki page for `AUTO_DEFENSE_ITEM`. Retrieved via the MediaWiki API at
revision 73987. Documents the Cloaking branch fully but delegates the cache outcomes to a
shared `{{Investigate the station}}` template.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'AUTO_DEFENSE_ITEM' in the datafiles."*
- Locations: Civilian Sector, Engi Controlled Sector, Engi Homeworlds, Rebel Controlled
  Sector, Rebel Stronghold, Slug Controlled Nebula, Slug Home Nebula, **Zoltan Controlled
  Sector, Zoltan Homeworlds**, with `alsooccur=exitandfiller`, `LRSmap=ship`,
  `unique=true`. The Zoltan entries are notable: the Zoltan neutral-list reference to this
  event is **commented out** in `events_zoltan.xml`. It can still reach Zoltan space
  through the generic `NEUTRAL` / `OVERRIDE_NEUTRAL` filler lists.
- Documents the **Cloaking** blue option and, importantly, that it has **two outcomes** —
  a clean approach, or being detected and forced into the fight.
- Reward on the kill: **medium scrap** *(scrap only)* — matching `autoReward level="MED"`
  `scrap_only` — then *"Investigate the station"*, i.e. `DEFENSE_ITEM_LIST`.
- **Comparison note:** *"This event is very similar to the Auto-ship near storage station in
  nebula event, but this event is missing Hacking and Improved Cloaking blue options."*
- Categorised `Random_Events`, `Unique_Events`, `Filler_Events`, `Auto-ship fights`.

## Events Covered
- [[event-auto-ship-near-storage-station]]

## Other Pages Touched
- [[item-cloaking]], [[event-auto-ship-near-sensor-station]],
  [[event-auto-ship-near-radar-station]], [[concept-rebel-fleet-advance]]

## Reliability Notes
`medium`. Version unstated. Accurate on structure and reward level. The Zoltan locations
are defensible via the filler lists even though the Zoltan-specific route is disabled in
the files.

## Contradictions Flagged
- Zoltan sector reach vs the commented-out `events_zoltan.xml` entry — recorded on
  [[event-auto-ship-near-storage-station]].

## Links
- Source URL: https://ftl.fandom.com/wiki/Auto-ship_near_storage_station
- [[source-events-rebel]], [[source-events-ships]], [[source-events-zoltan]],
  [[source-text-events-xml]]
