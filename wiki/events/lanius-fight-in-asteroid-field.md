---
id: event-lanius-fight-in-asteroid-field
type: event
event_name: LANIUS_FIGHT_ASTEROID
sectors: [[[sector-abandoned-sector]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [lanius, combat, no-choice, asteroid-field, hazard, unique, advanced-edition]
---

# Lanius fight in asteroid field — `LANIUS_FIGHT_ASTEROID`

## Summary
A `LANIUS_SHIP` fight with an asteroid field on top. No choices, no avoid, no blue
option — the only thing that distinguishes it from [[event-lanius-fight]] is
`<environment type="asteroid"/>`, which means incoming rocks for the whole engagement.

## Trigger & Where It Appears
- Sector: [[sector-abandoned-sector]] only.
- List: `HOSTILE_ENVIRONMENT_LANIUS`, allocated `min=1 max=2` beacons per sector
  ([[source-sector-data-xml]]). That list has exactly three members —
  `LANIUS_FIGHT_ASTEROID`, `LANIUS_FIGHT_PULSAR`, `LANIUS_NOBOARDERS_PDS` — so **1/3**
  each *assuming uniform selection across list entries* ([[source-dlcevents-anaerobic]]).
  This hazard list exists in no other sector.
- `unique="true"` — at most once per sector.
- Long-range scanners show a ship **and** an asteroid field
  ([[source-fandom-lanius-fight-in-asteroid-field]]).

> **AE-only.** Both the sector and the source file are Advanced Edition content; there is
> no vanilla form.

## Text
> This beacon appears to have been set up within an asteroid field to access a mining
> settlement. However, half of the settlement has been disassembled by a number of Lanius
> scavengers. Their military escort moves in to scare you off.

(`event_LANIUS_FIGHT_ASTEROID_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(none)_ | — | Immediate combat with `LANIUS_SHIP` in an asteroid field; **default Lanius rewards**. | 100% |

The full `LANIUS_SHIP` surrender / escape / destroyed / dead-crew tables — including the
1/8 free crew member — are documented on [[event-lanius-fight]].

## Blue Options
None.

## Rewards & Risks
- Reward: default Lanius rewards ([[event-lanius-fight]]).
- Risk: asteroids hit both ships, but they hit *you* while you are also under fire, and
  they punish a slow kill. Defence drones and high engines mitigate; there is no option to
  disengage.

## Strategy Notes
- Unavoidable once entered — the danger is committed before you see the choice screen,
  because there is no choice screen.

## Related
- [[event-lanius-fight]] — the plain version, and the `LANIUS_SHIP` reward tables
- [[event-lanius-fight-near-pulsar]], [[event-lanius-fight-with-friendly-asb-support]] —
  the other two members of `HOSTILE_ENVIRONMENT_LANIUS`
- [[entity-lanius]], [[sector-abandoned-sector]]
- [[event-lanius-surrender]] — the `LANIUS_SURRENDER` aftermath this hull loads

## Open Questions
- [ ] Numeric values behind default Lanius rewards.

## Sources
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-lanius-fight-in-asteroid-field]] (per raw/wiki/lanius-fight-in-asteroid-field.md)
