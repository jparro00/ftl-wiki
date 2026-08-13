---
id: event-battlefield-wreckage
type: event
event_name: WRECKAGE_EVENT
sectors: [[[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: any
hostile: false
blue_options: [sensors lvl 2, sensors lvl 3]
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 7
tags: [blue-option, sensors, salvage, weapon-reward, fight-risk, repeatable, advanced-edition, filler]
---

# Battlefield wreckage — `WRECKAGE_EVENT`

## Summary
The aftermath of a ship battle, and one of the few events in the game that pays off
**Sensors** — a subsystem with almost no other event use. With Sensors 2 you take a
guaranteed medium haul; with Sensors 3 you get a coin-flip between a large haul and a free
weapon. Without Sensors you can still poke around, but a third of those pokes start a
fight.

## Trigger & Where It Appears
- Event lists: `NEUTRAL` and `NEUTRAL_EXIT` in `newEvents.xml` and `NEUTRAL_ENGI` in
  `events_engi.xml`, all three tagged as DLC additions
  ([[source-newevents]], [[source-events-engi]]), plus the Advanced Edition replacements
  `OVERRIDE_NEUTRAL` and `OVERRIDE_NEUTRAL_EXIT` ([[source-dlceventsoverwrite]]).
  `NEUTRAL_ENGI` has no Advanced Edition override — it is used as-is in both editions.
- Sector allocations ([[source-sector-data-xml]]):
  `NEUTRAL_ENGI` at `min=4 max=6` in [[sector-engi-controlled-sector]] and `min=5 max=7`
  in [[sector-engi-homeworlds]]; `NEUTRAL` at `min=1 max=2` in
  [[sector-slug-controlled-nebula]] and [[sector-slug-home-nebula]].
- `NEUTRAL` is additionally the engine's hardcoded filler list and `NEUTRAL_EXIT` its
  exit-beacon counterpart; neither `NEUTRAL_EXIT` nor the filler role appears in
  `sector_data.xml`, which is expected rather than suspicious
  ([[concept-sector-event-allocation]]). Fandom records `alsooccur=exitandfiller`
  ([[source-fandom-battlefield-wreckage]]).
- **Not** `unique` — it can recur, and Fandom agrees (`unique=false`).
- Beacon: ordinary. Despite one text variant describing a nebula, the event declares **no**
  `<environment>` — there is no nebula or storm effect.

## Text
`[varies: textList WRECKAGE_TEXT]` — two entries, no repeats
([[source-newevents]], [[source-text-events-xml]]):

1. *What at first seems to be a simple nebula is actually filled with a good amount of debris from a brutal exchange between several ships. Wreckage drifts by your screens and tumbles into the depths of the nebula to be lost to sight. It's hard to determine who the combatants were without closer investigation.*
2. *You have jumped into the aftermath of what seems to have been a brutal exchange between several ships. Wreckage drifts by your screens, and you can still see the remains of the dying ships sparking and breaking apart. It's hard to determine who the combatants were without closer investigation.*

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | **(Improved Sensors)** Use your Sensors to scan the wreckage. | `req="sensors" lvl="2"` `max_group="0"` | *"You scan the battlefield, and with the aid of your Sensors, you are able to salvage a moderate amount of material from the wreckage. You prepare to jump."* → `<autoReward level="MED">stuff</autoReward>` | 100% |
| 2 | **(Advanced Sensors)** Use your Sensors to scan the wreckage. | `req="sensors" lvl="3"` `max_group="0"` | Loads `WRECKAGE_SCANNED` — two entries, below. | — |
| 3 | Investigate the battlefield. | — (`hidden="true"`) | Loads `WRECKAGE_INVESTIGATE` — nine entries, below. | — |
| 4 | Ignore the wreckage and continue on. | — | `<event/>` — nothing happens. | 100% |

### `WRECKAGE_SCANNED` (Sensors 3) — two entries, no repeats (1/2 each)
**Assuming uniform selection across list entries** ([[concept-event-list-weighting]]):

| Odds | Text | Effect |
|---|---|---|
| 1/2 | *You scan the battlefield, and with the aid of your Sensors, you are able to salvage a good amount of material from the wreckage. Well-stocked, you prepare to jump.* | `<autoReward level="HIGH">stuff</autoReward>` |
| 1/2 | *You scan the battlefield and find a prototype military vessel in the debris! The crew has been killed, but their working prototype weapon array is still intact! You salvage it and bring it aboard.* | `<autoReward level="LOW">weapon</autoReward>` |

### `WRECKAGE_INVESTIGATE` (no Sensors needed) — nine entries, one repeated four times
`event_WRECKAGE_INVESTIGATE_1_text` appears **four times**, every other entry once.
**Assuming uniform selection across list entries** ([[concept-event-list-weighting]]),
that gives:

| Odds | Text | Effect |
|---|---|---|
| **4/9** | *You scan the battlefield, and find little remains. Disappointed, you prepare to jump.* | Nothing. |
| 1/9 | *You scan the battlefield, and are able to salvage some useful material from the wreckage.* | `<autoReward level="MED">stuff</autoReward>` |
| 1/9 | *As you approach the wreckage, a Mantis ship screams into the system... either sensing prey - or to finish the job its fellows started.* | `<ship load="MANTIS_FIGHT" hostile="true"/>` |
| 1/9 | *The wreckage appears to be a battle between Federation fighters and Rebel cruisers. Though outnumbered, it looks like the Federation fought valiantly. As you begin a more detailed scan of the wreckage, Rebel reinforcements arrive in the system and target your ship!* | `<ship load="REBEL" hostile="true"/>` |
| 1/9 | *As you approach the wreckage, a Zoltan ship makes its arrival. It immediately mistakes you for one of the attackers, declares you as hostile aggressors in violation of Zoltan space, and opens fire!* | `<ship load="ZOLTAN_SHIP" hostile="true"/>` |
| 1/9 | *As you approach the wreckage, a Slug ship makes its arrival. It hesitates for a moment, as if surprised to see anyone remaining, and then jumps away without a word. You resume scanning the system, wary of any other visitors.* | Nothing. |

Net: **5/9 nothing, 1/9 a medium haul, 3/9 a fight.** Fandom's `{{DuplicateEvent|4}}`
marker on the "little remains" line independently confirms the four-fold repetition
([[source-fandom-battlefield-wreckage]]).

### The three ships
All three give default rewards ([[source-events-ships]]):

| Ship | Blueprint | Surrender | Escape |
|---|---|---|---|
| `MANTIS_FIGHT` | `SHIPS_MANTIS` (crew 80% Mantis / 20% Engi) | none declared | none declared |
| `REBEL` | `SHIPS_REBEL` | **50%** at `min=2 max=3` → `PIRATE_SURRENDER` | 50% at `min=3 max=4` → `PIRATE_ESCAPE` |
| `ZOLTAN_SHIP` | `SHIPS_ZOLTAN` | none declared | none declared |

The `REBEL` figure follows [[concept-surrender-offers]] — `chance="0.5"` is the
probability the ship *keeps fighting*, so the surrender chance is 50%. Fandom renders the
same two bands as "50% escape at 30–40% hull, 50% surrender at 20–30% hull"
([[source-fandom-battlefield-wreckage]]); that hull-percentage reading is Fandom's
interpretation of `min`/`max`, not a file claim.

## Blue Options
- **Sensors level 2** (`req="sensors" lvl="2"`) — a guaranteed `MED` `stuff` haul with no
  fight risk. This is the single best argument for buying Sensors 2 on a ship that starts
  with Sensors 1.
- **Sensors level 3** (`req="sensors" lvl="3"`) — upgrades that to a 1/2 chance of a `HIGH`
  `stuff` haul and a 1/2 chance of a **free weapon** (with `LOW` scrap attached).

Both carry `max_group="0"`. On [[event-trade-scrap-for-upgrades]] Fandom describes
`max_group` as the mechanism that picks the right level within a group of choices, which
would mean a Sensors-3 ship sees only the Advanced option. Neither source states this
outright for `WRECKAGE_EVENT` — left as an open question below.

A commented-out duplicate of the Sensors-2 choice header sits immediately above the event
in the file; it is inert ([[source-newevents]]).

### Fandom's reward figures
Fandom expands the `autoReward` levels into concrete resource bands
([[source-fandom-battlefield-wreckage]]): medium `stuff` = fuel 2–4, missiles 2–4, drone
parts 1; high `stuff` = fuel 3–6, missiles 4–8, drone parts 1–2, each with some scrap.
Those numbers are not in `newEvents.xml` — the files say only `LOW` / `MED` / `HIGH` — so
they are recorded here as Fandom's claim.

## Rewards & Risks
- Sensors 2: guaranteed medium resources-plus-scrap, zero risk.
- Sensors 3: guaranteed *either* a large haul *or* a weapon, zero risk.
- No Sensors: 5/9 nothing, 1/9 medium haul, 3/9 a fight with default rewards. Two of the
  three fights (`MANTIS_FIGHT`, `ZOLTAN_SHIP`) declare no surrender and no escape, so they
  must be fought to a finish.
- Ignoring costs nothing.

## Strategy Notes
- *Opinion:* this event is the strongest single reason Sensors upgrades pay for
  themselves, and it is repeatable — Engi sectors allocate `NEUTRAL_ENGI` 4–7 times, so
  multiple visits per sector are realistic.
- Without Sensors, "Investigate" is a real gamble: it is 3/9 to start an unavoidable
  fight for a 1/9 shot at a medium haul. On a healthy ship that trade is fine (default
  rewards from a fight usually beat a medium haul); on a damaged one, take choice 4.
- Slug crew do **not** help here despite the nebula flavour — the only gate is Sensors.

## Related
- [[event-nebula-wreckage]] — the other salvage-the-debris event, easily confused with
  this one
- [[event-terraforming-scan]], [[event-rebel-checkpoint]] — the other AE additions to the
  `NEUTRAL` / `OVERRIDE_NEUTRAL` filler pool
- [[event-mantis-fight]], [[event-rebel-fight]], [[event-zoltan-fight]] — the three fights
  it can start
- [[concept-event-list-weighting]] — basis for the 4/9 and 1/2 figures
- [[concept-surrender-offers]] — how the `REBEL` surrender number is read
- [[event-pirate-surrender]] — the shared `PIRATE_SURRENDER` aftermath this hull loads
- [[event-pirate-escape]] — the shared `PIRATE_ESCAPE` aftermath this hull loads

## Open Questions
- [ ] Whether event-list selection is truly uniform.
- [ ] Does `max_group="0"` hide the Sensors-2 option from a Sensors-3 ship, or are both
      shown?
- [ ] Which weapon pool does `autoReward level="LOW" weapon` draw from?
- [ ] Confirm Fandom's `stuff` resource bands against a run.

## Sources
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-events-engi]] (per raw/gamedata/events_engi.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-battlefield-wreckage]] (per raw/wiki/battlefield-wreckage.md)
