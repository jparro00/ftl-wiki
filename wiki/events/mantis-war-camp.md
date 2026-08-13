---
id: event-mantis-war-camp
type: event
event_name: QUEST_MANTIS_INVASION_START
sectors: [[[sector-civilian-sector]], [[sector-federation-space]], [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: quest
hostile: false
blue_options: []
chain: [[[chain-mantis-war-camp]]]
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [quest-start, unique, scrap-reward, mantis]
---

# Mantis war camp — `QUEST_MANTIS_INVASION_START`

## Summary
A settlement asks you to scout a Mantis war camp. Unusually for a quest start, **accepting
pays immediately** (`MED scrap_only`) and costs nothing, so the decision is essentially free
money plus an optional marker. The marker itself ([[event-quest-mantis-invasion]]) is where
the risk lives.

## Trigger & Where It Appears
- Event lists: `QUESTS`, `QUESTS_ZOLTAN`, and `OVERRIDE_QUESTS` under AE
  ([[source-newevents]], [[source-dlceventsoverwrite]])
- Sector allocations ([[source-sector-data-xml]]):
  [[sector-federation-space]] `QUESTS 1–1`, [[sector-civilian-sector]] `QUESTS 0–2`,
  [[sector-zoltan-controlled-sector]] / [[sector-zoltan-homeworlds]] `QUESTS_ZOLTAN 0–1`
- `unique="true"` ([[source-events-xml]])
- Beacon: no ship staged; [[source-fandom-mantis-war-camp]] marks `LRSmap=noship`

> ⚠️ **CONTRADICTION:** sector coverage.
> - Game files: `QUESTS` is allocated `min=1 max=1` in `STANDARD_SPACE`
>   ([[source-sector-data-xml]]), so [[sector-federation-space]] is in scope.
> - Fandom: lists three sectors and omits Federation space ([[source-fandom-mantis-war-camp]]).
>
> Trusting the game files (`high` vs `medium`); same omission pattern as every other
> `QUESTS`-list event.

## Text
> You receive a request, "All of our military ships have been destroyed or damaged during
> the rebellion. However, there have been reports of a Mantis war camp only a few jumps from
> us. Can you help?"

(`event_QUEST_MANTIS_INVASION_START_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Pledge to do what you can. | — | *"Thank you! If you can just give us a count on their numbers perhaps we can get the Rebels to help."* → `autoReward level="MED"` **`scrap_only`** **and** `<quest event="QUEST_MANTIS_INVASION"/>`. | 100% |
| 2 | Apologize and decline. | — | *"There's no way you are crazy enough to want to take on a Mantis war-band."* → nothing. | 100% |

Choice 1 is `hidden="true"`, so the scrap payment is not previewed ([[source-events-xml]]).
[[source-fandom-mantis-war-camp]] records the same reward.

## Blue Options
None here. The blue options are on the destination, [[event-quest-mantis-invasion]] —
a missile weapon and a Fire Bomb.

## Rewards & Risks
- Accepting is **strictly positive at this beacon**: `MED scrap_only` up front, no cost, no
  ship, no fight.
- All the risk is at the marker, where two of the three routes end in a Mantis patrol
  fight.
- Declining forfeits the scrap as well as the quest.

## Strategy Notes
- Always accept. The payment is unconditional and you are never obliged to actually jump to
  the marker. *(Derived from the effect list — the `autoReward` fires on the choice, not on
  completing the quest; no source states the advice.)*
- Whether to *visit* the marker is a separate decision, and depends entirely on whether you
  hold a Fire Bomb — see [[event-quest-mantis-invasion]].

## Related
- [[event-quest-mantis-invasion]] — the quest marker this places
- [[event-mantis-fight]] — the ordinary Mantis encounter
- [[chain-mantis-war-camp]]
- [[entity-mantis]]

## Open Questions
- [ ] Does the settlement react in any way if you take the scrap and never visit the marker?
      Nothing in the files suggests so.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-fandom-mantis-war-camp]] (per raw/wiki/mantis-war-camp.md)
