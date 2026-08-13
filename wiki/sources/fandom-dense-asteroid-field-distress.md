---
id: source-fandom-dense-asteroid-field-distress
type: source
source_kind: wiki
raw: raw/wiki/dense-asteroid-field-distress.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [crystal-route, ship-unlock, distress, blue-option]
---

# Fandom — "Dense asteroid field distress"

## Summary
Community wiki page for `ASTEROID_DERELICT_SHIP`, retrieved via the MediaWiki API at
revision 74718. Categorised as a Ship Unlocking Event and opens by declaring it step 1 of the
Crystal Cruiser unlock.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'ASTEROID_DERELICT_SHIP' in the
  datafiles."*
- Locations: Engi Controlled Sector, Engi Homeworlds, Pirate Controlled Sector, Rock
  Controlled Sector, Rock Homeworlds; `distress=true`, `LRSmap=noship`, `unique=true` —
  matching the three `NEUTRAL_*` list memberships in the files.
- **A structural observation worth keeping**: *"This is the only event with a distress beacon
  that is in the 'neutral' pool of events instead of the 'distress' pool during sector
  generation."* The files confirm the odd combination — a `<distressBeacon/>` tag on an event
  that lives only in `NEUTRAL_ENGI`, `NEUTRAL_PIRATE` and `NEUTRAL_ROCK`.
- Confirms the Rock Plating branch leads to the same "Find remains of a ship" outcome as the
  1-in-3 search result, which the file's duplicated text ids bear out.
- Confirms the weapon-vs-stasis-pod fork and its `LOW` scrap on both sides.
- Its damage figure (5 hull, 1 engines) matches the **AE** reading of the DLC-marked tag.
- Links to a collapsed *"Calculated chances of occurrence"* template that was **not expanded
  in the retrieved text**, so no odds were recoverable from it.

## Events Covered
- [[event-dense-asteroid-field-distress]]

## Other Pages Touched
- [[chain-crystal-cruiser-unlock]], [[item-damaged-stasis-pod]], [[item-rock-plating]],
  [[event-ancient-device]]

## Reliability Notes
`medium`. No version stated; damage figures imply Advanced Edition.

## Contradictions Flagged
None on outcomes. The 5-hull figure is the AE reading of a 4-hull base tag plus a
DLC-marked engines tag, recorded as a version difference rather than a conflict.

## Links
- Source URL: https://ftl.fandom.com/wiki/Dense_asteroid_field_distress
- [[source-events-xml]], [[source-events-rock]], [[source-events-engi]], [[source-events-pirate]]
