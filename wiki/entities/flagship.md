---
id: entity-flagship
type: entity
entity_kind: ship
hostility: hostile
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [boss, endgame, last-stand, flagship, artillery, three-phase]
---

# The Rebel Flagship

## Summary
The endgame boss: one ship, fought in **three phases** at the Federation Base in
[[sector-the-last-stand]], with a separate blueprint for each phase × each difficulty × each
edition — **eighteen `shipBlueprint` entries in `bosses.xml`**, all of them named
"Rebel Flagship" in `text_blueprints.xml` ([[source-bosses]], [[source-text-blueprints]]).

It is the only ship in the game built around **artillery mounts** rather than a weapons
system, and the only one that does not end when its crew dies (see
[[event-boss-automated]]).

A second, incomplete Flagship also exists: `BOSS_SPECIAL` / `BOSS_DEMO`, class name
**"Flagship Construction"**, fought at the [[event-rebel-shipyard]] beacon in
[[sector-rebel-stronghold]] ([[source-blueprints]], [[source-events-rebel]]).

## Traits / Stats

### The three phases (base game blueprints)

| | Phase 1 (`BOSS_1_*`) | Phase 2 (`BOSS_2_*`) | Phase 3 (`BOSS_3_*`) |
|---|---|---|---|
| Hull | 20 | 22 | 20 |
| Max power (E / N / H) | 40 / 42 / 42 | 42 / 44 / 44 | 29 / 31 / 31 |
| Shields (Easy) | 6 | 6 | 6 |
| Shields (Normal & Hard) | 8 | 8 | 8 |
| Engines | 2 | 3 | **6** |
| Artillery | `BOSS_1` `_2` `_3` `_4` | `BOSS_1` `_2` `_3` | `BOSS_1` `_2` |
| Drone system | — | **8 power** | — |
| Drones carried | — | `DEFENSE_1`, `COMBAT_1`, `COMBAT_BEAM`, `BOARDER_BOSS` (4 slots, 10 parts) | — |
| Teleporter | — | — | **2 power** |
| Cloaking | 2 | — | — |
| Doors | 3 | — | — |
| Other | medbay 3, oxygen 2, pilot 3 | medbay 3, oxygen 2, pilot 3 | medbay 3, oxygen 2, pilot 3 |
| `boardingAI` | — | — | **`invasion`** |

(per [[source-bosses]])

Layouts: Easy and Normal both use the `_easy` layout (`boss_1_easy` etc.); **Hard uses the
full layout** (`boss_1`, `boss_2`, `boss_3`). Difficulty changes the ship's floor plan, not
just its numbers.

Every phase declares `<weaponList count="0" missiles="10"/>` and has its `weapons` system
commented out — the Flagship has **no conventional weapons system to disable**. All its
firepower is artillery.

### The artillery
| Mount | Present in | Notes |
|---|---|---|
| `ARTILLERY_BOSS_1` | phases 1, 2, 3 | laser |
| `ARTILLERY_BOSS_2` | phases 1, 2, 3 | missile, **shield-piercing 5** |
| `ARTILLERY_BOSS_3` | phases 1, 2 | beam |
| `ARTILLERY_BOSS_4` | phase 1 only | ion |

Full per-weapon numbers are tabulated on [[event-boss-text-1]] (per [[source-blueprints]];
all four are `NOLOC="1"` with placeholder `desc` text, so the player never sees their
stat cards).

> **Advanced Edition differences** ([[source-bosses]]). `bosses.xml` carries a second block
> of nine blueprints suffixed `_DLC`:
> - **Phase 1 `_DLC`** — adds `<hacking power="3" room="2"/>`. A `<mind>` tag is present but
>   commented out.
> - **Phase 2 `_DLC`** — mechanically identical to the base Normal/Hard versions
>   (`hacking` and `mind` are both present-but-commented-out). Only `BOSS_2_EASY_DLC` differs
>   from its base counterpart, being raised to 8 shield power / 44 max power.
> - **Phase 3 `_DLC`** — adds `<mind power="3" room="4"/>` and raises max power to 32.
>
> Across all three phases, **Easy difficulty loses its shield discount in AE**: every `_DLC`
> Easy blueprint runs 8 shield power like Normal and Hard.
>
> Net effect: AE phase 1 hacks you, AE phase 3 mind-controls you, AE phase 2 is unchanged,
> and Easy is no longer easier in the shield department.

### The construction-yard Flagship
| Blueprint | Class name | Hull | Max power | Crew | Systems |
|---|---|---|---|---|---|
| `BOSS_SPECIAL` | Flagship Construction | 10 | 14 | 3/8 human | shields 2/8, teleporter 1/2, medbay, engines 2/6, oxygen, `hacking` (off), `mind` (off), artillery `BOSS_1` + `_2` at power 1/4 |
| `BOSS_DEMO` | Flagship Construction | 20 | 30 | 6 human | shields 8, teleporter 2, medbay, engines 5, oxygen, artillery `BOSS_1` + `_2` at power 4 |

(per [[source-blueprints]], [[source-text-blueprints]])

`BOSS_SPECIAL` is the one the game actually uses: `events_rebel.xml` defines
`<ship name="FLASHSHIP_CONSTRUCTION_SHIP" auto_blueprint="BOSS_SPECIAL">` (the typo is in the
file) with `<destroyed load="FLAGSHIP_CONSTRUCTION_DONE"/>`
([[source-events-rebel]]). It carries 20 missiles, `boardingAI: sabotage`, and — unlike the
real Flagship — a `<crewCount>`. `BOSS_DEMO` is used by `IMPOSSIBLE_PIRATE` in
`newEvents.xml`, not by the shipyard event ([[source-newevents]]).

> ⚠️ **CONTRADICTION / unresolved.** `blueprints.xml` also defines unsuffixed `BOSS_1`,
> `BOSS_2` and `BOSS_3` — all named "Rebel Flagship" — with systems the `bosses.xml`
> variants do not have (phase 1 with a teleporter, sensors and a drone system; phase 2 with a
> teleporter and sensors) ([[source-blueprints]] vs [[source-bosses]]). Nothing in the data
> states which set the running game loads. Most likely the unsuffixed trio is the legacy
> pre-difficulty definition superseded by the `_EASY`/`_NORMAL`/`_HARD` set, but that is not
> confirmed. Already flagged on [[event-boss-text-1]]; recorded here too.

## Where They Appear
- [[sector-the-last-stand]] (`FINAL`, `minSector` 7, `unique`) — the three-phase fight at the
  Federation Base
- [[sector-rebel-stronghold]] (`REBEL_SECTOR_MINIBOSS`, `minSector` 4, `unique`) — the
  guaranteed `FLAGSHIP_CONSTRUCTION` beacon, i.e. the second, unfinished Flagship

(per [[source-sector-data-xml]])

## Events Involving Them
- [[event-boss-text-1]] — phase 1 announcement (+ full phase-1 loadout and artillery table)
- [[event-boss-text-2]] — phase 2
- [[event-boss-text-3]] — phase 3
- [[event-boss-escaped]] — fires when a phase ends with the Flagship jumping out; the only
  paying event in the sequence
- [[event-boss-automated]] — fires when you kill the crew instead of the hull; the AI takes
  over and the fight continues
- [[event-boss-destroyed]] — the win
- [[event-boss-stalemate]] — engine-level "the ship jumped away" text
- [[event-rebel-shipyard]] — the second Flagship under construction
- [[event-last-stand-start]] · [[event-federation-base]] · [[event-fight-in-last-stand]] —
  the surrounding sector content
- [[chain-the-flagship]] — the sequence as a whole

## How To Fight / Deal With Them
Everything below is read directly off the blueprints; no strategy source in this wiki covers
the fight yet.

- **There is no weapons system.** Targeting "their weapons" is not an option — each artillery
  mount is its own room. Phase 1 has four, phase 2 three, phase 3 two
  ([[source-bosses]]).
- **`ARTILLERY_BOSS_2` pierces 5 shield layers**, so shields alone never stop the Flagship's
  missile mount ([[source-blueprints]]).
- **Killing the crew does not win.** [[event-boss-automated]] explicitly denies the crew-kill
  shortcut that ends nearly every other fight.
- **Phase 2 is the drone phase**: 8 power into drones, carrying a defence drone, two combat
  drones and `BOARDER_BOSS`. Expect boarders you did not have to let aboard.
- **Phase 3 is the boarding phase**: it is the only phase with a teleporter, and the only one
  whose `boardingAI` is `invasion` rather than `sabotage` — its boarders come for your crew,
  not your systems. It also has 6 engine power, double phase 2's.
- **Phase 1 cloaks**; phases 2 and 3 do not.
- **In AE, phase 1 also hacks and phase 3 also mind-controls** ([[source-bosses]]).
- Hull is 20 / 22 / 20 — a total of 62 hull across the run, with a full repair implied
  between phases (not stated in the data; recorded as an open question).

## Related
- [[entity-rebels]] — the faction that built it
- [[entity-federation]] — what it is pointed at
- [[sector-the-last-stand]], [[sector-rebel-stronghold]]

> **Naming note.** Some event pages link `entity-rebel-flagship`; that resolves to this page.

## Open Questions
- [ ] Which blueprint set the game loads — `BOSS_n` or `BOSS_n_<difficulty>[_DLC]`.
- [ ] The Flagship's crew complement. **No phase blueprint carries a `<crewCount>` tag**, yet
      [[event-boss-automated]] presupposes a crew to kill ([[source-bosses]]).
- [ ] Whether the hull repairs between phases, and whether damage carries over.
- [ ] Whether the Flagship's super shield (widely described by players) exists anywhere in
      `raw/gamedata/` — no `ENERGY_SHIELD` or equivalent augment appears on any boss
      blueprint in the files read here. **Do not assert it from memory.**
- [ ] Where `BOSS_DEMO` (hull 20, 6 crew, "Flagship Construction") is reachable, given
      `IMPOSSIBLE_PIRATE` is its only reference.

## Sources
- [[source-bosses]] (per raw/gamedata/bosses.xml)
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-boss]] (per raw/gamedata/events_boss.xml)
- [[source-events-rebel]] (per raw/gamedata/events_rebel.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
