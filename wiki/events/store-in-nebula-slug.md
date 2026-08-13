---
id: event-store-in-nebula-slug
type: event
event_name: NEBULA_STORE_SLUG
sectors: [[[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: store
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [store, nebula, guaranteed]
---

# Store in nebula (Slug) — `NEBULA_STORE_SLUG`

## Summary
The Slug sectors' own store beacon, sited inside the clouds. No choices, no risk — the
store just opens. It is guaranteed twice per Slug sector, on top of the generic `STORE`
allocation, which makes Slug space unusually reliable for shopping.

## Trigger & Where It Appears
- Sectors: [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]
- **Guaranteed:** `<event name="NEBULA_STORE_SLUG" min="2" max="2"/>` in both
  `SLUG_SECTOR` and `SLUG_HOME` — exactly two per sector, in addition to
  `<event name="STORE" min="0" max="1"/>` ([[source-sector-data-xml]])
- Beacon: store inside a nebula — the event carries both `<store/>` and
  `<environment type="nebula"/>` ([[source-events-slug]])
- Not `unique`

## Text
Drawn from the `NEBULA_STORE_SLUG` text list — two variants
([[source-events-slug]], [[source-text-events-xml]]):

> - A huge Slug teleports from nowhere onto the bridge! Before you can open fire, he's
>   spread his wares across the helm and is brandishing things at you.
> - You cautiously approach a Slug colony on a huge asteroid. It's a brave person who sets
>   foot on a Slug planet - it can take weeks to get the mucus out of your clothes - but
>   there's business to be done.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | (none) | — | A store opens. | 100% |

The event data says nothing about the store's stock or its rarity weighting; that is
resolved elsewhere in the game.

## Rewards & Risks
A store, with no cost or risk attached to the beacon itself.

## Strategy Notes
- Two guaranteed stores per sector is generous, and both sit in nebula beacons — so you
  arrive with sensors down but nothing hostile present.
- Do not confuse it with [[event-slug-store-ship]] (`NEBULA_SLUG_FAKE_STORE`), which
  advertises itself as a merchant and is mostly an ambush.

## Related
- [[event-slug-store-ship]] — the fake-store trap in the same sectors
- [[event-slug-drink]], [[event-slug-repair-station]] — the other Slug events that can open
  a store
- [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]

## Open Questions
- [ ] Whether Slug stores have any faction-specific stock weighting.

## Sources
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-store-in-nebula-slug]] (per raw/wiki/store-in-nebula-slug.md)
