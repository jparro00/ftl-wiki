---
id: sector-slug-home-nebula
type: sector
sector_id: SLUG_HOME
sector_class: nebula
faction: [[[entity-slugs]]]
min_sector: 3
unique: true
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-15
sources: 13
tags: [nebula, homeworld, ship-unlock, map-generation]
---

# Slug Home Nebula

## Summary
Unique Slug home sector — the largest event pool in the game at 12 allocation lines.
[[sector-slug-controlled-nebula]]'s table plus a guaranteed `NEBULA_SLUG_FIGHT_UNLOCK`
beacon, which is the [[chain-slug-cruiser-unlock]] start.

It is also the most extreme placement case in the game: the table allocates **19–35 slots
against a map of at most 24 beacons**, so roughly a third of what it asks for cannot be
placed. Because every `NEBULA_*` list is filled first, the shortfall lands entirely on the
clear-space half of the table (per [[source-fandom-sectors]], [[source-xftl-sector-map]]).

## Character & Hazards
`unique="true"`, `minSector="3"` (per [[source-sector-data-xml]]).

**`minSector` counts from zero.** [[source-fandom-sectors]] states this sector "can occur
only once per game and only at sector **4** or higher". That is consistent across the whole
file — `ENGI_HOME` is `minSector="2"` and Fandom says sector 3+, `ROCK_HOME` is
`minSector="4"` and Fandom says 5+ — so the player-facing floor here is **sector 4**, and
the last sector it can appear in is 7 (sector 8 is always `FINAL`).

Environment, and what it costs:

| Effect | Detail | Source |
|---|---|---|
| Sensors dead at cloud beacons | No enemy rooms, crew, or weapon-charge bars; the system is present but non-functional | [[source-fandom-sensors]], [[source-fandom-environmental-hazards]] |
| Sensor workarounds | [[item-slug-crew]] telepathy and [[item-lifeform-scanner]] show enemy crew regardless | [[source-fandom-environmental-hazards]] |
| Fleet pursuit | A nebula beacon in a **nebula sector** advances the fleet 51px vs 64px normal — a ~20% reduction, not the 50% (32px) the same beacon buys in a non-nebula sector | [[source-xftl-sector-map]] |
| Plasma/ion storms | Reactor halved (rounded up); Zoltan power and [[item-backup-battery]] unaffected; the enemy reactor is halved too | [[source-fandom-environmental-hazards]] |
| Fleet overtake | Any nebula beacon the Rebels take **always** becomes an ion storm (nebula exit beacons excepted) | [[source-fandom-rebel-fleet]] |
| Anti-ship batteries | Never present at a nebula beacon — unless you are **waiting** there out of fuel, which removes the nebula environment and adds an ASB | [[source-fandom-rebel-fleet]], [[source-fandom-environmental-hazards]] |

> ⚠️ **CONTRADICTION — how much a nebula beacon slows the fleet here.** Three wordings:
> [[source-fandom-environmental-hazards]] says visiting a nebula beacon in a nebula sector
> slows the fleet "by only 20% instead of the regular 50%" (reduce *by* 20%);
> [[source-fandom-rebel-fleet]] says it "reduces the Rebel advance rate only partially (by
> 1/5 of regular beacon advance rate)", which reads the same way but is easy to misread as
> reduce-*to*-20%; [[concept-nebula-mechanics]] separately records a community figure of
> "80% of normal pursuit". [[source-xftl-sector-map]] settles the arithmetic from the
> binary — **64px normal, 51px nebula-in-nebula-sector, 32px nebula-in-normal-sector** —
> which makes Environmental Hazards' phrasing the correct one and Rebel Fleet's merely
> badly worded. All three kept; the pixel figures are the ones to bet on, and they are
> still one person's disassembly, not a game file.

**Storm beacons are not cloud beacons.** `STORM_SLUG` is the one hazard line in the table
whose name does not start `NEBULA_`, so by the developers' own prefix rule those beacons
are not generated as nebulae ([[concept-nebula-mechanics]], [[source-events-slug]]). They
carry `<environment type="storm"/>` from the event instead: half reactor, and none of the
nebula fleet discount. Fandom reports exactly that from play.

## How the map is built here

The generation rules below are community reverse-engineering, not game files
([[source-fandom-sectors]] citing [[source-xftl-sector-map]]).

1. **Beacons are placed first** — a 6×4 grid, each cell 80% likely to hold a beacon, with a
   guard against too many empty cells. **At most 24.** [[source-fandom-sectors]] opens by
   stating sectors hold "between 19 and 24 beacons"; [[source-xftl-sector-map]] describes
   the count as *bounded, not fixed*, and states no floor. Nothing in `raw/gamedata/`
   corroborates either figure.
2. **The five `NEBULA_*` lines are filled first, out of file order**, because the cloud
   graphics must be drawn before anything else. Here that is `NEBULA_SLUG_FIGHT_UNLOCK`,
   `NEBULA_STORE_SLUG`, `NEBULA_NOTHING_SLUG`, `NEBULA_HOSTILE_SLUG` and
   `NEBULA_NEUTRAL_SLUG` — 13–19 of the 24 beacons before the rest of the table starts.
3. **Clouds that overlap ordinary beacons convert them**, and those beacons draw from the
   shared `NEBULA` list, which this sector's table never names.
4. **The remaining lines fill in file order until the beacons run out**, at which point
   generation stops. Four lines can be cut entirely if everything above them rolls high:
   `HOSTILE_SLUG`, `DISTRESS_BEACON_SLUG`, `STORM_SLUG` and `NEUTRAL`
   (per `sectors/data/slug-home-nebula.sector.json`, derived from the 24-beacon ceiling).
5. **Leftover beacons fall back to `NEUTRAL`** (`OVERRIDE_NEUTRAL` under AE — whether the
   engine substitutes it is unresolved, [[concept-sector-event-allocation]]). This sector
   is unusual in that `NEUTRAL` is *also* its last allocation line, so the same list can be
   reached two ways — though never in the same run, since leftovers exist only when the map
   is not full and the line is starved only when it is.
6. **The exit beacon is not in the table** — it draws from the shared `EXIT_LIST`, and an
   exit inside cloud graphics is always an empty event ([[source-fandom-sectors]]).

## Event Pool

File order, with the order the game actually fills them:

| # filled | Event list | min | max | Note |
|---|---|---|---|---|
| 1 | `NEBULA_SLUG_FIGHT_UNLOCK` | 1 | 1 | nebula-first; the ship unlock |
| 6 | `STORE` | 0 | 1 | |
| 2 | `NEBULA_STORE_SLUG` | 2 | 2 | nebula-first |
| 7 | `ITEMS` | 0 | 2 | |
| 8 | `NOTHING_SLUG` | 0 | 2 | |
| 9 | `HOSTILE_SLUG` | 1 | 2 | can be cut entirely |
| 10 | `DISTRESS_BEACON_SLUG` | 3 | 4 | can be cut entirely |
| 3 | `NEBULA_NOTHING_SLUG` | 2 | 4 | nebula-first |
| 4 | `NEBULA_HOSTILE_SLUG` | 5 | 7 | nebula-first |
| 11 | `STORM_SLUG` | 1 | 3 | can be cut entirely |
| 5 | `NEBULA_NEUTRAL_SLUG` | 3 | 5 | nebula-first |
| 12 | `NEUTRAL` | 1 | 2 | can be cut entirely; also the fallback list |

Start beacon: `START_BEACON_SLUG`. Totals: 19–35 allocated slots
(per [[source-sector-data-xml]]; fill order per [[source-fandom-sectors]]).

> The allocation range is **not** the number of stops. The map holds at most 24 beacons and
> discards the rest — [[source-fandom-sectors]]' own NOTE 1 warns that the counts it prints
> "are taken straight from the game files and can be misleading".

## Beacon markers — what the map advertises

Distress and store markers are drawn only on beacons **adjacent** to your position; exit
and quest markers show from any distance ([[source-fandom-beacons]]).

**Distress.** Five events in the pool carry the distress tag: `REFUGEE_DISTRESS_SLUG`,
`SLUG_DISTRESS_MANTIS`, `SLUG_DISTRESS_QUESTION`, `SLUG_DISTRESS_ROCK` and `TRAP_BEACON`.
All five come from `DISTRESS_BEACON_SLUG`; **nothing outside that line carries the tag**, so
this sector cannot show the extra distress beacons [[source-fandom-sectors]] describes for
Engi space. The reverse mismatch does occur: `PIRATE_CIVILIAN_BEACON`,
`SLUG_DISTRESS_RESCUE` and `SLUG_DISTRESS_TRICK` are allocated from the distress list but
carry no tag and never show the marker — Fandom calls this class of case a mistake in the
data.

[[source-fandom-template-distress-events-by-sectors]] independently lists exactly those five
for "Slug Nebulas", which is a clean confirmation of the derived set. It also gives the
Long-Ranged Scanners reading for each: only `TRAP_BEACON` shows "possible ship detected";
the other four show a plain unvisited-location diamond. LRS never names the event, and
[[source-fandom-beacons]] warns its ship reading is not always accurate.

**Stores.** Guaranteed stores are `STORE` 0–1 plus `NEBULA_STORE_SLUG` 2 — which is
precisely how [[source-fandom-template-stores-number-of-stores-by-sectors]] scores this
sector (**0–1 stores + 2 nebula stores**). The two nebula stores are filled before the table
can run dry, so they are the reliable pair; the third is a coin flip in its own roll rather
than a casualty of the squeeze. Beyond those,
[[source-fandom-template-stores-additional-stores-from-events-by-sectors]] lists four
store-opening events for Slug Nebulas: **Large trade station** (AE `OVERRIDE_ITEMS` only),
**Pirate briber**, **Slug drink**, and **"Slug transport with military escort"**. The pool
also produces [[event-slug-store-ship]] (`NEBULA_SLUG_FAKE_STORE`), whose shop sits behind
an ambush. See [[concept-stores]].

## Chains That Run Through It
- [[chain-slug-cruiser-unlock]] — starts at the guaranteed
  [[event-slug-home-nebula-surrender]] beacon. **Confirmed** as the Slug Cruiser unlock by
  [[source-fandom-slug-home-nebula-surrender]]; the earlier inference from the event id is
  now sourced.
- [[chain-slug-pirate-trap]] — starts at `QUEST_SLUG_PIRATE_TRAP` in `NEBULA_NEUTRAL_SLUG`.
- `NEBULA_BATTLEFIELD` plants the `SECRET_WORD_ABADOTH` marker.

**Quest markers are hard to place in this sector.** [[source-xftl-sector-map]] gives the
`AddQuest` candidate filter in full: a beacon is eligible only if it is unvisited, **not a
nebula beacon**, not the exit, not fleet-overtaken, not already a quest, not a store, not a
distress beacon, not your current beacon, and reachable — and it must be fewer jumps away
than the number of jumps before the Rebels take it. In a sector this heavily clouded the
legal set is small. An unplaceable quest is deferred to the next sector, except from sector
7 onward, where it is not carried at all.

[[source-fandom-slug-home-nebula-surrender]] resolves how the unlock chain survives that
rule: *"this event occurs at a regular quest marker beacon, but when you arrive there will
be a nebula environment"* — the marker lands on a clear beacon and the nebula comes from
the event's own `<environment type="nebula"/>`.

> ⚠️ **CONTRADICTION — where a quest marker may go.** [[source-fandom-beacons]] says a
> marker overwrites any event "unless it is a store, exit, or another quest marker" and
> that markers "cannot appear in nebula **area**". [[source-xftl-sector-map]] gives a
> longer filter that also excludes visited, fleet-taken, distress and current beacons, and
> makes the nebula exclusion **per beacon**, not per area. Fandom itself carries
> `@to-do: test and verify` on this claim. The engine list is the better bet; both are kept
> here and in [[concept-quest-beacon-placement]].

## Factions & Ships
- [[entity-slugs]] — dominant faction
- Crew rarity (store assortment and crew-kill rewards): Slug 2, Human 2, Engi 4, Mantis 4,
  Zoltan 4, Rockman 4 (per [[source-sector-data-xml]]; [[source-fandom-sectors]] lists the
  same tiers as "2: Slug, Human / 4: Engi, Mantis, Zoltan, Rockmen").

## Strategy Notes
- **The nebula half is what you actually get.** 13–19 of at most 24 beacons are spoken for
  before the clear-space lines are touched, so plan for cloud encounters, blind sensors and
  the hacker family rather than for the table's bottom four lines.
- **The fleet discount is worse at home than abroad.** ~20% per nebula jump here versus 50%
  for the same beacon in a non-nebula sector ([[source-xftl-sector-map]]) — the purple
  colour does not buy the breathing room it buys elsewhere.
- **A plasma-storm beacon is a trap**: half reactor and no fleet discount
  ([[concept-nebula-mechanics]]). This is one of the four lines the map can starve, and the
  only one whose loss is an improvement.
- **Bring a Slug or a Lifeform Scanner.** Both are written specifically to defeat the
  sensor blackout ([[concept-nebula-mechanics]], [[concept-blue-options]]); Hacking counters
  the four remote-hack fights.
- _Opinion, unsourced:_ [[source-fandom-sectors]] argues sector colour is a poor guide to
  danger and that players should route on sector knowledge instead. It offers no measured
  data for the nebula sectors specifically.

## Related
- [[sector-slug-controlled-nebula]] — the same table minus the unlock beacon, `unique="false"`
- [[sector-uncharted-nebula]] — the other wall-to-wall nebula sector
- [[concept-nebula-mechanics]] · [[concept-rebel-fleet-advance]] ·
  [[concept-quest-beacon-placement]] · [[concept-sector-event-allocation]] ·
  [[concept-stores]] · [[concept-blue-options]]

## Open Questions
- [x] ~~Confirm `NEBULA_SLUG_FIGHT_UNLOCK` is the Slug Cruiser unlock.~~ Confirmed by
      [[source-fandom-slug-home-nebula-surrender]].
- [ ] Do `req="sensors"` blue options still appear at a cloud beacon, where the system is
      installed but non-functional? The unlock chain's Sensors 2 branch reads as though it
      does (*"You overclock your sensors, trying to get them to function in the clouds"*),
      but nothing states the general rule ([[concept-nebula-mechanics]]).
- [ ] How often does the squeeze actually bite? `at_risk` is a possibility derived from
      every line above rolling its maximum, not a measured frequency; no source gives the
      distribution.
- [ ] Is Fandom's **"Slug transport with military escort"** the same event as
      [[event-slug-store-ship]] (`NEBULA_SLUG_FAKE_STORE`)? The intro text on the Slug store
      ship page describes a Slug transport with a military escort, but this repo holds no
      page under that title to check.
- [ ] Does the beacon floor of 19 in [[source-fandom-sectors]] hold? Its own citation
      ([[source-xftl-sector-map]]) states only a bounded count with an empty-cell guard.

## Sources
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml) — allocation table, `minSector`, `unique`, rarity, start beacon
- [[source-text-sectorname-xml]] (per raw/gamedata/text_sectorname.xml) — display name
- [[source-fandom-sectors]] (per raw/wiki/sectors.md) — generation order, nebula-first rule, fallback, exit list, NOTE 1
- [[source-xftl-sector-map]] (per raw/modding/2026-08-15-xftl-sector-map.txt) — 6×4 grid, `AddQuest` filter, fleet advance in pixels
- [[source-fandom-beacons]] (per raw/wiki/beacons.md) — marker visibility, quest marker rules
- [[source-fandom-environmental-hazards]] (per raw/wiki/environmental-hazards.md) — nebula, storm, ASB
- [[source-fandom-sensors]] (per raw/wiki/sensors.md) — what each sensor level shows, and the nebula blackout
- [[source-fandom-rebel-fleet]] (per raw/wiki/rebel-fleet.md) — pursuit rates, overtake behaviour
- [[source-fandom-stores-and-resources]] (per raw/wiki/stores-and-resources.md) — store availability
- [[source-fandom-template-stores-number-of-stores-by-sectors]] (per raw/wiki/template-stores-number-of-stores-by-sectors.md) — 0–1 stores + 2 nebula stores
- [[source-fandom-template-stores-additional-stores-from-events-by-sectors]] (per raw/wiki/template-stores-additional-stores-from-events-by-sectors.md) — store-opening events
- [[source-fandom-template-distress-events-by-sectors]] (per raw/wiki/template-distress-events-by-sectors.md) — the five distress-marked events and their LRS readings
- [[source-fandom-slug-home-nebula-surrender]] (per raw/wiki/slug-home-nebula-surrender.md) — the unlock chain and its quest-marker note
