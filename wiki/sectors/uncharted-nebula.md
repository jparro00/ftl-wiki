---
id: sector-uncharted-nebula
type: sector
sector_id: NEBULA_SECTOR
sector_class: nebula
faction: []
min_sector: 0
unique: false
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-15
sources: 13
tags: [nebula]
---

# Uncharted Nebula

## Summary
The unfactioned nebula sector. Its pool is built from dedicated `NEBULA_*` lists rather
than the generic ones, and it carries a `NEBULA_STORE`. Because every `NEBULA_*` list is
placed **before** anything else on the map, almost the whole sector is generated as cloud
first, and the handful of ordinary beacons — the second store, the item beacons, the
distress calls — are fitted into what is left ([[source-fandom-sectors]]).

Fandom's own blurb for it is *"You may put a few light years on the fleet, but that's only
useful if you make it out the other side."* That promise is weaker here than it sounds:
a nebula jump **inside a nebula sector** costs the Rebels only about a fifth of their
normal advance, where the same beacon in an ordinary sector costs them half
([[source-xftl-sector-map]]).

## Character & Hazards

### Nebula, everywhere
`sector_data.xml` allocates four `NEBULA_*` lines — 17–19 of the sector's 19–26 allocated
slots ([[source-sector-data-xml]]). On top of that, the cloud **graphics** are drawn during
nebula generation and any ordinary beacon they overlap is converted into another nebula
beacon, drawing from the shared `NEBULA` list that this sector's definition never names
([[source-fandom-sectors]]). This is the sourced explanation for jumping to a beacon that
shows no cloud and arriving in one anyway.

- **Sensors are disabled outright** inside a nebula — not degraded, off. **Slug crew** and
  the **Lifeform Scanner** see through it regardless ([[source-fandom-sensors]],
  [[source-fandom-environmental-hazards]]). See [[item-lifeform-scanner]],
  [[item-slug-crew]], [[concept-nebula-mechanics]].
- **Ion / plasma storms halve your reactor** (rounded up). Zoltan power and the Backup
  Battery are unaffected, and the enemy's reactor is halved too
  ([[source-fandom-environmental-hazards]]). Four events in this pool carry a storm:
  `STORM_REBEL`, `STORM_AUTO`, `STORM_ITEMS` and `NEBULA_ROCK_RACIST`.
- **Nebula beacons never carry an ASB.** The one exception is being *out of fuel and
  waiting* at one when the fleet arrives: the nebula environment is stripped and an ASB
  appears ([[source-fandom-rebel-fleet]], [[source-fandom-environmental-hazards]]).
- **A nebula beacon the fleet overtakes always becomes an ion storm** — except a nebula
  **exit** beacon, which cannot ([[source-fandom-rebel-fleet]]).
- **An exit beacon inside cloud graphics is always an empty event**
  ([[source-fandom-sectors]]).

### Rebel pursuit — the numbers
`StarMap` advances the danger zone by a fixed number of pixels per jump
([[source-xftl-sector-map]]):

| Jump from | Advance | Relative |
|---|---|---|
| a normal beacon | 64 px | — |
| a nebula beacon in a **normal** sector | 32 px | −50% |
| a nebula beacon in a **nebula** sector (here) | 51 px | −~20% |

So the sector's standing discount is roughly one fifth, matching the game's own
`map_nebula_fleet_loc` string — *"The Rebel Fleet was prepared for the nebula in this
sector"* ([[concept-nebula-mechanics]]).

> ⚠️ **CONTRADICTION — resolved, both sides recorded.**
> [[source-fandom-environmental-hazards]] and [[source-fandom-sectors]] say pursuit is
> reduced *"by 20%"* in a nebula sector (against 50% elsewhere), i.e. **reduced by** a
> fifth. [[source-fandom-rebel-fleet]] says the rate is reduced *"only partially (by 1/5 of
> regular beacon advance rate)"*, which reads naturally as **reduced to** a fifth — a
> fourfold difference in the same phrase.
> [[source-xftl-sector-map]]'s pixel figures settle it: 51/64 ≈ 0.797, so it is
> **reduced by ~20%**. The Environmental Hazards phrasing is correct; the Rebel Fleet
> page's phrasing is misleading rather than a separate claim, and stays on record.

Against that thin discount, four events in this sector's pool carry `modifyPursuit="1"` —
they *advance* the fleet by an extra jump — and **nothing in the pool delays it**
([[source-sector-data-xml]] via the extracted trees): `NEBULA_AUTO_WARNING`,
`NEBULA_REBEL_UNDETECTED`, `NEBULA_REBEL_CHASE` and `CIVILIAN_ASTEROIDS_BEACON`. Letting a
scout or Rebel ship escape doubles the pursuit rate for that turn
([[source-fandom-rebel-fleet]]). See [[concept-rebel-fleet-advance]].

> The earlier version of this page said this sector "advances the fleet and never delays
> it". That is still true of its **events**; it was never true of its **beacons**. The
> environment gives a standing ~20% discount per nebula jump that the event pool then
> partly gives back.

### Danger and routing
Fandom's commentary that sector colour does not track danger, and that a sector should be
chosen on its contents, is **unsourced opinion** on that page — reasoning plus a link to a
Reddit profit thread, not measured data ([[source-fandom-sectors]]).

## Generation & placement
Per [[source-fandom-sectors]] and [[source-xftl-sector-map]] (community reverse-engineering
of the generator, not game files):

1. Beacons are placed first — a 6×4 grid, each cell 80% likely to hold one, so **at most
   24**; Fandom states the range as 19–24. Beacons connect to beacons in adjacent cells
   within 165 px.
2. **All four `NEBULA_*` lines are filled first**, out of file order, because the cloud
   graphics must be drawn before anything else.
3. Then `STORE`, `ITEMS`, `DISTRESS_BEACON` in file order, each rolling its own min–max
   inclusive and filling completely before the next begins.
4. When the beacons run out, generation stops. Leftover beacons instead take events from
   `NEUTRAL` (`OVERRIDE_NEUTRAL` under AE).
5. The exit beacon is not in the table — it draws from the shared `EXIT_LIST`.

Consequences specific to this sector:

- The allocation totals **19–26** against a map of at most 24, so the squeeze is mild
  compared with the Slug nebulas (18–34 and 19–35). Only the **last** line,
  `DISTRESS_BEACON`, has real slack: up to 23 slots are spoken for above it, so a high roll
  leaves one beacon for a line that wants three.
- Conversely the minimum, 19, can fall short of a 24-beacon map, so this sector really can
  reach the `NEUTRAL` fallback. Both `NEUTRAL` and `OVERRIDE_NEUTRAL` contain
  `PIRATE_BRIBER`, a store-opening event ([[source-newevents]],
  [[source-dlceventsoverwrite]],
  [[source-fandom-template-stores-additional-stores-from-events-by-sectors]]).
- Under AE, `dlcEventsOverwrite.xml` adds `STORE_REBELSIDE` (Large trade station) to the
  `ITEMS` list — which matches Fandom's store table marking Large trade station as
  available in Uncharted Nebula. Whether the engine actually substitutes `OVERRIDE_ITEMS`
  is still open ([[concept-sector-event-allocation]]).

## Stores
Guaranteed stores here are **0–1 plain plus 1 nebula store**, so 1–2
([[source-sector-data-xml]], [[source-fandom-template-stores-number-of-stores-by-sectors]]).
The nebula store is placed first of all, before any other line, so it cannot be crowded
out by allocation.

> ⚠️ **CONTRADICTION:** `sector_data.xml` gives `NEBULA_STORE` a **minimum of 1**, i.e. a
> guaranteed store ([[source-sector-data-xml]]). Fandom states that "due to issues with how
> sectors are generated, about **0.8% of Uncharted Nebulas have no stores at all**", citing
> a Reddit thread ([[source-fandom-template-stores-number-of-stores-by-sectors]],
> [[source-fandom-sectors]]). Both are recorded: the XML describes the *allocation*, the
> observation describes the *realisation*, and no source here explains the mechanism. The
> allocation is the higher-reliability claim; the 0.8% figure is a single community
> measurement and is the only source that speaks to what actually generates.

Beyond the guaranteed ones, `ESCORT_BEACON` (Escort civilians FTL haywire) in the distress
pool can open a store, and Fandom lists Large trade station and Pirate briber as store
openers reachable in this sector
([[source-fandom-template-stores-additional-stores-from-events-by-sectors]]).
See [[concept-stores]].

## Quest markers
The sector allocates **no `QUESTS` line at all**; all three quest starts sit in the distress
pool — `CIVILIAN_ASTEROIDS_BEACON`, `REBEL_VS_FEDERATION` and `ESCORT_BEACON`
([[source-sector-data-xml]]).

`StarMap::AddQuest` will only place a marker on a beacon that is unvisited, **not a nebula
beacon**, not the exit, not fleet-overtaken, not already a quest, **not a store**, **not a
distress beacon**, and not the one you are standing on — and it must be fewer jumps away
than the number of jumps before the Rebels take it ([[source-xftl-sector-map]]). In a
sector generated almost entirely as cloud, qualifying beacons are scarce, so a quest opened
here is unusually likely to be **delayed into the next sector**. [[source-fandom-beacons]]
states the same nebula exclusion more loosely ("cannot appear in nebula area") and a
shorter exclusion list; the engine list is the better bet. See
[[concept-quest-beacon-placement]].

## Beacon markers
Distress and store markers are drawn only on beacons **adjacent** to you, so they are a
next-jump signal rather than a sector plan; exit and quest markers are visible from any
distance ([[source-fandom-beacons]], [[source-xftl-sector-map]]).

In this sector's pool, twelve events carry the distress tag, while two events allocated
*from* the distress list carry no tag and so never show the marker —
`PIRATE_CIVILIAN_BEACON` and `REBEL_VS_FEDERATION`. Fandom calls that second case a
mistake in the data ([[source-fandom-sectors]]). Nothing outside the distress line carries
the tag here, so — unlike Engi space — this sector cannot show *more* distress beacons
than its allocation.

## Event Pool

Placement order, not file order (nebula lines jump the queue):

| # | Event list | min | max | Notes |
|---|---|---|---|---|
| 1 | `NEBULA_STORE` | 1 | 1 | placed first; the guaranteed shop |
| 2 | `NEBULA_EMPTY` | 4 | 4 | placed first |
| 3 | `NEBULA_HOSTILE` | 5 | 6 | placed first; contains `NEBULA_EMPTY` twice |
| 4 | `NEBULA_NEUTRAL` | 7 | 8 | placed first; every ship here is a choice |
| 5 | `STORE` | 0 | 1 | may allocate none |
| 6 | `ITEMS` | 1 | 3 | AE adds `STORE_REBELSIDE` |
| 7 | `DISTRESS_BEACON` | 1 | 3 | last; the line that goes short |

Start beacon: `START_BEACON_NEBULA`.

47 distinct events across the pool: 5 always open in combat, 15 can lead to it, 6 can cost
a crew member outright, 3 put boarders aboard, and 21 carry at least one blue option
(per `sectors/data/uncharted-nebula.sector.json`, built from [[source-sector-data-xml]] and
the event trees).

Notable members: [[event-store-in-nebula-uncharted]], [[event-empty-nebula-beacon]],
[[event-nebula-lost-ship]], [[event-rebel-fight-chance-in-nebula]],
[[event-asteroid-belt-distress]], [[event-rebel-ship-attacking-federation-loyalists]],
[[event-escort-civilians-ftl-haywire]], [[event-crew-hiring-station]].

## Chains That Run Through It
- No chain starts here by allocation. Three quest starts sit in the distress pool, two of
  them targeting `HIDDEN_FEDERATION_BASE_LIST` (`CIVILIAN_ASTEROIDS_BEACON`,
  `REBEL_VS_FEDERATION`) and one `QUEST_ESCORT_ARRIVE` (`ESCORT_BEACON`) — all subject to
  the marker restrictions above.

## Factions & Ships
- _Unfactioned._ Rebels, pirates, Mantis and Rock ships all appear, none as sector owner.
- Store crew rarity: Human 1, Slug 3, Engi / Mantis / Zoltan / Rockman 4
  ([[source-sector-data-xml]], [[source-fandom-sectors]]). Slug is the least-rare
  non-human here and the only crew that sees through the cloud.

## Strategy Notes
- Sensors upgrades are inert for most of this sector; [[item-lifeform-scanner]] and
  [[item-slug-crew]] carry disproportionate value here ([[concept-nebula-mechanics]]).
- The fog is a weak hedge against the fleet: ~20% off per nebula jump, with four events
  able to hand a whole jump back ([[source-xftl-sector-map]]).
- Leave enough spare reactor capacity before jumping — arriving in an ion storm strips
  power automatically, which can drop shields into an enemy drone
  ([[source-fandom-environmental-hazards]]).
- _Opinion, unmeasured:_ Fandom argues sector colour is a poor danger proxy and that the
  store count is the important difference between sectors ([[source-fandom-sectors]]).

## Open Questions
- [x] ~~Sensor/vision penalties are a nebula mechanic but are not declared in
      `sector_data.xml`~~ — answered 2026-08-15: nebulas disable Sensors entirely, Slug crew
      and the Lifeform Scanner excepted ([[source-fandom-sensors]],
      [[source-fandom-environmental-hazards]]).
- [ ] What actually causes the ~0.8% storeless generation, given `NEBULA_STORE` has a
      minimum of 1? No source here gives a mechanism.
- [ ] Do `req="sensors"` blue options still open inside a nebula, where the system exists
      but does not function? ([[concept-nebula-mechanics]] — unresolved.)
- [ ] Does the AE `OVERRIDE_ITEMS` list replace `ITEMS` here?
      ([[concept-sector-event-allocation]])
- [ ] What is the actual beacon floor for a generated map? Fandom says 19–24; the grid
      rule alone only gives the ceiling ([[source-fandom-sectors]],
      [[source-xftl-sector-map]]).

## Sources
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-text-sectorname-xml]] (per raw/gamedata/text_sectorname.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-fandom-sectors]] (per raw/wiki/sectors.md)
- [[source-xftl-sector-map]] (per raw/modding/2026-08-15-xftl-sector-map.txt)
- [[source-fandom-environmental-hazards]] (per raw/wiki/environmental-hazards.md)
- [[source-fandom-sensors]] (per raw/wiki/sensors.md)
- [[source-fandom-rebel-fleet]] (per raw/wiki/rebel-fleet.md)
- [[source-fandom-beacons]] (per raw/wiki/beacons.md)
- [[source-fandom-stores-and-resources]] (per raw/wiki/stores-and-resources.md)
- [[source-fandom-template-stores-number-of-stores-by-sectors]] (per raw/wiki/template-stores-number-of-stores-by-sectors.md)
- [[source-fandom-template-stores-additional-stores-from-events-by-sectors]] (per raw/wiki/template-stores-additional-stores-from-events-by-sectors.md)
