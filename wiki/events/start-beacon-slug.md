---
id: event-start-beacon-slug
type: event
event_name: START_BEACON_SLUG
sectors: [[[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: empty
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [structural, start-beacon, varies-text, guaranteed, flavour]
---

# Start beacon (Slug) — `START_BEACON_SLUG`

## Summary
The arrival beacon for both Slug sectors. Mechanically empty — it prints one of five
scene-setting strings and nothing else. Guaranteed exactly once per Slug sector, because
both sector definitions name it as their `<startEvent>`.

## Trigger & Where It Appears
- Sectors: [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]
- Beacon: the sector's entry beacon. It is **not** drawn from any event list — both
  `SLUG_SECTOR` and `SLUG_HOME` declare
  `<startEvent>START_BEACON_SLUG</startEvent>` ([[source-sector-data-xml]]).
- Fires exactly once per Slug sector, on arrival, unconditionally.
- **No `<environment>` tag.** Despite both sectors being nebula sectors, the start beacon
  itself declares no nebula — unlike, for example, `NEBULA_NOTHING_SLUG`, which does
  ([[source-events-slug]]).
- **No Fandom page joins this event** — the community wiki does not document start
  beacons separately. Everything here comes from the game files.

## Text
`[varies: textList START_BEACON_SLUG]` — five entries, no repeats, so **assuming uniform
selection across list entries** ([[concept-event-list-weighting]]) each is 1/5
([[source-events-slug]]).

The five variants ([[source-text-events-xml]]):

1. *The only thing that can render a nebula more dangerous is if it's also home to the Slugs. This particular nebula is just that.*
2. *This nebula is home to the telepathic Slugs. They'd sell their own slime for a crate of scrap, but they much prefer to just take it.*
3. *You're told the Slug home world is somewhere in this nebula. You can't see them, but you know they're watching.*
4. *The Slugs that live in this nebula field are a leisure-centered civilization. Everything in Slug life is done in the pursuit of more currency and more time in which to spend it on extravagant ventures. This, inevitably, leads to much treachery in open space.*
5. *The Slugs developed on an ocean planet where the ability to telepathically sense another organism was more important than sight. Today they use this ability to navigate unfettered the depths of the nebulas they inhabit.*

Variant 3 mentions the Slug home world but is available in **both** Slug sectors — the
same start event serves both, so the arrival text does not tell you which one you are in.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | None. | — | Nothing happens. The event body contains only a `<text load=...>` element — no reward, ship, store, environment or effect. | 100% |

## Blue Options
None.

## Rewards & Risks
Neither. This beacon is free and inert.

## Strategy Notes
- Nothing to decide. The value of the page is confirming that **your first beacon in a
  Slug sector is always safe** — it cannot be a fight, a store, or a distress beacon.
- It is also one of the few beacons in a Slug sector guaranteed *not* to be in a nebula,
  since no environment tag is declared. That matters in the Slug sectors specifically,
  where nebula beacons blind your sensors.
- Use the sector name, not this text, to tell [[sector-slug-controlled-nebula]] from
  [[sector-slug-home-nebula]] ([[source-text-sectorname-xml]]).

## Related
- [[event-empty-beacon-slug]], [[event-empty-nebula-beacon-slug]] — the other inert Slug
  beacons, allocated by count rather than fixed at the entry point
- [[event-start-beacon-zoltan]], [[event-start-beacon-rock]], [[event-start-beacon-engi]]
  — the same structural pattern in other sectors
- [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]] — both declare this as
  their `<startEvent>`

## Open Questions
- [ ] Confirm textList selection is uniform across the five entries.
- [ ] Do the two Slug sectors weight the five variants differently? Nothing in
      `sector_data.xml` suggests so — both simply name the same `<startEvent>`.
- [ ] Were all five variants present in vanilla, or were any added in AE? Neither the
      event nor its text list carries a DLC annotation.

## Sources
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
