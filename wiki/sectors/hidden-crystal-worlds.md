---
id: sector-hidden-crystal-worlds
type: sector
sector_id: CRYSTAL_HOME
sector_class: special
faction: [[[entity-crystal-men]]]
min_sector: 0
unique: true
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-15
sources: 15
tags: [hidden, crystal-route, ship-unlock, over-allocated]
---

# Hidden Crystal Worlds

## Summary
The hidden sector at the end of the Crystal route. Not reachable by normal map routing —
it is entered via [[chain-crystal-cruiser-unlock]]. It is also the one sector in the game
whose event allocation **cannot be satisfied**: its six lines demand a minimum of 25 beacons
against a map that holds at most 24, so `NEUTRAL_CRYSTAL` — the last line — can never be
filled, in any run, on any map. ([[source-sector-data-xml]], [[source-fandom-sectors]])

## Character & Hazards

### Not on the map at all
> "The Crystal sector is unique in that it is not technically part of the map. Gameplay-wise,
> it is a standalone sector separate from Rock Homeworlds. Exiting from the Crystal sector
> will send you to a random sector after the Rock Homeworlds; this sector may not be
> necessarily connected to the Rock Homeworlds."
> ([[source-fandom-sectors]], per `raw/wiki/sectors.md`)

It is never shown on the sector map, is reachable only through [[event-ancient-device]], and
**the Rebel fleet still follows you through it** ([[source-fandom-sectors]]). `minSector="0"`
despite `unique="true"`, because entry is by chain rather than by depth
([[source-sector-data-xml]]).

Enemy strength here scales to the Rock Homeworlds' sector number, and on exit you do not
choose your next sector ([[source-fandom-ancient-device]]).

**Bug:** restarting the game while inside this sector starts a new game in a Civilian sector
with the "Next Sector" button unable to open the sector map, so sector 2 is picked at random
([[source-fandom-sectors]]).

### No environmental hazards from the pool
No event in `events_crystal.xml` carries an `<environment>` element, and neither do the four
generic events `ITEMS_CRYSTAL` borrows from `events.xml` (`FIND_WEAPON`, `FIND_DRONE`,
`REFUEL_STATION`, `REPAIR_STATION`). So no asteroid field, sun, pulsar or nebula can be
rolled here from the sector's own pool ([[source-events-crystal]], [[source-events-xml]]) —
none of the hazard classes catalogued in [[source-fandom-environmental-hazards]] and
[[concept-hazards]] can occur.

The one hazard that can still appear is the Rebel fleet's: a captured beacon overwrites the
event and any hazard that was there, and commonly carries an Anti-Ship Battery
([[source-fandom-rebel-fleet]], [[concept-anti-ship-battery]]).

Consequence for Long-Ranged Scanners, which report *hazard* and *possible ship* for adjacent
beacons ([[source-fandom-beacons]]): in this sector the hazard channel is always silent, so
the augment functions purely as a ship detector.

## How Generation Plays Out Here

The generator places beacons first (a 6×4 grid, each cell 80% likely to hold one), then walks
the sector definition **in file order**, rolling each line's count between its min and max
inclusive and filling it completely before moving to the next. When the beacons run out,
generation stops and the remaining lines get nothing.
([[source-fandom-sectors]], [[source-xftl-sector-map]], [[concept-sector-event-allocation]])

Applied to this sector's table:

| # | Line | min | max | Cumulative before it (min–max) | Outcome |
|---|---|---|---|---|---|
| 1 | `STORE_CRYSTAL` | 2 | 3 | 0–0 | always placed in full |
| 2 | `ITEMS_CRYSTAL` | 2 | 2 | 2–3 | always placed in full |
| 3 | `NOTHING_CRYSTAL` | 2 | 2 | 4–5 | always placed in full |
| 4 | `HOSTILE_CRYSTAL` | 6 | 10 | 6–7 | always placed in full |
| 5 | `BOARDERS_CRYSTAL` | 1 | 2 | 12–17 | always placed in full |
| 6 | `NEUTRAL_CRYSTAL` | 12 | 12 | 13–19 | **can never be filled** |

Start beacon: `START_BEACON_CRYSTAL` (a `<startEvent>`, outside the table). Exit beacon: from
the shared `EXIT_LIST`, also outside the table ([[source-fandom-sectors]]).

Three things follow, and all three are specific to this sector:

1. **The shortfall is structural, not unlucky.** Lines 1–5 total 13–19. Even in the best case
   — every line above rolling its minimum, on a maximum 24-beacon map — 11 beacons remain for
   a line that wants 12. On a 24-beacon map the neutral line therefore receives **5 to 11** of
   its 12; on a 19-beacon map (the floor stated by [[source-fandom-sectors]]) it can receive
   **nothing at all**. `NEUTRAL_CRYSTAL` is the only line in any of the 19 sectors flagged
   `always_short`, and this is the only sector with `cannot_meet_minimum: true`
   (`sectors/data/*.sector.json`).
2. **Everything above the neutral line always lands.** Lines 1–5 cap out at 19, comfortably
   under 24, so the stores, item beacons, empty beacons, fights and boarders are never the
   thing that gets cut. A high `HOSTILE_CRYSTAL` roll costs you neutral encounters, not
   fights.
3. **The fallback list can never fire here.** Fallback events are assigned only when the game
   reaches the *end* of the sector definition with beacons left over ([[source-fandom-sectors]]).
   This table runs out of map before it runs out of lines, so no filler event can ever appear
   in this sector. Every beacon you visit comes from one of the six lines above (or is the
   start, the exit, or the quest marker).

> ⚠️ **CONTRADICTION:** [[source-fandom-sectors]] lists this sector's beacons as
> "12 neutral encounters", a figure taken verbatim from `sector_data.xml`
> ([[source-sector-data-xml]]) — while the same page's *Technical details of sector generation
> and events* section describes the truncation rule that makes 12 unreachable. The page warns
> about exactly this in its own NOTE 1 ("the count and type of Beacons in the sector
> descriptions are taken straight from the game files and can be misleading"). Both readings
> are true of different things: **12 is the allocation, and the realisation is always less.**
> This sector is the extreme case of that gap in the whole game.

> ⚠️ **CONTRADICTION:** which list is the fallback. [[source-fandom-sectors]] says leftover
> beacons draw from `NEUTRAL` (`OVERRIDE_NEUTRAL` under AE). The game files' own comment on
> `NEUTRAL_EXIT` in `newEvents.xml` says *"This event list is hardcoded to fill out a sector
> if it ran out of all other calls for that sector … TECHNICALLY it uses the EXIT_LIST above
> us now"* ([[source-newevents]]). Unresolved — and **moot in this sector**, since no fallback
> can ever be reached here. Recorded because it affects every other sector page.

### Beacon floor — 19, and where it comes from
[[source-fandom-sectors]] states a sector holds "between 19 and 24 beacons" but does not show
the derivation. [[source-xftl-sector-map]] supplies it: a cell is left empty on a 20% roll,
*unless* at least one empty cell exists already and empties are at least 20% of the cells
processed so far, in which case the cell is forced to hold a beacon. Walking that forward over
24 cells caps empties at 5, giving a floor of 19 — consistent with Fandom's figure. The one
soft spot is the phrase "cells populated thus far", which could mean processed cells or placed
beacons; either reading caps empties near 5.

The sector-page pipeline (`tools/SECTOR-PAGE.md` §11) currently treats the floor as unknown and
claims only the 24 ceiling. That is the conservative reading, not a contradiction of the above.

## Event Pool

| Event list | min | max | Contents |
|---|---|---|---|
| `STORE_CRYSTAL` | 2 | 3 | [[event-store-crystal]] |
| `ITEMS_CRYSTAL` | 2 | 2 | [[event-crystalline-cache]], [[event-crystal-scrap-collector]], `FIND_DRONE`, `FIND_WEAPON`, `REFUEL_STATION`, `REPAIR_STATION` |
| `NOTHING_CRYSTAL` | 2 | 2 | [[event-empty-beacon-crystal]] |
| `HOSTILE_CRYSTAL` | 6 | 10 | [[event-crystal-fight]] (×3), [[event-crystal-fight-with-surrender-offer-hull-repairs]], [[event-rebel-fight-crystal]], [[event-crystal-fight-with-surrender-offer-human-crew]], [[event-auto-ship-fight-crystal]] |
| `BOARDERS_CRYSTAL` | 1 | 2 | [[event-boarders-crystal]] |
| `NEUTRAL_CRYSTAL` | 12 | 12 | [[event-rebel-ship-attacking-crystal-ship]], [[event-crystal-fight-choice]], [[event-mantis-ship-attacking-crystal]], [[event-pirate-ship-attacking-crystal]], [[event-crystal-ship-attacking-federation-loyalists]], [[event-federation-deserters]], [[event-crystalline-research-facility]], [[event-crystal-chat]], [[event-crystalline-ship-messaging-about-rebels]], [[event-crystalline-men-buried]] |

Start beacon: [[event-start-beacon-crystal]], which plants the `CRYSTAL_UNLOCK` quest marker
on arrival.

24 distinct events — the smallest pool of any sector except The Last Stand (8). 13 of them are
`unique="true"`, so with 12 neutral slots drawing on a 10-event list where 6 are once-only, and
6–10 hostile slots drawing on a 5-event list where 3 are, repetition is forced by arithmetic.
(See [[concept-event-uniqueness]] for the unresolved scope of `unique`.)

`HOSTILE_CRYSTAL` names `CRYSTAL_FIGHT` three times; a repeated list entry is the only weighting
the shipped files contain ([[concept-event-list-weighting]]).

## Beacon Markers — What The Map Shows

**No event in this sector's pool carries `<distressBeacon/>`, and the sector allocates no
`DISTRESS_BEACON_*` line and no `QUESTS_*` line at all.** Hidden Crystal Worlds and The Last
Stand are the only two of the 19 sectors with zero distress-marked events
([[source-sector-data-xml]], [[source-events-crystal]]).

That inverts the usual finding. Elsewhere the interesting fact is that *more* distress markers
appear than the distress line allocates, because distress-tagged events sit in other lists
([[source-fandom-sectors]] NOTE 1). Here the count is exactly zero on both sides: the map draws
store markers, the exit, and — once the arrival beacon plants it — one quest marker. Nothing
else is previewed at all.

Marker rules that apply ([[source-fandom-beacons]]):
- Distress and store markers are drawn on beacons **within 1 jump**; the exit is visible from
  the start; a quest marker is visible from any distance once spawned.
- A quest marker **replaces the event at the beacon it overwrites**, unless that beacon is a
  store, the exit, or another quest.

> ⚠️ **CONTRADICTION:** [[source-fandom-beacons]] says store beacons are "visible within 1 FTL
> jump range". The generated sector pages currently print "the two fixed store beacons are
> labelled on the map from the start" (`tools/sector-vocab.json`, `markers.store`), which
> disagrees with the source and with the same file's own `markers.distress` string ("the map
> only draws distress and store markers on beacons adjacent to you"). The source is the better
> bet; the vocabulary string looks like a bug affecting all 19 pages.

### Where the cruiser marker lands
`START_BEACON_CRYSTAL` plants `CRYSTAL_UNLOCK` before your first jump, so the placement filter
runs at its most permissive. Per [[source-xftl-sector-map]] (`StarMap::AddQuest`) the marker
needs a beacon that is unvisited, not a nebula, not the exit, not overtaken, not already a
quest, not a store, not your current beacon, reachable, and closer in jumps than the Rebels'
arrival. In this sector there are no nebula beacons and no distress beacons, so almost every
beacon qualifies and the marker essentially always lands in-sector — and, because the table
over-subscribes the map, it always lands on a beacon that already had an event, costing you one
encounter. See [[concept-quest-beacon-placement]].

## Stores & Economy

- **2–3 guaranteed stores**, placed first, so they always survive the squeeze. Fandom's
  cross-sector store table agrees with `sector_data.xml`
  ([[source-fandom-template-stores-number-of-stores-by-sectors]]).
- **No sector-specific store-opening event exists here.** Fandom states it outright: "Hidden
  Crystal Worlds and The Last Stand sectors don't have sector-specific store opening
  opportunity/chance events (however, [[event-pirate-briber]] can occur in these sectors)"
  ([[source-fandom-template-stores-additional-stores-from-events-by-sectors]]). `PIRATE_BRIBER`
  reaches a sector as a filler event or as an exit-beacon event; it is a member of
  `NEUTRAL_EXIT`, which `EXIT_LIST` loads ([[source-newevents]]). Since the filler route is
  closed here (§How Generation Plays Out, point 3), **the exit beacon is the only route by
  which a fourth shop can appear.**
- **Crystal weapons and Crystal crew are obtainable nowhere else.** "Other crystal weapons and
  crystal crewmembers cannot be acquired outside of Hidden Crystal Worlds (except for one
  particular [[event-zoltan-research-facility]] event, regarding the crew)"
  ([[source-fandom-stores-and-resources]]).
- `rarityList` sets every non-Crystal crew race to 0 (never sold) and Crystal to 1, and it is
  the only table carrying `CRYSTAL_BURST_1/2` and `CRYSTAL_HEAVY_1/2`
  ([[source-sector-data-xml]], [[source-fandom-store-crystal]], [[concept-blueprint-rarity]]).
- **Crystal Lockdown Bomb** is rarity 3 here, against 4 in [[sector-rock-controlled-sector]]
  and 2 in [[sector-rock-homeworlds]] ([[source-sector-data-xml]], [[source-fandom-sectors]]).

## Chains That Run Through It
- [[chain-crystal-cruiser-unlock]] — this sector is the destination. You arrive via the
  Crystal-crew blue option on [[event-ancient-device]] in [[sector-rock-homeworlds]];
  the payoff is [[event-crystal-unlock]] at the quest marker planted on arrival.

## Factions & Ships
- [[entity-crystal-men]] — dominant faction

## Strategy Notes
- **Bring the fleet clock with you.** There is no nebula beacon in this sector, so the usual
  halving of the Rebel advance by jumping into cloud is unavailable
  ([[source-fandom-rebel-fleet]], [[concept-rebel-fleet-advance]]). Of the events that touch
  pursuit, exactly one branch delays it — the Distraction Buoys route through
  [[event-crystalline-ship-messaging-about-rebels]] — while
  [[event-crystalline-men-buried]], [[event-rebel-ship-attacking-crystal-ship]] and the
  bluffed branch of the same messaging event advance it (`modifyPursuit` is signed; positive
  advances the fleet). Distraction Buoys additionally postpones the advance by one turn at
  sector entry ([[source-fandom-rebel-fleet]]).
- **Shopping is front-loaded and the list is short.** 2–3 stores selling only Crystal crew and
  Crystal weapons, no event route to a fourth shop except the exit, and nothing in the pool
  that trades resources at scale. Arrive with the scrap you intend to spend.
- **The realised sector is smaller than the table reads.** Discount the "12 neutral encounters"
  figure: plan for the stores, the two item beacons, the two empties, 6–10 fights and 1–2
  boarding events as the guaranteed content, with the Crystalline conversations as whatever the
  map has room left for.
- _Fandom offers no danger or routing commentary for this sector beyond the above; nothing here
  is opinion sourced from it._

## Open Questions
- [x] ~~Whether it always replaces a normal sector or is appended~~ — neither: it is not part
  of the sector graph at all, and exiting drops you at a random sector *after* Rock Homeworlds
  which need not connect to it ([[source-fandom-sectors]]). Closed 2026-08-15.
- [ ] How the sector is entered mechanically once the chain completes — the transition is
  described in outcome terms by [[source-fandom-sectors]], but no held source shows the engine
  path.
- [ ] Do the arrival beacon and the exit beacon consume grid cells that the allocation table
  cannot then fill? Both are known to be outside the table
  ([[source-fandom-sectors]], [[source-sector-data-xml]]), and both sit on the beacon map
  ([[source-xftl-sector-map]] — the exit is picked from the two right-most grid columns). If
  they do, subtract two from every realised figure in *How Generation Plays Out Here*, and the
  neutral line's ceiling drops from 11 to 9. No source held here settles it.
- [ ] [[source-xftl-sector-map]] notes that `StarMap::GetRandomSectorChoice` has a value ">2"
  that draws a grey dot on the sector map, and speculates it "might be somehow related to the
  crystal homeworlds? Or maybe just something cut". Unresolved.
- [ ] Whether `unique="true"` is per sector or per run — matters more here than anywhere, since
  13 of 24 pool events carry it ([[concept-event-uniqueness]]).

## Sources
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-text-sectorname-xml]] (per raw/gamedata/text_sectorname.xml)
- [[source-events-crystal]] (per raw/gamedata/events_crystal.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-fandom-sectors]] (per raw/wiki/sectors.md)
- [[source-fandom-beacons]] (per raw/wiki/beacons.md)
- [[source-fandom-rebel-fleet]] (per raw/wiki/rebel-fleet.md)
- [[source-fandom-environmental-hazards]] (per raw/wiki/environmental-hazards.md)
- [[source-fandom-stores-and-resources]] (per raw/wiki/stores-and-resources.md)
- [[source-fandom-template-stores-number-of-stores-by-sectors]] (per raw/wiki/template-stores-number-of-stores-by-sectors.md)
- [[source-fandom-template-stores-additional-stores-from-events-by-sectors]] (per raw/wiki/template-stores-additional-stores-from-events-by-sectors.md)
- [[source-xftl-sector-map]] (per raw/modding/2026-08-15-xftl-sector-map.txt)
- [[source-fandom-ancient-device]] (per raw/wiki/ancient-device.md)
- [[source-fandom-store-crystal]] (per raw/wiki/store-crystal.md)
