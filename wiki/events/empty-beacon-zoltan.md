---
id: event-empty-beacon-zoltan
type: event
event_name: NOTHING_ZOLTAN
sectors: [[[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: empty
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [empty, varies-text, repeatable, flavour]
---

# Empty beacon (Zoltan) — `NOTHING_ZOLTAN`

## Summary
The Zoltan sectors' "nothing happens" beacon. Mechanically inert, but its seven flavour
strings are the game's own in-fiction briefing on the sector — including an explicit
statement of how to beat the Zoltan Super Shield.

## Trigger & Where It Appears
- Sectors: [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]
- Beacon: empty, no ship on Long-Ranged Scanners
  ([[source-fandom-empty-beacon-zoltan]]).
- Allocated **directly by the sector**, not through an event list:
  `<event name="NOTHING_ZOLTAN" min="1" max="2"/>` in both `ZOLTAN_SECTOR` and
  `ZOLTAN_HOME` ([[source-sector-data-xml]]). So 1–2 of these are guaranteed per sector.
- **Not** `unique="true"` — it repeats.

## Text
`[varies: textList NOTHING_ZOLTAN]` — drawn from a seven-entry text list
(`text_NOTHING_ZOLTAN_1` … `_7`) with no repeated entries, so each is equally likely
([[source-events-zoltan]], per raw/gamedata/events_zoltan.xml). The file carries the
developer note `<!-- TO DO - need more -->` after the third entry.

The seven variants ([[source-text-events-xml]]):

1. *There are some mineral-rich asteroids here that the Zoltan have left idle, but you've none of the necessary equipment to mine them.*
2. *You have to admit - Zoltan space is a beautiful and peaceful place indeed. However, re-engaging the FTL and finishing your mission is your priority, not sight-seeing.*
3. *A light asteroid field is entering the atmosphere of a nearby planet - a fireworks show on a galactic scale. There's little for it but to take in the ambience and program the next jump.*
4. *You stumble upon some Zoltan military vessels engaging in combat training. Their Energy Shields are impressive, but you note how quickly beam and ion weaponry take them down.*
5. *You don't have time to hail the Zoltan ship that was waiting at this beacon before it jumps away. They are a careful race.*
6. *A Zoltan shipyard is stationed at this beacon. You admire the display of hundreds of glowing Zoltan performing delicate exterior work on a massive transport ship.*
7. *A message broadcast from a nearby planet announces the presence of an ancient Zoltan monastery available for visiting. Likely just a tourist trap, but still too bad you don't have the time to visit.*

Fandom's seven bullets match the seven game strings exactly, in the same order — the two
sources fully agree here ([[source-fandom-empty-beacon-zoltan]]).

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | None. | — | Nothing happens. The event body contains only a `<text load=...>` element — no reward, ship, or effect of any kind. | 100% |

## Blue Options
None. Variant 1 dangles unmineable asteroids and variant 7 an unvisitable monastery, but
neither is gated content — there is no `req` anywhere in the event.

## Rewards & Risks
Neither. This beacon costs you one jump's worth of Rebel fleet advance and one fuel, and
returns nothing.

## Strategy Notes
- Nothing to do here. Its only practical value is as a safe waypoint when routing.
- **Variant 4 is the in-game hint for the whole sector:** *"Their Energy Shields are
  impressive, but you note how quickly beam and ion weaponry take them down."* That is
  the counter to [[item-zoltan-shield]] and to the six-to-eight
  [[event-zoltan-fight]]-class encounters the sector allocates.

## Related
- [[event-start-beacon-zoltan]] — the sector's other purely textual event
- [[event-store-zoltan]] — the third `<textList>`-driven structural event
- [[item-zoltan-shield]] — what variant 4 is about
- [[event-zoltan-fight]] — where that advice matters

## Open Questions
- [ ] Confirm textList selection is uniform across the seven entries.
- [ ] Are all seven variants present in vanilla, or were any added in AE?

## Sources
- [[source-events-zoltan]] (per raw/gamedata/events_zoltan.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-empty-beacon-zoltan]] (per raw/wiki/empty-beacon-zoltan.md)
