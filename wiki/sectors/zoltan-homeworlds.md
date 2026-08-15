---
id: sector-zoltan-homeworlds
type: sector
sector_id: ZOLTAN_HOME
sector_class: unknown
faction: [[[entity-zoltan]]]
min_sector: 2
unique: true
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-15
sources: 10
tags: [homeworld, ship-unlock]
---

# Zoltan Homeworlds

## Summary
Unique Zoltan home sector. [[sector-zoltan-controlled-sector]]'s allocation table plus a
guaranteed `ZOLTAN_PEACE_QUEST` beacon (per [[source-sector-data-xml]]).

That one extra line matters more than it looks. The table allocates **21–33 beacon slots**
against a map that holds **at most 24**, and allocation stops the moment the beacons run
out ([[source-fandom-sectors]], [[source-xftl-sector-map]]). Both named beacons sit near
the top of the queue and are therefore safe; what this sector actually risks losing is the
bottom of its table — `ITEM_ZOLTAN`, `QUESTS_ZOLTAN` and `NEUTRAL_ZOLTAN`.

## Character & Hazards
`unique="true"`, `minSector="2"`. Two guaranteed named beacons — `ZOLTAN_CREW_STUDY`
and `ZOLTAN_PEACE_QUEST`. (per [[source-sector-data-xml]])

**How the map is filled** ([[source-fandom-sectors]], citing the xftl teardown recorded at
[[source-xftl-sector-map]]; see [[concept-sector-event-allocation]]):

- Beacons are laid out first — a 6×4 grid, each cell ~80% likely to hold one, so **at most
  24**. Fandom states the range as 19–24 per sector.
- Lines are then filled **in sector-definition order**, each rolling its own min–max
  inclusive, and **generation stops when the beacons run out**.
- **`NEBULA_ZOLTAN` jumps the queue** — every `NEBULA_*` list is processed first, because
  the cloud graphics have to be drawn before anything else. A cloud drawn over an ordinary
  beacon converts it, and that beacon draws from the shared `NEBULA` list, which is **not
  part of this sector's pool**.
- Beacons still empty at the end take events from `NEUTRAL` (`OVERRIDE_NEUTRAL` under AE).
  With a minimum allocation of 21 against at most 24 beacons, that fallback has little room
  to fire here.
- The **exit beacon is not in the table** — it draws from the shared `EXIT_LIST`, and an
  exit covered by cloud graphics is always empty.

**Placement order and what is at risk** (per `sectors/data/zoltan-homeworlds.sector.json`,
derived from [[source-sector-data-xml]] under the rules above):

| # | Line | min–max | Note |
|---|---|---|---|
| — | `NEBULA_ZOLTAN` | 2–6 | placed first, out of file order |
| 1 | `ZOLTAN_CREW_STUDY` | 1 | safe |
| 2 | `ZOLTAN_PEACE_QUEST` | 1 | safe |
| 3 | `STORE_ZOLTAN` | 2 | safe |
| 4 | `NOTHING_ZOLTAN` | 1–2 | |
| 5 | `DISTRESS_BEACON_ZOLTAN` | 1–2 | |
| 6 | `HOSTILE_ZOLTAN` | 6–8 | |
| 7 | `BOARDERS_ZOLTAN` | 1–2 | |
| 8 | `ITEM_ZOLTAN` | 1–2 | **may be cut** |
| 9 | `QUESTS_ZOLTAN` | 0–1 | **may be cut** |
| 10 | `NEUTRAL_ZOLTAN` | 5–6 | **may be cut** |

Three at-risk lines is joint-second-worst in the game: only [[sector-slug-home-nebula]]
(four) is worse, and [[sector-slug-controlled-nebula]] also has three. The plain
[[sector-zoltan-controlled-sector]] risks only two — the extra guaranteed envoy beacon is
what pushes `ITEM_ZOLTAN` into the danger zone.

**Hazards carried by the pool itself:** nebula on 10 events, plasma/ion storm on 4,
asteroid field on 2. Nebula beacons disable sensors (a Slug or a Lifeform Scanner still
sees enemy crew) and **halve the Rebel advance** for that jump — this is not a nebula
sector, so the reduction is the full 50%, not the 20% nebula sectors get
([[source-fandom-environmental-hazards]], [[source-fandom-rebel-fleet]]). A nebula beacon
overtaken by the fleet always becomes an ion storm and never carries an ASB
([[source-fandom-rebel-fleet]]).

**Stores.** Two guaranteed and no nebula stores, matching the community store table for
Zoltan sectors ([[source-fandom-template-stores-number-of-stores-by-sectors]]). Additional
stores from events in Zoltan space: [[event-zoltan-trade-hub]] and [[event-pirate-briber]],
plus [[event-large-trade-station]] as an **exit-beacon** event
([[source-fandom-template-stores-additional-stores-from-events-by-sectors]]). The store
line is filled early, so the two guaranteed ones always exist; both extras ride on lines
that may be cut.

**Crew on sale.** `rarityList` puts Zoltan at rarity 1 — the most common crew here, and
only [[sector-zoltan-controlled-sector]] matches that. Rarity governs store assortment
probability and event crew-kill rewards ([[source-fandom-stores-and-resources]],
[[source-sector-data-xml]]). The same source notes Crystal crew cannot be acquired outside
[[sector-hidden-crystal-worlds]] **except through one event** — `ZOLTAN_CREW_STUDY`, which
is guaranteed here.

## Event Pool

| Event list | min | max |
|---|---|---|
| `ZOLTAN_CREW_STUDY` | 1 | 1 |
| `ZOLTAN_PEACE_QUEST` | 1 | 1 |
| `STORE_ZOLTAN` | 2 | 2 |
| `NOTHING_ZOLTAN` | 1 | 2 |
| `DISTRESS_BEACON_ZOLTAN` | 1 | 2 |
| `NEBULA_ZOLTAN` | 2 | 6 |
| `HOSTILE_ZOLTAN` | 6 | 8 |
| `BOARDERS_ZOLTAN` | 1 | 2 |
| `ITEM_ZOLTAN` | 1 | 2 |
| `QUESTS_ZOLTAN` | 0 | 1 |
| `NEUTRAL_ZOLTAN` | 5 | 6 |

Start beacon: `START_BEACON_ZOLTAN` (see [[concept-start-beacons]]).

Pool totals across all lines: 58 distinct events, 14 that fight on arrival, 23 that can
fight below a choice, 5 that can cost a crew member, 8 that put boarders aboard.

> ⚠️ **CONTRADICTION:** the beacon counts printed for this sector by
> [[source-fandom-sectors]] ("2 stores, 1–2 various items, 0–1 quests, 5–6 neutral
> encounters", …) describe **allocation**, not what lands on the map. The same page's own
> NOTE 1 and its generation section say so outright: the counts come "straight from the game
> files and can be misleading", and a line low in the table "might not even exist on the map,
> because all beacons may have been 'filled' by other events already". Both readings are
> kept: the `sector_data.xml` numbers are the request, the generation rules decide the
> delivery. Here the gap is unusually wide — 33 slots requested, 24 beacons at most.

## Beacon markers
What the sector map can show before you jump — distress and store markers, and only on
beacons adjacent to you ([[source-fandom-beacons]]). Membership below is from the event
data; the claim that `<distressBeacon/>` is what draws the marker is Fandom's, not the game
files'.

- **Distress-marked (8):** `ZOLTAN_DISTRESS_MANTIS`, `ZOLTAN_DISTRESS_SHELL`,
  `REFUGEE_DISTRESS_ZOLTAN`, `DISTRESS_SATELLITE_DEFENSE`, `DISTRESS_STATION_FIRE`,
  `FRIENDLY_BEACON`, `TRAP_BEACON`, `STRANDED_BEACON`. **Every one of them is on the
  `DISTRESS_BEACON_ZOLTAN` line, and no event on any other line carries the tag** — so
  this sector shows exactly the 1–2 distress markers it allocates. That is the opposite of
  the [[sector-engi-homeworlds]] case Fandom uses as its example, where distress-tagged
  events in the neutral pool inflate the count ([[source-fandom-sectors]]).
- **Store-marked (3):** `STORE_ZOLTAN`, plus `ZOLTAN_TRADE_HUB` (quests line) and
  `PIRATE_BRIBER` (neutral line) — the two extras sit outside the store allocation, on
  lines that may be cut.

## Chains That Run Through It
- [[chain-zoltan-cruiser-unlock]] — `ZOLTAN_PEACE_QUEST` is its guaranteed first beacon and
  is allocated **only** by this sector. Two beacons, no gate, no required fight.
- [[chain-crystal-cruiser-unlock]] — the guaranteed `ZOLTAN_CREW_STUDY` beacon is
  **step 2** (the Zoltan research facility). Note this is *not* distinctive to the
  homeworlds: [[sector-zoltan-controlled-sector]] allocates `ZOLTAN_CREW_STUDY` at the same
  `min="1" max="1"` ([[source-sector-data-xml]]), and the event also appears in the Engi
  sectors' neutral pool. The envoy is what makes this sector unique, not the Crystal step.

> ⚠️ **CONTRADICTION — where a quest marker may be placed.** [[source-fandom-beacons]]
> says a quest marker overwrites any event "unless it is a store, exit, or another quest
> marker" and "cannot appear in nebula area". `StarMap::AddQuest` as read from the binary
> gives a longer filter: not visited, not nebula, not the exit, not fleet-overtaken, no
> existing quest, not a store, **not a distress beacon**, not the player's current beacon,
> and reachable in fewer jumps than the Rebels need to take it
> ([[source-xftl-sector-map]]). Both recorded; the engine list is the better bet on
> mechanism, the Fandom page carries its own `@to-do: test and verify` on this claim.
>
> It bites here specifically: this sector can hold 2–6 nebula beacons, two stores and a
> distress beacon, all of them ineligible, so the [[chain-zoltan-cruiser-unlock]] marker
> can fail to find a candidate and be pushed into the next sector — where it still appears
> whichever sector you pick. Both sources agree that a marker pushed from sector 7 is lost
> instead ([[source-fandom-beacons]], [[source-xftl-sector-map]]).

## Factions & Ships
- [[entity-zoltan]] — dominant faction. Only two of the seven `HOSTILE_ZOLTAN` events
  actually load a Zoltan ship; the rest are pirates, Mantis, Rebels and an Engi escort.

## Strategy Notes
- The two things worth routing here for — the envoy and the research facility — are the two
  things the map cannot take away from you. Everything the sector is *advertised* to hold
  below them (its free items, its quest, most of its neutral encounters) is what gets cut
  when the rolls run high.
- *Opinion:* [[source-fandom-sectors]] states that "Zoltan sectors have many fights and are
  among the most dangerous", against Engi sectors being "very safe". It is argued from one
  Reddit sector-profit thread, not from measured data — recorded as opinion. The pool itself
  does show 6–8 guaranteed hostile beacons plus 1–2 boarder beacons, and 14 events that open
  fire on arrival.
- Nebula beacons here are worth taking on the way through when the fleet is close: full 50%
  advance reduction, at the cost of blind sensors
  ([[source-fandom-environmental-hazards]]).
- Arriving late is worse than arriving early for the unlock chain, because a quest marker
  that cannot be placed in sector 7 is dropped rather than delayed
  ([[source-xftl-sector-map]]).

## Open Questions
- [x] ~~Does `ZOLTAN_PEACE_QUEST` gate the Zoltan Cruiser unlock?~~ Yes — it is the trigger
      event of [[chain-zoltan-cruiser-unlock]], which ends in `<unlockShip id="7"/>`.
- [ ] Nebula clouds convert ordinary beacons and fill them from the shared `NEBULA` list.
      Does that list contain distress-tagged events? If so, this sector's clean
      one-to-one distress marker count would no longer hold.
- [ ] Does `OVERRIDE_HOSTILE_ZOLTAN` actually replace `HOSTILE_ZOLTAN` under AE? It adds
      `REBEL_PULSAR`, which would put a pulsar hazard in this sector's pool. Unresolved for
      every sector — see [[concept-sector-event-allocation]].
- [ ] The **beacon floor**. [[source-fandom-sectors]] says 19–24 per sector;
      [[source-xftl-sector-map]] gives the mechanism (6×4 grid, 20% empty chance, guarded so
      empties stay ≈20%) without stating a floor, and `raw/gamedata/` states neither. The 24
      ceiling is the only figure used on this page's tooling.

## Sources
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-text-sectorname-xml]] (per raw/gamedata/text_sectorname.xml)
- [[source-fandom-sectors]] (per raw/wiki/sectors.md) — allocation order, the 24-beacon
  ceiling, nebula-first, the NEUTRAL fallback, `EXIT_LIST`, and NOTE 1
- [[source-xftl-sector-map]] (per raw/modding/2026-08-15-xftl-sector-map.txt) — the grid,
  and `StarMap::AddQuest`'s marker filter
- [[source-fandom-beacons]] (per raw/wiki/beacons.md) — distress/store markers are adjacent-
  only; quest marker placement and carry-over
- [[source-fandom-rebel-fleet]] (per raw/wiki/rebel-fleet.md) — nebula advance reduction,
  ion storm and ASB behaviour on overtaken beacons
- [[source-fandom-environmental-hazards]] (per raw/wiki/environmental-hazards.md) — nebula,
  plasma storm and asteroid effects
- [[source-fandom-stores-and-resources]] (per raw/wiki/stores-and-resources.md) — rarity,
  store contents, and the Crystal-crew exception
- [[source-fandom-template-stores-number-of-stores-by-sectors]]
  (per raw/wiki/template-stores-number-of-stores-by-sectors.md)
- [[source-fandom-template-stores-additional-stores-from-events-by-sectors]]
  (per raw/wiki/template-stores-additional-stores-from-events-by-sectors.md)
