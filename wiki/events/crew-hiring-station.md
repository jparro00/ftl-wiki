---
id: event-crew-hiring-station
type: event
event_name: TAVERN_HIRE
sectors: [[[sector-civilian-sector]], [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-federation-space]], [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]], [[sector-pirate-controlled-sector]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]], [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]], [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]], [[sector-uncharted-nebula]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [crew, scrap-cost, varies-text, unique, items-pool]
---

# Crew hiring station — `TAVERN_HIRE`

## Summary
A mercenary hiring post. Two crew are on offer at independently rolled prices; you may
take one or walk away. It is the game's only pure crew-purchase event outside a store,
and it appears in the `ITEMS` pool, so it competes for the item beacons of almost every
sector in the game.

## Trigger & Where It Appears
- Event list: `ITEMS` in `newEvents.xml`, tagged `<!-- DLC - old event - down below-->`
  ([[source-newevents]]), and `OVERRIDE_ITEMS` in the Advanced Edition replacement
  ([[source-dlceventsoverwrite]]).
- `ITEMS` is allocated by 14 sector definitions ([[source-sector-data-xml]]) — every
  playable sector except the two Zoltan sectors (which use `ITEM_ZOLTAN`),
  [[sector-abandoned-sector]], [[sector-hidden-crystal-worlds]] and
  [[sector-the-last-stand]].
- `ITEMS` is also half of `EXIT_LIST` (`EXIT_LIST` = `NEUTRAL_EXIT` + `ITEMS`), so this
  event can also fill an **exit beacon** ([[source-newevents]]). Fandom records the same
  with `alsooccur=exit` ([[source-fandom-crew-hiring-station]]).
- `unique="true"` — at most once per run.
- Beacon: ordinary; no distress flag, no environment, no ship on scanners.

**Why `version: both`:** the developer comment calls it an *"old event"* re-added with the
DLC, and it is listed in `OVERRIDE_ITEMS` among the un-annotated base entries rather than
in the `<!--DLC-->`-tagged block ([[source-dlceventsoverwrite]]). Both readings point at
pre-AE content. The other three AE trading events in the same pool are marked
`version: ae` on that same evidence, so this one is deliberately different.

### Odds of drawing it
`ITEMS` has **13 distinct members, none duplicated**, so **assuming uniform selection
across list entries** ([[concept-event-list-weighting]]) each `ITEMS` beacon has a
**1/13** chance of being this event. Under Advanced Edition the pool is `OVERRIDE_ITEMS`,
which adds `STORE_REBELSIDE` for **14 members → 1/14**
([[source-dlceventsoverwrite]]). This is a genuine AE-vs-vanilla difference in the draw
rate, not in the event.

## Text
`[varies: textList TAVERN_HIRE_TEXT]` — three entries, no repeats
([[source-newevents]], [[source-text-events-xml]]):

1. *You find a space station set up for travelers. Browsing through its listings, you find a tavern full of mercenaries for hire. You look for potential crewmembers.*
2. *There are a number of ships stationed around a rest stop. You immediately receive a message saying, "If you're looking for some bodies to fill your ship, you've come to the right place!"*
3. *This Beacon seems to serve as a meeting place for local traffic. It seems you can find crew willing to fight on your ship here... for a price.*

Fandom lists the same three, in a different order and with variant 3 reading *"a meeting
place"* → *"meeting place"* ([[source-fandom-crew-hiring-station]]).

## Choices & Outcomes

Both hire options carry the **same label**, `event_TAVERN_HIRE_c1_choice` — "Hire a
crewmember." They differ only in the scrap band rolled:

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Hire a crewmember. | — | `<crewMember amount="1"/>` and **−25 to −45 scrap**. | 100% |
| 2 | Hire a crewmember. | — | `<crewMember amount="1"/>` and **−25 to −55 scrap**. | 100% |
| 3 | Don't hire anyone. | — | `<event/>` — nothing happens. | 100% |

([[source-newevents]]) Both offers are present at once, so this is a two-candidate
shortlist, not a random price. The `<crewMember amount="1"/>` element carries no `class`,
so the species is generated rather than fixed.

Fandom adds a detail the files do not state: **"The crew race and their skills are shown
prior to the trade."** ([[source-fandom-crew-hiring-station]]) — i.e. you see who you are
buying and at what price before committing. Nothing in `newEvents.xml` encodes that; it
is engine behaviour for `crewMember` offers.

## Blue Options
None. No `req` attribute appears on any choice.

## Rewards & Risks
- **Reward:** one crew member for 25–45 or 25–55 scrap. Skills and species are rolled.
- **Risk:** none mechanical — no fight, no boarders, no fuel cost. The only risk is the
  scrap.
- The two bands overlap heavily; the second offer's ceiling is 10 scrap higher, so the
  cheaper listing is not reliably the second one.

## Strategy Notes
- *Opinion:* 25–45 scrap for a body is competitive with store pricing and much better
  than nothing on a ship that started short-crewed. The value depends entirely on the
  rolled species and skills, which you get to see first — so this is a low-regret event.
- Because it is `unique="true"`, it will not come round again. If the crew on offer is
  useful and the scrap is affordable, taking it is usually correct.
- Its `ITEMS`-pool placement means it competes with the drone, weapon and free-item
  events for the same beacons — a sector that rolls this has one fewer chance at a free
  weapon.

## Related
- [[event-trade-scrap-for-upgrades]], [[event-improve-reactor-for-supplies]] — the other
  two AE trading events that share the `ITEMS` pool
- [[event-slaver-friendly]], [[event-slaver-hostile]] — the other main routes to crew
- [[concept-event-list-weighting]] — basis for the 1/13 and 1/14 figures
- [[concept-sector-event-allocation]] — how `ITEMS` reaches 14 sectors

## Open Questions
- [ ] What species pool and skill distribution does an unclassed `<crewMember amount="1"/>`
      draw from?
- [ ] Are the two offers guaranteed to be different species, or can they duplicate?
- [ ] Does the displayed price come from the same roll that is charged, or is it re-rolled
      on acceptance?

## Sources
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-crew-hiring-station]] (per raw/wiki/crew-hiring-station.md)
