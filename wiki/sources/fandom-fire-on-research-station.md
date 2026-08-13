---
id: source-fandom-fire-on-research-station
type: source
source_kind: wiki
raw: raw/wiki/fire-on-research-station.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [distress, blue-option, crew-loss-risk, clone-bay-revival, augment-reward, named-crew]
---

# Fandom — "Fire on research station"

## Summary
Community wiki page for `DISTRESS_STATION_FIRE`, retrieved via the MediaWiki API at revision
74065. Covers both gamble branches and both blue options, and names the recruitable
survivor.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'DISTRESS_STATION_FIRE' in the
  datafiles."*
- Locations: Abandoned Sector, Civilian Sector, Mantis ×2, Pirate, Rebel ×2, Rock ×2,
  Uncharted Nebula, Zoltan ×2 — the joint-widest list in this batch, matching membership in
  every faction distress list **except** `DISTRESS_BEACON_ENGI`.
- **Names the crewmember**: *"You receive a crewmember named Dr. Jones"*, matching
  `<crewMember amount="1" id="name_DrJones"/>` and the `name_DrJones` string. It does not
  state a species, and neither does the file.
- Confirms the Rock-crew branch pays an **augmentation** with high scrap and the Repair-Drone
  branch a **drone schematic** with high scrap — matching `autoReward level="HIGH"` `augment`
  and `HIGH` `drone`.
- Notably does **not** mark a drone-part cost on the Repair Drone option, consistent with the
  file: unlike the other drone blue options in this batch, this branch has no `item_modify`.
- Its damage figure (4 hull, 1 random system) matches the **AE** reading of the DLC-marked
  tag.

## Events Covered
- [[event-fire-on-research-station]]

## Other Pages Touched
- [[item-repair-drone]], [[entity-rock-men]], [[event-giant-alien-spiders]],
  [[event-unknown-disease-on-mining-colony]]

## Reliability Notes
`medium`. No version stated; the damage figure implies Advanced Edition, and it documents
the Clone Bay revival line, which is AE-only content.

## Contradictions Flagged
None. Every choice, gate and reward level matches the game files.

## Links
- Source URL: https://ftl.fandom.com/wiki/Fire_on_research_station
- [[source-events-xml]], [[source-newevents]], [[source-text-events-xml]], [[source-sector-data-xml]]
