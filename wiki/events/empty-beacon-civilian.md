---
id: event-empty-beacon-civilian
type: event
event_name: NOTHING
sectors: [[[sector-civilian-sector]], [[sector-federation-space]]]
beacon_type: empty
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [empty, filler, no-choice]
---

# Empty beacon (Civilian) — `NOTHING`

## Summary
The baseline empty beacon: you arrive, a line of scenery text plays, nothing happens, and
you jump on. It is the ancestor of every sector-flavoured `NOTHING_*` variant
(`NOTHING_ROCK`, `NOTHING_SLUG`, `NOTHING_ZOLTAN`, …) and is the version used by the
generic and civilian sectors.

## Trigger & Where It Appears
- Beacon: **empty**. The event has no choices and no effects at all — it is one line:

  ```xml
  <event name="NOTHING">
      <text load="NOTHING"/>
  </event>
  ```

  ([[source-events-xml]], line 365) — note this lives in `events.xml`, not `newEvents.xml`;
  `newEvents.xml` only references the slot name in its `eventCounts` blocks.
- Allocated directly by `sector_data.xml` as a sector event slot, `min=1 max=2`, in
  `STANDARD_SPACE` ([[sector-federation-space]]) and `CIVILIAN_SECTOR`
  ([[sector-civilian-sector]]) ([[source-sector-data-xml]]). Every other sector type uses
  its own `NOTHING_<FACTION>` slot instead.
- Not `unique` — one or two per qualifying sector.

> ⚠️ **CONTRADICTION:** sector scope.
> - Fandom titles the page "Empty beacon (Civilian)" and scopes it to the Civilian Sector
>   only ([[source-fandom-empty-beacon-civilian]]).
> - `sector_data.xml` allocates the `NOTHING` slot in `STANDARD_SPACE` as well
>   ([[source-sector-data-xml]]).
>
> Trusting the game files (`high` vs `medium`). This looks like a naming artefact rather
> than a real disagreement — the Fandom page needed a disambiguating title and picked the
> civilian one.

## Text
`[varies: textList NOTHING]` — nine variants, drawn at random
([[source-events-xml]], [[source-text-events-xml]]). Several carry image directives:
variants 1, 2, 8 and 9 force `planet="NONE"`, and variants 4, 5 and 7 force
`planet="PLANET_POPULATED_SMALL"`; variant 1 also sets `back="BG_DARK"`.

Representative variants:

> Your jump leads you to nothing but empty space. This Jump Beacon serves no purpose other
> than as a connection.

> The nearby planet shows sign of habitation and great beauty. A rudimentary automated
> planetary defense system is looping its message into space: "Warning! Quarantine Level 5
> in effect under FHA Act 22, article 11.2. Warning! Quarantine Level 5..."

> Your jump leads to a remarkable binary star system. The view is beautiful, but there is
> nothing else around.

Fandom lists all nine ([[source-fandom-empty-beacon-civilian]]) and they match the
`text_NOTHING_1` … `text_NOTHING_9` strings exactly.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none — the event defines no `<choice>` elements)* | — | Text plays, nothing happens. | 100% |

## Blue Options
None.

## Rewards & Risks
Neither. The beacon exists to be a map connection and to pace the sector.

## Strategy Notes
- Useful only as free FTL charge time and a safe place to repair breaches or put out
  fires. Because `sector_data.xml` guarantees one to two of these per qualifying sector,
  a civilian or generic sector always has at least one dead beacon in it.
- Its presence is also a small piece of routing information: an empty beacon is one fewer
  chance at scrap in a sector, so a map with several visible dead ends is worth less.

## Related
- [[event-empty-beacon-slug]], [[event-empty-beacon-rock]], [[event-empty-beacon-zoltan]],
  [[event-empty-beacon-engi]], [[event-empty-beacon-mantis]], [[event-empty-beacon-pirate]],
  [[event-empty-beacon-rebel]], [[event-empty-beacon-crystal]], [[event-empty-beacon-lanius]]
  — the sector-flavoured variants
- [[event-empty-nebula-beacon]] — the nebula equivalent
- [[sector-civilian-sector]], [[sector-federation-space]]

## Open Questions
- [ ] Whether the nine text variants are equally weighted (the `textList` states no
      weights).
- [ ] Whether the AE build changes this event at all — no `<!--DLC-->` marker appears on it
      and no `OVERRIDE_NOTHING` list exists in `dlcEventsOverwrite.xml`, which is why
      `version` is recorded as `both`.

## Sources
- [[source-events-xml]] (per `raw/gamedata/events.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-empty-beacon-civilian]] (per `raw/wiki/empty-beacon-civilian.md`)
