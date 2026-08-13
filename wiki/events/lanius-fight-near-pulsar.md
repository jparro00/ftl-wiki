---
id: event-lanius-fight-near-pulsar
type: event
event_name: LANIUS_FIGHT_PULSAR
sectors: [[[sector-abandoned-sector]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [lanius, combat, no-choice, pulsar, hazard, unique, advanced-edition]
---

# Lanius fight near pulsar — `LANIUS_FIGHT_PULSAR`

## Summary
A `LANIUS_SHIP` fight inside a pulsar's EM pulses. No choices. Identical to
[[event-lanius-fight]] except for `<environment type="pulsar"/>` and the flavour text,
which makes a point of the Lanius not caring about the hazard.

## Trigger & Where It Appears
- Sector: [[sector-abandoned-sector]] only.
- List: `HOSTILE_ENVIRONMENT_LANIUS`, allocated `min=1 max=2` per sector
  ([[source-sector-data-xml]]); three members, so **1/3** *assuming uniform selection
  across list entries* ([[source-dlcevents-anaerobic]]).
- `unique="true"` — at most once per sector.
- Long-range scanners show a ship **and** a pulsar
  ([[source-fandom-lanius-fight-near-pulsar]]).

> **AE-only.** Pulsar hazards themselves are an Advanced Edition addition, as is the
> sector and the file this event lives in.

## Text
> There appears to be some sort of research station near a pulsar, although it's hard to
> tell since a portion of it has been melted. The Lanius ship that has been working at it
> moves in to intercept you, totally oblivious to the threat of EM pulses.

(`event_LANIUS_FIGHT_PULSAR_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(none)_ | — | Immediate combat with `LANIUS_SHIP` under pulsar EM pulses; **default Lanius rewards**. | 100% |

Reward tables: see [[event-lanius-fight]].

## Blue Options
None.

## Rewards & Risks
- Reward: default Lanius rewards ([[event-lanius-fight]]).
- Risk: pulsar pulses knock out systems and drop shields on both ships periodically. The
  event text's joke — the Lanius being "oblivious" — has no mechanical effect recorded in
  any source here; the hazard is symmetric as far as the XML says.

## Strategy Notes
- Unavoidable once entered. Ships that lean on shields suffer most; boarding crews benefit
  from the enemy's systems going down too.

## Related
- [[event-lanius-fight]] — the plain version and the reward tables
- [[event-lanius-fight-in-asteroid-field]],
  [[event-lanius-fight-with-friendly-asb-support]] — the rest of the hazard list
- [[entity-lanius]], [[sector-abandoned-sector]]
- [[event-lanius-surrender]] — the `LANIUS_SURRENDER` aftermath this hull loads

## Open Questions
- [ ] Whether the pulsar's effect is genuinely symmetric (the text implies the Lanius are
      unbothered; the XML gives `environment type="pulsar"` with no `target`).

## Sources
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-lanius-fight-near-pulsar]] (per raw/wiki/lanius-fight-near-pulsar.md)
