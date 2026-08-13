---
id: event-stalemate-surrender
type: event
event_name: STALEMATE_SURRENDER
sectors: []
beacon_type: unknown
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 2
tags: [orphan, engine-invoked, combat-resolution, fuel-reward, no-choice]
---

# Stalemate surrender — `STALEMATE_SURRENDER`

## Summary
The bail-out an unresolvable fight gets: the enemy silently powers down its weapons, you
scoop 2 fuel out of the wreckage of the exchange, and the ship stops being hostile. It has
no choices and belongs to no event list — the engine hands it to you when a battle cannot
be finished.

## Trigger & Where It Appears
- **Not in any sector event list.** No `load="STALEMATE_SURRENDER"` exists anywhere in
  `raw/gamedata/` — the only occurrences of the id are its own definition and its text
  entry ([[source-events-xml]], [[source-text-events-xml]]). An event defined but never
  referenced must be invoked by the engine by name.
- Its immediate neighbour in the file is `BOSS_STALEMATE` ("The ship jumped away without
  warning. You prepare to pursue."), the boss-fight equivalent, which places both in a
  small family of engine-side combat-resolution events ([[source-events-xml]]).
- The **exact** condition that fires it is not stated anywhere in the data files. The name
  and the prose ("The ship suddenly disables their weapons. There's no explanation and they
  don't respond to hails") both point at a fight neither side can finish, but this wiki
  will not assert the rule without a source. See Open Questions.
- No Fandom page joins this event, and no Fandom page in `raw/wiki/` mentions the id at
  all.

## Text
> The ship suddenly disables their weapons. There's no explanation and they don't respond
> to hails. It seems during the battle they lost some fuel cells from their storage. You
> quickly collect it and leave.

(`event_STALEMATE_SURRENDER_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none)* | — | `<item_modify><item type="fuel" min="2" max="2"/></item_modify>` — **exactly +2 fuel**, then `<ship hostile="false"/>`: the enemy ship stays on screen but stops fighting. | 100% |

The fuel figure is one of the few flat, non-random rewards in the whole event set —
`min="2" max="2"` ([[source-events-xml]]).

## Blue Options
None.

## Rewards & Risks
- Reward: +2 fuel, guaranteed, and the fight ends.
- No risk in the event itself. Note there is **no** scrap, no `autoReward`, and no
  `destroyed`/`deadCrew` payout — a stalemate pays you the fuel to leave, nothing more.
- `<ship hostile="false"/>` does not remove the enemy; it disarms it. Nothing in the event
  prevents you from attacking again.

## Version differences
No `<!--DLC-->` marker on the event or its text ([[source-events-xml]]). Present unchanged
in both editions.

## Related
- [[concept-surrender-offers]] — the *other* kind of surrender, the `<surrender chance>`
  block on enemy ship definitions. This event is unrelated to that mechanism: it has no
  `chance` roll at all.
- [[event-boss-stalemate]] — the sibling engine event for the flagship

## Open Questions
- [ ] What exactly triggers it? Candidates: a fight where the player has no working
      weapons, or one where neither ship can damage the other. No source in `raw/`
      states the rule.
- [ ] Can it fire in a nebula / asteroid environment, or against boarding-only enemies?
- [ ] Is the disarmed ship still lootable if you finish it off afterwards?

## Sources
- [[source-events-xml]] (per `raw/gamedata/events.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
</content>
