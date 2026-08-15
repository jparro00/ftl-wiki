---
id: event-empty-nebula-beacon
type: event
event_name: NEBULA_EMPTY
sectors: [[[sector-civilian-sector]], [[sector-federation-space]], [[sector-pirate-controlled-sector]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]], [[sector-uncharted-nebula]], [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: nebula
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 9
tags: [nebula, empty, filler, no-choice, no-reward]
---

# Empty nebula beacon — `NEBULA_EMPTY`

## Summary
Nothing happens, nine different ways. `NEBULA_EMPTY` is the nebula pool's filler: a text
list, an environment tag, and no mechanics whatsoever. Its value to a run is negative
only in the sense that a jump was spent — and positive in that the fleet advanced 20% less
than it would have from a non-nebula beacon.

## Trigger & Where It Appears
- Beacon: nebula (`<environment type="nebula"/>`).
- No `unique` attribute — it repeats freely, and it is deliberately over-weighted.
- **Directly allocated** in [[sector-uncharted-nebula]] at `min=4 max=4`
  ([[source-sector-data-xml]]) — four guaranteed empty beacons per Uncharted Nebula.
- Additionally reachable through `NEBULA` ([[source-newevents]]), `NEBULA_PIRATE`
  ([[source-events-pirate]]), `NEBULA_REBEL` ([[source-events-rebel]]) and
  `NEBULA_ZOLTAN` ([[source-events-zoltan]]). It is the **first entry in every one of
  those lists**, and `NEBULA_ZOLTAN` lists it **twice**, doubling its weight there.
- Long-range scanners show no ship ([[source-fandom-empty-nebula-beacon]]).

## Text
The prose is drawn from the `NEBULA_EMPTY_LIST` text list and **varies across nine
strings** ([[source-events-nebula]], [[source-text-events-xml]]) — no single one is *the*
event text. All nine are transcribed on [[source-fandom-empty-nebula-beacon]]. A few:

> You can't see anything through the thick gases surrounding your ship. Without knowing
> what is out there, all you can do is wait for your FTL to charge.

> Your crew are constantly looking out of the windows, checking for hostiles. They jump at
> every creak and moan of the ship. The tension is almost palpable...

> With the sensors down, you spend a good deal of time staring out the window. It is, you
> must admit, rather beautiful here.

> There's nothing here, save for vast swirls of gas reflecting rays from a distant sun.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(none — the event has no `<choice>` elements)_ | — | Nothing happens. | 100% |

The complete event body is `<text load="NEBULA_EMPTY_LIST"/>` and
`<environment type="nebula"/>` ([[source-events-nebula]]).

## Blue Options
None.

## Rewards & Risks
Neither. The only cost is the jump itself.

## Strategy Notes
- Four of these are guaranteed in [[sector-uncharted-nebula]], and it is the lead entry in
  four other nebula pools — a large fraction of nebula beacons in any sector resolve to
  nothing at all. That is the structural argument against routing through nebula-heavy
  space for loot: the pool is diluted by design ([[source-sector-data-xml]],
  [[source-newevents]]).
- The counter-argument is the fleet-pursuit discount for jumping out of a nebula beacon,
  noted on [[source-fandom-rebel-fight-in-plasma-storm]] (80% of normal advance in Slug
  sectors). That figure is Fandom's; no game file read here states it.

## Related
- [[event-boarders-humans-in-nebula]] — the same "empty" long-range-scanner signature,
  with boarders
- [[event-start-beacon-nebula]] — the other pure-text nebula event
- [[sector-uncharted-nebula]]

## Open Questions
- [ ] Whether the nine text variants are equally weighted (the list states no weights).
- [ ] The exact nebula fleet-pursuit discount, and whether it applies outside Slug sectors.

## Sources
- [[source-events-nebula]] (per raw/gamedata/events_nebula.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-empty-nebula-beacon]] (per raw/wiki/empty-nebula-beacon.md)
