---
id: concept-empty-beacons
type: concept
version: both
first_seen: 2026-08-13
last_updated: 2026-08-13
sources: 4
related_events: []
tags: [mechanics, filler, pool-structure, worldbuilding, no-choice]
---

# Empty beacons — the events where nothing happens

## Definition & Context

Every sector has an event whose entire job is to be **nothing**: a line of flavour text, no
choices, no ship, no reward. There are **ten `NOTHING*` events**, one per faction flavour, plus
several nebula and fuel variants ([[source-events-xml]] and siblings):

`NOTHING` · `NOTHING_CRYSTAL` · `NOTHING_ENGI` · `NOTHING_LANIUS` · `NOTHING_MANTIS` ·
`NOTHING_PIRATE` · `NOTHING_REBEL` · `NOTHING_ROCK` · `NOTHING_SLUG` · `NOTHING_ZOLTAN`

plus `NEBULA_EMPTY`, `NEBULA_NOTHING_SLUG`, `FUEL_NOTHING`, `FUEL_NOTHING_DISTRESS`.

## Why they exist

**They are pool ballast.** A sector's event allocation reserves a number of beacons; something
has to occupy the slots that are not encounters. Without a `NOTHING` event the pool would have
to be all content, which would make every jump significant and exhaust the interesting events
far too quickly. See [[concept-sector-event-allocation]].

That gives them a real, if indirect, mechanical role: **an empty beacon is the cost of the
Rebel fleet advancing one more step for nothing.** They are the reason exploring is a gamble
rather than a guaranteed profit.

## They are also where the worldbuilding lives

Because they carry no mechanics, the flavour text is unconstrained, and it is some of the
densest writing in the game. The counts vary by faction — [[event-empty-beacon-engi]] has ten
strings, [[event-empty-beacon-zoltan]] seven, [[event-empty-beacon-lanius]] six vignettes about
what the Lanius have already eaten.

For several factions **the empty beacon is the primary source** of what the wiki knows about
them, because the encounter events are all combat. [[entity-lanius]] and [[entity-zoltan]] both
draw on their empty-beacon strings.

## The variants that are not quite empty

- **[[event-empty-beacon-last-stand]]** (`BOSS_FLEETS_FED`) — the safe draw in
  [[sector-the-last-stand]]: a beacon the Rebel fleet has not reached, still Federation-held.
  Mechanically inert, strategically the best result in that sector.
- **[[event-abandoned-station]]** (`EMPTY_STATION2`) — looks like an empty beacon and is not.
  Six equally likely outcomes, three harmless and three not.
- **[[event-lanius-empty-distress-beacon-1]]** and **-2** — *distress* beacons that resolve to
  nothing, which is worse than an empty beacon because you spent a jump on a promise.

## Implications For Play

- **Nothing to decide, which is the point.** An empty beacon has no choices at all — the
  renderer that builds event cards produces a header and no tree.
- **The distress-that-is-empty variants are the real cost.** A `NOTHING` on an ordinary beacon
  is a small loss; a distress signal that resolves to nothing cost you a deliberate detour.
- **Their frequency is a sector-quality signal.** A sector whose pool is thin draws them more
  often — see [[concept-sector-event-allocation]].

## Where It Applies
[[event-empty-beacon-civilian]], [[event-empty-beacon-engi]], [[event-empty-beacon-mantis]],
[[event-empty-beacon-rock]], [[event-empty-beacon-slug]], [[event-empty-beacon-zoltan]],
[[event-empty-beacon-rebel]], [[event-empty-beacon-pirate]], [[event-empty-beacon-crystal]],
[[event-empty-beacon-lanius]], [[event-empty-nebula-beacon]],
[[event-empty-nebula-beacon-slug]], [[event-empty-beacon-last-stand]].

## Related
- [[concept-sector-event-allocation]] — the pools these fill
- [[concept-start-beacons]] — the other structurally-required no-choice event
- [[concept-rebel-fleet-advance]] — what an empty beacon actually costs you
- [[concept-event-list-weighting]] — how often they come up

## Open Questions
- [ ] Whether the flavour strings within one `NOTHING` event are equally weighted.
- [ ] Whether any sector's allocation guarantees a minimum number of empty beacons, or whether
      they simply fill whatever the content events do not.
- [ ] Whether `NEBULA_NOTHING_TEST` is a live event or a development stub.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
