---
id: sector-abandoned-sector
type: sector
sector_id: LANIUS_SECTOR
sector_class: hostile
faction: [[[entity-lanius]]]
min_sector: 1
unique: false
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-16
sources: 12
tags: [advanced-edition, lanius, hazard]
---

# Abandoned Sector

## Summary
The Lanius sector, added in Advanced Edition. Display name is "Abandoned Sector" but its
in-game id is `LANIUS_SECTOR`. It can repeat within a run and has no minimum sector depth
(per [[source-sector-data-xml]]). Fandom groups it with the **hostile (red)** sectors and
tags the whole section as Advanced Edition Content
([[source-fandom-sectors]], per raw/wiki/sectors.md).

> Naming trap: there is a **separate, distinct** `ABANDONED_SECTOR` entry in
> `sector_data.xml` which is *not* this sector — see [[sector-vestigial-definitions]].

> This page previously carried `sector_class: special`, which was our own classification
> rather than a sourced one. Changed to `hostile` to match Fandom's grouping. Recording the
> earlier value rather than deleting it.

### Version
The draw lists settle it without needing a source that *says* so: `LANIUS_SECTOR` is in
`<sectorType name="OVERRIDE_HOSTILE">` and **not** in `<sectorType name="HOSTILE">`, the
only difference between those two lists ([[source-sector-data-xml]]). With the DLC off the
map has no list that can roll this sector at all. That is the same `OVERRIDE_X` substitution
[[concept-sector-event-allocation]] resolves for event lists, applied to sector selection.

Both sources that discuss the sector directly call it Advanced Edition content:
[[source-fandom-sectors]] flags the section with the AE banner, and
[[source-fandom-ftl-advanced-edition]] (per raw/wiki/ftl-advanced-edition.md) records
Subset's own announcement of "a new sector and events" and "a new race … closely tied to
the new sector, which has been tentatively named the 'Abandoned Sector'" — the Lanius.
Corroborating detail: the sector's guaranteed hazard line can produce a **pulsar**, and
"you can encounter a pulsar only if you play with Advanced Edition content on"
([[source-fandom-environmental-hazards]], per raw/wiki/environmental-hazards.md).

Caveat worth keeping: [[source-fandom-ftl-advanced-edition]] also notes that *some* AE
events can be met with AE content disabled. No source in `raw/` states what happens to
this **sector** with AE content off; the AE banner is the strongest claim we hold.

## Character & Hazards
Carries `HOSTILE_ENVIRONMENT_LANIUS` (1–2), which is the only environmental-hazard line
allocated by any non-nebula sector in `sector_data.xml` — the only comparable line is
`STORM_SLUG` in the Slug nebulas. It resolves to three events
(per `sectors/data/abandoned-sector.sector.json`, built from [[source-sector-data-xml]] and
the event trees):

| Event | Environment | Mechanic (per [[source-fandom-environmental-hazards]]) |
|---|---|---|
| `LANIUS_FIGHT_ASTEROID` — [[event-lanius-fight-in-asteroid-field]] | asteroid field | Periodic asteroids: 1 shield layer or 1 hull+system damage, small chance of fire/breach. Frequency scales with **your own** shield system level. |
| `LANIUS_FIGHT_PULSAR` — [[event-lanius-fight-near-pulsar]] | pulsar | Ion pulse every 11–18s ionising 2 systems on each ship; damage = 1 + 0.5×(system power), rounded down. Shields are always one of the two if powered. **AE-only hazard.** |
| `LANIUS_NOBOARDERS_PDS` — [[event-lanius-fight-with-friendly-asb-support]] | ASB (PDS), targeting the **enemy** | The battery fires at the Lanius, not at you; the tree can return 8 hull repaired afterwards. |

Asteroid fields and pulsars impose permanent **IN DANGER** status while you remain at the
beacon, which blocks ship/reactor upgrades, the cargo bay, and crew management
([[source-fandom-environmental-hazards]]). The same source lists enemy ASBs as imposing it;
it says nothing about a *friendly* ASB, so `LANIUS_NOBOARDERS_PDS` is unknown on that point.

> ⚠️ **CORRECTION (superseded claim):** this page previously said
> `HOSTILE_ENVIRONMENT_LANIUS` was probably about **oxygen drain** (marked unsourced at the
> time). It is not — the line is weather. Recorded here rather than silently removed.

> ⚠️ **CORRECTION (superseded claim):** this page previously said `ITEM_LANIUS` 2–4 was
> "the heaviest item allocation in the game". It is not. Both Engi sectors allocate
> `ITEMS` 2–2 **plus** `ITEMS_ENGI` 3–3 = 5 fixed item beacons; the Abandoned Sector's 2–4
> is second, and the largest single item line (per [[source-sector-data-xml]]).

**No nebula line at all.** The sector allocates no `NEBULA_*` entry, so no cloud graphics
are drawn: sensors work at every beacon, no beacon can be converted to a nebula beacon, and
there is no beacon that halves the Rebel fleet's advance for a turn
([[source-fandom-rebel-fleet]], per raw/wiki/rebel-fleet.md). Fleet delay here comes only
from events — `LANIUS_AUTO_REBEL`, `LANIUS_GROUP_AUTO` and `PIRATE_BRIBER` each carry
`modifyPursuit` −1.

## Event Pool

The entries below are in **`sector_data.xml` file order, which is placement order**: the
generator fills each line completely, in order, and stops when the map's beacons run out
([[source-fandom-sectors]]; [[source-xftl-sector-map]]). Lines near the top are effectively
guaranteed; lines near the bottom are a wish list.

| # | Event list | min | max | Slots used before it (min–max) |
|---|---|---|---|---|
| 1 | `STORE_LANIUS` | 2 | 2 | 0–0 |
| 2 | `NOTHING_LANIUS` | 1 | 2 | 2–2 |
| 3 | `DISTRESS_BEACON_LANIUS` | 1 | 2 | 3–4 |
| 4 | `HOSTILE_LANIUS` | 5 | 6 | 4–6 |
| 5 | `HOSTILE_ENVIRONMENT_LANIUS` | 1 | 2 | 9–12 |
| 6 | `BOARDERS_LANIUS` | 1 | 2 | 10–14 |
| 7 | `ITEM_LANIUS` | 2 | 4 | 11–16 |
| 8 | `QUESTS_LANIUS` | 0 | 1 | 13–20 |
| 9 | `NEUTRAL_LANIUS` | 5 | 6 | 13–21 |

Start beacon: `START_BEACON_LANIUS`. The **exit beacon is not in this table** — it draws
from the shared `EXIT_LIST` ([[source-fandom-sectors]]). Beacons still empty when the table
is exhausted are filled from `NEUTRAL`, replaced by `OVERRIDE_NEUTRAL` under AE
(same source; whether the override actually substitutes is still open —
[[concept-sector-event-allocation]]).

**Allocation is not map size.** The table asks for **18–27 slots**; the map holds **at most
24 beacons**. At the maximum roll the only line that can be trimmed is the last one,
`NEUTRAL_LANIUS`, because everything above it fits inside 24 even at its own maxima (21).
No line in this sector can be cut out entirely — which is not true of every sector.

Fandom's own beacon listing for this sector matches the file exactly, both in figures and in
order (2 stores / 1–2 empty / 1–2 distress / 5–6 hostile / 1–2 hostile environment / 1–2
boarders / 2–4 various items / 0–1 quests / 5–6 neutral), even though the page warns in
general that its listings do "**not** completely reflect the actual order of events in the
game files" ([[source-fandom-sectors]]).

### Beacon markers
`<distressBeacon/>` and `<store/>` on an event are what put a marker on the sector map, and
markers are only drawn for beacons within 1 jump ([[source-fandom-beacons]], per
raw/wiki/beacons.md).

- **Distress markers match the allocation exactly here.** All twelve distress-tagged events
  in the sector's pool belong to `DISTRESS_BEACON_LANIUS`, and every event in that list
  carries the tag — no leakage in either direction. [[source-fandom-sectors]] NOTE 1 warns
  that other sectors show *more* distress beacons than their distress line allocates (its
  worked example is Engi); the Abandoned Sector is the clean case. The twelve names are
  confirmed independently by
  [[source-fandom-template-distress-events-by-sectors]], whose Abandoned column lists the
  same twelve.
- **Store markers exceed the two guaranteed stores.** Besides `STORE_LANIUS`,
  `LANIUS_SCARED_CIVILIAN` ([[event-lanius-lone-ship]]) and `PIRATE_BRIBER`
  ([[event-pirate-briber]]) both carry `<store/>`, and both are allocated from
  `NEUTRAL_LANIUS` — the last line. This matches
  [[source-fandom-template-stores-additional-stores-from-events-by-sectors]], which lists
  exactly those two for the Abandoned column (plus [[event-large-trade-station]], marked as
  an exit-beacon-only occurrence here).
- **Guaranteed store count is 2**, agreeing with
  [[source-fandom-template-stores-number-of-stores-by-sectors]] and with
  [[source-sector-data-xml]] (`STORE_LANIUS` min = max = 2).
- **Long-Ranged Scanners** adds a hazard reading and a possible-ship reading for adjacent
  beacons only ([[source-fandom-beacons]]). Per
  [[source-fandom-template-distress-events-by-sectors]], four of the twelve distress events
  here read as "possible ship detected" — [[event-lanius-ship-attacking-civilian-distress]],
  [[event-lanius-fight-distress]], [[event-pirate-ship-distress-trap]] and
  [[event-friendly-ship-out-of-fuel]] — and two of those four (`LANIUS_DISTRESS_TRAP`,
  `TRAP_BEACON`) open in combat. The other eight read as a plain unvisited location.

### Quest markers
`QUESTS_LANIUS` is allocated 0–1, so a run can cross the sector without one. When a marker
is planted, [[source-xftl-sector-map]] gives the engine's candidate filter: the target
beacon must be unvisited, not a nebula beacon, not the exit, not fleet-overtaken, not
already a quest, not a store, not a distress beacon, not the player's current beacon, and
reachable — and it must be fewer jumps away than the number of jumps before the Rebels take
it. With no nebula in this sector, the practical exclusions here are the two stores, the
one or two distress beacons and the exit.

## Chains That Run Through It
- The Hidden Federation Base quest, started by `FEDERATION_PLANET_SIGNAL`
  ([[event-encrypted-federation-signal]]) — the only quest start in the sector's pool
  (`quest_start_events` = 1). Targets `HIDDEN_FEDERATION_BASE_LIST` and
  `FEDERATION_BASE_ASSIST`.
- No ship unlocks here (`unlock_ships` is empty).

## Factions & Ships
- [[entity-lanius]] — dominant faction. Only two of the six `HOSTILE_LANIUS` events are
  Lanius hulls; the rest are Rebel, pirate and auto-ship fights.

## Crew In Stores
Rarity from `sector_data.xml` (lower = more common), and it matches Fandom's table for this
sector exactly ([[source-fandom-sectors]]):

| Rarity | Races |
|---|---|
| 2 | Lanius (`anaerobic`), Human |
| 3 | Engi, Mantis, Rockman |
| 4 | Zoltan, Slug |

This is the **only** sector where Lanius crew can be bought or won —
"Lanius crewmembers are only encountered in Abandoned sectors"
([[source-fandom-stores-and-resources]], per raw/wiki/stores-and-resources.md). That source
also notes AE-specific store behaviour that applies here: stores gained a second page in AE,
and with AE content **off** a bug frequently leaves store slots empty.

## Strategy Notes
- Two guaranteed stores, and they are the first line placed, so they survive any crowding of
  the map (derived from placement order, [[source-fandom-sectors]]).
- The hazard line is placed fifth of nine and its predecessors use at most 12 slots, so it
  always places: expect one or two IN DANGER beacons per visit
  ([[source-fandom-environmental-hazards]] for the effect).
- Fandom's own framing: colour-coding is a poor guide to danger — "it's best to choose your
  next sector based on an understanding of that specific sector, rather than just looking at
  its colour" ([[source-fandom-sectors]]). *Marked as opinion; the page cites reasoning and
  a Reddit thread, not measured data.*

## Contradictions

> ⚠️ **CONTRADICTION — how many beacons a sector actually has.**
> [[source-fandom-sectors]] opens by stating every sector contains "between 19 and 24
> beacons" (per raw/wiki/sectors.md). The generation description on that same page, and
> [[source-xftl-sector-map]] which it cites, describe only a 6×4 grid with an 80% chance per
> cell plus a guard against too many empty cells — that yields a **ceiling of 24 and no
> stated floor**. `sectors/data/abandoned-sector.sector.json` and the generated sector page
> therefore use 24 as the ceiling and claim no minimum. Both readings are recorded: 19 is
> Fandom's figure and nothing else in `raw/` supports it. Neither figure is in the game
> files at all.

> ⚠️ **CONTRADICTION — allocation vs. what you see.** The `min`/`max` figures above are the
> *allocation request*, not the number of beacons of that type on the map.
> [[source-fandom-sectors]] NOTE 1 says so explicitly about the very numbers it prints:
> "the count and type of Beacons in the sector descriptions are taken straight from the game
> files and can be misleading". Both are true of different things — the XML gives the
> allocation, NOTE 1 describes the realisation. Reliability: the XML is `high`, the
> realisation rules are `medium` and second-hand.

## Open Questions
- [x] ~~What `HOSTILE_ENVIRONMENT_LANIUS` covers~~ — answered: asteroid field, pulsar, and a
  friendly planetary ASB. Not oxygen. (per the sector data + [[source-fandom-environmental-hazards]])
- [x] ~~Whether this sector requires the AE DLC to be enabled~~ — both Fandom pages classify
  it as Advanced Edition Content, and its hazard line contains an AE-gated hazard. See
  **Version** above for the residual caveat.
- [ ] Does a **friendly** ASB (`LANIUS_NOBOARDERS_PDS`) impose IN DANGER? The hazards page
  names only enemy ASBs.
- [ ] Does `OVERRIDE_NEUTRAL` actually replace `NEUTRAL` as the fallback list under AE, and
  do the `OVERRIDE_*` twins substitute for this sector's lists at all?
  ([[concept-sector-event-allocation]])
- [ ] Is `unique="true"` scoped per sector or per run? ([[concept-event-uniqueness]])
- [ ] What is the actual floor on beacon count — see the contradiction above.

## Sources
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-text-sectorname-xml]] (per raw/gamedata/text_sectorname.xml)
- [[source-fandom-sectors]] (per raw/wiki/sectors.md)
- [[source-fandom-environmental-hazards]] (per raw/wiki/environmental-hazards.md)
- [[source-fandom-beacons]] (per raw/wiki/beacons.md)
- [[source-fandom-rebel-fleet]] (per raw/wiki/rebel-fleet.md)
- [[source-fandom-stores-and-resources]] (per raw/wiki/stores-and-resources.md)
- [[source-fandom-ftl-advanced-edition]] (per raw/wiki/ftl-advanced-edition.md)
- [[source-fandom-template-stores-number-of-stores-by-sectors]]
  (per raw/wiki/template-stores-number-of-stores-by-sectors.md)
- [[source-fandom-template-stores-additional-stores-from-events-by-sectors]]
  (per raw/wiki/template-stores-additional-stores-from-events-by-sectors.md)
- [[source-fandom-template-distress-events-by-sectors]]
  (per raw/wiki/template-distress-events-by-sectors.md)
- [[source-xftl-sector-map]] (per raw/modding/2026-08-15-xftl-sector-map.txt)
