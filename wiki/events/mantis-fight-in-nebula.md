---
id: event-mantis-fight-in-nebula
type: event
event_name: NEBULA_MANTIS_FIGHT
sectors: [[[sector-civilian-sector]], [[sector-federation-space]], [[sector-uncharted-nebula]]]
beacon_type: nebula
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [nebula, mantis, no-choice, combat, default-rewards]
---

# Mantis fight in nebula — `NEBULA_MANTIS_FIGHT`

## Summary
A forced Mantis fight at a nebula beacon. Five flavour texts wrapped around
`<ship load="MANTIS_FIGHT" hostile="true"/>`. Mechanically identical to
[[event-mantis-fight]] apart from the environment tag — and to
[[event-mantis-fight-choice-in-nebula]] apart from having no choice.

## Trigger & Where It Appears
- Beacon: nebula (`<environment type="nebula"/>`).
- `unique="false"` — explicitly allowed to repeat.
- Lists: `NEBULA` ([[source-newevents]]) and `NEBULA_HOSTILE`
  ([[source-events-nebula]]) — reaching [[sector-federation-space]] (`NEBULA` 0–4),
  [[sector-civilian-sector]] (`NEBULA` 0–8) and [[sector-uncharted-nebula]]
  (`NEBULA_HOSTILE` 5–6) ([[source-sector-data-xml]]).
- Long-range scanners show a ship ([[source-fandom-mantis-fight-in-nebula]]).
- Flagged `NEW` in the file's header comment — a later addition to the nebula pool.

## Text
The prose is drawn from the `NEBULA_MANTIS_FIGHT` text list and **varies across five
strings** ([[source-events-nebula]], [[source-text-events-xml]]). All five are transcribed
on [[source-fandom-mantis-fight-in-nebula]]:

> Nebulas are known to be popular Mantis hunting grounds. Information you would have done
> well to heed here.

> A Mantis ship, lost in the storm, hails you. "Sensors are out. We have no local
> telemetry. We will take yours." You detect a power increase in their weapons systems.

> A Mantis ship hails you through the storm: "These are sacred Urggghtnag clan hunting
> grounds. You are prey." Shields up!

Two of the five say **"storm"** even though the event's environment tag is `nebula`, not
`storm` — the text list was evidently written to cover both and reused here
([[source-events-nebula]]).

Note the text list is *also* named `NEBULA_MANTIS_FIGHT`, the same as the event. Unlike the
`eventList` collisions that disable [[event-pirate-fight-in-nebula]] and
[[event-rebel-fight-in-nebula]], a `textList` sharing an event's name is harmless — no
source reports any problem, and Fandom does not flag this event as unreachable.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(none — the event has no `<choice>` elements)_ | — | Immediate combat with a Mantis ship (`ship load="MANTIS_FIGHT" hostile="true"`), default rewards. | 100% |

The `MANTIS_FIGHT` definition has **no surrender and no escape** —
`<destroyed load="DESTROYED_DEFAULT"/>` (`MED` / `standard`),
`<deadCrew load="DEAD_CREW_DEFAULT"/>`, crew `80% mantis / 20% engi`
([[source-events-ships]], [[source-fandom-mantis-fight-in-nebula]]).

## Blue Options
None.

## Rewards & Risks
- Reward: default combat rewards.
- Risk: a Mantis warship fought with sensors offline. No escape, no surrender, no choice —
  the highest-commitment encounter in the nebula pool.

## Strategy Notes
- Nothing to decide. The lever is route choice: [[sector-uncharted-nebula]] allocates 5–6
  `NEBULA_HOSTILE` beacons per sector and this is one of eight entries in that list
  ([[source-sector-data-xml]], [[source-events-nebula]]).

## Related
- [[event-mantis-fight-choice-in-nebula]] — same ship, same sector, but you may decline
- [[event-mantis-fight]] — the non-nebula baseline
- [[entity-mantis]], [[sector-uncharted-nebula]], [[sector-civilian-sector]]

## Open Questions
- [ ] Whether the five text variants are equally weighted.
- [ ] Numeric values behind `DESTROYED_DEFAULT`.

## Notes on sector coverage
> ⚠️ **CONTRADICTION:** [[source-fandom-mantis-fight-in-nebula]] lists two sectors
> (Civilian Sector, Uncharted Nebula). The game files add [[sector-federation-space]],
> because `sector_data.xml` allocates the `NEBULA` list — which contains
> `NEBULA_MANTIS_FIGHT` — to `STANDARD_SPACE` at `min=0 max=4`
> ([[source-sector-data-xml]], [[source-newevents]]).
>
> Trusting the game files (`high` vs `medium`). This is the same Federation-Space omission
> that recurs across the Fandom pages in this batch.

## Sources
- [[source-events-nebula]] (per raw/gamedata/events_nebula.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-mantis-fight-in-nebula]] (per raw/wiki/mantis-fight-in-nebula.md)
