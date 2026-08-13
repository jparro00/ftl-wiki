---
id: event-pirate-escape
type: event
event_name: PIRATE_ESCAPE
sectors: []
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [aftermath, escape, orphan, no-choice, pirates, rebels, shared-sub-event]
---

# Pirate escape — `PIRATE_ESCAPE`

## Summary
The generic "the enemy is charging its FTL" warning. Nine different hulls hand their
`<escape>` block to this one event; it prints a single line and leaves the fight running.
It is the last-chance notice that the wreck — and its scrap — is about to jump away.

## Trigger & Where It Appears
- **Not in any sector event list.** It is reached only from `<escape load=...>` blocks in
  ship definitions, so it inherits the sectors of whatever hull invoked it.
- Ships that load it ([[source-events-ships]], [[source-events-boss]]):

| Ship | `<escape>` declaration |
|---|---|
| `PIRATE` | `chance="0.5" min="2" max="4"` |
| `PIRATE_SLAVER` | `chance="0.5" min="2" max="4"` |
| `JELLY_PIRATE_WITHBOARDERS` | `chance="0.3" min="2" max="4" timer="15"` |
| `STORM_PIRATE_SUPPLY_FUEL` | `chance="0.5" min="2" max="4"` |
| `STORM_PIRATE_SUPPLY_AMMO` | `chance="0.5" min="2" max="4"` |
| `REBEL` | `chance="0.5" min="3" max="4"` |
| `JELLY` | `chance="0.5" min="3" max="4"` |
| `JELLY_UNLOCK1` | `chance="0.5" min="3" max="4"` |
| `ZOLTAN_PIRATE` | `chance="0.5" min="2" max="4"` |
| `BOSS_SCOUT_RESCUE` (`events_boss.xml`) | `chance="0.5" min="4" max="8"` |

- `min`/`max` are hull points, and the `<escape>` element is the sibling of `<surrender>`
  analysed in [[concept-surrender-offers]]. **Whether `chance` on `<escape>` is inverted
  the same way is explicitly unresolved there** — do not assume `1 − chance` for escape.
- No Fandom page joins this event; the community wiki renders it as the
  `SurrenderEscape` template on each parent fight page.

## Text
> The enemy ship appears to be powering up its FTL. It's trying to escape!

(`event_PIRATE_ESCAPE_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none — the event body is `<text/>` plus `<ship hostile="true"/>`)* | — | The fight continues, hostile, with the enemy FTL charging. If it completes, the ship's own `<gotaway>` block resolves. | 100% |

The `<ship hostile="true"/>` line simply re-asserts the existing fight; the event adds no
rewards, damage, or branches of its own ([[source-events-xml]]).

## Blue Options
None.

## Rewards & Risks
- No reward and no cost. The mechanical consequence lives in each hull's `<gotaway>`
  block, which differs per ship — most pay nothing, a few (e.g. `BOSS_SCOUT_RESCUE`) do
  something more interesting.
- The real risk is opportunity cost: an escaped ship is scrap you did not collect.

## Strategy Notes
- *Opinion:* when this fires, switch to whatever kills fastest and stop worrying about
  system targeting. There is no in-event way to stop the jump; only damage output matters.
- A ship that escapes still leaves you the beacon; you are not forced to jump.

## Related
- [[event-pirate-surrender]] — the surrender counterpart, loaded by many of the same hulls
- [[entity-pirates]], [[entity-rebels]], [[entity-slugs]] — the hulls that load it
- [[concept-surrender-offers]] — and its open question on whether `<escape chance>` is
  inverted too

## Open Questions
- [ ] Is `chance` on `<escape>` the probability of escaping, or (like `<surrender>`) the
      probability of *not* escaping?
- [ ] What does the `timer="15"` on `JELLY_PIRATE_WITHBOARDERS` change relative to the
      default escape countdown?

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-events-boss]] (per raw/gamedata/events_boss.xml)
