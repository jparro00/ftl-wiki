---
id: event-slug-repair-station
type: event
event_name: NEBULA_SLUG_HULLFIX
sectors: [[[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: nebula
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [unique, nebula, hull-repair, extortion, system-malfunction, hull-damage-risk, scrap-cost, fuel-cost]
---

# Slug repair station — `NEBULA_SLUG_HULLFIX`

## Summary
A Slug repair station offers to patch your hull. Accepting free repairs docks you to the
station and then extorts you for fuel or scrap; asking to pay up front is either an honest
50-scrap-for-10-hull trade or an ambush. There is no wholly safe way to get the repair, but
there is a way to walk away with it and pay nothing.

## Trigger & Where It Appears
- Sectors: [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]] — via the
  `NEBULA_NEUTRAL_SLUG` event list (`min 3 / max 5` per sector)
  ([[source-events-slug]], [[source-sector-data-xml]])
- Beacon: nebula (`<environment type="nebula"/>`), `unique="true"`

## Text
> You arrive to find a small Slug repair station. "Greetingsss traveller! Care for a fix
> up? We could eassily patch up ssome of that damage."

(`event_NEBULA_SLUG_HULLFIX_text`, per [[source-text-events-xml]])

## Choices & Outcomes

All three choices are `hidden="true"`.

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | No thanks. | — | "Too bad! Trussst iss a rare commodity these days." Nothing happens. | 100% |
| 2 | Sure. | — | Rolls `NEBULA_SLUG_HULLFIX_RESULT1` — 3 entries, below. | see below |
| 3 | Ask if they would like payment. | — | Rolls `NEBULA_SLUG_HULLFIX_REQUEST` — 2 entries, below. | see below |

### `NEBULA_SLUG_HULLFIX_RESULT1` (choice 2 — "Sure")

| Entry | Text | Effect |
|---|---|---|
| 1 | "…they repair 10 hull damage… but discover that you can't detach from the station." | `<damage amount="-10"/>` — **+10 hull** — then *Demand an explanation* → `RESULT2` |
| 2 | "…you notice only one damage has been repaired." | `<damage amount="-1"/>` — **+1 hull** — then *Demand an explanation* → `RESULT2` |
| 3 | "An EMP blast resonates throughout the ship and your engines shut down." | `<ship load="JELLY_STATUS_ENGINES" hostile="true"/>` + `<status type="limit" target="player" system="engines" amount="1"/>` — fight with **Engines capped at level 1**. Destroyed: `MED standard`; crew killed: `HIGH standard` |

### `NEBULA_SLUG_HULLFIX_RESULT2` — "Demand an explanation"

Reached from entries 1 and 2 above. Two entries:

| Entry | Demand | Pay | Refuse |
|---|---|---|---|
| 1 | "Perhaps some fuel would be an appropriate compensssation?" | *Give them the 15 fuel they demand* → `<item type="fuel" min="-15" max="-15"/>`, released | *That's ridiculous!* → a planted bomb: `<damage amount="4"/>` + `<damage amount="1" system="random"/>` + `<ship load="JELLY" hostile="true"/>`, default rewards |
| 2 | "…we've taken the liberty of installing a limiter on your weapons system." | *Give them the 50 scrap they demand* → `<item type="scrap" min="-50" max="-50"/>`, released | *Let's get out of here!* → `<ship load="JELLY_STATUS_WEAPONS" hostile="true"/>` + `<status type="divide" … system="weapons" amount="2"/>` — fight with **Weapon Control halved**; `HIGH standard` either way |

Fandom reads the bomb's two damage tags as "**5 hull** damage, 1 damage to a random
**system**" ([[source-fandom-slug-repair-station]]); the files state them separately as `4`
and `1` ([[source-events-slug]]). Same numbers, different bookkeeping.

The `RESULT2` entry-2 branch carries a dev note in the source:
`<!-- TO DO - TEST-->` ([[source-events-slug]]).

### `NEBULA_SLUG_HULLFIX_REQUEST` (choice 3 — "Ask if they would like payment")

| Entry | Text | Effect |
|---|---|---|
| 1 | "Ahhh. A fellow businessman. We offer to fix 10 damage for 50 ssscrap." | **Accept** → `<damage amount="-10"/>` + `<item type="scrap" min="-50" max="-50"/>` — 10 hull for 50 scrap, honestly transacted. **Decline** → nothing happens |
| 2 | "…Just kill the crew and we can ssstrip…" | `<ship load="JELLY" hostile="true"/>` — default rewards |

## Rewards & Risks
- Up to **10 hull repaired** — for 15 fuel, for 50 scrap, or occasionally for nothing if
  you refuse and win the resulting fight.
- Risks: an Engines-capped fight, a Weapons-halved fight, 4+1 damage from a planted bomb, or
  a straight ambush.
- Fandom notes that **revisiting the beacon clears the system malfunction, but the enemy
  ship and rewards are unchanged** ([[source-fandom-slug-repair-station]]).

## Strategy Notes
- Choice 3 is the tidier gamble: half the time it is a clean 50-scrap-for-10-hull deal
  (which you can decline for free), half the time it is a default-rewards fight you would
  probably have taken anyway.
- Choice 2 always ends in either extortion or a handicapped fight; the "+1 hull" entry is
  the worst outcome in the event, since you pay full extortion for one point of hull.
- Refusing the fuel demand costs 4 hull, 1 system damage and a fight — but you keep the 10
  hull you were just given and win default rewards. On a healthy ship that is often the
  better line. *(Opinion, weighing the effects listed in [[source-events-slug]].)*
- 15 fuel is a large sum this deep into Slug space; treat the fuel demand as the more
  expensive of the two.

## Related
- [[event-slug-store-ship]], [[event-slug-drink]] — the other Slug hospitality traps
- [[event-slug-hacker-choice]] — the other event that halves a system for a fight
- [[entity-slugs]]

## Open Questions
- [ ] Whether the entries within each list are equally weighted.
- [ ] Whether `RESULT2` entry 2's `divide weapons 2` behaves as designed (dev note says
      untested).

## Sources
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-fandom-slug-repair-station]] (per raw/wiki/slug-repair-station.md)
