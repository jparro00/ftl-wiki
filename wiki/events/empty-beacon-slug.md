---
id: event-empty-beacon-slug
type: event
event_name: NOTHING_SLUG
sectors: [[[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: empty
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [empty, filler]
---

# Empty beacon (Slug) — `NOTHING_SLUG`

## Summary
The Slug sectors' empty beacon outside the clouds. No choices, no effects; five flavour
texts, all of which lean on the same joke — you are relieved to be out of the nebula and
your sensors work again.

## Trigger & Where It Appears
- Sectors: [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]
- Allocated directly by sector: `<event name="NOTHING_SLUG" min="0" max="2"/>` in both
  `SLUG_SECTOR` and `SLUG_HOME` ([[source-sector-data-xml]])
- Beacon: ordinary — **no** `<environment type="nebula"/>` tag, which is the whole point of
  the variant. Not `unique` ([[source-events-slug]])

## Text
Drawn from the `NOTHING_SLUG` text list — five variants, one shown at random
([[source-events-slug]], [[source-text-events-xml]]):

> - You arrive at the beacon and are relieved at the sight of open space. Nebulas are
>   terribly claustrophobic.
> - This beacon marks a 'small' gap in the nebula. No colonies or ships in scanning
>   distance.
> - You are relieved to see your sensors blink back on after the jump. No ships detected.
> - The Slugs rely heavily on their telepathic powers and are reluctant to give up that
>   advantage by extending beyond nebulas. It's unlikely you'll encounter any this far from
>   the clouds.
> - You arrive in an area clear of nebula and quickly check to see if the sensors are
>   working. Everything is fine and no ships are detected in the vicinity.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | (none) | — | Nothing happens. | 100% |

## Rewards & Risks
None. Costs a jump.

## Strategy Notes
- Filler, and rarer than its nebula sibling (`0–2` versus `2–4` per sector).

## Related
- [[event-empty-nebula-beacon-slug]] — the nebula equivalent, `NEBULA_NOTHING_SLUG`
- [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]

## Open Questions
- [ ] Whether the five text variants are equally weighted.

## Sources
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-empty-beacon-slug]] (per raw/wiki/empty-beacon-slug.md)
