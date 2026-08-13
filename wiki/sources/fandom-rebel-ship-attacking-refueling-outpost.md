---
id: source-fandom-rebel-ship-attacking-refueling-outpost
type: source
source_kind: wiki
raw: raw/wiki/rebel-ship-attacking-refueling-outpost.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [rebel, fuel-reward, optional-fight]
---

# Fandom — "Rebel ship attacking refueling outpost"

## Summary
The community wiki page for `SQUAT_REFUEL_STATION`. Retrieved via the MediaWiki API at
revision 73815. Notably careful — it documents both win branches separately and annotates
its own reasoning about the enemy ship's behaviour in HTML comments.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'SQUAT_REFUEL_STATION' in the
  datafiles."*
- Locations: Civilian Sector, Rebel Controlled Sector, Rebel Stronghold, The Last Stand.
  `LRSmap=ship`, `unique=true`. The Last Stand entry corresponds to the event's membership
  in `BOSS_NEUTRAL`. Omits [[sector-federation-space]].
- Cites the enemy as `SQUAT_REFUEL_STATION` in `events_ships.xml` and states it *"doesn't
  surrender nor tries to escape"*, adding that the surrender/escape information is **absent
  in the file** and that in-game experience supports it. This matches the file exactly.
- Distinguishes the two win branches correctly: destroyed → **medium** scrap with
  resources; crew killed → **high** scrap with resources. Matches `autoReward level="MED"`
  and `level="HIGH"` `standard`.
- Reads the follow-up `autoReward level="MED"` `fuel` as **2–4 fuel** — a numeric claim the
  game file does not make.
- Categorised `Random_Events`, `Unique_Events`, `Fuel reward opportunity`.

## Events Covered
- [[event-rebel-ship-attacking-refueling-outpost]]

## Other Pages Touched
- [[event-auto-ship-attacking-outpost]], [[sector-the-last-stand]],
  [[concept-rebel-fleet-advance]]

## Reliability Notes
`medium`. Version unstated. One of the better-reasoned pages in this batch — it separates
what the file says from what play confirms. The 2–4 fuel figure is a community reading of
`MED` `fuel`, not a file value; treat it as unconfirmed.

## Contradictions Flagged
None outright. The 2–4 fuel number is recorded on the event page as a Fandom-only claim.

## Links
- Source URL: https://ftl.fandom.com/wiki/Rebel_ship_attacking_refueling_outpost
- [[source-events-rebel]], [[source-events-ships]], [[source-events-boss]],
  [[source-text-events-xml]]
