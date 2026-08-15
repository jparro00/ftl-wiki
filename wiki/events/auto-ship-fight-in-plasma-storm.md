---
id: event-auto-ship-fight-in-plasma-storm
type: event
event_name: STORM_AUTO
sectors: [[[sector-civilian-sector]], [[sector-federation-space]], [[sector-pirate-controlled-sector]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]], [[sector-uncharted-nebula]], [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: nebula
hostile: true
blue_options: [[[item-engines]], [[item-cloaking]]]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 8
tags: [plasma-storm, rebel, auto-ship, blue-option, engines, cloaking, optional-fight, unique]
---

# Auto-ship fight in plasma storm — `STORM_AUTO`

## Summary
The same Rebel drone as [[event-auto-ship-fight-in-nebula]], but in a plasma storm and
with three ways out. It is the cleanest **tiered blue option** in the nebula file: Engines
3–5 gives you a coin flip, Engines 6+ gives you a guarantee, and Cloaking gives you a
guarantee with no level requirement at all.

## Trigger & Where It Appears
- Beacon: **plasma storm** (`<environment type="storm"/>`).
- `unique="true"` — once per run.
- Lists: `NEBULA` ([[source-newevents]]), `NEBULA_HOSTILE` ([[source-events-nebula]]) and
  `NEBULA_REBEL` ([[source-events-rebel]]) — reaching Federation Space and Civilian via
  `NEBULA`, both Rebel sectors via `NEBULA_REBEL`, Pirate and Zoltan space through the
  nested `NEBULA_REBEL` entry, and [[sector-uncharted-nebula]] via `NEBULA_HOSTILE`
  ([[source-sector-data-xml]]).
- Long-range scanners show **no ship** despite the fight
  (`LRSmap=noship+plasmastorm`, [[source-fandom-auto-ship-fight-in-plasma-storm]]).

## Text
> You jump into a sector of the nebula beset by a plasma storm. An automated Rebel scout
> stationed at the beacon moves in to attack.

(`event_STORM_AUTO_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Prepare to fight. | — | `<ship load="REBEL_AUTO" hostile="true"/>` — fight the auto-ship. | 100% |
| 2 | **(Engines)** Attempt to out-run it. | `req="engines" lvl="3"` (`max_group="0"`, `hidden="true"`) | `STORM_AUTO_ESCAPE`, two entries — **(a)** *"You successfully lose the ship in the storm."* → nothing; **(b)** *"Despite your advanced engines you are unable to shake them; you turn and prepare for a fight."* → fight `REBEL_AUTO`. | unknown (2-entry list) |
| 3 | **(Improved Engines)** Attempt to out-run it. | `req="engines" lvl="6"` (`max_group="0"`, `hidden="true"`) | *"You successfully lose the ship in the storm."* — guaranteed clean escape. | 100% |
| 4 | **(Cloaking)** Use your cloaking to escape. | `req="cloaking"`, no level, `hidden="true"` | *"By using your advanced cloaking system you easily lose your pursuer in the storm."* — guaranteed clean escape. | 100% |

Choices 2 and 3 share `max_group="0"`, which is how the file prevents both Engines tiers
from appearing at once. [[source-fandom-auto-ship-fight-in-plasma-storm]] reads the
resulting behaviour as **Engines 3-5 → choice 2, Engines 6+ → choice 3**, which is the
correct interpretation of two `req="engines"` choices with different `lvl` values in the
same group.

The `REBEL_AUTO` ship carries **no surrender and no escape**, only
`<destroyed load="DESTROYED_DEFAULT"/>` → `autoReward level="MED">standard`
([[source-events-ships]], [[source-events-xml]]).

## Blue Options
- **[[item-engines]] level 3** — a gamble; half the branch is the fight you were avoiding.
- **[[item-engines]] level 6** — guaranteed escape. Engines 6 is a deep investment, so
  this is a genuine reward for it rather than a token gate.
- **[[item-cloaking]]** (any level) — guaranteed escape with **no level requirement**,
  making Cloaking strictly better than Engines here regardless of tier.

## Rewards & Risks
- Fighting pays `MED` / `standard` — the same as the plain nebula version of this fight.
- Escaping pays **nothing**. Every blue option in this event trades reward for safety.
- Risk: a plasma storm environment for the duration of the fight, on top of a nebula
  beacon's sensor blackout.

## Strategy Notes
- The blue options are *not* obviously correct here. Unlike
  [[event-auto-ship-warning-in-nebula]] there is no fleet-advance penalty for staying, and
  an auto-ship is a comparatively soft target — so on a healthy ship, choice 1 is the
  higher-value line and the escapes are the panic buttons. *(Opinion, derived from the
  reward structure; no source recommends a line.)*
- Engines 3 is the one option to be wary of: it costs you the choice and still leaves a
  chance of the fight, with nothing gained if it fails.

## Related
- [[event-auto-ship-fight-in-nebula]] — the identical fight with no escape options
- [[event-auto-ship-warning-in-nebula]] — the auto-ship you *must* kill
- [[event-rebel-fight-in-plasma-storm]] — the crewed storm equivalent, also with no choices
- [[item-engines]], [[item-cloaking]], [[concept-rebel-fleet-advance]], [[sector-uncharted-nebula]]

## Open Questions
- [ ] Weights inside `STORM_AUTO_ESCAPE` (2 entries, none stated).
- [ ] Whether a plasma storm's system-drain effect applies to the player's ship during this
      fight — no source read here says.

## Sources
- [[source-events-nebula]] (per raw/gamedata/events_nebula.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-auto-ship-fight-in-plasma-storm]] (per raw/wiki/auto-ship-fight-in-plasma-storm.md)
