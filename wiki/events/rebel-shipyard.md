---
id: event-rebel-shipyard
type: event
event_name: FLAGSHIP_CONSTRUCTION
sectors: [[[sector-rebel-stronghold]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [rebel, unique, ship-unlock, miniboss, guaranteed-beacon, weapon-reward, fleet-delay, ae-addition]
---

# Rebel shipyard — `FLAGSHIP_CONSTRUCTION`

## Summary
The miniboss. A guaranteed beacon in [[sector-rebel-stronghold]] where you can fight a
**second, unfinished Rebel Flagship** — and the reward is the largest single payout of any
random event in the game: a `HIGH` weapon, 5 fuel, 5 missiles, 5 drone parts, a two-turn
fleet delay, and the **Federation Cruiser unlock**. Or you can walk away for free.

## Trigger & Where It Appears
- Sector: [[sector-rebel-stronghold]] **only** — `sectorDescription name="REBEL_SECTOR_MINIBOSS"`
  in `raw/gamedata/sector_data.xml`, which is `minSector="4" unique="true"` and allocates
  `<event name="FLAGSHIP_CONSTRUCTION" min="1" max="1"/>` ([[source-sector-data-xml]]).
  So it is a **guaranteed beacon** whenever you route through that sector, and the sector
  itself cannot appear before sector 4 and can appear at most once per run.
- It is in **no event list** — placement is direct from the sector definition, not from a
  pool ([[source-events-rebel]]).
- `unique="true"`.
- Long-range scanners show **no ship** ([[source-fandom-rebel-shipyard]]) — nothing warns
  you that this is the miniboss beacon.
- Defined in the DLC section of `events_rebel.xml`, under the `SPECIAL` header — this is
  **Advanced Edition** content ([[source-events-rebel]]).

## Text
> You arrive at the beacon to find yourself in a huge Rebel shipyard, scaffolding and
> construction drones filling the sector! The entire system looks devoted to ship
> construction, the nearby planets and moons ruthlessly mined to harvest resources for a
> ship of immense size...

(`event_FLAGSHIP_CONSTRUCTION_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Look around. | — | *"Warning lights flash as scans identify the gigantic ship under construction - it's a second Rebel Flagship!… get ready, you've got a hell of a fight on your hands."* → fight `<ship load="FLASHSHIP_CONSTRUCTION_SHIP" hostile="true"/>`. Win by hull or by crew kill → `FLAGSHIP_CONSTRUCTION_DONE`. | 100% (deterministic) |
| 2 | Leave immediately. | — | *"You feel the mission is the highest priority and it's too risky to stay in such a dangerous location."* → nothing happens. | 100% |

### The `FLASHSHIP_CONSTRUCTION_SHIP`
`<ship name="FLASHSHIP_CONSTRUCTION_SHIP" auto_blueprint="BOSS_SPECIAL">` — the ship id is
misspelled in the file ("FLASHSHIP"), quoted as-is ([[source-events-rebel]]).

- **`destroyed`** → loads `FLAGSHIP_CONSTRUCTION_DONE` directly.
- **`deadCrew`** → *"You detect no more lifesigns on the incomplete Flagship. You'd expect a
  ship of that size to have more security measures, but perhaps their computer systems
  aren't complete yet."* → a hidden choice *"Pillage the ship for supplies."* → the same
  `FLAGSHIP_CONSTRUCTION_DONE`.
- No surrender, no escape.

The `BOSS_SPECIAL` blueprint (`raw/gamedata/blueprints.xml`, [[source-blueprints]]) is
class **"Flagship Construction"** ([[source-text-blueprints]]), layout `boss_3` — the same
layout as the real Flagship's third phase:

| Stat | Value |
|---|---|
| Hull | `health amount="10"` |
| Max power | 14 |
| Crew | `class="human"`, `amount="3" max="8"` |
| Shields | power 2, max 8 |
| Engines | power 2, max 6 |
| Weapons room | **commented out** — `weaponList count="0" missiles="20"` |
| Artillery | **two** — `ARTILLERY_BOSS_1` and `ARTILLERY_BOSS_2`, power 1, max 4 |
| Teleporter | power 1, max 2 |
| Medbay, Oxygen, Pilot | present |
| Hacking | power 1, `start="false"` |
| Mind Control | power 1, `start="false"` |
| Boarding AI | `sabotage` |

[[source-fandom-rebel-shipyard]] adds that, unlike the real
[[entity-flagship]], this ship's **system levels and crew count scale with difficulty
and sector number**; its layout resembles the Flagship's Phase 3 on Hard (artillery rooms
connected to the rest of the ship, regardless of your actual difficulty) but it **lacks
Mind Control and the Power Surge**.

> ⚠️ **CONTRADICTION:** the blueprint **does declare a Mind Control system**
> (`<mind power="1" room="3" start="false"/>`, [[source-blueprints]]), where
> [[source-fandom-rebel-shipyard]] says the ship lacks it. The `start="false"` flag is the
> likely reconciliation — the system is installed but not active at the start of the fight,
> so it may never fire and would read in play as "absent". Trusting the game files on what
> the blueprint *contains* (`high` vs `medium`); Fandom's observation of in-play behaviour
> is probably also accurate. Note the same flag sits on Hacking, which Fandom does not
> mention at all.

### `FLAGSHIP_CONSTRUCTION_DONE` — the payout
> While the second flagship was not yet finished, it doesn't make the battle any less of a
> victory... and you've crippled the Rebel fleet's strength considerably! While you don't
> overstay your welcome, you quickly salvage choice bits of metal, drones, and even an
> unusual object or two from the wreckage and prepare to jump!

All of the following, together ([[source-events-rebel]]):

| Effect | Value |
|---|---|
| `autoReward level="HIGH"` `weapon` | a high-tier weapon **plus** the scrap that comes with a `HIGH` roll |
| `item_modify` fuel | **+5** |
| `item_modify` missiles | **+5** |
| `item_modify` drones | **+5** |
| `modifyPursuit amount="-2"` | Rebel fleet **delayed 2 turns** |

Then a hidden `continue`:

> As you are leaving you detect an interesting Federation ship signal. Apparently the Rebels
> were reverse engineering the advanced weaponry on a prototype Federation cruiser. You
> don't know how they captured the ship intact but you program its FTL drive to return the
> ship to the nearest Federation base. You just hope it gets there unharmed.

→ `<unlockShip id="4"/>`. [[source-fandom-rebel-shipyard]] identifies ship 4 as the
**Federation Cruiser** (Layout A), and notes it can alternatively be unlocked by winning the
game with the Engi Cruiser.

## Blue Options
None. There is no `req=` anywhere in the event — no system, augment or crew lets you take
this beacon safely.

## Rewards & Risks
- Reward: the single largest random-event payout in the game — `HIGH` weapon, +5/+5/+5
  resources, a **two-turn** fleet delay (double what any other event grants), and a ship
  unlock.
- Risk: **a Flagship-class enemy, mid-run**. It scales with sector and difficulty. There is
  no surrender, no escape, and no bail-out once choice 1 is taken; losing here ends the run.
- Choice 2 costs nothing but forfeits everything.

## Strategy Notes
- *(Opinion.)* This is a pure "is my ship finished?" check. The rewards are enormous and the
  fleet delay alone can be worth a beacon or two of extra looting — but the ship is a
  Flagship variant, not a scaled-up Rebel cruiser, and taking it with an unfinished build
  is how runs end in sector 5.
- The unlock is the reason most players take it. If you already own the Federation Cruiser,
  the fight is evaluated purely on the weapon + resources + fleet delay.
- Because the sector is `minSector="4"` and `unique="true"`, you get at most one shot per
  run, and only if you route into the Rebel Stronghold ([[source-sector-data-xml]]).

## Related
- [[sector-rebel-stronghold]] — the only place this occurs
- [[entity-flagship]] — the real one
- [[concept-rebel-fleet-advance]]
- [[concept-ship-unlocks]], [[concept-rebel-fleet-advance]]

## Open Questions
- [ ] How the `BOSS_SPECIAL` blueprint's declared levels scale with difficulty and sector —
      Fandom asserts they do, the blueprint states only base/max values.
- [ ] Does the `start="false"` Mind Control / Hacking ever come online mid-fight?
- [ ] Numeric value of `HIGH` `weapon` (which weapon pool, what scrap).
- [ ] Whether `unlockShip id="4"` is Layout A only, as Fandom implies.

## Sources
- [[source-events-rebel]] (per `raw/gamedata/events_rebel.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-blueprints]] (per `raw/gamedata/blueprints.xml`)
- [[source-text-blueprints]] (per `raw/gamedata/text_blueprints.xml`)
- [[source-fandom-rebel-shipyard]] (per `raw/wiki/rebel-shipyard.md`)
