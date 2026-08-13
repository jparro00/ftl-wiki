---
id: item-reactor
type: item
item_kind: system
rarity: unknown
unlocks_blue: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [system, power]
---

# Reactor

## Summary
The ship's power plant. Unlike every other system on this list the reactor has **no
`<systemBlueprint>` entry** in the blueprint files — it exists only as a `system="reactor"`
target for `<upgrade>` tags and `req="reactor"` gates in the event files. Its cost curve and
maximum are therefore not stated in any source in `raw/`.

## Stats
- No `<systemBlueprint name="reactor">` exists in [[source-blueprints]], [[source-dlcblueprints]] or [[source-dlcblueprintsoverwrite]]. Power, cost and upgrade curve are **unknown** from these files.
- The event files gate on it with `req="reactor" max_lvl="24"`, which implies a 24-bar ceiling but does not state one ([[source-newevents]]).

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
- Seven distinct events grant a reactor bar, more than grant any single augment.

## Related
- [[item-weapons]], [[item-shields]], [[item-engines]], [[item-drone-control]] — the four systems that eat reactor bars fastest

## Open Questions
- [ ] The reactor's real upgrade cost curve and maximum — not present in any file in `raw/gamedata/`.
- [ ] Whether `max_lvl="24"` is the true ceiling or just the highest value the event authors needed.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-events-engi]] (per raw/gamedata/events_engi.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
