---
id: source-fandom-template-distress-events-by-sectors
type: source
source_kind: wiki
raw: raw/wiki/template-distress-events-by-sectors.md
game_version: unknown
date: 2026-08-15
ingested: 2026-08-15
reliability: medium
tags: [beacon, distress, marker, lrs, sector, routing]
---

# Fandom — Template: "Distress events, by sectors"

## Summary
The table transcluded into the `Random Events` page, retrieved at revision 74574. It lists
**30 events** that appear on the map as a distress beacon, which sectors each can occur in,
and — uniquely — **what Long-Ranged Scanners reports at that beacon**. It is the direct
answer to "does the distress icon follow the `<distressBeacon/>` tag or the allocation list?"

## Key Takeaways
- **The table has exactly 30 rows, and `raw/gamedata/` contains exactly 30
  `<distressBeacon/>` tags.** They correspond one-for-one. The icon follows the **tag**.
- The list therefore **crosses allocation lists**. [[event-dense-asteroid-field-distress]]
  (`ASTEROID_DERELICT_SHIP`, the Damaged Stasis Pod that starts the Crystal route) is in the
  table and does carry `<distressBeacon/>`, despite being allocated from `NEUTRAL_ENGI` /
  `NEUTRAL_ROCK` rather than from any `DISTRESS_BEACON_*` list.
- Conversely, events allocated from `DISTRESS_BEACON_*` lists that carry **no** tag —
  `ENGI_STATION_DISTRESS`, `PIRATE_CIVILIAN_BEACON`, `REBEL_VS_FEDERATION` — are **absent**
  from the table. The `Random Events` page states why, verbatim: *"some other events were
  meant to occur at a distress beacon, but they won't due to coding errors — these events
  are not included in the category"* ([[source-fandom-random-events]]).
- **The LRS column** gives, per event, the icon the augment shows before you jump. Only three
  distinct values occur across all 30 rows:
  - `Map_icon_diamond_yellow.png` — *"An unvisited location."* — **23 of 30**, i.e. LRS tells
    you nothing beyond "distress, unvisited";
  - `Map_icon_ship.png` — *"Possible ship detected."* — **6 of 30**;
  - `Map_icon_hazard_no_ship.png` — *"An unvisited location. Asteroid field detected in this
    location."* — **1 of 30**.
  So **LRS resolves a distress beacon's identity in only about a fifth of cases**, and never
  by naming the event.
- Sector columns cover Civilian, Engi, Zoltan, Mantis, Pirate, Rebel, Rock, Abandoned, Slug
  Nebulas, Uncharted Nebula — i.e. which distress events are reachable where.

## Events Covered
All 30, including [[event-asteroid-belt-distress]], [[event-crushed-pirate]],
[[event-dense-asteroid-field-distress]], [[event-giant-alien-spiders]],
[[event-pirate-ship-distress-trap]], [[event-unknown-disease-on-mining-colony]],
[[event-single-life-form-on-moon]], [[event-friendly-ship-out-of-fuel]], the five
`REFUGEE_*` events and the seven Lanius distress events.

## Other Pages Touched
- [[concept-beacon-markers]] (to be written), [[concept-sector-event-allocation]],
  [[item-long-ranged-scanners]], all of `wiki/sectors/`

## Reliability Notes
`medium` by convention, but the row count and membership were checked against every
`<distressBeacon/>` tag in `raw/gamedata/` in this pass and matched exactly — treat the
membership as high-confidence. The per-sector `+` cells were **not** individually verified.

## Contradictions Flagged
None — and it **resolves** a mismatch we had: the on-map distress marker is not the
`DISTRESS_BEACON_*` allocation entry. Both facts stand and describe different things.

## Links
- Source URL: https://ftl.fandom.com/wiki/Template:Distress_events_by_sectors
- [[source-fandom-random-events]], [[source-fandom-beacons]], [[source-fandom-augmentations]],
  [[source-text-misc]], [[source-events-xml]]
