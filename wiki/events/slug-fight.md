---
id: event-slug-fight
type: event
event_name: SLUG_FIGHT
sectors: [[[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unique, combat, default-rewards]
---

# Slug fight — `SLUG_FIGHT`

## Summary
The plain Slug ambush outside the clouds: no choices, no environment, straight into a
fight with a standard Slug ship at default rewards. The clean-air counterpart to
[[event-slug-fight-in-nebula]].

## Trigger & Where It Appears
- Sectors: [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]] — via the
  `HOSTILE_SLUG` event list (`min 1 / max 2` per sector)
  ([[source-events-slug]], [[source-sector-data-xml]])
- Beacon: ordinary hostile — no `<environment>` tag, so your sensors work
- `unique="true"` ([[source-events-slug]])

## Text
> It's rare for the Slugs to stay exposed in open space for long periods - the ship here
> may be lost, or just passing through, but either way he moves in to attack!

(`event_SLUG_FIGHT_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | (none) | — | `<ship load="JELLY" hostile="true"/>` — fight a Slug ship, default rewards. | 100% |

### The enemy — `JELLY`

`auto_blueprint="SHIPS_JELLY"`, with ([[source-events-ships]]):

- `<surrender chance="0.5" min="3" max="4" load="SLUG_SURRENDER"/>`
- `<escape chance="0.5" min="3" max="4" load="PIRATE_ESCAPE"/>`
- `<destroyed load="DESTROYED_DEFAULT"/>`, `<deadCrew load="DEAD_CREW_DEFAULT"/>`

Fandom renders the `min`/`max` as "30–40% hull" ([[source-fandom-slug-fight-in-nebula]]).

Accepting the surrender rolls `SLUG_SURRENDER_LIST` — three entries, each of which also
sets the ship non-hostile ([[source-events-slug]]):

| Entry | Reward |
|---|---|
| 1 | `<autoReward level="HIGH">fuel_only</autoReward>` |
| 2 | `<autoReward level="LOW">stuff</autoReward>` |
| 3 | `<autoReward level="MED">stuff</autoReward>` |

## Rewards & Risks
- Default rewards on a kill; on a surrender, one of the three payloads above — note that
  one of them is fuel only.
- Risk is an ordinary ship fight with no imposed system handicap, which makes this the
  gentlest of the Slug hostile events.

## Strategy Notes
- Nothing distinguishes this fight mechanically; the value is that it is *not* in a nebula,
  so you keep sensors and the enemy has no fire weapons forced on it.
- A `HIGH` `fuel_only` surrender is a real outcome — if you are scrap-hungry rather than
  fuel-hungry, the surrender is not automatically the better deal.

## Related
- [[event-slug-fight-in-nebula]] — the nebula version, `NEBULA_SLUG_FIGHT`
- [[event-slug-home-nebula-surrender]] — the ship-unlock fight that imitates it
- [[entity-slugs]]
- [[event-pirate-escape]] — the shared `PIRATE_ESCAPE` aftermath this hull loads

## Open Questions
- [ ] Whether the three `SLUG_SURRENDER_LIST` entries are equally weighted.

## Sources
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-fandom-slug-fight]] (per raw/wiki/slug-fight.md)
