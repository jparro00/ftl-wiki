---
id: event-pirate-fight-slug
type: event
event_name: SLUG_PIRATE
sectors: [[[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [combat, pirate, surrender, varies-text, repeatable, slug-sector]
---

# Pirate fight (Slug) — `SLUG_PIRATE`

## Summary
Pirates working the edges of Slug territory. A plain forced fight with three flavour
variants — but against the standard `PIRATE` hull, which means a 50% surrender offer and a
50% escape attempt are both on the table. Unlike most Slug-sector hostiles this one is
explicitly `unique="false"`, so it can recur.

## Trigger & Where It Appears
- Event list: `HOSTILE_SLUG` in `events_slug.xml` ([[source-events-slug]]). No
  `OVERRIDE_HOSTILE_SLUG` exists ([[source-dlceventsoverwrite]]), so the pool is the same
  in both editions.
- `HOSTILE_SLUG` is allocated at `min=1 max=2` in both `SLUG_SECTOR`
  ([[sector-slug-controlled-nebula]]) and `SLUG_HOME` ([[sector-slug-home-nebula]])
  ([[source-sector-data-xml]]).
- **`unique="false"` — explicitly repeatable.** The attribute is written out rather than
  omitted, and Fandom agrees (`unique=false`) ([[source-fandom-pirate-fight-slug]]).
- Beacon: hostile, ship visible on Long-Ranged Scanners (`LRSmap=ship`)
  ([[source-fandom-pirate-fight-slug]]).
- **No `<environment>`** — non-nebula beacon despite the sector.

### Odds of drawing it
`HOSTILE_SLUG` has five distinct members, none duplicated. **Assuming uniform selection
across list entries** ([[concept-event-list-weighting]]), each non-nebula hostile beacon in
a Slug sector is this event **1/5** of the time. Because it is not unique, it can fill more
than one of them.

## Text
`[varies: textList SLUG_PIRATE]` — three entries, no repeats. The text list carries the
**same name as the event**, and is itself marked `unique="false"`
([[source-events-slug]], [[source-text-events-xml]]):

1. *There appears to be a pirate ship nearby. Be on your guard; anyone trying to hunt in Slug territory is either formidable or deeply stupid, and in space, either can be dangerous.*
2. *"We knew anyone foolish enough to try and sneak through a Slug nebula would stick to open space. Yield your goods and we may let you live." You cut the transmission in lieu of a response.*
3. *Before you can take a moment's rest from the ever present nebulas in this sector, a pirate ship appears behind you and opens fire.*

Fandom lists the same three verbatim ([[source-fandom-pirate-fight-slug]]).

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | None. | — | `<ship load="PIRATE" hostile="true"/>` — immediate combat, default rewards. | 100% |

### The `PIRATE` ship
`auto_blueprint="SHIPS_PIRATE"` ([[source-events-ships]]):

| Branch | Declaration | Reading |
|---|---|---|
| Surrender | `chance="0.5" min="3" max="4"` → `PIRATE_SURRENDER` | **50% surrender chance** — `chance` is the probability the ship keeps fighting, so surrender is `1 − chance` ([[concept-surrender-offers]]) |
| Escape | `chance="0.5" min="2" max="4"` → `PIRATE_ESCAPE` | 50% escape attempt |
| Got away | `ship_PIRATE_gotaway_text` | a distinct text if it succeeds |
| Destroyed / dead crew | `DESTROYED_DEFAULT` / `DEAD_CREW_DEFAULT` | default rewards |

Fandom's page does not spell the surrender/escape figures out for this event, describing
it only as a Pirate ship with default rewards
([[source-fandom-pirate-fight-slug]]); the numbers above come from the ship block.

## Blue Options
None. No `req` attribute appears anywhere in the event.

## Rewards & Risks
- **Reward:** default rewards, or whatever `PIRATE_SURRENDER` pays if it offers.
- **Risk:** ordinary pirate hull. The escape branch is the real annoyance — a fleeing
  pirate costs you the reward entirely.
- Because it can recur, a Slug sector can serve this fight twice.

## Strategy Notes
- *Opinion:* strictly better to meet than [[event-mantis-fight-slug]] — half the time the
  pirate offers surrender and you bank a payout without finishing the fight.
- If you want the surrender rather than the escape, focus damage on weapons and engines
  early; both branches trigger in the same low-hull region (`min`/`max` 2–4 vs 3–4), so the
  order they fire in is not fixed.
- The scanner shows a ship here, so it can be routed around.

## Related
- [[event-pirate-fight]] — the generic pirate encounter
- [[event-pirate-fight-in-nebula]] — the nebula-flagged variant
- [[event-mantis-fight-slug]], [[event-rebel-fight-slug]], [[event-slug-fight]] — the rest
  of the `HOSTILE_SLUG` pool
- [[concept-surrender-offers]] — how the 50% is derived
- [[concept-event-list-weighting]] — basis for the 1/5 figure
- [[event-pirate-surrender]] — the shared `PIRATE_SURRENDER` aftermath this hull loads
- [[event-pirate-escape]] — the shared `PIRATE_ESCAPE` aftermath this hull loads

## Open Questions
- [ ] Whether event-list selection is truly uniform.
- [ ] What `PIRATE_SURRENDER` pays out.
- [ ] Whether the escape check or the surrender check resolves first when both thresholds
      are crossed at once.

## Sources
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-pirate-fight-slug]] (per raw/wiki/pirate-fight-slug.md)
