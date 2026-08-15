---
id: sector-mantis-controlled-sector
type: sector
sector_id: MANTIS_SECTOR
sector_class: hostile
faction: [[[entity-mantis]]]
min_sector: 0
unique: false
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-15
sources: 14
tags: [hostile, boarders, store-poor, no-nebula]
---

# Mantis Controlled Sector

## Summary
Mantis space: seven allocation lists, 37 distinct events, and the two structural absences
that shape everything else — **no `QUESTS_*` list and no `NEBULA_*` list**. It is the
sector with the thinnest store economy in the game outside the nebula sectors, and the only
place where nothing on the map can slow the Rebel fleet down.

> ⚠️ **CORRECTION (2026-08-15):** this page previously called it "the narrowest event pool
> of any faction sector". The data does not support that superlative — the Crystal sector
> is narrower still (24 events across 6 lists), and pool breadth is not what distinguishes
> this sector anyway. The structural point underneath it — no quest list, no nebula list —
> is true and is kept. (per [[source-sector-data-xml]])

## Trigger & Where It Appears
`minSector="0"`, `unique="false"` — can appear from the first choosable sector onward and
can repeat within a run. Grouped under `<sectorType name="HOSTILE">` (and
`OVERRIDE_HOSTILE`) in the XML, and listed under "Hostile Sectors" on the community wiki —
both agree, so `sector_class: hostile`.
(per [[source-sector-data-xml]], [[source-fandom-sectors]])

Start beacon: `START_BEACON_MANTIS` ([[event-start-beacon-mantis]]). Soundtrack: `mantis`,
`debris`, `void`.

## Character & Hazards
- Up to 2 boarding beacons (`BOARDERS_MANTIS` 1–2) — the highest guaranteed-boarding range
  in the game, from a pool of only two events, one of which (`MANTIS_BOARDERS`) is listed
  twice. (per [[source-sector-data-xml]], [[source-events-mantis]])
- 6–7 guaranteed hostile beacons, of which only three of the six pool events are Mantis
  ships; the rest are a Rebel warship and two automated scouts.
- **Nothing here delays the Rebel fleet.** No event in any of the seven lists carries a
  negative `modifyPursuit`, and the one event that touches pursuit at all —
  [[event-auto-ship-warning]] — makes it *worse* if the scout completes its jump. With no
  `NEBULA_*` list there are also no nebula beacons to halve the advance, and the sector's
  own lists do not contain the fleet-delaying mercenary (it lives in the shared fallback
  list). (per [[source-sector-data-xml]], [[source-fandom-rebel-fleet]],
  [[source-newevents]]; see [[concept-rebel-fleet-advance]])
- Environmental hazards are rare: two sun events (`MANTIS_SUN_FIGHT`, `BOARDERS_SUN`) and
  one asteroid field (`AUTO_ASTEROID`). (see [[concept-solar-flares]], [[concept-hazards]])

## Event Pool

Entries in **file order**, which is also the order the generator fills them.

| # | Event list | min | max | Section |
|---|---|---|---|---|
| 1 | `STORE_MANTIS` | 1 | 2 | store |
| 2 | `NOTHING_MANTIS` | 2 | 3 | empty |
| 3 | `DISTRESS_BEACON_MANTIS` | 1 | 3 | distress |
| 4 | `HOSTILE_MANTIS` | 6 | 7 | hostile |
| 5 | `BOARDERS_MANTIS` | 1 | 2 | boarders |
| 6 | `ITEMS` | 1 | 2 | items |
| 7 | `NEUTRAL_MANTIS` | 6 | 7 | neutral |

Allocation total: **18–26 slots**. (per [[source-sector-data-xml]])

Advanced Edition override twins exist for two of these lists: `OVERRIDE_HOSTILE_MANTIS`
adds `REBEL_PULSAR`, and `OVERRIDE_ITEMS` adds `STORE_REBELSIDE`
([[event-large-trade-station]]). Whether the engine substitutes them is unresolved —
[[concept-sector-event-allocation]]. (per [[source-dlceventsoverwrite]])

### How generation actually fills it
The allocation table is a filling queue, not a map. Beacons are placed first on a 6×4 grid
with an 80% chance per cell, so **at most 24 exist**; lines are then filled top to bottom,
each rolling its own min–max inclusive, and generation stops the moment the beacons run
out. (per [[source-fandom-sectors]], [[source-xftl-sector-map]])

What that means here:

- At maximum rolls the first six lines take 19 slots, comfortably inside 24, so **no line
  above `NEUTRAL_MANTIS` is ever at risk**. The stores, the distress beacons, all six to
  seven fights and both boarding beacons are always placed. The entire overrun — up to 2
  slots at the maximum roll — falls on `NEUTRAL_MANTIS`, the last line.
- At the minimum roll the table asks for only 18 slots, below the 24-beacon ceiling, so
  leftover beacons are filled from the shared `NEUTRAL` fallback (`OVERRIDE_NEUTRAL` under
  AE). That list is where `PIRATE_BRIBER` ([[event-pirate-briber]]) and `MERCENARY` live —
  neither of which is in any Mantis list.
  (per [[source-newevents]], [[source-dlceventsoverwrite]])
- The exit beacon is not in the table; it draws from the shared `EXIT_LIST`. With no nebula
  clouds drawn here, the "exit inside a cloud is always empty" case cannot occur.
  (per [[source-fandom-sectors]])

> Fandom's own beacon bullets for this sector — *1–2 stores, 2–3 empty, 1–3 distress, 6–7
> hostile, 1–2 boarders, 1–2 various items, 6–7 neutral* — match `sector_data.xml` **in
> both counts and order**, despite the page's blanket warning that its listings do "not
> completely reflect the actual order of events in the game files". For this sector the
> community listing happens to be in true placement order.
> (per [[source-fandom-sectors]], [[source-sector-data-xml]])

## Beacon Markers
`<distressBeacon/>` is what puts a distress marker on the map, and it does not have to match
the distress allocation line. **In this sector it does, exactly, in both directions:**

- Eight events carry the distress tag: `ESCORT_BEACON`, `FRIENDLY_BEACON`, `TRAP_BEACON`,
  `DISTRESS_TRAPPED_MINER`, `DISTRESS_INFESTATION`, `DISTRESS_SATELLITE_DEFENSE`,
  `DISTRESS_STATION_FIRE`, `DISTRESS_STATION_DISEASE` — which is precisely the contents of
  `DISTRESS_BEACON_MANTIS`, no more and no less.
- Nothing outside that list carries the tag, so the Engi-style overflow described in
  Fandom's NOTE 1 (where `NEUTRAL_ENGI` events add extra distress markers) **does not
  happen here**. The 1–3 distress markers you can count are the 1–3 the table allocated.
- Independently confirmed: the Fandom "Distress events, by sectors" table lists exactly
  those same eight events in its Mantis column.
  (per [[source-events-xml]], [[source-fandom-template-distress-events-by-sectors]],
  [[source-fandom-sectors]])

Three of the eight load a ship at the beacon — `ESCORT_BEACON` and `FRIENDLY_BEACON`
(friendly), `TRAP_BEACON` (hostile pirate) — which is what Long-Ranged Scanners reads as a
ship contact; the Fandom table's LRS column agrees. Distress and store markers are only
drawn on beacons adjacent to you. (per [[source-events-xml]], [[source-fandom-beacons]],
[[source-fandom-template-distress-events-by-sectors]]; see [[concept-map-reveal]])

## Store Economy
The routing headline for this sector.

| | |
|---|---|
| Guaranteed stores | **1–2** (`STORE_MANTIS`, first line, never squeezed) |
| Nebula stores | none — no nebula list |
| Store-opening events in the pool | **1** — `ESCORT_BEACON` ([[event-escort-civilians-ftl-haywire]]) |
| Store-opening events under AE only | `STORE_REBELSIDE` via `OVERRIDE_ITEMS`, if overrides apply |
| Reachable as filler / exit only | `PIRATE_BRIBER`, `STORE_REBELSIDE` |

1–2 guaranteed stores is the joint-lowest non-nebula allocation, shared with the starting
Civilian sector, Mantis Homeworlds, Pirate Controlled, Rebel Controlled and Rebel
Stronghold. The two nebula sector families list a lower guaranteed count (0–1) but add
dedicated nebula stores on top — 1 in Uncharted, 2 in the Slug nebulas — so they are not
poorer in practice. (per [[source-sector-data-xml]],
[[source-fandom-template-stores-number-of-stores-by-sectors]])

What separates them is the *extra* stores. Reading `<store/>` across each sector's own
lists: Pirate Controlled carries four store-opening events, Rock carries three, and Mantis
Controlled carries **one** — `ESCORT_BEACON`, and only via its quest destination. Accepting
the escort plants a marker whose destination list `QUEST_ESCORT_ARRIVE` has four outcomes,
one of which is 5 hull repaired plus a store. Taking the **Advanced FTL Navigation** blue
option instead pays a high standard reward on the spot but plants no marker — and so gives
up the sector's only in-pool shot at another counter.
(per [[source-events-xml]], [[source-sector-data-xml]])

`PIRATE_BRIBER`, which tops up stores in most sectors, is in no Mantis list at all; it can
only arrive from the shared fallback list or at the exit beacon.
(per [[source-newevents]], [[source-dlceventsoverwrite]],
[[source-fandom-template-stores-additional-stores-from-events-by-sectors]];
see [[concept-stores]])

Partial compensation sits on the `ITEMS` line (1–2 beacons from 13 events):
[[event-refueling-station]] sells fuel at 2 scrap against a store's 3, and
[[event-repair-station]] charges a flat 2 scrap per hull point while store repair prices
scale with sector number. (per [[source-events-xml]], [[source-fandom-stores-and-resources]])

> ⚠️ **CONTRADICTION:** [[source-fandom-template-stores-additional-stores-from-events-by-sectors]]
> summarises its own table as "Mantis carries none at all beyond the universal
> [[event-pirate-briber]]" and lists the Escort-civilians-FTL-haywire row as covering
> "Civilian, Pirate, Rebel, Rock, Slug, Uncharted". The raw table marks **Mantis**, not
> Slug, in that row, and [[source-fandom-escort-civilians-ftl-haywire]]'s own Locations
> template names Mantis Controlled Sector and Mantis Homeworlds. `DISTRESS_BEACON_MANTIS`
> contains `ESCORT_BEACON` outright. **Bet on the game files:** Mantis space does carry one
> store-opening chance event of its own. The summary page appears to have read the table
> one column off and needs correcting.
> (per raw/wiki/template-stores-additional-stores-from-events-by-sectors.md,
> raw/gamedata/sector_data.xml, raw/gamedata/events.xml)

> ⚠️ **CONTRADICTION:** the same Fandom table marks [[event-large-trade-station]] as an
> ordinary (non-grey) Mantis event, i.e. one that can arise from the sector's own lists.
> `STORE_REBELSIDE` appears only in `OVERRIDE_ITEMS` in `dlcEventsOverwrite.xml`, never in
> the base `ITEMS` list in `newEvents.xml`. **Resolution — this is a version difference:**
> with Advanced Edition content off it cannot come from the `ITEMS` line at all, and with AE
> on it depends on whether the engine substitutes `OVERRIDE_` lists, which no file here
> states ([[concept-sector-event-allocation]]). It can reach the sector as an exit-beacon
> event either way.
> (per [[source-dlceventsoverwrite]], [[source-newevents]],
> [[source-fandom-template-stores-additional-stores-from-events-by-sectors]])

## Chains That Run Through It
No `QUESTS_MANTIS` allocation exists, but **two events in the pool plant quest markers**:

- [[event-mantis-ship-collectors]] (`DONOR_MANTIS_CHASE`, in `HOSTILE_MANTIS`) → the
  rematch at [[event-donor-mantis-chase2]].
- [[event-escort-civilians-ftl-haywire]] (`ESCORT_BEACON`, in `DISTRESS_BEACON_MANTIS`) →
  `QUEST_ESCORT_ARRIVE`.

Fandom's NOTE 1 states the general rule these are an instance of: the "quest" beacon count
describes only the `QUESTS` event list, not every event that can plant a marker. A quest
marker overwrites whatever event sat on the beacon it lands on, unless that beacon is a
store, an exit, or another marker; if too few jumps remain it is pushed into the next
sector instead, and sector 8 can hold none at all.
(per [[source-sector-data-xml]], [[source-fandom-sectors]], [[source-fandom-beacons]];
see [[concept-quest-beacon-placement]])

Unlike the Mantis Homeworlds, no ship-unlock chain starts here — `unlock_ships` for this
sector's pool is empty. (per [[source-sector-data-xml]])

## Factions & Ships
- [[entity-mantis]] — dominant faction
- Crew rarity in stores and as kill rewards: Mantis 1, Human 2, Engi 3, Rockman 4; Zoltan
  and Slug are rarity 0 and cannot appear. Fandom's crew list for this sector agrees.
  (per [[source-sector-data-xml]], [[source-fandom-sectors]];
  see [[concept-blueprint-rarity]])

## Strategy Notes
- **Arrive stocked.** 1–2 stores, one in-pool route to a third, and no nebula store. The
  `ITEMS` line is the substitute and it is only 1–2 beacons wide.
- **Budget the fleet, not the map.** With no nebula beacon to halve the advance and no
  event that delays it, every jump costs full pursuit — including the jumps spent clearing
  boarders. (per [[source-fandom-rebel-fleet]])
- **Distress markers here mean what they say** — 1–3 of them, all drawn from one list of
  eight. Three of the four crew-killing events in the sector sit in that list, so a distress
  marker is simultaneously the sector's best-signposted reward and its main way to lose a
  crew member.
- Opinion, unsourced beyond community commentary: Fandom's colour coding calls this a "red"
  hostile sector, while cautioning that colour is a poor proxy for danger.
  (per [[source-fandom-sectors]] — flagged as the wiki's own opinion)

## Open Questions
- [x] ~~No `QUESTS_MANTIS` list exists — are Mantis-sector quests really absent?~~
  **Answered 2026-08-15: no.** Two pool events plant quest markers despite the missing
  allocation line (see Chains, above).
- [ ] Do `OVERRIDE_` lists actually replace their base lists at runtime? This decides
  whether [[event-large-trade-station]] and `REBEL_PULSAR` belong in this sector's pool.
  Tracked in [[concept-sector-event-allocation]].
- [ ] The beacon **floor**. [[source-fandom-sectors]] states sectors hold "between 19 and
  24 beacons", but the generation rule it cites is an independent 80% roll per grid cell
  plus a vague clause preventing too many empty cells — which is what would have to supply
  the 19. Nothing in `raw/gamedata/` states either number. Until it is pinned down, "how
  many stops does this sector actually have" stays unanswered, and only the 24 ceiling is
  used. (per [[source-fandom-sectors]], [[source-xftl-sector-map]])
- [ ] Is `unique="true"` scoped per sector or per run? 23 of the 37 pool events are marked
  unique, so the answer materially changes what a single visit can show you.
  [[concept-event-uniqueness]]

## Sources
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-text-sectorname-xml]] (per raw/gamedata/text_sectorname.xml)
- [[source-events-mantis]] (per raw/gamedata/events_mantis.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-fandom-sectors]] (per raw/wiki/sectors.md)
- [[source-fandom-beacons]] (per raw/wiki/beacons.md)
- [[source-fandom-rebel-fleet]] (per raw/wiki/rebel-fleet.md)
- [[source-fandom-stores-and-resources]] (per raw/wiki/stores-and-resources.md)
- [[source-fandom-template-stores-number-of-stores-by-sectors]]
  (per raw/wiki/template-stores-number-of-stores-by-sectors.md)
- [[source-fandom-template-stores-additional-stores-from-events-by-sectors]]
  (per raw/wiki/template-stores-additional-stores-from-events-by-sectors.md)
- [[source-fandom-template-distress-events-by-sectors]]
  (per raw/wiki/template-distress-events-by-sectors.md)
- [[source-xftl-sector-map]] (per raw/modding/2026-08-15-xftl-sector-map.txt)
