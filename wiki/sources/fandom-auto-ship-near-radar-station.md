---
id: source-fandom-auto-ship-near-radar-station
type: source
source_kind: wiki
raw: raw/wiki/auto-ship-near-radar-station.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [rebel, auto-ship, blue-option, fleet-delay, fleet-advance-risk, map-reveal]
---

# Fandom — "Auto-ship near radar station"

## Summary
The community wiki page for `AUTO_DEFENSE_RADAR`, the most branching event in
`events_rebel.xml`. Retrieved via the MediaWiki API at revision 74662. The most detailed
page in this batch — it transcribes both nested outcome tables and annotates the drone
requirement with a footnote.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'AUTO_DEFENSE_RADAR' in the
  datafiles."*
- Locations: Rebel Controlled Sector, Rebel Stronghold **only**. `LRSmap=ship`,
  `unique=true`. This matches the file — the event is in `NEUTRAL_REBEL` and nothing else.
- **Names the eligible drones** for `req="COMBAT_DRONE_LIST"`: Combat Drone Mark I, Combat
  Drone Mark II, Anti-Ship Beam Drone I, Anti-Ship Beam Drone II — i.e. `COMBAT_1`,
  `COMBAT_2`, `COMBAT_BEAM`, `COMBAT_BEAM_2`. It **omits `DRONE_FIREBEAM`**, the fifth entry
  in the blueprint list, which is a weapon blueprint rather than an ownable drone.
- Records the **drone-part cost** on both the blue option and the post-fight Hacking option
  (`{{Transaction|1|subtract_drones}}`), matching the `item_modify` tags.
- Transcribes `DEFENSE_RADAR_LIST` in full — fleet delayed 1 turn / map revealed / nothing /
  pursuit doubled — and the post-fight three-way choice including the Hacking blue option
  that grants map reveal **and** a fleet delay together.
- Renders `modifyPursuit amount="-1"` as *"Rebel Fleet is delayed for 1 turn"* and
  `amount="1"` as *"pursuit is doubled for 1 jump"* — two different renderings of the same
  ±1 magnitude.
- Categorised `Random_Events`, `Unique_Events`, `Drone Parts use Events`,
  `Rebel Fleet advancement risk`, `Rebel Fleet delay opportunity`,
  `Beacon Map reveal opportunity`, `Auto-ship fights`.

## Events Covered
- [[event-auto-ship-near-radar-station]]

## Other Pages Touched
- [[item-hacking]], [[item-drones]], [[concept-rebel-fleet-advance]],
  [[concept-rebel-fleet-advance]]

## Reliability Notes
`medium`. Version unstated. Structurally the most faithful page in this batch; the only
soft spots are the `modifyPursuit` renderings and the omitted `DRONE_FIREBEAM` entry
(which is likely correct in effect).

## Contradictions Flagged
- `DRONE_FIREBEAM` omitted from the eligible-drone list — recorded on
  [[event-auto-ship-near-radar-station]] as a data oddity rather than an error.
- Asymmetric wording for `modifyPursuit ±1`.

## Links
- Source URL: https://ftl.fandom.com/wiki/Auto-ship_near_radar_station
- [[source-events-rebel]], [[source-events-ships]], [[source-autoblueprints]],
  [[source-text-events-xml]]
