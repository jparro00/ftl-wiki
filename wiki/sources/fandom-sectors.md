---
id: source-fandom-sectors
type: source
source_kind: wiki
raw: raw/wiki/sectors.md
game_version: both
date: 2026-08-15
ingested: 2026-08-15
reliability: medium
tags: [sector, map-generation, beacon-allocation, routing]
---

# Fandom — "Sectors"

## Summary
The hub page for sectors, retrieved at revision 74796. Every individual sector title on
Fandom (`Civilian Sector`, `Rock Homeworlds`, `Uncharted Nebula`, …) is a **redirect to
this one page** — there are no per-sector pages to fetch. It restates the beacon
allocation from `sector_data.xml` sector by sector, and adds the one thing the XML cannot
carry: the **map-generation algorithm** that decides how many of those allocated events
ever reach a beacon.

## Key Takeaways
- **Beacon count**: a sector contains "between 19 and 24 beacons". Generation is a 6×4
  grid; each cell has an 80% chance of holding a beacon at a random position within it,
  with a floor that prevents too many empty cells. A beacon connects to beacons in
  *adjacent* cells within 165 pixels. Cited to the xftl reverse-engineering notes, not to
  the game files.
- **Sector colour odds**: 48% green (civilian), 32% red (hostile), 20% purple (nebula).
  Same citation.
- **Allocation is ordered and truncating.** Events are assigned in the order the lines
  appear in the sector definition; each line rolls a count between its min and max
  inclusive. "Once all beacons on the map have been assigned events, the process stops."
  This is why stores and homeworld set-pieces sit at the top of every definition, and why
  bottom-of-list unique events ([[event-zoltan-wise-man]],
  [[event-auto-ship-carrying-shield-virus]]) are rare — several sectors allocate more
  event slots than 24 beacons can hold.
- **Nebula lists jump the queue.** Any `NEBULA_*` list is processed *first*, regardless of
  its position in the definition, because the map has to draw the purple cloud graphics.
  Clouds that overlap non-nebula beacons convert them into extra nebula beacons, assigned
  from the default `NEBULA` list.
- **Fallback**: leftover beacons take events from `NEUTRAL`, replaced by `OVERRIDE_NEUTRAL`
  when AE content is on.
- **Exit beacon events are not in the sector definition** — they come from a shared
  `EXIT_LIST`. An exit inside nebula cloud graphics is always an empty event.
- **The page warns against its own numbers.** Its explicit NOTE 1: counts are "taken
  straight from the game files and can be misleading". Specifically — "stores" means
  *guaranteed* stores only; "distress" counts only the `DISTRESS_BEACON_*` list, so a
  sector can show more DISTRESS beacons than listed (Engi is given as an example: 4 rather
  than the listed 1–3, because distress-tagged events in `NEUTRAL_ENGI` are placed first);
  and "quest" counts only the `QUESTS` list, so quests can both exceed and fail to appear.
- **Colour is not danger.** "The colour-coding of sectors is misleading… Engi sectors have
  few fights and are very safe, Zoltan sectors have many fights and are among the most
  dangerous." Presented as reasoning plus a Reddit profit-data link, not as measured data.
- **Sector availability rules** match `sector_data.xml` `minSector`/`unique` exactly, read
  as 1-indexed: Engi/Zoltan/Mantis Homeworlds at sector 3+, Rebel Stronghold and Rock
  Homeworlds at 5+, Slug Controlled Nebula and Slug Home Nebula at 4+, all "once per game"
  except Slug Controlled Nebula.
- **Hidden Crystal Worlds is off-map**: reachable only via [[event-ancient-device]], not
  part of the sector graph, and exiting drops you into a random sector *after* Rock
  Homeworlds that need not connect to it. The Rebel fleet still follows you through.
- **The Last Stand mechanics** (sector 8 always): +10 hull and +10 fuel on arrival; the
  Flagship jumps once per two of your jumps and wins if it holds the Federation Base for 3
  consecutive jumps; the Rebel fleet takes *random individual beacons* each turn rather
  than advancing as a front; you may wait even with fuel, and a fight entered after waiting
  starts with a full FTL charge; 3 repair beacons give 15 hull, 22–44 scrap, 5 fuel,
  4 missiles, 5 drone parts, once each.
- Per-sector crew rarity tables (which races can be bought or won as a crew-kill reward)
  and soundtrack lists are given for every sector.
- **Not covered anywhere on the page**: how the *sector graph* is built — how many next-sector
  choices you see, which sectors connect to which, or any depth/ordering rule beyond
  `minSector`.

## Events Covered
- Only by reference: [[event-ancient-device]], [[event-zoltan-research-facility]],
  [[event-engi-fleet-discussion]], [[event-legendary-thief-kazaaakplethkilik]],
  [[event-rebel-shipyard]], [[event-rock-war-vessel-encounter]],
  [[event-unarmed-zoltan-transport]], [[event-slug-home-nebula-surrender]],
  [[event-zoltan-wise-man]], [[event-auto-ship-carrying-shield-virus]]

## Other Pages Touched
- Every page in `wiki/sectors/`, plus [[concept-event-list-weighting]],
  [[source-sector-data-xml]]

## Reliability Notes
`medium`. Every allocation figure spot-checked against `sector_data.xml` matched — the
starting sector, Civilian, Engi, Zoltan, Rock, Mantis, Pirate, Rebel, Slug, Uncharted,
Crystal and Final store lines all agree, and Fandom's "6–8 hostile" style figures are just
`HOSTILE_*` + `HOSTILE1` summed. The generation algorithm, beacon count and colour odds
are second-hand from xftl and **cannot be verified from anything in `raw/`**.

## Contradictions Flagged
None against `sector_data.xml`. Two things to keep visible:

> ⚠️ **UNVERIFIABLE, NOT CONTRADICTED:** "19–24 beacons per sector", the 6×4/80% grid, the
> 165-pixel connection radius and the 48/32/20 sector-colour split are all sourced to
> <https://gitlab.com/znixian/xftl/-/blob/master/doc/sector-map>, which this repo does not
> hold. `sector_data.xml` says nothing about beacon counts or sector-draw odds.

> ⚠️ **SOURCE CONTRADICTS ITSELF BY DESIGN:** the page's own NOTE 1 says the per-sector
> store/distress/quest counts it prints — which are the `sector_data.xml` numbers already
> in `wiki/sectors/` — do not describe what a player sees. Both readings are true of
> different things: the XML gives the *allocation*, the page's caveats give the
> *realisation*.

## Links
- Source URL: https://ftl.fandom.com/wiki/Sectors
- [[source-sector-data-xml]], [[source-fandom-beacons]], [[source-fandom-rebel-fleet]],
  [[source-fandom-stores-and-resources]], [[source-fandom-environmental-hazards]]
