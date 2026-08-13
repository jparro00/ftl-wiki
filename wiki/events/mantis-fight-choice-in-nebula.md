---
id: event-mantis-fight-choice-in-nebula
type: event
event_name: NEBULA_MANTIS_CHOICE
sectors: [[[sector-uncharted-nebula]]]
beacon_type: nebula
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [nebula, mantis, optional-fight, default-rewards, unique]
---

# Mantis fight choice in nebula — `NEBULA_MANTIS_CHOICE`

## Summary
A Mantis ship lets you go. You can accept that, or shoot first. Two choices, no blue
options, no requirements — a clean risk/reward decision with the reward being nothing more
than a Mantis ship's default drop.

## Trigger & Where It Appears
- Beacon: nebula (`<environment type="nebula"/>`).
- `unique="true"` — once per run.
- **[[sector-uncharted-nebula]] only.** Its single list is `NEBULA_NEUTRAL`
  ([[source-events-nebula]]), which `sector_data.xml` allocates only to `NEBULA_SECTOR`,
  at `min=7 max=8` ([[source-sector-data-xml]]). Fandom agrees
  ([[source-fandom-mantis-fight-choice-in-nebula]]).
- Arrives non-hostile: `<ship load="MANTIS_FIGHT" hostile="false"/>`. Long-range scanners
  show a ship.
- Flagged `NEW` in the file's own header comment, alongside `NEBULA_PIRATE`,
  `NEBULA_MANTIS_FIGHT`, `NEBULA_WEAPONS_TRADER`, `NEBULA_ROCK_RACIST` and
  `NEBULA_REBEL_CHASE` — a batch of later additions to the nebula pool
  ([[source-events-nebula]]).

## Text
> Navigating the fog blind, you practically bump hulls with a Mantis ship. They hail you:
> "Pah! This transgression will be overlooked. Nebula, very dangerous. Next time, humans
> all die."

(`event_NEBULA_MANTIS_CHOICE_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | There won't be a next time. Open fire! | — | `<ship hostile="true"/>` — fight the `MANTIS_FIGHT` ship already at the beacon. Default rewards. | 100% |
| 2 | This place is dangerous enough. Move on. | — | Empty `<event/>` — nothing happens. | 100% |

The `MANTIS_FIGHT` ship definition in `events_ships.xml` has **no surrender and no escape
element** — it fights to the end ([[source-events-ships]],
[[source-fandom-mantis-fight-choice-in-nebula]]). Its outcomes are
`<destroyed load="DESTROYED_DEFAULT"/>` (`autoReward level="MED">standard`) and
`<deadCrew load="DEAD_CREW_DEFAULT"/>` (mostly `MED` / `standard`, one `HIGH` entry). Crew
composition is `80% mantis / 20% engi` ([[source-events-ships]], [[source-events-xml]]).

## Blue Options
None — unusual for a nebula "neutral" event, most of which offer at least one system gate.

## Rewards & Risks
- Reward: default combat rewards only — `MED` / `standard` on destruction, or the
  `DEAD_CREW_DEFAULT` roll if you board and clear it (one of that list's five entries pays
  `HIGH`).
- Risk: a full Mantis warship that cannot be made to surrender or flee, fought **inside a
  nebula** with sensors down. Mantis crews are the game's strongest boarders.

## Strategy Notes
- Because the ship neither surrenders nor escapes, there is no partial outcome: you either
  destroy it or you take the whole fight. Fighting is a commitment, not a probe.
- Boarding it is the higher-EV line if you can win the crew fight, since `DEAD_CREW_DEFAULT`
  contains the only `HIGH` payout on offer here — but it is an 80%-Mantis crew, which is
  the worst possible boarding target. *(Opinion, derived from the ship definition; no
  source recommends either line.)*

## Related
- [[event-mantis-fight-in-nebula]] — the same ship, same sector pool, but forced
- [[event-mantis-fight]] — the non-nebula baseline using the same `MANTIS_FIGHT` ship
- [[event-mantis-fight-choice]] — the non-nebula equivalent of this decision
- [[entity-mantis]], [[sector-uncharted-nebula]]

## Open Questions
- [ ] Numeric values behind `DESTROYED_DEFAULT` / `DEAD_CREW_DEFAULT`.
- [ ] Whether the `80/20` mantis/engi crew split is rolled per crew slot or per ship.

## Sources
- [[source-events-nebula]] (per raw/gamedata/events_nebula.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-mantis-fight-choice-in-nebula]] (per raw/wiki/mantis-fight-choice-in-nebula.md)
