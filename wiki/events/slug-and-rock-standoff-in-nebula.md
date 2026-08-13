---
id: event-slug-and-rock-standoff-in-nebula
type: event
event_name: ROCK_SLUG_ARGUMENT_NEBULA
sectors: [[[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: nebula
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [slug, rock, nebula, unique, reactor-upgrade, advanced-edition]
---

# Slug and Rock standoff in nebula — `ROCK_SLUG_ARGUMENT_NEBULA`

## Summary
A two-line nebula wrapper around [[event-rock-and-slug-standoff]]. You detect ships running
hot somewhere in the murk; approaching loads the Rock/Slug reactor-debt standoff intact,
with the nebula environment still in effect. All the substance is on the parent page — this
event exists so the Rock-sector encounter can also appear in Slug space.

## Trigger & Where It Appears
- `unique="true"` — once per run.
- Beacon: **nebula**. The event declares `<environment type="nebula"/>`
  ([[source-newevents]], line 1514).
- Sole list membership: `NEBULA_NEUTRAL_SLUG`, marked `<!-- DLC - newEvents-->`
  ([[source-events-slug]], line 91) → [[sector-slug-controlled-nebula]] and
  [[sector-slug-home-nebula]] ([[source-sector-data-xml]]).
- Fandom agrees on scope and marks the location box `nebula=true`
  ([[source-fandom-slug-and-rock-standoff-in-nebula]]).

## Text
> You detect multiple ships running at maximum power nearby, but you can't see anything
> through this thick nebula.

(`event_ROCK_SLUG_ARGUMENT_NEBULA_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Get closer. | — | `<event load="ROCK_SLUG_ARGUMENT"/>` — loads [[event-rock-and-slug-standoff]] whole, including its choices, its `ROCK_SLUG_COMMAND` pool, the `ROCK_SLUG_REACTOR_SHIP` fight and the `ROCK_SLUG_GRATEFUL` reward pool. | 100% |
| 2 | Ignore them. | — | `<event/>` — nothing happens. | 100% |

Because the nebula environment is declared on **this** event rather than on the loaded one,
it persists into the standoff — Fandom states the same
([[source-fandom-slug-and-rock-standoff-in-nebula]]). Any fight that results from the
standoff is therefore fought inside a nebula, with sensors suppressed.

**Everything downstream of "Get closer" is documented on
[[event-rock-and-slug-standoff]]** — the debt, the 10–15 scrap payoff, the demand branch's
1/3 fight / 1/3 agreement / 1/3 reactor explosion split, and the free-or-paid reactor bar.

## Blue Options
None on this event; none on the loaded one either.

## Rewards & Risks
Identical to [[event-rock-and-slug-standoff]] — up to a free reactor bar, down to a Rock
ship fight or 3 hull plus two random system hits — with the added handicap that it all
happens inside a nebula.

## Strategy Notes
- *(Opinion.)* The nebula tag is the only difference that matters. If the standoff sends you
  into the `ROCK_SLUG_REACTOR_SHIP` fight here, you fight it blind, so the "pay off the
  debt" line is more attractive in this version than in the Rock-sector one.
- Because both events are `unique="true"` and are separate ids, encountering one does not
  by itself consume the other — but the shared reward is a reactor bar either way.

## Related
- [[event-rock-and-slug-standoff]] — the parent event; all outcomes live there
- [[entity-rock-men]], [[entity-slugs]]
- [[item-reactor]]

## Open Questions
- [ ] Whether `unique="true"` on both ids means a run can genuinely see the standoff twice
      (once per sector type) — the files do not say.

## Sources
- [[source-newevents]] (per `raw/gamedata/newEvents.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-events-slug]] (per `raw/gamedata/events_slug.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-slug-and-rock-standoff-in-nebula]] (per `raw/wiki/slug-and-rock-standoff-in-nebula.md`)
