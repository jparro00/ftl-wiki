---
id: sector-engi-controlled-sector
type: sector
sector_id: ENGI_SECTOR
sector_class: civilian
faction: [[[entity-engi]]]
min_sector: 0
unique: false
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-15
sources: 14
tags: [civilian, stores, items, map-generation]
---

# Engi Controlled Sector

## Summary
Engi-flavoured sector with its own parallel set of event lists — every generic list is
replaced by an `_ENGI` variant except `ITEMS`. It is repeatable and has no depth
requirement, so a run can pass through more than one. Its supply allocation is the most
generous in the game — five item beacons (more than any other sector; only
[[sector-engi-homeworlds]] matches it) and two to three guaranteed stores (joint-highest),
both placed near the top of the table — set against a hostile list that contains no Engi
ship at all. (per [[source-sector-data-xml]],
[[source-fandom-template-stores-number-of-stores-by-sectors]])

Grouped with the **civilian** sectors: `sector_data.xml` lists `ENGI_SECTOR` inside
`<sectorType name="CIVILIAN">`, and Fandom files it under "Civilian Sectors" (green on the
map). (per [[source-sector-data-xml]], [[source-fandom-sectors]])

## Character & Hazards

### Placement order — the table is a queue
The allocation table is not a description of the map; it is the order in which beacons get
filled. Per [[source-fandom-sectors]] and [[source-xftl-sector-map]]:

1. The **map is laid out first** — a 6×4 grid, each cell 80% likely to hold a beacon, so
   **at most 24**. Fandom puts the realised range at **19–24 beacons**; neither figure
   comes from the game files.
2. Lines are then filled **in `sector_data.xml` order**, each rolling its own min–max
   inclusive and finishing before the next begins.
3. **When the beacons run out, generation stops.** A line near the bottom can be cut short.
4. Beacons still empty at the end draw from `NEUTRAL` (`OVERRIDE_NEUTRAL` under AE).
5. The **exit beacon is not in the table** — it draws from the shared `EXIT_LIST`.

What that means here: the table asks for **19–27 slots**. Its *maximum* exceeds the
24-beacon ceiling, so `HOSTILE_ENGI` — the last line — is the one that absorbs the
shortfall. No line in this sector is at risk of receiving *nothing*: even at every
preceding line's maximum, only 20 slots are spoken for before the hostile line begins.
(per [[source-sector-data-xml]] as extracted to `sectors/data/engi-controlled-sector.sector.json`)

> **Inference, not a sourced claim:** the start beacon (`START_BEACON_ENGI`) and the exit
> beacon are both outside the allocation table, so a 19-beacon map has ~17 beacons for a
> table whose *minimum* is 19. On the small end of Fandom's range this sector cannot place
> even its minimum, which would make a truncated `HOSTILE_ENGI` the ordinary case rather
> than an edge case. Nothing in `raw/` states this directly; it is arithmetic on
> [[source-fandom-sectors]]'s beacon range and the XML's counts.

This sector allocates **no `NEBULA_*` line**, so the queue-jumping rule in
[[concept-sector-event-allocation]] never fires here and no cloud graphics are drawn: no
beacon in an Engi Controlled Sector halves the Rebel advance, and the exit is never forced
to the empty in-cloud event. (per [[source-fandom-sectors]], [[source-fandom-rebel-fleet]])

### Beacon markers vs the allocation table
`<distressBeacon/>` on an event, not membership of `DISTRESS_BEACON_ENGI`, is what puts a
distress marker on the map — and the two sets do not match here. Nine events in this
sector's pool carry the tag:

| Event | Allocated from | LRS reading |
|---|---|---|
| [[event-dense-asteroid-field-distress]] (`ASTEROID_DERELICT_SHIP`) | `NEUTRAL_ENGI` | unvisited location |
| [[event-asteroid-belt-distress]] (`CIVILIAN_ASTEROIDS_BEACON`) | `DISTRESS_BEACON_ENGI` | unvisited location |
| [[event-engi-research-station]] (`DISTRESS_ENGI_REACTOR`) | `DISTRESS_BEACON_ENGI` | unvisited location |
| [[event-engi-distress-rebel-fight]] (`DISTRESS_ENGI_REBEL`) | `DISTRESS_BEACON_ENGI` | possible ship detected |
| [[event-giant-alien-spiders]] (`DISTRESS_INFESTATION`) | `DISTRESS_BEACON_ENGI` | unvisited location |
| [[event-malfunctioning-defense-system]] (`DISTRESS_SATELLITE_DEFENSE`) | `DISTRESS_BEACON_ENGI` | unvisited location |
| [[event-crushed-pirate]] (`DISTRESS_TRAPPED_MINER`) | `DISTRESS_BEACON_ENGI` | unvisited location |
| [[event-friendly-ship-out-of-fuel]] (`FRIENDLY_BEACON`) | `DISTRESS_BEACON_ENGI` | possible ship detected |
| [[event-pirate-ship-distress-trap]] (`TRAP_BEACON`) | `DISTRESS_BEACON_ENGI` | possible ship detected |

Two mismatches, in both directions:

- **Marked but not allocated as distress:** `ASTEROID_DERELICT_SHIP` sits in `NEUTRAL_ENGI`
  and still shows the marker, so the sector can show **more** distress beacons than the
  1–3 the distress line rolls. [[source-fandom-sectors]] uses this exact event in this
  exact sector as its worked example, giving **4** as the observed count.
- **Allocated as distress but unmarked:** [[event-engi-ship-attacked-by-mantis-ship]]
  (`ENGI_STATION_DISTRESS`) sits in `DISTRESS_BEACON_ENGI` and carries no distress tag, so
  a beacon rolled off that line can show nothing at all. Fandom calls this class of case a
  mistake in the data.

The LRS column and the membership above are independently corroborated:
[[source-fandom-template-distress-events-by-sectors]]'s Engi column lists exactly these
nine events — including Dense asteroid field distress, and excluding Engi ship attacked by
Mantis ship — which is a second source agreeing with the tags read out of
`raw/gamedata/`. Only three of the nine read as a ship under Long-Ranged Scanners, and two
of those three ([[event-engi-distress-rebel-fight]],
[[event-pirate-ship-distress-trap]]) start combat on arrival.

> ⚠️ **CONTRADICTION — the mechanism, not the outcome.** [[source-fandom-sectors]] NOTE 1
> explains the extra Engi distress beacon by saying `NEUTRAL_ENGI` events are "populating
> the beacon map **before** the events from `DISTRESS_BEACON_ENGI`". `sector_data.xml`
> gives the opposite order: `DISTRESS_BEACON_ENGI` is the **fifth** line and `NEUTRAL_ENGI`
> the **seventh**, so the distress line rolls first and the neutral line adds its marker
> afterwards. The *outcome* Fandom describes (up to 4 distress markers where the table says
> 1–3) is unaffected — both lines are filled either way — but the causal story is wrong for
> this sector. The same page warns that its own listing "does **not** completely reflect the
> actual order of events in the game files", which is very likely where the error came from.
> Game files outrank the community wiki on file order: trust `sector_data.xml`
> ([[source-sector-data-xml]]). Fandom's claim is recorded, not deleted, because the
> player-facing conclusion it supports is correct.

### Stores
Two to three **guaranteed** stores, the joint-highest count in the game (tied with the
Civilian Sector and Hidden Crystal Worlds), and `STORE_ENGI` is the **first** line in the
table, so nothing can crowd it out.
(per [[source-fandom-template-stores-number-of-stores-by-sectors]], [[source-sector-data-xml]])

[[source-fandom-template-stores-additional-stores-from-events-by-sectors]] lists four
events that can open an *additional* store in an Engi sector:
[[event-large-trade-station]], [[event-escort-civilians]], [[event-pirate-briber]] and
[[event-settlement-mercenary-work]]. Three of the four are in this sector's extracted pool
(`QUEST_ESCORT` in `QUESTS_ENGI`; `PIRATE_BRIBER` in `NEUTRAL_ENGI`; `MERCENARY_WORK_START`
in `QUESTS_ENGI`). The fourth is not — and that is interesting:

> **Evidence bearing on an open question.** `STORE_REBELSIDE` (Large trade station) reaches
> this sector only through `OVERRIDE_ITEMS`, the AE replacement for `ITEMS`, whose
> substitution [[concept-sector-event-allocation]] records as unconfirmed. Fandom marks
> Large trade station as a plain entry for Engi, reserving its grey "exit-beacon only"
> marking for other sectors — i.e. it claims the event occurs in Engi sectors proper. That
> is consistent with `OVERRIDE_ITEMS` being live under AE, but it is one medium-reliability
> table, not a resolution. The question stays open.
> (per [[source-fandom-template-stores-additional-stores-from-events-by-sectors]],
> [[source-dlceventsoverwrite]])

### Quest markers
`QUESTS_ENGI` allocates exactly one beacon from four candidates, but **six** events in the
pool can plant a marker — `CIVILIAN_ASTEROIDS_BEACON` and `ENGI_STATION_DISTRESS` do it
from outside the quest line. The number of quest beacons you see is therefore not the
allocation figure, and per [[source-fandom-sectors]] a quest beacon may fail to appear at
all if the map is already full.

Where the marker can land is a separate filter, from [[source-xftl-sector-map]]
(`StarMap::AddQuest`): not a visited beacon, not a nebula beacon, not the exit, not a
fleet-taken beacon, not one that already has a quest, not a store, not a distress beacon,
not your current beacon, and it must be reachable and **closer to you than the Rebels are
to it**. With nothing eligible the quest is pushed to the next sector. Full detail and the
disagreement with [[source-fandom-beacons]]'s shorter exclusion list are recorded in
[[concept-quest-beacon-placement]] and [[source-xftl-sector-map]].

### The Rebel fleet here
With no nebula line, nothing on this map slows the pursuit: the advance is the flat
per-jump rate everywhere. `SQUAT_WARNING` ([[event-rebel-ship-warning]]) is a scout that
costs a jump of your lead if it gets its FTL up, and `ENGI_FLEET_DELAY` sells two jumps of
delay for two missiles. (per [[source-fandom-rebel-fleet]], [[source-xftl-sector-map]],
[[source-events-engi]])

## Event Pool

| # | Event list | min | max | Section |
|---|---|---|---|---|
| 1 | `STORE_ENGI` | 2 | 3 | store |
| 2 | `ITEMS` | 2 | 2 | items |
| 3 | `NOTHING_ENGI` | 1 | 2 | empty |
| 4 | `ITEMS_ENGI` | 3 | 3 | items |
| 5 | `DISTRESS_BEACON_ENGI` | 1 | 3 | distress |
| 6 | `QUESTS_ENGI` | 1 | 1 | quests |
| 7 | `NEUTRAL_ENGI` | 4 | 6 | neutral |
| 8 | `HOSTILE_ENGI` | 5 | 7 | hostile |

Numbered in `sector_data.xml` order, which is also fill order (§ Placement order).
Start beacon: `START_BEACON_ENGI`. Totals: **19–27 slots** allocated against a map of at
most **24** beacons.

The lists resolve to **56 distinct events**; 33 of them carry `unique="true"`, whose scope
is itself unsettled ([[concept-event-uniqueness]]). Nine start combat on arrival, 23 can
lead to combat below a choice, 5 can kill a crew member, 6 put boarders aboard and 22 have
at least one blue option. The full membership with per-event tags is generated into
`sectors/data/engi-controlled-sector.sector.json` and rendered at
`sectors/sector-engi-controlled-sector.html`.
(per [[source-events-xml]], [[source-events-engi]], [[source-dlcevents]])

Two AE `OVERRIDE_` twins touch this sector and are **not** merged into the pool, because
whether the engine substitutes them is unresolved ([[concept-sector-event-allocation]]):
`OVERRIDE_ITEMS` adds [[event-large-trade-station]], and `OVERRIDE_HOSTILE_ENGI` adds
[[event-pirate-fight-near-pulsar]]. (per [[source-dlceventsoverwrite]])

Notably, **no event in `HOSTILE_ENGI` is an Engi ship** — the line is Mantis, Rebel and
pirate hulls only. The only Engi ships in the sector that can end up shooting at you come
out of `NEUTRAL_ENGI`, in [[event-the-engi-virus]] and [[event-engi-smashed-ships]].

## Chains That Run Through It
- **The hidden Federation base** — three events here can plant the
  `HIDDEN_FEDERATION_BASE_LIST` marker: [[event-encrypted-federation-signal]],
  [[event-asteroid-belt-distress]], and [[event-engi-ship-attacked-by-mantis-ship]] through
  its Engi-crew blue option. _Chain page not yet created._
- **The Crystal route** — both halves sit in `NEUTRAL_ENGI`:
  [[event-dense-asteroid-field-distress]] hands over the Damaged Stasis Pod and
  [[event-zoltan-research-facility]] turns it into a Crystal crew member.
- No ship-unlock chain starts here; that is the difference from
  [[sector-engi-homeworlds]], which prepends a guaranteed `ENGI_UNLOCK_1` beacon.

## Factions & Ships
- [[entity-engi]] — dominant faction, and the only faction that never fights you on the
  hostile line

## Strategy Notes
- The supply lines (`STORE_ENGI`, `ITEMS`, `ITEMS_ENGI`) all sit above the distress, quest,
  neutral and hostile lines, so a bad map costs you fights and flavour, never stores or
  item beacons. (derived from [[source-sector-data-xml]] + [[source-fandom-sectors]])
- A distress marker here is worth reading before jumping: only two of the nine
  distress-marked events open with combat, and Long-Ranged Scanners separates them from the
  rest. (per [[source-fandom-template-distress-events-by-sectors]])
- **Opinion, unsourced:** [[source-fandom-sectors]] asserts "Engi sectors have few fights
  and are very safe", contrasting them with Zoltan sectors. It is presented as reasoning
  plus a link to a Reddit profit-data thread this repo does not hold, not as measured data.
  The allocation does support the first half — `HOSTILE_ENGI` at 5–7 is the lowest
  hostile-line minimum of any non-nebula sector, every other one starting at 6 — but "very
  safe" is commentary. (allocation figures per [[source-sector-data-xml]])

## Open Questions
- [x] ~~Which events populate each list.~~ Answered — extracted from `events*.xml` into
  `sectors/data/engi-controlled-sector.sector.json`.
- [x] ~~Map colour / hostility classification — not in `sector_data.xml`.~~ Answered — it
  *is* in `sector_data.xml`, under `<sectorType name="CIVILIAN">`, and
  [[source-fandom-sectors]] files it as a green civilian sector.
- [ ] Does `OVERRIDE_ITEMS` actually replace `ITEMS` here? Fandom's additional-stores table
  is suggestive but not decisive. ([[concept-sector-event-allocation]])
- [ ] What is the **floor** on beacons per map? [[source-xftl-sector-map]] describes the
  80%-per-cell roll and an anti-emptiness guard but states no minimum;
  [[source-fandom-sectors]] asserts 19 without showing the derivation. The inference above
  about `HOSTILE_ENGI` being routinely truncated depends on it.
- [ ] Is 4 the true ceiling on distress markers here, as Fandom's example implies? It
  assumes `ASTEROID_DERELICT_SHIP` is the only marked event outside the distress line —
  which matches the extracted data, but Fandom's own note hedges ("or even more?").
- [ ] Is `unique` scoped per sector or per run? Matters more here than in a homeworld
  sector, because this one can repeat. ([[concept-event-uniqueness]])

## Sources
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-text-sectorname-xml]] (per raw/gamedata/text_sectorname.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-events-engi]] (per raw/gamedata/events_engi.xml)
- [[source-dlcevents]] (per raw/gamedata/dlcEvents.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-fandom-sectors]] (per raw/wiki/sectors.md)
- [[source-xftl-sector-map]] (per raw/modding/2026-08-15-xftl-sector-map.txt)
- [[source-fandom-beacons]] (per raw/wiki/beacons.md)
- [[source-fandom-rebel-fleet]] (per raw/wiki/rebel-fleet.md)
- [[source-fandom-stores-and-resources]] (per raw/wiki/stores-and-resources.md)
- [[source-fandom-template-stores-number-of-stores-by-sectors]]
  (per raw/wiki/template-stores-number-of-stores-by-sectors.md)
- [[source-fandom-template-stores-additional-stores-from-events-by-sectors]]
  (per raw/wiki/template-stores-additional-stores-from-events-by-sectors.md)
- [[source-fandom-template-distress-events-by-sectors]]
  (per raw/wiki/template-distress-events-by-sectors.md)
