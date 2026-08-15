---
id: sector-mantis-homeworlds
type: sector
sector_id: MANTIS_HOME
sector_class: hostile
faction: [[[entity-mantis]]]
min_sector: 2
unique: true
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-15
sources: 15
tags: [homeworld, ship-unlock, store-poor]
---

# Mantis Homeworlds

## Summary
Unique Mantis home sector. [[sector-mantis-controlled-sector]]'s pool plus a guaranteed
`MANTIS_NAMED_THIEF` beacon — the only allocation difference between the two, verified line
by line against `sector_data.xml` (per [[source-sector-data-xml]]). It is one of the
game's poorest sectors for stores, and it allocates no nebula line at all, so nothing in
it slows the Rebel fleet.

## Character & Hazards
- `unique="true"`, `minSector="2"` (per [[source-sector-data-xml]]). Fandom states the same
  rule as "only once per game and only at sector **3** or higher" — the same fact with a
  1-indexed reading of `minSector` (per [[source-fandom-sectors]]).
- Filed by Fandom under **Hostile Sectors** (red on the sector map), which is why
  `sector_class` is `hostile` here (per [[source-fandom-sectors]]).
- Fandom's own beacon list for this sector matches `sector_data.xml` exactly, **and in this
  case matches the file order too** — although the page warns that its listings generally do
  not reflect the real order (per [[source-fandom-sectors]], `raw/wiki/sectors.md`).
- Crew that can be bought in stores or won as a crew-kill reward here, by rarity (1 = common):
  Mantis 1, Human 2, Engi 3, Rockman 4. Zoltan and Slug are listed at rarity 0, which means
  they cannot be found randomly here (per [[source-sector-data-xml]]; rarity-0 meaning per
  [[source-fandom-stores-and-resources]]; the same crew list appears in
  [[source-fandom-sectors]], which omits the rarity-0 races entirely).
- Soundtrack: `mantis`, `debris`, `void` (per [[source-sector-data-xml]]).

## Event Pool

The lines below are in **file order, which is also the order the generator fills them**
(per [[source-fandom-sectors]]; see [[concept-sector-event-allocation]]).

| # | Event list | min | max | Notes |
|---|---|---|---|---|
| 1 | `MANTIS_NAMED_THIEF` | 1 | 1 | Named beacon, placed first |
| 2 | `STORE_MANTIS` | 1 | 2 | Guaranteed stores |
| 3 | `NOTHING_MANTIS` | 2 | 3 | |
| 4 | `DISTRESS_BEACON_MANTIS` | 1 | 3 | 8 events; the sector's deepest pool |
| 5 | `HOSTILE_MANTIS` | 6 | 7 | |
| 6 | `BOARDERS_MANTIS` | 1 | 2 | |
| 7 | `ITEMS` | 1 | 2 | Shared list, not Mantis-specific |
| 8 | `NEUTRAL_MANTIS` | 6 | 7 | Filled last |

Start beacon: `START_BEACON_MANTIS`.

### What the allocation means on an actual map
- Beacons are placed **before** any event is assigned: a 6×4 grid, each cell 80% likely to
  hold one, so **at most 24 beacons** (per [[source-fandom-sectors]], [[source-xftl-sector-map]]).
- The sector allocates **19–27 slots**, so its totals are not the number of stops — on a
  full map it asks for more than the map can hold (per [[source-sector-data-xml]] summed;
  ceiling per [[source-fandom-sectors]]).
- Because generation stops when the beacons run out, the overspend can only reach the
  **last** line: everything through `ITEMS` is placed even at maximum rolls (20 slots before
  `NEUTRAL_MANTIS`), so `NEUTRAL_MANTIS` is the only line that can be cut short, and no line
  here can be skipped entirely. The guaranteed thief beacon and both stores sit at the top
  and are never at risk.
- When rolls come in low, up to five beacons can be left over and filled from the shared
  `NEUTRAL` fallback list (`OVERRIDE_NEUTRAL` under AE) (per [[source-fandom-sectors]]).
- The **exit beacon is not in the table** — it draws from the shared `EXIT_LIST`
  (per [[source-fandom-sectors]]).

> ⚠️ **UNVERIFIABLE, NOT CONTRADICTED:** the "19–24 beacons per sector" figure, the 6×4/80%
> grid and the stop-when-full rule come from a reverse-engineering teardown this repo does
> not hold, quoted by Fandom ([[source-fandom-sectors]], [[source-xftl-sector-map]]).
> `sector_data.xml` states nothing about beacon counts. Nothing here claims a beacon
> *minimum*; the allocation minimum (19) is a different quantity.

## Beacon Markers
The map marks stores and distress beacons, but only within one jump
(per [[source-fandom-beacons]]).

- All eight events in `DISTRESS_BEACON_MANTIS` carry a `<distressBeacon/>` tag, and **no
  other event in this sector's pool does** (per [[source-events-mantis]],
  [[source-events-xml]]), so here the distress markers you can see correspond exactly to
  the 1–3 the table allocates. That is not general: Fandom's worked example is the Engi
  sector, where a distress-tagged event in `NEUTRAL_ENGI` is placed earlier and produces
  more distress markers than the table's distress count (per [[source-fandom-sectors]]).
- `ESCORT_BEACON` (Escort civilians FTL haywire) is both distress-marked **and** a
  store-opening event — so the sector's one unplanned shop arrives wearing a distress
  marker, not a store marker (event defined in [[source-events-xml]], list membership in
  [[source-events-mantis]]; also listed for Mantis space in
  [[source-fandom-template-stores-additional-stores-from-events-by-sectors]]).

## Stores
- **1–2 guaranteed stores**, matching `STORE_MANTIS` — the lowest tier of any non-nebula
  sector apart from The Last Stand, level with Pirate and Rebel space (per
  [[source-fandom-template-stores-number-of-stores-by-sectors]], [[source-sector-data-xml]]).
  "Guaranteed" here means the `STORE_*` allocation only; event-spawned stores are counted
  separately (per [[source-fandom-stores-and-resources]]). See [[concept-stores]].
- The store line is filled second, so both allowed stores always land.
- The only event in the sector's own pool that can open an extra store is `ESCORT_BEACON`,
  one of eight events on a line allocated 1–3 beacons. Under Advanced Edition,
  `OVERRIDE_ITEMS` would add `STORE_REBELSIDE` (Large trade station) to the item line
  (list per [[source-dlceventsoverwrite]], event per [[source-dlcevents]]) — whether the
  engine substitutes `OVERRIDE_*` lists at all is unresolved
  ([[concept-sector-event-allocation]]).
- `PIRATE_BRIBER` is in none of this sector's allocated lists; Fandom marks it here as a
  **filler or exit-beacon** event only, which is reachable because low rolls can leave
  beacons for the fallback list (per
  [[source-fandom-template-stores-additional-stores-from-events-by-sectors]]).

> ⚠️ **CONTRADICTION — does Mantis space carry a store-opening event of its own?**
> [[source-fandom-template-stores-additional-stores-from-events-by-sectors]] concludes in
> prose that "**Mantis carries none at all** beyond the universal Pirate briber". The raw
> table it summarises says otherwise: in the Mantis column it marks **Escort civilians FTL
> haywire** and **Large trade station** with a plain `+`, and marks *Pirate briber* grey,
> i.e. filler/exit only (`raw/wiki/template-stores-additional-stores-from-events-by-sectors.md`).
> The game files agree with the table, not the prose: `ESCORT_BEACON` is a member of
> `DISTRESS_BEACON_MANTIS` and its tree opens a store, and `STORE_REBELSIDE` is in
> `OVERRIDE_ITEMS` (per [[source-events-mantis]], [[source-events-xml]],
> [[source-dlceventsoverwrite]]). **Bet on the
> game files**: this sector has exactly one in-pool store-opener plus one AE-conditional
> one. The practical point survives either way — that is a very thin supplement to 1–2
> guaranteed stores.

## The Rebel Fleet Here
- The sector allocates **no `NEBULA_*` line**, so there is no beacon in it that halves the
  fleet's advance the way a nebula beacon in a non-nebula sector does
  (per [[source-fandom-rebel-fleet]]; mechanism in [[concept-rebel-fleet-advance]]).
  The same absence means sensors are never blacked out here.
- Nothing in the pool delays the fleet, and one event advances it: `AUTO_WARNING` is a
  Rebel scout whose `gotaway` branch carries `<modifyPursuit amount="1"/>` — letting it get
  away costs a jump of pursuit (event per [[source-events-rebel]], the ship block
  `REBEL_AUTO_WARNING` per [[source-events-ships]]; the same
  effect is described as doubling the pursuit rate for one turn in
  [[source-fandom-rebel-fleet]]).

## Chains That Run Through It
- **`MANTIS_NAMED_THIEF`** — guaranteed, exactly one beacon, placed first.
  **It is not a multi-stage unlock chain.** The event loads a non-hostile ship; both choices
  turn it hostile; the ship's `deadCrew` branch loads `MANTIS_NAMED_THIEF_DEFEAT`, and inside
  that single beacon the `medbay lvl=2` / `clonebay lvl=2` branch emits `unlockShip id="2"`
  together with the `CREW_STIMS` augment and a Mantis crew member with `all_skills="2"`
  (per [[source-events-mantis]] `raw/gamedata/events_mantis.xml`, [[source-events-ships]]).
  Destroying the ship instead ends the event with a MED reward and no unlock.
  The `MANTIS_NAMED_THIEF_STASH` quest marker is an additional reward on that branch (and on
  a plain branch that needs no Medbay), **not** a required step for the unlock.
  See [[concept-ship-unlocks]]; the files name only the numeric id, so no ship is named here.
- **`DONOR_MANTIS_CHASE`** (hostile pool) plants `DONOR_MANTIS_CHASE2`, and `ESCORT_BEACON`
  (distress pool) plants `QUEST_ESCORT_ARRIVE` — three quest starts in the sector in total.
- Quest markers can only take over a beacon that is unvisited, not a nebula beacon, not the
  exit, not fleet-overtaken, not already a quest, **not a store and not a distress beacon**,
  and closer to you than the fleet is to it; otherwise the marker is pushed into the next
  sector, and from sector 7 it is dropped (per [[source-xftl-sector-map]],
  [[source-fandom-beacons]]; see [[concept-quest-beacon-placement]]).

## Factions & Ships
- [[entity-mantis]] — dominant faction. Note that the hostile pool is not purely Mantis: it
  also contains `REBEL`, `AUTO_ASTEROID` and `AUTO_WARNING` (per [[source-events-mantis]]).

## Strategy Notes
- Arrive repaired and stocked. With 1–2 guaranteed stores and one thin in-pool store-opener,
  the shops you can see are effectively all there are
  (per [[source-fandom-template-stores-number-of-stores-by-sectors]]).
- Trigger quest-marker events early: the marker needs an ordinary unvisited beacon ahead of
  the fleet, or it slides into the next sector (per [[source-xftl-sector-map]]).
- _Opinion, unsourced beyond Fandom's own reasoning:_ Fandom argues sector colour is a poor
  guide to danger and that sectors should be judged individually, naming store count as the
  key difference between them. It offers no measurement for Mantis space specifically
  (per [[source-fandom-sectors]]).

## Open Questions
- [x] Is `MANTIS_NAMED_THIEF` the Mantis Cruiser unlock step? — **Answered**: it emits
  `unlockShip id="2"` directly, in a single event resolved at one beacon, not as a
  multi-stage chain. Which ship id 2 is remains unnamed in the files consulted here.
- [ ] Do the `OVERRIDE_*` lists (`OVERRIDE_ITEMS`, `OVERRIDE_HOSTILE_MANTIS`) actually
  replace their base lists under AE? ([[concept-sector-event-allocation]])
- [ ] Is the beacon *floor* real? Fandom says 19–24 per sector; the generation rule it cites
  gives only a ceiling plus an anti-emptiness guard.
- [ ] Is `unique="true"` scoped per sector or per run? ([[concept-event-uniqueness]])
- [ ] Fandom marks Large trade station as available in Mantis space without an AE caveat,
  while the only route this repo can see is the AE `OVERRIDE_ITEMS` list. Is it reachable
  with AE content off?

## Sources
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-text-sectorname-xml]] (per raw/gamedata/text_sectorname.xml)
- [[source-events-mantis]] (per raw/gamedata/events_mantis.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-events-rebel]] (per raw/gamedata/events_rebel.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-dlcevents]] (per raw/gamedata/dlcEvents.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-fandom-sectors]] (per raw/wiki/sectors.md)
- [[source-fandom-beacons]] (per raw/wiki/beacons.md)
- [[source-fandom-rebel-fleet]] (per raw/wiki/rebel-fleet.md)
- [[source-fandom-stores-and-resources]] (per raw/wiki/stores-and-resources.md)
- [[source-fandom-template-stores-number-of-stores-by-sectors]]
  (per raw/wiki/template-stores-number-of-stores-by-sectors.md)
- [[source-fandom-template-stores-additional-stores-from-events-by-sectors]]
  (per raw/wiki/template-stores-additional-stores-from-events-by-sectors.md)
- [[source-xftl-sector-map]] (per raw/modding/2026-08-15-xftl-sector-map.txt)
