---
id: sector-slug-controlled-nebula
type: sector
sector_id: SLUG_SECTOR
sector_class: nebula
faction: [[[entity-slugs]]]
min_sector: 3
unique: false
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-15
sources: 14
tags: [nebula]
---

# Slug Controlled Nebula

## Summary
Slug space, and a nebula sector throughout. The widest event pool in the game at 11
lists, including a dedicated ion-storm list. Its table asks for **18–34 beacons against a
map that holds at most 24**, so the bottom of that table is a wish list rather than a
promise — and because every `NEBULA_*` line is placed *first*, the lines that get cut are
the ones a player would most want (distress, storms, and the generic neutral pool).

## Character & Hazards

### When it can appear
`minSector="3"` — the deepest floor of any non-unique sector, so it cannot appear early.
`unique="false"`, so it can repeat within a run. (per [[source-sector-data-xml]])

> ⚠️ **CONTRADICTION:** [[source-sector-data-xml]] gives `minSector="3"`; the community
> wiki says this sector occurs "only at sector **4** or higher"
> ([[source-fandom-sectors]], per `raw/wiki/sectors.md`).
> **Likely resolution — not an error but a zero-indexed field.** The same +1 offset holds
> across every sector where both sources state a floor: `ENGI_HOME` 2 / "sector 3",
> `MANTIS_HOME` 2 / "sector 3", `ZOLTAN_HOME` 2 / "sector 3", `ROCK_HOME` 4 / "sector 5",
> `REBEL_SECTOR_MINIBOSS` 4 / "sector 5", and `FINAL` 7 for the eighth sector
> (per `raw/gamedata/sector_data.xml`). Read as "sector `minSector + 1` at the earliest",
> i.e. **sector 4** here. Both values are kept above: the frontmatter carries the file's
> literal `3`.

### How the map is actually filled
The allocation table is a **queue, not a shopping list**. Beacons are placed first — a 6×4
grid with an 80% chance per cell, so **at most 24** — and the sector's lines are then filled
in order until the beacons run out, at which point generation stops
([[source-fandom-sectors]]; [[source-xftl-sector-map]], per
`raw/modding/2026-08-15-xftl-sector-map.txt`).

Three consequences specific to this sector:

1. **The four `NEBULA_*` lines are processed before everything else**, out of file order,
   because the purple cloud graphics have to be drawn first. That is
   `NEBULA_STORE_SLUG` (2), `NEBULA_NOTHING_SLUG` (2–4), `NEBULA_HOSTILE_SLUG` (5–7) and
   `NEBULA_NEUTRAL_SLUG` (3–5) — **12–18 of at most 24 beacons committed before the file's
   first line is read**. Both guaranteed nebula stores are therefore never squeezed out.
2. **Three lines are at risk of being cut entirely** if everything above rolls high:
   `DISTRESS_BEACON_SLUG`, `STORM_SLUG` and `NEUTRAL`. `STORM_SLUG` is the notable one — it
   is a cloud environment whose list name does not begin `NEBULA_`, so it is *not* promoted
   to the front and sits tenth of eleven.
3. **`NEUTRAL` is both the last line and the fallback.** Beacons still empty when the table
   ends are filled from `NEUTRAL` (`OVERRIDE_NEUTRAL` under AE), so it is the one list that
   can be handed far more than its 1–2 allocation — or nothing at all.
   ([[source-fandom-sectors]])

A cloud drawn over an ordinary beacon converts it, and that beacon draws from the **shared
`NEBULA` list**, which this sector's table never names — so some encounters here come from
a pool no sector definition lists. ([[source-fandom-sectors]])

The **exit beacon is not in the table**; it draws from the shared `EXIT_LIST`, and an exit
that lands under cloud graphics is always an empty event.
([[source-fandom-sectors]], [[source-fandom-beacons]])

### Nebula environment — where the sensors go
A nebula disables Sensors outright. **Slug crew or a Lifeform Scanner still reveal enemy
crew**, which is why a Slug aboard is worth more here than the blue-option count suggests
([[source-fandom-sensors]], [[source-fandom-environmental-hazards]]).

The environment is a property of the **event**, not of the beacon: the `NEBULA_*` list name
draws the cloud graphic, but an `<environment type="nebula"/>` tag on any event puts you in
a nebula wherever it lands. In this sector that is not theoretical — **four of the eight
`DISTRESS_BEACON_SLUG` events carry the nebula tag** ([[source-events-slug]]):

| Distress event | Nebula environment? | Distress marker? |
|---|---|---|
| [[event-slug-ship-boarding-rock-ship]] `SLUG_DISTRESS_ROCK` | yes | yes |
| [[event-slug-moons-question]] `SLUG_DISTRESS_QUESTION` | yes | yes |
| [[event-slug-oxygen-malfunction]] `SLUG_DISTRESS_TRICK` | yes | **no** |
| [[event-slocknog]] `SLUG_DISTRESS_RESCUE` | yes | **no** |
| [[event-mantis-ship-attacking-slug-ship]] `SLUG_DISTRESS_MANTIS` | no | yes |
| [[event-refugee-distress-slug]] `REFUGEE_DISTRESS_SLUG` | no | yes |
| [[event-pirate-ship-attacking-civilian-distress]] `PIRATE_CIVILIAN_BEACON` | no | **no** |
| [[event-pirate-ship-distress-trap]] `TRAP_BEACON` | no | yes |

So the distress line is the one place here where you can jump to a beacon the map did not
draw as a cloud and arrive with your sensors dead — exactly the confusion
[[source-fandom-sectors]] describes. Every event inside the four `NEBULA_*` lists carries
the tag as well; 25 of the sector's 71 pool events are nebula, 3 more are storms.

### Plasma / ion storms
`STORM_SLUG` (1–3) is unique to the two Slug sectors. A storm **halves your reactor,
rounded up**, and power is stripped off systems automatically as you arrive — shields can
be down before a shot is fired. Zoltan power and the Backup Battery are unaffected, and the
**enemy reactor is halved too**. ([[source-fandom-environmental-hazards]])

### The Rebel fleet — nebula cover is worth less at home
Visiting a nebula beacon slows the fleet by 50% in an ordinary sector but only **20% inside
a nebula sector** ([[source-fandom-sectors]], [[source-fandom-environmental-hazards]]).
[[source-xftl-sector-map]] gives the underlying numbers read out of the binary: the danger
zone advances **64 px** per jump from a normal beacon, **32 px** from a nebula beacon in a
normal sector, and **51 px** from a nebula beacon in a nebula sector — 51/64 ≈ 80%, i.e. a
~20% discount. This sector is therefore the *worst* place in the game to try to buy time by
hiding in cloud, despite being the cloudiest.

> ⚠️ **CONTRADICTION:** [[source-fandom-rebel-fleet]] (per `raw/wiki/rebel-fleet.md`) says
> nebula beacons in a nebula sector reduce the advance "by 1/5 of regular beacon advance
> rate", which reads as *to* one fifth. [[source-fandom-environmental-hazards]] and
> [[source-fandom-sectors]] both say **20%**, and [[source-xftl-sector-map]]'s pixel figures
> confirm it is a ~20% *reduction*, not a reduction to 20%. The rebel-fleet wording is
> retained here but should be read as loose phrasing, not a second claim.

Two more fleet interactions matter in a sector this cloudy
([[source-fandom-rebel-fleet]], [[source-fandom-environmental-hazards]]):

- A nebula beacon taken by the fleet **always gains an ion storm** (nebula *exit* beacons
  never do).
- Nebula beacons **never carry an Anti-Ship Battery** — except if you are waiting there out
  of fuel, in which case the nebula is removed and the ASB appears.

### Quest markers are hard to place here
`StarMap::AddQuest` filters out beacons that are nebula, a store, a distress beacon, the
exit, already visited, already quested, fleet-taken, or your current position; if nothing
qualifies, the quest is pushed to the next sector (and cancelled outright if that would be
sector 8). ([[source-xftl-sector-map]], [[source-fandom-beacons]],
[[source-fandom-sectors]]; see [[concept-quest-beacon-placement]])

With 12–18 beacons committed to clouds before anything else is placed, plus 2–3 stores and
up to 4 distress beacons excluded on top, the candidate pool here is unusually thin — and
**both of this sector's quest-planting events, [[event-nebula-wreckage]] and
[[event-slug-comm-tapping]], are themselves inside the clouds.**

### Beacon markers
Five pool events carry the distress tag and so raise a marker on an adjacent beacon:
`SLUG_DISTRESS_ROCK`, `SLUG_DISTRESS_QUESTION`, `SLUG_DISTRESS_MANTIS`,
`REFUGEE_DISTRESS_SLUG`, `TRAP_BEACON`. All five come from `DISTRESS_BEACON_SLUG` itself —
**no event allocated from another list here carries the tag**, so unlike Engi space this
sector can never show *more* distress markers than its distress allocation. It can easily
show fewer: three of the eight distress events raise no marker at all.

[[source-fandom-template-distress-events-by-sectors]] independently lists exactly those five
events for "Slug Nebulas", and records what Long-Ranged Scanners reads on each: only
`TRAP_BEACON` shows *"Possible ship detected"*; the other four show *"An unvisited
location"* — which does not mean safe, since `SLUG_DISTRESS_ROCK` and `SLUG_DISTRESS_MANTIS`
can both end in combat. Markers are drawn only on beacons **adjacent** to you
([[source-fandom-beacons]]).

### Stores
0–1 guaranteed store plus **2 nebula stores** — matching
[[source-fandom-template-stores-number-of-stores-by-sectors]] exactly against
`sector_data.xml`. Because both nebula stores are on a `NEBULA_*` line they are placed
first and can never be squeezed out; the plain `STORE` line's 0 is a genuine roll, not a
casualty of the map filling up. Three further pool events can open a shop:
[[event-pirate-briber]], [[event-slug-drink]] and [[event-slug-store-ship]]
([[source-fandom-stores-and-resources]],
[[source-fandom-template-stores-additional-stores-from-events-by-sectors]]).

> ⚠️ **CONTRADICTION (unresolved, worth flagging):**
> [[source-fandom-template-stores-additional-stores-from-events-by-sectors]] lists **Large
> trade station** as an available store-opening event in Slug Nebulas. In this sector that
> event (`STORE_REBELSIDE`) is reachable *only* through `OVERRIDE_ITEMS`, the AE twin of the
> `ITEMS` list — whose substitution [[concept-sector-event-allocation]] records as an open
> question. The Fandom table is therefore weak evidence that AE `OVERRIDE_` lists **do**
> replace their base lists; it is a community table, not a game file, so it does not settle
> it. The same table also names "Slug transport with military escort", which this repo has
> not yet matched to an event id.

## Event Pool

File order, with the **placement position** the generator actually uses (`NEBULA_*` lines
promoted to the front) and whether the line can be cut when the map fills:

| # placed | Event list | min | max | Notes |
|---|---|---|---|---|
| 1 | `NEBULA_STORE_SLUG` | 2 | 2 | cloud line — placed first |
| 2 | `NEBULA_NOTHING_SLUG` | 2 | 4 | cloud line |
| 3 | `NEBULA_HOSTILE_SLUG` | 5 | 7 | cloud line — largest single allocation |
| 4 | `NEBULA_NEUTRAL_SLUG` | 3 | 5 | cloud line — 13 events, both quest starts |
| 5 | `STORE` | 0 | 1 | |
| 6 | `ITEMS` | 0 | 2 | AE twin `OVERRIDE_ITEMS` adds `STORE_REBELSIDE` |
| 7 | `NOTHING_SLUG` | 0 | 2 | |
| 8 | `HOSTILE_SLUG` | 1 | 2 | |
| 9 | `DISTRESS_BEACON_SLUG` | 3 | 4 | **may be cut** |
| 10 | `STORM_SLUG` | 1 | 3 | **may be cut** — Slug sectors only |
| 11 | `NEUTRAL` | 1 | 2 | **may be cut**, and also the leftover fallback |

Totals: **18–34 allocated slots against at most 24 beacons.**
Start beacon: `START_BEACON_SLUG`.
(per [[source-sector-data-xml]]; placement order per [[source-fandom-sectors]])

The community wiki's beacon list for this sector matches the file's counts line for line,
and even its list order — but [[source-fandom-sectors]] states outright that its ordering
does not reflect the game files, so the agreement is coincidence and the *placement* order
above still differs from both. ([[source-fandom-sectors]])

Crew rarity (store assortment and crew-kill rewards): Slug 2, Human 2, Engi / Mantis /
Zoltan / Rockman 4 — identical in [[source-sector-data-xml]] and [[source-fandom-sectors]].

## Chains That Run Through It
Two quest markers can be planted from this sector's pool, both from `NEBULA_NEUTRAL_SLUG`:

- [[event-nebula-wreckage]] `NEBULA_BATTLEFIELD` → `SECRET_WORD_ABADOTH` — the dying
  stranger's coordinates and the ABADOTH password. _Chain page not yet created._
- [[event-slug-comm-tapping]] `QUEST_SLUG_PIRATE_TRAP` → `QUEST_SLUG_PIRATE_TRAP2`.
  _Chain page not yet created._

Both start inside the clouds, so their markers are competing for the small non-nebula
remainder of the map (see *Quest markers*, above).

## Factions & Ships
- [[entity-slugs]] — dominant faction

## Strategy Notes
- 3–4 guaranteed distress beacons is the heaviest **distress allocation** in the game — but
  it is the last-but-two line, so it is one of the three that can be squeezed out entirely.
  The allocation is not a promise of stops. (per [[source-sector-data-xml]],
  [[source-fandom-sectors]])
- Hiding in cloud to slow the fleet is worth ~20% here rather than the usual 50%. If fleet
  delay is what you need, this sector is a poor place to buy it.
  (per [[source-xftl-sector-map]], [[source-fandom-environmental-hazards]])
- A Slug crewman is the only way to keep reading enemy crew once sensors are gone, and
  Slug rarity here is 2 — the joint-cheapest in the sector's store table.
  (per [[source-fandom-sensors]], [[source-sector-data-xml]])
- Long-Ranged Scanners narrow, but do not name, an adjacent distress beacon: a ship
  reading is `TRAP_BEACON`, a plain location reading is one of the other four.
  (per [[source-fandom-template-distress-events-by-sectors]], [[source-fandom-beacons]])
- _Opinion, unsourced in the files:_ [[source-fandom-sectors]] characterises nebula sectors
  as generally more dangerous and warns that sector colour is a poor guide to danger. It
  offers no per-sector danger ranking for this one.

## Open Questions
- [x] ~~What `STORM_SLUG` events do mechanically~~ — answered: a plasma/ion storm halves the
  reactor (rounded up), strips power automatically on arrival, spares Zoltan power and the
  Backup Battery, and halves the enemy reactor too
  ([[source-fandom-environmental-hazards]]).
- [x] ~~Which distress events are traps~~ — answered from the trees and the distress-marker
  data: `TRAP_BEACON` is combat on arrival and `SLUG_DISTRESS_TRICK` is a boarding, and
  `SLUG_DISTRESS_TRICK` raises **no** distress marker at all.
- [ ] What is the map's **beacon floor**? Every source here gives the 24 ceiling and the
  80%-per-cell rule; none states a minimum, so "18–34 allocated" cannot be turned into a
  number of stops.
- [ ] Does the AE `OVERRIDE_ITEMS` / `OVERRIDE_NEUTRAL` substitution actually happen? The
  Fandom store table implies yes for `OVERRIDE_ITEMS` here; no game file says so.
  ([[concept-sector-event-allocation]])
- [ ] Which event id is Fandom's "Slug transport with military escort", listed as a
  store-opening event for Slug Nebulas?
- [ ] Do the shared `NEBULA` filler events — drawn by cloud-converted beacons — appear in
  this sector in practice, and which of them?
- [ ] Is a `STORM_SLUG` beacon treated as a "nebula beacon" by the quest-placement filter
  and by the fleet-advance rate? The sources describe storms as a nebula sub-environment
  but neither rule names them.

## Related
- [[sector-slug-home-nebula]] — the near-twin: identical table plus one guaranteed
  `NEBULA_SLUG_FIGHT_UNLOCK` beacon, and `unique="true"`
- [[sector-uncharted-nebula]] — the other nebula sector
- [[concept-nebula-mechanics]] · [[concept-quest-beacon-placement]] ·
  [[concept-sector-event-allocation]] · [[concept-rebel-fleet-advance]] · [[concept-stores]]

## Sources
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-text-sectorname-xml]] (per raw/gamedata/text_sectorname.xml)
- [[source-fandom-sectors]] (per raw/wiki/sectors.md)
- [[source-fandom-beacons]] (per raw/wiki/beacons.md)
- [[source-fandom-environmental-hazards]] (per raw/wiki/environmental-hazards.md)
- [[source-fandom-sensors]] (per raw/wiki/sensors.md)
- [[source-fandom-rebel-fleet]] (per raw/wiki/rebel-fleet.md)
- [[source-fandom-stores-and-resources]] (per raw/wiki/stores-and-resources.md)
- [[source-fandom-template-stores-number-of-stores-by-sectors]]
  (per raw/wiki/template-stores-number-of-stores-by-sectors.md)
- [[source-fandom-template-stores-additional-stores-from-events-by-sectors]]
  (per raw/wiki/template-stores-additional-stores-from-events-by-sectors.md)
- [[source-fandom-template-distress-events-by-sectors]]
  (per raw/wiki/template-distress-events-by-sectors.md)
- [[source-xftl-sector-map]] (per raw/modding/2026-08-15-xftl-sector-map.txt)
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-events-nebula]] (per raw/gamedata/events_nebula.xml)
