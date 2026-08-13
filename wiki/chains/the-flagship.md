---
id: chain-the-flagship
type: chain
trigger_event: [[[event-last-stand-start]]]
steps: [[[event-last-stand-start]], [[event-federation-base]], [[event-boss-text-1]], [[event-boss-text-2]], [[event-boss-text-3]], [[event-boss-destroyed]]]
sectors: [[[sector-the-last-stand]]]
reward: Victory — the Federation Victory achievements; no in-run payout
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 7
tags: [endgame, last-stand, flagship, boss, scripted, engine-driven, three-phase, orphan-events]
---

# The Flagship (the Last Stand)

## Summary
The endgame sequence: you reach the Federation Base in [[sector-the-last-stand]], the
Rebel Flagship arrives to destroy it, and you fight it in **three phases** at the same
beacon. Destroy the third phase and the run ends in victory
([[source-events-boss]], [[source-bosses]]).

Structurally it is unlike every other chain in this wiki. There are no `<quest>` tags, no
`eventList` memberships and no `sector_data.xml` allocations anywhere in it — **every**
event in the sequence is an orphan in the data, invoked by the game's endgame scripting by
hard-coded name ([[source-events-boss]], [[source-sector-data-xml]]). The events carry the
prose; `bosses.xml` carries the ship. Nothing in the files wires the two together.

## How It Starts
- The `FINAL` sector (`minSector="7"`, `unique="true"`) is the destination
  ([[source-sector-data-xml]]). Reaching it is a routing outcome, not an event.
- Trigger: [[event-last-stand-start]] (`LAST_STAND_START`) — the outpost briefing, fired
  *"the first time you arrive at the base, before the rebel fleet arrives"* per the XML's
  own comment ([[source-events-boss]]). It pays **+10 fuel and +10 hull** and sets
  `<fleet>fed</fleet>`.
- The sector's declared `startEvent` is `BOSS_NEUTRAL`, which the file itself annotates
  *"STUPID, since it's starting you at the 'exit'"* — so `LAST_STAND_START` is not the
  start beacon in the allocation sense ([[source-sector-data-xml]]).

### The sector around the fight
`FINAL` allocates a fixed beacon budget ([[source-sector-data-xml]]):

| Allocation | Contents |
|---|---|
| `STORE` ×1 | the only shop in the sector |
| `BOSS_REPAIR_STATION` ×3 | [[event-repair-station-in-last-stand]] |
| `BOSS_HOSTILE` ×6 | three copies of [[event-fight-in-last-stand]] (`BOSS_SCOUT`) |
| `BOSS_NEUTRAL` ×7–10 | [[event-rebel-ship-attacking-civilians-in-last-stand]], [[event-rebel-fight-among-federation-and-rebel-fleets]], [[event-empty-beacon-last-stand]], [[event-rebel-ship-attacking-refueling-outpost]], [[event-rebel-fight]] |

`BOSS_WARNING_NODE` — [[event-rebel-fight-among-rebel-fleet]] and
[[event-rebel-fight-among-federation-and-rebel-fleets]] — has no sector allocation; the
engine calls it by name for the warning beacons ([[source-events-boss]],
[[concept-sector-event-allocation]]).

## Steps

1. **[[event-last-stand-start]]** — `LAST_STAND_START` (raw: events_boss.xml)
   Docking at the Federation outpost and briefing Admiral Tully. `+10 fuel`,
   `<damage amount="-10"/>` (10 hull repaired). One-time.

2. **[[event-federation-base]]** — `FEDERATION_BASE` (raw: events_boss.xml)
   The arrival text at the base beacon itself: *"…You hang back near the far side of the
   moon to avoid the conflict… You prepare to face the Flagship."* A single `<text>` tag —
   no choices, no ship, no reward ([[source-events-boss]]).

   > Not to be confused with `FEDERATION_BASE_ASSIST` or `HIDDEN_FEDERATION_BASE_LIST` in
   > `events.xml`, which are unrelated mid-game quest content
   > ([[source-events-xml]]).

3. **[[event-boss-text-1]]** — `BOSS_TEXT_1` — **phase 1**
   *"This is it... The Rebel flagship… There's no turning back!"* A bare `<text>` tag; the
   fight is configured from `bosses.xml` ([[source-bosses]]). Phase 1 is the artillery
   phase: four `ARTILLERY_BOSS_*` mounts, cloaking, and 20 hull.

4. **[[event-boss-text-2]]** — `BOSS_TEXT_2` — **phase 2**
   *"…it has redirected considerable power to its drones."* Drops the fourth artillery
   mount, the doors and the cloak; adds an 8-power drone system with a four-drone list
   (including `BOARDER_BOSS`). 22 hull ([[source-bosses]]).

5. **[[event-boss-text-3]]** — `BOSS_TEXT_3` — **phase 3**
   *"…it's transferred power to the teleporter as well as... some kind of super weapon."*
   Two artillery mounts, a teleporter, 6-power engines and an `invasion` boarding AI.
   20 hull ([[source-bosses]]).

### The interrupts

- **[[event-boss-escaped]]** — `BOSS_ESCAPED` fires when a phase ends with the Flagship
  FTL-ing out rather than dying: *"Just as you finally gain the upper hand it finds a way
  to make an FTL jump."* It is the **only event in the whole sequence that pays anything**
  — `autoReward level="HIGH"` `standard` — plus a
  `<status type="clear" target="player" system="sensors" amount="100"/>`
  ([[source-events-boss]]).
- **[[event-boss-automated]]** — `BOSS_AUTOMATED` fires when you wipe the Flagship's crew
  instead of its hull: an onboard AI takes over and the fight continues crewless. Text
  only ([[source-events-boss]]).

### The ending

- **[[event-boss-destroyed]]** — `BOSS_DESTROYED`. *"Its explosion rocks your ship and you
  shudder with relief. You did it. The Federation is saved...."* No `autoReward` — the run
  is over, so there is nothing to pay ([[source-events-boss]]).

> ⚠️ The `Continue...` branch of `BOSS_DESTROYED` still contains a **beta-era developer
> message** addressing the player as a tester and pointing at the Subset Games forums
> (`event_BOSS_DESTROYED_c1_text`, [[source-text-events-xml]]). It is present in the
> 1.6.x data extracted for this wiki. Whether the shipped game displays it — as opposed to
> handing off to the ending sequence — is **not stated in any file examined here**. See
> [[event-boss-destroyed]].

## Requirements
- Reach sector 8. `FINAL` is `minSector="7"`, `unique="true"`
  ([[source-sector-data-xml]]).
- Nothing else. **There is no crew, system, augment or choice gate anywhere in the
  sequence** — none of the events carries a `req=`, and only `LAST_STAND_START` and
  `BOSS_DESTROYED` carry a `<choice>` at all ([[source-events-boss]]).

The real requirement is the ship you arrive with, and that is not something the event data
describes.

## Reward
- **Victory.** `achievements.xml` defines `ACH_WIN_EASY` (*"Federation Victory (Easy)"*,
  *"Beat the boss on Easy."*) and `ACH_WIN_NORMAL` (*"Beat the boss on Normal."*)
  ([[source-achievements]]).
- `autoReward level="HIGH"` `standard` per surviving phase, from `BOSS_ESCAPED`
  ([[source-events-boss]]).
- +10 fuel and +10 hull once, from `LAST_STAND_START`.
- Three [[event-repair-station-in-last-stand]] beacons and one store are the sector's
  entire resupply budget ([[source-sector-data-xml]]).

`BOSS_DESTROYED` itself pays nothing.

## Failure Modes
- **Losing a phase fight.** The run ends; there is no retreat branch defined in any of the
  three phase events.
- **Arriving underbuilt.** The three phases are fought back to back at one beacon with
  only the phase rewards and three repair stations in between.
- **Spending the sector's beacons badly.** Six `BOSS_HOSTILE` and seven-to-ten
  `BOSS_NEUTRAL` beacons sit between you and the base, and the Rebel fleet is closing on
  it the whole time.
- **Wiping the crew rather than the hull** does not fail anything — it triggers
  [[event-boss-automated]] and the fight continues.

## Strategy Notes
- Each survived phase pays `HIGH standard`, so the resource curve through the fight is:
  phase 1 → payout → phase 2 → payout → phase 3 → nothing. Budget repairs and ammunition
  around that. *(Reading of the reward tags, not a sourced strategy claim.)*
- The phase blueprints tell you what to prepare for and the events do not:
  artillery/cloak, then drones and boarding drones, then a teleporter and an `invasion`
  boarding AI ([[source-bosses]]). Defence drones matter in phase 2; anti-boarding
  capability matters in phase 3.
- Difficulty changes the blueprint, not the sequence — `*_EASY`, `*_NORMAL` and `*_HARD`
  variants differ mainly in shield layers and max power ([[source-bosses]]).
- **No Fandom page in this raw set covers the Flagship sequence**, so the community's
  phase-by-phase tactics are unsourced here.

## Related
- [[sector-the-last-stand]] — the sector this all happens in
- [[event-rebel-shipyard]] — `FLAGSHIP_CONSTRUCTION` in [[sector-rebel-stronghold]], where
  the Flagship is built; destroying the construction ship unlocks the Federation Cruiser
  (`<unlockShip id="4"/>`, [[source-events-rebel]])
- [[event-boss-stalemate]] — a similarly-named orphan one-liner that is **not** part of
  this sequence; it lives in `events.xml`, not `events_boss.xml`
- [[entity-flagship]], [[entity-federation]], [[concept-rebel-fleet-advance]]
- [[concept-sector-event-allocation]] — why "orphan in the data" does not mean unreachable
  here

## Open Questions
- [ ] What applies the sensors status that `BOSS_ESCAPED` and `BOSS_DESTROYED` both clear.
- [ ] Is `BOSS_ESCAPED`'s `HIGH` reward granted after every phase, or only some?
- [ ] Is `event_BOSS_DESTROYED_c1_text` reachable in the retail build, or dead text
      superseded by the ending sequence?
- [ ] Does `FEDERATION_BASE` play on every arrival at the base beacon or only the first?
- [ ] Nothing in `raw/gamedata/` states the phase order or the transition rules — the
      sequence above is assembled from event prose plus the three `bosses.xml` blueprint
      sets. An engine-side source would confirm it.
- [ ] `ACH_WIN_EASY` and `ACH_WIN_NORMAL` are defined but no `ACH_WIN_HARD` appears in
      `achievements.xml`. Is Hard-mode victory tracked elsewhere?

## Sources
- [[source-events-boss]] (per raw/gamedata/events_boss.xml)
- [[source-bosses]] (per raw/gamedata/bosses.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-achievements]] (per raw/gamedata/achievements.xml)
- [[source-events-rebel]] (per raw/gamedata/events_rebel.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
