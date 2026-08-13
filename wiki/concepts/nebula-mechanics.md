---
id: concept-nebula-mechanics
type: concept
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 10
related_events: []
tags: [mechanics, nebula, environment, sensors]
---

# Nebulae, sensors, and storms

## Definition & Context
A nebula is a **beacon-level environment**, not a sector type — though three sectors are
built almost entirely out of them. It changes two things, and the game states both itself:

> *"You're inside a nebula. Your sensors will not function, but the Rebel fleet will advance
> more slowly towards you."* — `tooltip_nebula` ([[source-text-tooltips]])

> *"The nebula here will make fleet pursuit slower but will disrupt your sensors."*
> — `map_nebula_loc` ([[source-text-misc]])

Neither string gives a number for either effect, and no other file does either.

## How a beacon becomes a nebula

Two mechanisms, and the developers wrote the first one down. At the top of
`events_nebula.xml` ([[source-events-nebula]]):

```
	NOTE: we need to make all lists with "NEBULA_" in it trigger the creation of a nebula
```

So the **event-list name prefix** is the trigger: a beacon filled from any list whose name
starts `NEBULA_` is generated as a nebula. Second, individual events carry an explicit tag:

```xml
<environment type="nebula"/>
```

**42 live instances**, spread across `events_slug.xml` (22), `events_nebula.xml` (15),
`events_zoltan.xml` (2), `newEvents.xml` (2) and `events_rebel.xml` (1)
([[source-events-nebula]], [[source-events-slug]]).

The two mechanisms overlap heavily but not perfectly, and the mismatch has an observable
consequence — see *Plasma storms outside nebulae*, below.

## Which sectors have nebula beacons

`sector_data.xml` defines a `sectorType name="NEBULA"` containing `NEBULA_SECTOR`,
`SLUG_HOME` and `SLUG_SECTOR`. But nebula beacons are allocated far more widely
([[source-sector-data-xml]]):

| Sector | Nebula allocation | Wiki page |
|---|---|---|
| `NEBULA_SECTOR` | `NEBULA_STORE` 1, `NEBULA_EMPTY` 4, `NEBULA_HOSTILE` 5–6, `NEBULA_NEUTRAL` 7–8 | [[sector-uncharted-nebula]] |
| `SLUG_HOME` | `NEBULA_STORE_SLUG` 2, `NEBULA_NOTHING_SLUG` 2–4, `NEBULA_HOSTILE_SLUG` 5–7, `NEBULA_NEUTRAL_SLUG` 3–5, `NEBULA_SLUG_FIGHT_UNLOCK` 1, **`STORM_SLUG` 1–3** | [[sector-slug-home-nebula]] |
| `SLUG_SECTOR` | same, minus `NEBULA_SLUG_FIGHT_UNLOCK` | [[sector-slug-controlled-nebula]] |
| `CIVILIAN_SECTOR` | `NEBULA` **0–8** | [[sector-civilian-sector]] |
| `ZOLTAN_SECTOR` / `ZOLTAN_HOME` | `NEBULA_ZOLTAN` 2–6 | [[sector-zoltan-controlled-sector]] / [[sector-zoltan-homeworlds]] |
| `PIRATE_SECTOR` | `NEBULA_PIRATE` 0–5 | [[sector-pirate-controlled-sector]] |
| `REBEL_SECTOR` / `REBEL_SECTOR_MINIBOSS` | `NEBULA_REBEL` 0–5 | [[sector-rebel-controlled-sector]] / [[sector-rebel-stronghold]] |
| `STANDARD_SPACE` | `NEBULA` 0–4 | [[sector-federation-space]] |
| `ENGI_*`, `MANTIS_*`, `ROCK_*`, `CRYSTAL_HOME`, `FINAL` | **none** | — |
| `LANIUS_SECTOR` | `NEBULA_LANIUS` 2–6 — **commented out** | — |

Two things worth reading off that table:

- **The Uncharted Nebula and both Slug sectors are wall-to-wall nebula**: every allocated
  list except `STORE`, `ITEMS`, `NOTHING_SLUG`, `HOSTILE_SLUG`, `DISTRESS_BEACON_SLUG`,
  `NEUTRAL` and `STORM_SLUG` is `NEBULA_`-prefixed. They are not *entirely* nebula.
- **[[sector-civilian-sector]] is the wildcard**: `NEBULA` at 0–8 is the widest range of any
  allocation in the file. A Civilian sector can be nebula-free or nearly half nebula.
- The Lanius sector was meant to have nebulae and the line was disabled
  ([[source-sector-data-xml]]).

## Effect 1 — sensors stop working

`tooltip_sensors`: *"Sensors: Enables view of all rooms and info for enemy ships."*
([[source-text-tooltips]]). In a nebula that is switched off. Three things in the data are
built specifically to work around it:

| Workaround | Description string | Source |
|---|---|---|
| **Lifeform Scanner** (`LIFE_SCANNER`) | *"Detects the location of any life forms, even when sensors don't function."* | [[source-text-blueprints]] |
| **Slug crew** | *"Telepathic powers reveal rooms and lifeforms even when sensors are down."* (`crew_slug_power_1`) | [[source-text-blueprints]] |
| **The Slug Cruiser** | *"Designed for use inside nebulas, this cruiser lacks sensors and relies instead on the guile and cunning of the Slugs."* | [[source-text-blueprints]] |

This is why [[item-lifeform-scanner]] and [[item-slug-crew]] are disproportionately valuable
in the nebula sectors — and it is the mechanical reason 11 blue options are gated on
`req="slug"` ([[concept-blue-options]]).

A consequence the files do not state but the structure implies: `req="sensors"` gates **23
blue options**, the most of any requirement. Whether those gates still open inside a nebula —
where the system is present but non-functional — is **unknown**. `req` appears to test
possession, not function ([[concept-blue-options]]), so they probably still appear; nothing
confirms it.

## Effect 2 — the Rebel fleet advances more slowly

Both game strings above say so. Neither quantifies it. What the files *do* provide is a
second, reduced tier for nebula **sectors**:

> *"The Rebel Fleet was prepared for the nebula in this sector, so it won't be as effective a
> hiding spot."* — `map_nebula_fleet_loc` ([[source-text-misc]])

So the game distinguishes a nebula beacon in an ordinary sector from a nebula beacon in a
nebula sector, and says the latter helps less.

**Fandom supplies the number the files withhold.** Three separate event pages state, in
almost identical words:

> *"In Slug sectors this event can occur in a non-nebula area of the beacon map. In that case
> the event will still have a plasma storm nebula environment, but the Fleet pursuit will be
> the full amount (instead of the **80%** that you would have when jumping from a nebula
> beacon in a Slug sector)."*
> — [[source-fandom-boarders-humans-in-plasma-storm]], and the same note on
> [[event-rebel-fight-in-plasma-storm]] and [[event-slug-fight-in-plasma-storm]]

Recorded, not adopted: **80% of normal pursuit when jumping *from* a nebula beacon in a Slug
sector**. It is a community figure with no version stated (`medium` reliability), and
nothing in `raw/gamedata/` corroborates it. It is also consistent with `map_nebula_fleet_loc`
— a *reduced* benefit in a nebula sector — which is why it is worth keeping. The
corresponding figure for a nebula beacon in a **non**-nebula sector is not stated by anyone.

See [[concept-rebel-fleet-advance]].

## Plasma storms — `<environment type="storm"/>`

```xml
<event name="STORM_REBEL">
	<environment type="storm"/>
```

**8 live instances.** The effect is stated once, in the tooltip:

> *"This section of the nebula is experiencing a plasma storm. Your main reactor can only
> function at half capacity."* — `tooltip_storm` ([[source-text-tooltips]])

Halved reactor output is the entire mechanic as far as the files go. Whether the nebula's
sensor blackout and fleet slowdown also apply at a storm beacon is **not stated**.

> ⚠️ **CONTRADICTION (internal to the game files, naming only):** the star-map string for
> these beacons is `map_ion_loc` — *"This section of the nebula is experiencing an **ion
> storm**."* — while the in-beacon tooltip calls the same thing a **plasma storm**
> (`tooltip_storm`). Same environment tag, two first-party names. The XML tag and event ids
> use neither: `type="storm"`, `STORM_*`. Fandom uses "plasma storm" throughout, matching the
> tooltip. ([[source-text-misc]] vs [[source-text-tooltips]])
>
> The `map_ion_loc` id is the older-looking of the two — "ion storm" survives only as a
> string name — so the wiki uses **plasma storm** and notes the id.

### The seven storm events

| Event | Live list membership | Nebula beacon? | Page |
|---|---|---|---|
| `STORM_AUTO` | `NEBULA`, `NEBULA_HOSTILE`, `NEBULA_REBEL` | yes | [[event-auto-ship-fight-in-plasma-storm]] |
| `STORM_REBEL` | `NEBULA`, `NEBULA_HOSTILE`, `NEBULA_REBEL`, **`STORM_SLUG`** | both | [[event-rebel-fight-in-plasma-storm]] |
| `STORM_ITEMS` | `NEBULA`, `NEBULA_PIRATE` (×2), `NEBULA_REBEL` | yes | [[event-plasma-storm-incapacitated-ships]] |
| `STORM_BOARDING` | `NEBULA` (AE re-add only), **`STORM_SLUG`** | both | [[event-boarders-humans-in-plasma-storm]] |
| `STORM_SLUG_FIGHT` | **`STORM_SLUG`** only | no | [[event-slug-fight-in-plasma-storm]] |
| `STORM_ZOLTAN_SUPPLY_CHOICE` | `NEBULA_ZOLTAN` | yes | [[event-pirate-ships-in-plasma-storm]] |
| `NEBULA_ROCK_RACIST` | `NEBULA_NEUTRAL` | yes | [[event-rock-ship-in-plasma-storm]] |

(`NEBULA_ROCK_RACIST` is a storm event whose id begins `NEBULA_`, so it lands on a nebula
beacon by name as well as by its list.)

### Plasma storms outside nebulae — where the two mechanisms come apart
`STORM_SLUG` is allocated 1–3 beacons in both Slug sectors, and its name does **not** begin
with `NEBULA_`. By the developers' own rule, those beacons are therefore not generated as
nebulae — even though the events they hold carry a storm environment.

That is exactly what Fandom reports from play: *"Despite being a plasma storm, this event
only occurs at non-nebula beacons. Fleet pursuit will be the full amount…"*
([[source-fandom-slug-fight-in-plasma-storm]]). A dev note in the game files and an
independent play observation converging on the same structural quirk is about as solid as
this wiki gets without engine code.

Practical upshot: a plasma-storm beacon in a Slug sector is a **trap** — half reactor power
*and* no fleet-slowing discount.

### An AE difference
`STORM_BOARDING` is commented out of `NEBULA_HOSTILE` (`events_nebula.xml`) and out of
`NEBULA_PIRATE` (`events_pirate.xml`), but Advanced Edition's `NEBULA` list in
`newEvents.xml` re-adds it with the note:

```xml
<event load="STORM_BOARDING"/>    <!-- DLC re-added - was removed previously -->
```

So boarding-in-a-storm is more likely in AE than in vanilla wherever the `NEBULA` list is
used ([[source-newevents]], [[source-events-nebula]], [[source-events-pirate]]).

## Other beacon environments, for contrast
`<environment>` takes six values in total ([[source-text-tooltips]] for the effects):

| `type` | Live uses | Effect (game's words) |
|---|---|---|
| `nebula` | 42 | sensors off, fleet slower |
| `PDS` | 16 | anti-ship battery fires on you (`target=` picks whose side) |
| `asteroid` | 15 | *"Periodically asteroids will strike your ship."* |
| `storm` | 8 | *"Your main reactor can only function at half capacity."* |
| `sun` | 7 | *"Solar flares will light the ship on fire. Shields will reduce the effect."* |
| `pulsar` | 4 | *"Periodic waves of electromagnetic energy will disrupt your systems."* |

`pulsar` and most `PDS` uses are Advanced Edition (`dlcEvents.xml`,
`dlcEvents_anaerobic.xml`) — the hazard variety at nebula and fleet beacons is largely an AE
addition. `FLEET_EASY_NEBULA`, the fleet-catches-you event for nebula beacons, uses
`type="storm"` rather than `type="nebula"` and carries **no** `<fleet>` tag, unlike its five
siblings ([[concept-rebel-fleet-advance]]).

## Implications For Play
- **Nebula sectors are the fleet-management sectors** — slower pursuit is the whole reason to
  route through them, and the discount is smaller there than at an isolated nebula beacon
  elsewhere.
- **Bring a Lifeform Scanner or a Slug** before a Slug sector; both are explicitly written to
  cancel the sensor blackout.
- **Avoid plasma-storm beacons in Slug space.** Half reactor power and none of the nebula
  upside.
- **[[sector-civilian-sector]] is unpredictable**: 0–8 nebula beacons, the widest allocation
  range in the game.
- Nebula sectors also raise Slug crew rarity from 0 — see [[concept-blueprint-rarity]].

## Where It Applies
- Sectors: [[sector-uncharted-nebula]] · [[sector-slug-controlled-nebula]] ·
  [[sector-slug-home-nebula]] · [[sector-civilian-sector]] ·
  [[sector-zoltan-controlled-sector]] · [[sector-pirate-controlled-sector]] ·
  [[sector-rebel-controlled-sector]]
- Nebula-only events: [[event-empty-nebula-beacon]] · [[event-nebula-lost-ship]] ·
  [[event-trade-resources-in-nebula]] · [[event-rebel-fight-in-nebula]] ·
  [[event-auto-ship-fight-in-nebula]] · [[event-auto-ship-warning-in-nebula]] ·
  [[event-boarders-rebels-in-nebula]] · [[event-slug-fight-in-nebula]] ·
  [[event-store-in-nebula-uncharted]] · [[event-store-in-nebula-slug]] ·
  [[event-nebula-wreckage]] · [[event-slug-store-ship]]
- Items: [[item-lifeform-scanner]] · [[item-slug-crew]] · [[item-sensors]]

## Related
- [[concept-rebel-fleet-advance]] — the other half of the fleet-speed question
- [[concept-stores]] — the two nebula store variants
- [[concept-blue-options]] — `req="sensors"` (23 gates) and `req="slug"` (11)
- [[concept-sector-event-allocation]] — how the allocation table is read
- Slug alias: two pages link this concept as `[[concept-nebula-mechanics]]`. Same subject, no page at
  that slug; worth reconciling on the next lint.

## Open Questions
- [ ] **How much slower is fleet pursuit in a nebula?** Fandom gives 80% for a Slug-sector
      nebula beacon; no figure exists for a nebula beacon in an ordinary sector, and the game
      files give none at all.
- [ ] Do `req="sensors"` blue options still appear at a nebula beacon, where the system is
      installed but non-functional?
- [ ] Does a `type="storm"` beacon also get the nebula sensor blackout and fleet slowdown, or
      only the halved reactor? `STORM_SLUG` says no to the fleet part; the sensor part is
      untested.
- [ ] Is `map_ion_loc` vs `tooltip_storm` a leftover rename, or do two distinct hazards exist
      that share one environment tag?
- [ ] Why was `NEBULA_LANIUS` commented out of `LANIUS_SECTOR`?
- [ ] Does the `NEBULA_`-prefix rule apply to the event *name* as well as the list name?
      `NEBULA_EMPTY` and `NEBULA_NOTHING_SLUG` are allocated directly as single events, not
      through a list, and both also carry an explicit `<environment type="nebula"/>` — so the
      wiki cannot tell which mechanism is doing the work.

## Sources
- [[source-text-tooltips]] (per raw/gamedata/text_tooltips.xml) — `tooltip_nebula`, `tooltip_storm`
- [[source-text-misc]] (per raw/gamedata/text_misc.xml) — `map_nebula_loc`, `map_nebula_fleet_loc`, `map_ion_loc`
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml) — the sensor workarounds
- [[source-events-nebula]] (per raw/gamedata/events_nebula.xml) — the `NEBULA_` prefix dev note
- [[source-events-slug]] (per raw/gamedata/events_slug.xml) — `STORM_SLUG`, 20 nebula tags
- [[source-events-pirate]] (per raw/gamedata/events_pirate.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml) — the AE `NEBULA` list
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml) — allocation
- [[source-fandom-boarders-humans-in-plasma-storm]] (per raw/wiki/boarders-humans-in-plasma-storm.md)
- [[source-fandom-slug-fight-in-plasma-storm]] (per raw/wiki/slug-fight-in-plasma-storm.md)
