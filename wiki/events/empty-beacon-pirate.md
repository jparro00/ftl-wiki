---
id: event-empty-beacon-pirate
type: event
event_name: NOTHING_PIRATE
sectors: [[[sector-pirate-controlled-sector]]]
beacon_type: empty
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [empty-beacon, flavor-only, pirate]
---

# Empty beacon (Pirate) — `NOTHING_PIRATE`

## Summary
The Pirate sectors' filler beacon. Nothing happens: no choices, no ship, no reward. Three
of its four flavour variants describe a near-miss with pirates that comes to nothing.
`sector_data.xml` guarantees 1–2 per Pirate sector ([[source-sector-data-xml]]).

## Trigger & Where It Appears
- Sector: [[sector-pirate-controlled-sector]]
- Allocation: `<event name="NOTHING_PIRATE" min="1" max="2"/>` — the file carries a dev
  note `<!-- need more -->` beside it ([[source-sector-data-xml]], per
  `raw/gamedata/sector_data.xml`)
- Beacon: ordinary, no ship present ([[source-fandom-empty-beacon-pirate]] marks it
  `LRSmap=noship`, `unique=false`)
- Not `unique` — the event element carries no `unique` attribute
  ([[source-events-pirate]])

## Text
Varies — `<text load="NOTHING_PIRATE"/>` over a four-entry `textList`
([[source-events-pirate]]). All four, per [[source-text-events-xml]]:

> As soon as you arrive, a small ship de-cloaks behind yours. You immediately power up the
> shields and weapons, but they continue on their trajectory unimpressed. You try to calm
> your nerves.

> A small pirate ship messages you, "That sure is a shiny ship you got there." You fire a
> warning shot across their bow and they respond, "Hey! No need for violence! It was just
> a comment..."

> The only thing within scanning range is an old abandoned mining structure and a resupply
> station. They appear to have been picked clean by marauders.

> You arrive to have a small fleet of Engi ships target you with a message, "Piracy
> results in negative societal impact. Not permitted." You assure them of your honest
> intentions and they allow you to pass.

[[source-fandom-empty-beacon-pirate]] transcribes the same four.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(no choices; continue)_ | — | Nothing happens. | 100% |

The event element contains only a `<text>` tag — no `<ship>`, `<autoReward>`,
`<boarders>`, `<item_modify>` or `<damage>` ([[source-events-pirate]]).

## Rewards & Risks
None of either. The de-cloaking ship in variant 1 and the pirate hail in variant 2 are
flavour; neither loads a `<ship>`.

## Strategy Notes
- Pure fuel cost. In a Pirate sector 1–2 beacons on the map are guaranteed to be these,
  which matters when you are budgeting productive jumps against the fleet advance.

## Related
- [[sector-pirate-controlled-sector]]
- [[event-start-beacon-pirate]] — the other purely-flavour structural Pirate beacon
- [[event-store-pirate]]
- [[entity-pirates]], [[entity-engi]]

## Open Questions
- [ ] Whether the four text variants are weighted evenly (the `textList` lists each id
      once, which implies uniform, but the game's selection rule is not documented here).

## Sources
- [[source-events-pirate]] (per raw/gamedata/events_pirate.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-empty-beacon-pirate]] (per raw/wiki/empty-beacon-pirate.md)
