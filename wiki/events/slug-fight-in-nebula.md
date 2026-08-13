---
id: event-slug-fight-in-nebula
type: event
event_name: NEBULA_SLUG_FIGHT
sectors: [[[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: nebula
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [combat, nebula, default-rewards]
---

# Slug fight in nebula — `NEBULA_SLUG_FIGHT`

## Summary
The bread-and-butter Slug nebula ambush. Five flavour texts, no choices, one Slug ship at
default rewards. Its importance is that it is **indistinguishable from
[[event-slug-home-nebula-surrender]]**, the Slug Cruiser unlock event, which uses the same
text list.

## Trigger & Where It Appears
- Sectors: [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]] — via the
  `NEBULA_HOSTILE_SLUG` event list (`min 5 / max 7` per sector, the biggest single
  allocation in these sectors) ([[source-events-slug]], [[source-sector-data-xml]])
- Beacon: nebula (`<environment type="nebula"/>`)
- **Not** `unique` — it can appear more than once per sector ([[source-events-slug]])

## Text
Drawn from the `NEBULA_SLUG_FIGHT` text list. The list declares ten `<text>` entries but
they are the same five ids listed twice, so there are five distinct variants
([[source-events-slug]], [[source-text-events-xml]]):

> - Your sensors are no match for the Slug's telepathic abilities - a ship you never even
>   saw opens fire from astern!
> - The Slug vessel you encounter here has obviously made a big score and is looking to
>   test its new armaments. They picked the wrong ship to attack.
> - A Slug passenger ship hails: "Please, your worthy alien highnessesss, we are unarmed
>   and sseeking asssylum." You approach cautiously, and weapons immediately spring from
>   their hull!
> - A Slug ship - a rogue, you suspect - approaches, but when he sees you're Federation he
>   thinks better of the sneak attack and fires everything he has.
> - Direct attacks are not preferred by the Slugs, but of the three you see at this beacon,
>   one has the brass to make a move on your position!

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | (none) | — | `<ship load="JELLY" hostile="true"/>` — fight a Slug ship, default rewards. | 100% |

### The enemy — `JELLY`

`auto_blueprint="SHIPS_JELLY"`; `surrender chance="0.5" min="3" max="4"` loading
`SLUG_SURRENDER`, `escape chance="0.5" min="3" max="4"`, default destroyed/deadCrew
([[source-events-ships]]). Fandom states this as "50% surrender chance at 30–40% hull, 50%
escape chance at 30–40% hull" ([[source-fandom-slug-fight-in-nebula]]).

Surrender rolls `SLUG_SURRENDER_LIST` — `HIGH fuel_only`, `LOW stuff`, or `MED stuff`
([[source-events-slug]]). See [[event-slug-fight]] for the table.

## Rewards & Risks
- Default rewards, or one of the three surrender payloads.
- Nebula environment: sensors are down for the fight.

## Strategy Notes
- In [[sector-slug-home-nebula]] this event and [[event-slug-home-nebula-surrender]] open
  identically. Fandom's rule of thumb: **if the Slug ship does not offer a surrender at low
  hull, it was this event** ([[source-fandom-slug-home-nebula-surrender]]). If you are
  hunting the Slug Cruiser, damage every Slug ship down instead of destroying it outright.

## Related
- [[event-slug-home-nebula-surrender]] — same intro text, different surrender; the ship
  unlock
- [[event-slug-fight]] — the non-nebula version
- [[entity-slugs]]

## Open Questions
- [ ] Whether the doubled text-list entries change the draw weighting at all (they are the
      same five ids, so probably not).

## Sources
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-fandom-slug-fight-in-nebula]] (per raw/wiki/slug-fight-in-nebula.md)
