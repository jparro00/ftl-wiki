---
id: source-fandom-auto-ship-near-storage-station-in-nebula
type: source
source_kind: wiki
raw: raw/wiki/auto-ship-near-storage-station-in-nebula.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [nebula, rebel, auto-ship, blue-option, cloaking, hacking, unique]
---

# Fandom — "Auto-ship near storage station in nebula"

## Summary
The community wiki page for `NEBULA_AUTO_DEFENSE_ITEM`. Retrieved via the MediaWiki API at
revision 74840. Fully enumerates all six choices, both sub-event branches, and the shared
"Investigate the station" loot table (rendered through a template this dump does not
expand).

## Key Takeaways
- **Names the in-game id:** *"This event is called 'NEBULA_AUTO_DEFENSE_ITEM' in the
  datafiles."*
- Locations: Civilian Sector, Pirate Controlled Sector, Rebel Controlled Sector, Rebel
  Stronghold, Slug Controlled Nebula, Slug Home Nebula, Uncharted Nebula, Zoltan
  Controlled Sector, Zoltan Homeworlds. `nebula=true`, `alsooccur=nebulafiller`,
  `LRSmap=ship+nebula`, `unique=true`.
- Records the **drone-part cost on both Hacking options** (`[ 1 subtract_drones ]`),
  matching the `<item_modify><item type="drones" min="-1" max="-1"/></item_modify>` in
  `events_nebula.xml`. Notably it puts the cost on the level-1 Hacking option too — which
  is correct, because the cost lives inside both `NEBULA_AUTO_DEFENSE_ITEM_HACK` branches
  rather than on the choice.
- Records that destroying the ship also opens the station: **medium scrap only**, then
  *"Investigate the station"*.
- The 50/50 failure branch of level-1 Cloaking and level-1 Hacking is transcribed.
- Cross-references the non-nebula twin: *"very similar to the Auto-ship near storage
  station event, but this one has more blue options."*
- The **"Investigate the station"** section is a `{{Investigate the station}}` template
  call; the dump does not include its body. The underlying table is `DEFENSE_ITEM_LIST`
  in `events_rebel.xml`.

## Events Covered
- [[event-auto-ship-near-storage-station-in-nebula]]

## Other Pages Touched
- [[concept-rebel-fleet-advance]], [[item-cloaking]], [[item-hacking]], [[sector-uncharted-nebula]]

## Reliability Notes
`medium`. Version unstated, but it documents the Hacking options, which are AE-only
(`<!--DLC-->` in the XML), so it describes at least an AE build.

## Contradictions Flagged
None.

## Links
- Source URL: https://ftl.fandom.com/wiki/Auto-ship_near_storage_station_in_nebula
- [[source-events-nebula]], [[source-events-rebel]], [[source-events-ships]],
  [[source-text-events-xml]]
