---
id: event-start-beacon-nebula
type: event
event_name: START_BEACON_NEBULA
sectors: [[[sector-uncharted-nebula]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [nebula, arrival, flavour, no-choice, no-reward, uncharted-nebula]
---

# Start beacon (nebula) — `START_BEACON_NEBULA`

## Summary
The arrival text for [[sector-uncharted-nebula]]. Pure flavour: six strings, no choices, no
mechanics. It fires once, on the beacon you enter the sector at, and exists to tell you
your sensors are about to stop working.

## Trigger & Where It Appears
- **Not in any event list** — it is wired in directly by `sector_data.xml`, which gives
  `NEBULA_SECTOR` the line `<startEvent>START_BEACON_NEBULA</startEvent>`
  ([[source-sector-data-xml]]). That is why the batch shows `lists: []`.
- **[[sector-uncharted-nebula]] only.** It is the sole sector using this start event; the
  Slug nebula sectors use `START_BEACON_SLUG`, and every other sector type has its own
  ([[source-sector-data-xml]]). `CIVILIAN_SECTOR` has none at all — its `startEvent` line
  is commented out with the note `JUSTIN TO DO`.
- Fires automatically on arrival at the sector's first beacon. It is not a beacon type you
  can route toward or avoid.
- No `unique` attribute — but the start beacon happens once per sector, so it fires once
  per Uncharted Nebula visited.
- **No Fandom page joins this event.** The slug here is derived from the in-game id rather
  than a wiki title.
- The generic equivalent for ordinary sectors is `START_BEACON` in
  `raw/gamedata/events.xml` ([[source-events-xml]]).

## Text
The prose is drawn from the `START_BEACON_NEBULA` text list and **varies across six
strings** ([[source-events-nebula]], [[source-text-events-xml]]):

> This nebula must have been an important hub at one point; placing all of these jump
> beacons would be no easy task. However, now it's hardly navigable.

> Nebulas were always dangerous places. Many electronics fail in these clouds. You will
> have to tread lightly.

> You've entered a sector thick with nebulas. You'll have to navigate on instinct.

> You've entered a nebula-rich sector. You may put a few light years on the fleet, but
> that's only useful if you make it out the other side.

> Thanks to the high nebula density of this sector very little of it has been charted, and
> rumours of what lurks in the depths abound.

> The gases that make up the nebulas in this sector threaten to impair your systems; but
> you have to press on.

The fourth string is the game stating the sector's actual trade-off in plain terms: nebula
beacons slow the Rebel fleet, at the cost of fighting blind.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(none — the event has no `<choice>` elements)_ | — | Nothing happens. Flavour text only. | 100% |

The complete event body is `<text load="START_BEACON_NEBULA"/>`
([[source-events-nebula]]) — it does not even carry an `<environment>` tag.

## Blue Options
None.

## Rewards & Risks
Neither.

## Strategy Notes
- Nothing to do. Recorded because it is a real, reachable, shipped event with its own
  `event_name` join key, and because its text is the only in-game statement of why anyone
  would route into [[sector-uncharted-nebula]] at all.

## Related
- [[event-store-in-nebula-uncharted]] — the sector's guaranteed store
- [[event-empty-nebula-beacon]] — its four guaranteed empties
- [[sector-uncharted-nebula]]

## Open Questions
- [ ] Whether the six variants are equally weighted.

## Sources
- [[source-events-nebula]] (per raw/gamedata/events_nebula.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
