---
id: item-reactor
type: item
item_kind: system
rarity: unknown
unlocks_blue: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-14
sources: 8
tags: [system, power, scrap-economy]
---

# Reactor

## Summary
The ship's power plant. Unlike every other system on this list the reactor has **no
`<systemBlueprint>` entry** in the blueprint files — it exists only as a `system="reactor"`
target for `<upgrade>` tags and `req="reactor"` gates in the event files. Its cost curve and
maximum are therefore not stated in any source in `raw/`.

## Stats
- No `<systemBlueprint name="reactor">` exists in [[source-blueprints]], [[source-dlcblueprints]] or [[source-dlcblueprintsoverwrite]]. Power, cost and upgrade curve are **unknown from the game files** — the numbers below come from outside them.
- The event files gate on it with `req="reactor" max_lvl="24"` ([[source-newevents]]) — see the ceiling note below.

### Cost curve
From [[source-fandom-template-reactor-power-cost]], banded by **the bar being bought**:

| Bar bought | Cost each |
|---|---|
| 1–5 | 30 scrap |
| 6–10 | **20 scrap** — the cheapest in the game |
| 11–15 | 25 scrap |
| 16–20 | 30 scrap |
| 21–25 | 35 scrap |

**Ceiling: 25 bars.** Maxing a typical 8-power ship costs **490 scrap**
([[source-fandom-ship]]). Contributes 25 of the game's 37-bar absolute power maximum.

The curve is **not monotonic** — bars 6–10 cost less than bars 1–5, so most ships start partway
through the cheapest band. The band-labelling ambiguity and the arithmetic that resolves it are
worked through on [[concept-power-and-reactor]].

> **The `max_lvl="24"` gates are consistent with a 25 cap, not a contradiction.** Both
> `req="reactor"` choices carry `max_lvl="24"` and `blue="false"` — inverse gates that hide the
> "take a reactor bar" option once the reactor is at 24 or above. That is exactly the condition
> a 25-bar ceiling requires. ([[source-newevents]], [[source-fandom-ship]])

## How To Get It
- Upgraded at stores (not modelled in the blueprint files).
- Event grants of `<upgrade system="reactor" amount="1"/>`:
  [[event-the-engi-virus]] ([[source-events-engi]]);
  [[event-asteroid-mining-colony]] (`HELP_MINERS_1` and `HELP_MINERS_2`),
  [[event-improve-reactor-for-supplies]] (`TRADER_UPGRADES_EXCHANGE_LIST`),
  [[event-trade-scrap-for-upgrades]] (`TRADER_UPGRADES_LIST`),
  [[event-rock-and-slug-standoff]] and [[event-slug-and-rock-standoff-in-nebula]]
  (`ROCK_SLUG_GRATEFUL`) ([[source-newevents]]);
  [[event-escort-civilians]] (`QUEST_ESCORT_ARRIVE`) and
  [[event-friendly-ship-out-of-fuel]] (`RANDOM_GIFT`) ([[source-events-xml]]).

## Blue Options It Unlocks
- **None.** The two `req="reactor"` choices in the data (`TRADER_UPGRADES_LIST` and
  `ROCK_SLUG_GRATEFUL`) both carry `max_lvl="24"` and `blue="false"` — they are inverse
  gates that hide the "take a reactor upgrade" choice from an already-maxed ship, and the
  game is explicitly told not to render them blue. ([[source-newevents]])

## Strategy Notes
- Reactor bars are the only thing every other system competes for, which is why so many
  events pay them out as a reward instead of scrap.
- Seven distinct events grant a reactor bar, more than grant any single augment — and at
  25–35 scrap apiece in the upper bands, those grants are worth more than they look.
- **The cheap bars are behind you at the start.** A typical ship begins around 8 power, inside
  the 20-scrap band; the price turns upward at bar 11.
- **Ion storms halve reactor power**, which is the argument for [[entity-zoltan]] crew and
  [[item-backup-battery]] — neither is halved ([[source-fandom-ship]]).
- The upgrade menu is blocked by **IN DANGER** (hostile ship or intruders), *not* by nebulas or
  ion storms on their own.

## Related
- [[concept-power-and-reactor]] — the cost curve, the ceiling, and the two non-reactor sources
- [[item-weapons]], [[item-shields]], [[item-engines]], [[item-drone-control]] — the four systems that eat reactor bars fastest
- [[item-backup-battery]], [[entity-zoltan]] — ion-immune power
- [[concept-scrap-economy]] — what 490 scrap competes with

## Open Questions
- [x] ~~The reactor's real upgrade cost curve and maximum — not present in any file in `raw/gamedata/`.~~
      **Answered 2026-08-14:** 30/20/25/30/35 per band of five, ceiling **25 bars**
      ([[source-fandom-template-reactor-power-cost]], [[source-fandom-ship]]). Still not in the
      game files — community-sourced at `medium` reliability.
- [x] ~~Whether `max_lvl="24"` is the true ceiling or just the highest value the event authors needed.~~
      **Answered 2026-08-14:** neither — it is an *inverse* gate, and 24 is exactly the value a
      25-bar ceiling implies. See the Stats note above.
- [ ] Whether the cost curve varies by difficulty — unstated either way by both sources.
- [ ] Per-ship starting reactor power; "about 8" is an average ([[source-fandom-ship]]).

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-events-engi]] (per raw/gamedata/events_engi.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-fandom-ship]] (per raw/wiki/ship.md)
- [[source-fandom-template-reactor-power-cost]] (per raw/wiki/template-reactor-power-cost.md)
