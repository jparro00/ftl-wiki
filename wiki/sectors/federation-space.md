---
id: sector-federation-space
type: sector
sector_id: STANDARD_SPACE
sector_class: special
faction: []
min_sector: 0
unique: false
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-15
sources: 9
tags: [starting-sector]
---

# Federation Space

## Summary
The sector every run begins in. Its event pool is the generic, faction-neutral one —
the baseline against which every other sector's pool is a variation. It is the sector
Fandom calls the **Civilian (Starting) Sector**: a trimmed-down Civilian Sector with
fewer stores, fewer item beacons and less nebula
([[source-fandom-sectors]], per raw/wiki/sectors.md).

## Sector Occurrence
`minSector="0"`, `unique="false"` in the file, but it is listed under
`<sectorType name="UNKNOWN">` and appears in **no** `CIVILIAN` / `HOSTILE` / `NEBULA`
draw list, so nothing can roll it as a later sector. That matches Fandom's flat claim
that this sector "is always and only Sector 1"
([[source-sector-data-xml]]; [[source-fandom-sectors]]).

Because it sits outside the three draw types, the 48% green / 32% red / 20% purple
sector-colour split reported by Fandom does not apply to it
([[source-fandom-sectors]], citing an xftl teardown this repo does not hold).

## Character & Hazards
Draws from the unfactioned lists. Notably the only sector in `sector_data.xml` whose
`HOSTILE_BOARDING` allocation is `min="0" max="0"` — the only entry with a maximum of
zero anywhere in the file. Eight boarding events are named and none of them can be
placed by the sector table. The Civilian Sector has the same line at `0–1` but
**commented out**, so neither civilian sector places boarders from that list.
(per [[source-sector-data-xml]])

Hazards reachable from the pool, read off the generated profile
(`sectors/data/federation-space.sector.json`):

| Hazard | Events in pool | Effect |
|---|---|---|
| Asteroid field | `AUTO_ASTEROID`, `BOARDERS_ASTEROID`, `PIRATE_ASTEROID` | periodic hull/shield hits, frequency scales with **your** shield level |
| Red giant / sun | `AUTO_SUN`, `BOARDERS_SUN`, `PIRATE_SUN` | solar flares set fires; shields reduce them |
| Nebula | 12 of the 16 `NEBULA` entries | sensors dead, Rebel advance halved for that jump ([[concept-nebula-mechanics]]) |
| Plasma/ion storm | `STORM_AUTO`, `STORM_BOARDING`, `STORM_ITEMS`, `STORM_REBEL` | reactor at half capacity |
| Pulsar | only via `OVERRIDE_HOSTILE1` (`REBEL_PULSAR`, `PIRATE_PULSAR`) | ionises 2 systems every 11–18s; AE only |

(hazard effects per [[source-fandom-environmental-hazards]], per raw/wiki/environmental-hazards.md;
membership per [[source-sector-data-xml]] and the event files)

`BOARDERS_ASTEROID` and `BOARDERS_SUN` sit on the dead `HOSTILE_BOARDING` line, so
asteroid and sun hazards only reach the map through `HOSTILE_CIVILIAN` and `HOSTILE1`.

## Event Pool
Beacon allocation per `sector_data.xml`, **in file order**, which is also the order the
generator fills the lines in (per [[source-fandom-sectors]]). Per-list membership is in the
generated profile `sectors/data/federation-space.sector.json`; the built page is
`sectors/sector-federation-space.html`.

| # | Event list | min | max | Notes |
|---|---|---|---|---|
| 1 | `STORE` | 1 | 2 | guaranteed stores — filled first, never squeezed |
| 2 | `ITEMS` | 1 | 1 | file comment: `DLC - CHanged from 1/2` — **1–2 in vanilla** |
| 3 | `NEUTRAL_CIVILIAN` | 2 | 4 | 23 events, and contains the whole 14-event distress list |
| 4 | `NOTHING` | 1 | 2 | |
| 5 | `DISTRESS_BEACON` | 1 | 2 | 14 events; 12 carry the distress tag |
| 6 | `HOSTILE_CIVILIAN` | 4 | 6 | |
| 7 | `NEBULA` | 0 | 4 | see the placement contradiction below |
| 8 | `QUESTS` | 1 | 1 | 6 events; not a guarantee of a quest beacon (below) |
| 9 | `HOSTILE1` | 2 | 2 | fixed pair, last line that places anything |
| 10 | `HOSTILE_BOARDING` | 0 | 0 | 8 events, no beacons |

Start beacon: `START_BEACON` ([[event-start-beacon]], [[concept-start-beacons]]).
Exit beacons are **not** in this table — they draw from the
shared `EXIT_LIST`, and an exit inside nebula cloud is always empty
([[source-fandom-sectors]]).

Totals: the maxima sum to **24**, exactly the map ceiling; the minima to 13.

`OVERRIDE_*` twins exist for `ITEMS` (adds `STORE_REBELSIDE`), `QUESTS` (adds
`QUEST_CONSTRUCTIONYARD`) and `HOSTILE1` (adds `REBEL_PULSAR`, `PIRATE_PULSAR`). Whether
the engine substitutes them is unresolved — see [[concept-sector-event-allocation]].

## Generation & Beacon Count
The allocation table is a filling queue, not a description of the map
([[source-fandom-sectors]], per raw/wiki/sectors.md, which cites xftl reverse-engineering):

- Beacons are placed **before** any event is assigned: a 6×4 grid, each cell 80% likely to
  hold one, with a rule preventing too many empty cells. A sector is said to hold
  **19–24 beacons**.
- Lines are then filled in definition order, each rolling its own min–max inclusive, each
  finished before the next starts. **When the beacons run out, generation stops.**
- Leftover beacons take events from `NEUTRAL` (`OVERRIDE_NEUTRAL` under AE).

> ⚠️ **UNVERIFIABLE, NOT CONTRADICTED:** the 19–24 beacon range, the 6×4 / 80% grid and
> the stop-when-full rule are sourced to an xftl teardown this repo does not hold.
> `sector_data.xml` says nothing about how many beacons a map has
> ([[source-fandom-sectors]]).

Consequence here: this table's maxima stop exactly at the ceiling (24), where the
Civilian Sector's run to 32, so on a *full* map every line here can be served. Maps are
usually not full — 24 cells at 80% each — and the shortfall lands at the bottom of the
table: `HOSTILE_BOARDING` (which places nothing anyway), then `HOSTILE1`, then `QUESTS`.

> ⚠️ **CONTRADICTION — where the nebula line is placed.**
> Fandom's technical section says every event list *"starting with `NEBULA_`"* is
> processed first, out of file order, because the cloud graphics must be drawn before
> anything else. This sector's line is named `NEBULA`, with no suffix, so by the letter of
> that rule it stays at position 7 — which is how `sectors/data/federation-space.sector.json`
> records it (`nebula_first: false`).
> But Fandom's **NOTE 2** says the Civilian (Starting) Sector — this sector — "has its
> beacons placed in proper order", and the listing it vouches for puts *"0-4 nebula
> beacons"* **first**, ahead of stores. Both statements are on the same page
> ([[source-fandom-sectors]]).
> Neither reading changes the totals (0–4 either way), so nothing about the budget turns
> on it; what it changes is which lines the clouds can convert. The mechanical argument —
> clouds must be drawn before beacons are assigned — favours nebula-first; the literal
> prefix rule favours file order. Recorded unresolved.

## What The Map Shows Before You Jump
Distress and store beacons are revealed within 1 jump; quest markers are visible from any
distance; the exit is visible from the start ([[source-fandom-beacons]], per
raw/wiki/beacons.md).

**Distress markers do not equal the distress line.** `<distressBeacon/>` on the *event* is
what draws the marker, and here:

- 12 of the 14 `DISTRESS_BEACON` events carry the tag. The two that do not —
  `PIRATE_CIVILIAN_BEACON` and `REBEL_VS_FEDERATION` — are allocated as distress but never
  show a marker. Fandom calls this class of mismatch a mistake in the data
  ([[source-fandom-sectors]] NOTE 1).
- All 14 also sit in `NEUTRAL_CIVILIAN`, which is filled **earlier**, so a map can show
  more distress markers than the 1–2 the distress line allocates. Fandom gives the Engi
  sector as its worked example of the same effect; here it arises from list overlap rather
  than from an event outside the allocation.

**Stores** ([[concept-stores]]). 1–2 guaranteed, matching Fandom's per-sector table
([[source-fandom-template-stores-number-of-stores-by-sectors]]). Four events in the pool
can open an additional store — `PIRATE_BRIBER`, `MERCENARY_WORK_START`, `QUEST_ESCORT`
(Escort civilians) and `ESCORT_BEACON` (Escort civilians FTL haywire) — and under the AE
`OVERRIDE_ITEMS` list, `STORE_REBELSIDE` (Large trade station) as well. Fandom's
additional-stores table lists exactly these for the Civilian column, whose footnote says
it also applies to the starting sector
([[source-fandom-template-stores-additional-stores-from-events-by-sectors]]).

**Quest beacons.** Nine events in the pool plant a quest marker; only six of them are on
the `QUESTS` line.

> ⚠️ **CONTRADICTION — is the quest beacon guaranteed?**
> `sector_data.xml` allocates `QUESTS` at `min="1" max="1"`, which reads as a guarantee
> and was recorded as one here on 2026-08-09 ([[source-sector-data-xml]]).
> Fandom's NOTE 1 uses **this sector** as its example against that reading: you can meet
> more than one quest beacon because other lists carry quest events, and "one 'quest'
> beacon might not even exist on the map, because all beacons may have been 'filled' by
> other events already" ([[source-fandom-sectors]]);
> [[source-fandom-beacons]] adds that quest-beacon existence is never guaranteed outside
> the Homeworlds ship-unlock quests.
> Resolution: these describe different things — the XML gives the *allocation*, Fandom the
> *realisation*. The allocation is certain; the beacon is not. Prefer the XML for what the
> sector asks for and Fandom for what a player sees.

A quest marker cannot be placed inside a nebula area, and if there is no room or few jumps
remain it is pushed into the next sector instead ([[source-fandom-beacons]]).

## The Rebel Fleet Here
- Visiting a nebula beacon in this (non-nebula) sector **halves** the fleet's advance for
  that jump ([[source-fandom-rebel-fleet]], [[source-fandom-environmental-hazards]]).
- Two events sell delay: `MERCENARY` (`modifyPursuit -2`) and `PIRATE_BRIBER` (`-1`).
- Five push it forward by one: `SQUAT_WARNING` and `AUTO_WARNING` (the fixed `HOSTILE1`
  pair), `NEBULA_AUTO_WARNING`, `NEBULA_REBEL_UNDETECTED`, and abandoning the civilians at
  `CIVILIAN_ASTEROIDS_BEACON` when they survive to report you. Fandom describes the
  scout/auto-ship case as doubling the pursuit rate for one turn
  ([[source-fandom-rebel-fleet]]); the files express it as `modifyPursuit="1"`.
- A beacon the fleet captures overwrites its event and hazard, always brings an ASB except
  in nebula or (on Easy) at the exit, and turns a captured nebula beacon into an ion storm
  ([[source-fandom-rebel-fleet]]).

## Chains That Run Through It
Nine events in the pool plant a quest marker, feeding six chains — plus one more that
only exists if the AE override list is live:

- [[chain-hidden-federation-base]] — [[event-encrypted-federation-signal]] (quest line),
  [[event-asteroid-belt-distress]] and
  [[event-rebel-ship-attacking-federation-loyalists]] (distress/neutral lines) all plant
  `HIDDEN_FEDERATION_BASE_LIST`; the first can also plant `FEDERATION_BASE_ASSIST`.
- [[chain-escort-civilians]] — [[event-escort-civilians]] (`QUEST_ESCORT`, quest line) and
  [[event-escort-civilians-ftl-haywire]] (`ESCORT_BEACON`, distress/neutral lines) →
  `QUEST_ESCORT_ARRIVE`.
- [[chain-merchant-s-request]] — [[event-merchant-s-request]] → `MERCHANT_DELIVER` /
  `MERCHANT_INVESTIGATE` / `MERCHANT_INVESTIGATE_DELIVER`.
- [[chain-capture-the-ship]] — [[event-capture-the-ship]] → `QUEST_CREWDEAD`.
- [[chain-mantis-war-camp]] — [[event-mantis-war-camp]] → `QUEST_MANTIS_INVASION`.
- [[chain-settlement-mercenary-work]] — [[event-settlement-mercenary-work]] →
  `QUEST_STORE_RESCUE`.
- [[chain-construction-yard]] — only reachable here if the AE `OVERRIDE_QUESTS` list is
  live (`QUEST_CONSTRUCTIONYARD`), which is unresolved.

No ship unlock starts here (`unlock_ships` is empty in the generated profile).

## Factions & Ships
- _Unfactioned / civilian._ Rebels are the fleet pursuit plus the Rebel ships in
  `HOSTILE_CIVILIAN`, `HOSTILE1` and the nebula line; pirates and auto-scouts carry the
  rest of the hostile pool. Mantis reach the map only through `MANTIS_FIGHT` (`HOSTILE1`),
  `NEBULA_MANTIS_FIGHT` and `QUEST_MANTIS_INVASION_START`. Mantis, Engi and Rock crew can
  also be bought or freed from the two slaver events.

## Crew In Stores
`sector_data.xml` gives **no `<rarityList>`** for `STANDARD_SPACE`, so nothing overrides
the default blueprint rarities — the generated profile's crew-rarity list is empty.
Fandom lists Human 1, Engi and Mantis 2, Rockmen 3, Zoltan 5 for this sector, which is the
same set it gives for every other sector whose definition also lacks a `rarityList`
(Civilian, Pirate, Rebel, Rebel Stronghold, The Last Stand)
([[source-fandom-sectors]]; [[source-sector-data-xml]]). Not a contradiction — Fandom is
reporting the defaults, not a sector override.

What a store here sells is sector-independent: unlimited hull repairs, limited resources,
and 2–4 slots of systems / weapons / drones / augments / crew, three random entries each.
If your ship has fewer than 11 systems and subsystems there is a 50% chance the first slot
is forced to systems, and shields and a medical system are guaranteed to appear if you do
not have them — which is why the first store of a run matters more than its scrap price
suggests ([[source-fandom-stores-and-resources]], per raw/wiki/stores-and-resources.md).

## Strategy Notes
- The store line is placed first, so 1–2 stores are dependable here even when the map is
  small; everything at the bottom of the table is not
  ([[source-fandom-sectors]], [[source-fandom-template-stores-number-of-stores-by-sectors]]).
- Nothing in this pool hands over a *named* weapon, drone or augment — every reward is a
  generic tier roll (generated profile: `named_items` is empty). Crew and fleet delay are
  the only routed-for prizes.
- Nebula stops are the cheapest fleet delay in the sector (half advance, no scrap), paid
  for with dead sensors ([[source-fandom-rebel-fleet]]).
- _Opinion, Fandom:_ sector colour is a poor proxy for danger — "it's best to choose your
  next sector based on an understanding of that specific sector, rather than just looking
  at its colour" ([[source-fandom-sectors]]; unsourced editorial on that page).

## Open Questions
- [x] ~~Which events populate each of these lists~~ — resolved; see
  `sectors/data/federation-space.sector.json` (85 distinct events across 10 entries).
- [x] ~~Map colour / hostility classification~~ — resolved: this sector belongs to
  `sectorType UNKNOWN` and is never drawn from the colour pools
  ([[source-sector-data-xml]], [[source-fandom-sectors]]).
- [ ] Is the bare `NEBULA` list hoisted to the front of the queue like a `NEBULA_*` list?
  See the contradiction above.
- [ ] Can the eight `HOSTILE_BOARDING` events reach the map at all — through the `NEUTRAL`
  fallback, an exit event, or not at all? No source here answers it.
- [ ] Does the engine substitute `OVERRIDE_ITEMS` / `OVERRIDE_QUESTS` /
  `OVERRIDE_HOSTILE1` under AE? ([[concept-sector-event-allocation]])
- [ ] What is the actual floor on beacons per map? Fandom says 19; the game files say
  nothing, and the 80%-per-cell rule alone implies no hard floor.

## Sources
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-text-sectorname-xml]] (per raw/gamedata/text_sectorname.xml)
- [[source-fandom-sectors]] (per raw/wiki/sectors.md)
- [[source-fandom-beacons]] (per raw/wiki/beacons.md)
- [[source-fandom-rebel-fleet]] (per raw/wiki/rebel-fleet.md)
- [[source-fandom-environmental-hazards]] (per raw/wiki/environmental-hazards.md)
- [[source-fandom-stores-and-resources]] (per raw/wiki/stores-and-resources.md)
- [[source-fandom-template-stores-number-of-stores-by-sectors]] (per raw/wiki/template-stores-number-of-stores-by-sectors.md)
- [[source-fandom-template-stores-additional-stores-from-events-by-sectors]] (per raw/wiki/template-stores-additional-stores-from-events-by-sectors.md)
