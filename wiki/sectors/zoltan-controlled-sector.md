---
id: sector-zoltan-controlled-sector
type: sector
sector_id: ZOLTAN_SECTOR
sector_class: civilian
faction: [[[entity-zoltan]]]
min_sector: 1
unique: false
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-15
sources: 10
tags: [crystal-route, nebula, quest-at-risk]
---

# Zoltan Controlled Sector

## Summary
Zoltan space. Guarantees a `ZOLTAN_CREW_STUDY` beacon even in the non-home variant —
one of only two non-unique sectors with a guaranteed named beacon. It allocates **20–32**
beacon slots against a map that holds **at most 24**, so the sector cannot always place
what it asks for: the bottom two lines, `QUESTS_ZOLTAN` and `NEUTRAL_ZOLTAN`, are the ones
that get dropped. (per [[source-sector-data-xml]], [[source-fandom-sectors]])

## Character & Hazards
`minSector="1"` — never the first sector. Listed by Fandom among the **Civilian (green)**
sectors, alongside [[sector-civilian-sector]] and [[sector-engi-controlled-sector]].
(per [[source-sector-data-xml]], [[source-fandom-sectors]])

### The map, before any event is placed
Beacon layout happens first and independently of the event lists: a **6×4 grid**, each cell
80% likely to hold a beacon at a random point inside it, with a guard that stops too many
cells coming up empty. So **at most 24 beacons**, and Fandom's lede states the observed
range as **19–24**. Beacons connect to beacons in adjacent cells within 165px.
(per [[source-xftl-sector-map]], [[source-fandom-sectors]]; see
[[concept-sector-event-allocation]])

> ⚠️ **CONTRADICTION — allocation vs. what reaches the map.** `sector_data.xml` says this
> sector places 2 stores, 1–2 distress and 0–1 quests. [[source-fandom-sectors]]'s own NOTE 1
> says those counts "are taken straight from the game files and can be misleading": the store
> figure counts guaranteed stores only, the distress figure counts only the
> `DISTRESS_BEACON_*` list, and "one 'quest' beacon might not even exist on the map, because
> all beacons may have been 'filled' by other events already." Both readings are kept — the
> XML gives the **allocation**, Fandom's caveat gives the **realisation**. For this sector the
> caveat bites hardest on quests (below); stores and distress sit high enough in the queue to
> survive (see [[#placement-order]]).

### Hazards in the pool
Derived from the event trees, not asserted: **asteroid fields** at `ZOLTAN_ASTEROID` and
`ZOLTAN_DISTRESS_MANTIS`; **nebula** at ten events and **plasma/ion storm** at four, all
inside `NEBULA_ZOLTAN`; and a **pulsar** at `REBEL_PULSAR`, which is added only by the
unconfirmed `OVERRIDE_HOSTILE_ZOLTAN` list ([[concept-sector-event-allocation]]).
Nebula kills your sensors; a plasma storm halves your reactor; the pulsar is Advanced
Edition content only. (per [[source-fandom-environmental-hazards]], [[concept-hazards]])

Because this is **not** a nebula sector, a nebula beacon here gives the **full pursuit
reduction** — Fandom's "halves the Rebel advance rate for that turn", which
[[source-xftl-sector-map]] measures as 32px of fleet advance instead of 64px. Nebula
sectors get only the reduced 51px version. A nebula run through a Zoltan sector is
therefore the cheapest fleet delay available here, cheaper than anything in the event pool.
(per [[source-fandom-rebel-fleet]], [[source-fandom-environmental-hazards]],
[[source-xftl-sector-map]]; see [[concept-rebel-fleet-advance]])

## Event Pool

| Event list | min | max |
|---|---|---|
| `ZOLTAN_CREW_STUDY` | 1 | 1 |
| `STORE_ZOLTAN` | 2 | 2 |
| `NOTHING_ZOLTAN` | 1 | 2 |
| `DISTRESS_BEACON_ZOLTAN` | 1 | 2 |
| `NEBULA_ZOLTAN` | 2 | 6 |
| `HOSTILE_ZOLTAN` | 6 | 8 |
| `BOARDERS_ZOLTAN` | 1 | 2 |
| `ITEM_ZOLTAN` | 1 | 2 |
| `QUESTS_ZOLTAN` | 0 | 1 |
| `NEUTRAL_ZOLTAN` | 5 | 6 |

Start beacon: `START_BEACON_ZOLTAN`. 57 distinct events across the pool.

Fandom prints the same ten lines with the same counts, and — unusually, given its own
warning that the page "does **not** completely reflect the actual order of events in the
game files" — in the **same order** the file uses. (per [[source-fandom-sectors]])

### Placement order {#placement-order}
The table above is a filling queue, not a shopping list. Lines are filled top to bottom,
each rolling its own count inclusive of min and max, and **when the beacons run out
generation stops**. `NEBULA_ZOLTAN` jumps the queue: every `NEBULA_*` list is processed
first because the purple cloud graphics have to be drawn before anything else.
(per [[source-fandom-sectors]])

| Filled | Line | Max consumed above it | Can be cut? |
|---|---|---|---|
| 1st | `NEBULA_ZOLTAN` | 0 | no |
| 2nd | `ZOLTAN_CREW_STUDY` | 6 | no |
| 3rd | `STORE_ZOLTAN` | 7 | no |
| 4th | `NOTHING_ZOLTAN` | 9 | no |
| 5th | `DISTRESS_BEACON_ZOLTAN` | 11 | no |
| 6th | `HOSTILE_ZOLTAN` | 13 | no |
| 7th | `BOARDERS_ZOLTAN` | 21 | no |
| 8th | `ITEM_ZOLTAN` | 23 | one beacon guaranteed, no more |
| 9th | `QUESTS_ZOLTAN` | 25 | **yes** |
| 10th | `NEUTRAL_ZOLTAN` | 26 | **yes** |

Consequences specific to this sector:

- **`ZOLTAN_CREW_STUDY` is safe.** It is filled second, behind at most six cloud beacons,
  so the Crystal-route research facility is placed before anything can crowd it out. This
  is what makes routing through Zoltan space a reliable way to serve step 2 of
  [[chain-crystal-cruiser-unlock]].
- **Both stores are safe** for the same reason, and the guaranteed count of 2 matches
  Fandom's store table exactly.
  (per [[source-fandom-template-stores-number-of-stores-by-sectors]])
- **At the maximum roll everywhere above it**, `ITEM_ZOLTAN` still takes the 24th beacon and
  both lines below it get nothing at all.
- **Leftover beacons do not come back to `NEUTRAL_ZOLTAN`.** The allocation floor is 20, so a
  low roll can leave beacons unassigned; those take the shared `NEUTRAL` list
  (`OVERRIDE_NEUTRAL` under AE), which is generic filler rather than Zoltan content.
  (per [[source-fandom-sectors]])
- **The exit beacon is not in this table** — it draws from the shared `EXIT_LIST`, and an
  exit that a cloud happens to cover is always an empty event.
  (per [[source-fandom-sectors]], [[source-fandom-beacons]])
- **The nebula count is a floor, not a total.** Clouds drawn over ordinary beacons convert
  them, and those beacons draw from the shared `NEBULA` list — events this sector never
  lists. (per [[source-fandom-sectors]])

### Beacon markers
Distress and store markers are drawn on the map only for beacons **within one jump**, so
they are a next-jump signal, not a sector plan. Quest markers, once planted, are visible
from any distance. (per [[source-fandom-beacons]])

- **Distress.** Eight events carry the distress tag, and **all eight are in
  `DISTRESS_BEACON_ZOLTAN`** — this sector has neither of the two mismatches Fandom warns
  about. Nothing leaks a distress marker in from another line, and no event in the distress
  line is missing its tag. (Fandom's own example of the leak is the Engi sector, not this
  one.) So the 1–2 the table promises is what the map shows.
  (per [[source-sector-data-xml]], [[source-fandom-sectors]])
- **Stores.** Beyond the two fixed beacons, [[event-pirate-briber]] and
  [[event-zoltan-trade-hub]] can open a shop. Fandom's additional-stores table lists exactly
  those two for Zoltan sectors, plus Large trade station marked grey as an exit-beacon-only
  possibility — and no trade-station event appears anywhere in this sector's pool.
  (per [[source-fandom-template-stores-additional-stores-from-events-by-sectors]],
  [[source-sector-data-xml]])
- **Crew rarity.** Zoltan 1; Human 2; Engi, Mantis, Rockman and Slug 3 — matching Fandom's
  table for this sector, and governing both store stock and crew-kill rewards.
  (per [[source-sector-data-xml]], [[source-fandom-sectors]],
  [[source-fandom-stores-and-resources]])

### Quests here are doubly unlikely
All four quest-starting events in the pool — [[event-zoltan-trade-hub]],
[[event-encrypted-federation-signal]], [[event-mantis-war-camp]] and
[[event-capture-the-ship]] — sit in `QUESTS_ZOLTAN`. That line rolls **0–1** to begin with,
*and* it is one of the two the queue can drop. Two independent ways to fly an entire Zoltan
sector and never see a quest start.

Marker placement narrows it further. A quest marker cannot be planted on a nebula beacon,
a store, the exit, a distress beacon, a visited beacon, a fleet-overtaken beacon or your
current beacon, and it must be **fewer jumps away than the number of jumps before the
Rebels take it** — so 2–6 cloud beacons in this sector are 2–6 places a marker cannot go.
If nothing qualifies the quest is pushed to the next sector, where it does not count against
that sector's quest allocation. (per [[source-xftl-sector-map]], [[source-fandom-beacons]];
see [[concept-quest-beacon-placement]])

## Chains That Run Through It
- [[chain-crystal-cruiser-unlock]] — the guaranteed `ZOLTAN_CREW_STUDY` beacon is
  **step 2**, the Zoltan research facility that turns the Damaged Stasis Pod into the
  Crystal crew member Ruwen. Guaranteed *and* placed second in the queue, so this sector
  reliably serves that step.
- [[chain-zoltan-primitives]] — starts at [[event-zoltan-trade-hub]], inside the at-risk
  quest line.
- [[chain-hidden-federation-base]] — [[event-encrypted-federation-signal]], same line.
- [[chain-mantis-war-camp]] and [[chain-capture-the-ship]] — same line again.

## Factions & Ships
- [[entity-zoltan]] — dominant faction

## Strategy Notes
- Because `ZOLTAN_CREW_STUDY` is `min=1` **and** near the top of the queue, routing through
  any Zoltan sector guarantees step 2 of [[chain-crystal-cruiser-unlock]] if you are
  carrying the stasis pod.
- Nebula beacons here are worth detouring for on pursuit grounds alone: full 50% advance
  reduction, unlike in a nebula sector. The cost is blind sensors.
  (per [[source-fandom-rebel-fleet]])
- Do not plan a run around a quest starting in this sector. See above.
- **Opinion, not data:** [[source-fandom-sectors]] asserts that sector colour misleads and
  that "Zoltan sectors have many fights and are among the most dangerous", against Engi
  being "very safe". It rests on a single Reddit thread of sector-profit data, is presented
  as reasoning rather than measurement, and no game file ranks sector danger.

> ⚠️ **CONTRADICTION — "among the most dangerous".** The data neither confirms nor refutes the
> ranking, and supports only the Engi half of the comparison. `HOSTILE_ZOLTAN` allocates 6–8
> against Engi's 5–7 (both sectors' own hostile lines, per `sector_data.xml`); this sector
> *also* allocates a 1–2 boarders line that neither Engi sector has, and its 2–6 nebula line
> contains four always-fight events. In total 14 of the 57 events in the pool start a fight on
> arrival. That is more fighting than Engi, not a measured position against every other sector.
> Both claims stand: Fandom's ranking is opinion resting on one Reddit thread; the allocation
> figures are fact. (per [[source-fandom-sectors]], [[source-sector-data-xml]])

## Open Questions
- [x] ~~Does `ZOLTAN_CREW_STUDY` do anything if you arrive without the stasis pod?~~
      **Answered** by the event tree (per [[source-events-zoltan]], `cards/trees/zoltan-research-facility.tree.json`).
      Without the pod there are three ways in: *Participate* rolls a three-entry list where two
      entries are the same polite thank-you and a small scrap reward and the third is a pirate
      ambush — 2 boarders and the `PIRATE_ZOLTAN_CREW_STUDY` ship, which pays a medium standard
      reward destroyed, a high one if you kill the crew, plus a random drone schematic from the
      rescued scientists; *Decline* does nothing at all; and an **Advanced Medbay (level 3)**
      trades your medical records for a random drone schematic and a small reward. See
      [[event-zoltan-research-facility]].
- [ ] Do cloud-converted beacons consume the `NEBULA_ZOLTAN` allocation, or are they extra on
      top of it? [[source-fandom-sectors]] says converted beacons draw from the shared `NEBULA`
      list, which implies extra, but does not say so outright.
- [ ] Is the 19-beacon floor real? [[source-fandom-sectors]] states 19–24, but the grid rule it
      cites bounds only the maximum.
- [ ] Does `OVERRIDE_HOSTILE_ZOLTAN` actually replace `HOSTILE_ZOLTAN`, adding `REBEL_PULSAR`?
      ([[concept-sector-event-allocation]])

## Sources
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-text-sectorname-xml]] (per raw/gamedata/text_sectorname.xml)
- [[source-fandom-sectors]] (per raw/wiki/sectors.md) — generation order, NOTE 1, danger claim
- [[source-xftl-sector-map]] (per raw/modding/2026-08-15-xftl-sector-map.txt) — grid, pursuit
  advance in pixels, `AddQuest` marker filter
- [[source-fandom-beacons]] (per raw/wiki/beacons.md) — marker visibility, quest markers, exits
- [[source-fandom-rebel-fleet]] (per raw/wiki/rebel-fleet.md) — nebula pursuit reduction
- [[source-fandom-environmental-hazards]] (per raw/wiki/environmental-hazards.md)
- [[source-fandom-stores-and-resources]] (per raw/wiki/stores-and-resources.md) — rarity
- [[source-fandom-template-stores-number-of-stores-by-sectors]]
  (per raw/wiki/template-stores-number-of-stores-by-sectors.md) — 2 guaranteed stores
- [[source-fandom-template-stores-additional-stores-from-events-by-sectors]]
  (per raw/wiki/template-stores-additional-stores-from-events-by-sectors.md)
