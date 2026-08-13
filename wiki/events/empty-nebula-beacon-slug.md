---
id: event-empty-nebula-beacon-slug
type: event
event_name: NEBULA_NOTHING_SLUG
sectors: [[[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: empty
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [empty, nebula, filler]
---

# Empty nebula beacon (Slug) — `NEBULA_NOTHING_SLUG`

## Summary
The Slug sectors' "nothing here" nebula beacon. No choices, no effects — six flavour
texts and a jump onward. Its only mechanical weight is that it occupies `2–4` beacons of
every Slug sector, crowding out the pool.

## Trigger & Where It Appears
- Sectors: [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]
- Allocated directly by sector, not through an event list:
  `<event name="NEBULA_NOTHING_SLUG" min="2" max="4"/>` in both `SLUG_SECTOR` and
  `SLUG_HOME` ([[source-sector-data-xml]])
- Beacon: nebula (`<environment type="nebula"/>`); not `unique`, so it can repeat
  ([[source-events-slug]])

## Text
The prose is drawn from the `NEBULA_NOTHING_SLUG` text list — six variants, one shown at
random ([[source-events-slug]], [[source-text-events-xml]]):

> - When it comes to Slugs, no news is not necessarily good news. However, if they are
>   watching, they don't seem to want to confront you.
> - It's not unusual to feel paranoia in a Slug controlled nebula, but for once, it is
>   unfounded.
> - Either this part of Slug space is deserted, or it's too dense for even Slugs to detect
>   your presence. Time to move.
> - This area of the nebula seems entirely empty until a small Slug transport and its
>   escorts emerges suddenly from through the clouds, only to disappear again in a matter
>   of seconds.
> - You explore around the beacon and are shocked when a rock the size of a small moon
>   suddenly looms ahead of you. Scans reveal the solid-looking rock is just a husk, almost
>   entirely mined out of useful minerals.
> - There are a number of small stations for travellers in the area, lit up by guiding
>   lights and advertisements. Only Slug ships are docked so you decide it's better to
>   avoid a confrontation and steer clear.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | (none) | — | Nothing happens. | 100% |

## Rewards & Risks
None either way. The beacon still costs a jump and one step of Rebel advance, and the
nebula environment applies (sensors offline, no FTL charge outside the beacon's own rules).

## Strategy Notes
- Filler. Worth noting only when counting the Slug sectors' pool: with `2–4` of these plus
  `0–2` [[event-empty-beacon-slug]], a meaningful share of every Slug sector is dead space.

## Related
- [[event-empty-beacon-slug]] — the non-nebula equivalent, `NOTHING_SLUG`
- [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]

## Open Questions
- [ ] Whether the six text variants are equally weighted.

## Sources
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-empty-nebula-beacon-slug]] (per raw/wiki/empty-nebula-beacon-slug.md)
