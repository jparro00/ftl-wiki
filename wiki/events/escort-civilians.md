---
id: event-escort-civilians
type: event
event_name: QUEST_ESCORT
sectors: [[[sector-civilian-sector]], [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-federation-space]], [[sector-pirate-controlled-sector]], [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]]]
beacon_type: quest
hostile: false
blue_options: []
chain: [[[chain-escort-civilians]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [quest-start, repeatable, fuel-reward, store-chance, rebel-fight, ae-vs-vanilla]
---

# Escort civilians — `QUEST_ESCORT`

## Summary
A lightly-armed civilian ship asks for an escort. Accepting pays a small fuel down-payment
immediately and places a quest marker whose payoff is one of three (AE: four) outcomes —
including a **free store with hull repairs** and, in Advanced Edition only, a **free reactor
upgrade**. One of the few quest starts that is explicitly `unique="false"`, so it can turn
up more than once.

## Trigger & Where It Appears
- Event lists: `QUESTS`, `QUESTS_ENGI`, `QUESTS_PIRATE`, `QUESTS_ROCK`, and
  `OVERRIDE_QUESTS` under AE ([[source-newevents]], [[source-dlceventsoverwrite]])
- Sector allocations ([[source-sector-data-xml]]):
  [[sector-federation-space]] `QUESTS 1–1`, [[sector-civilian-sector]] `QUESTS 0–2`,
  [[sector-engi-controlled-sector]] / [[sector-engi-homeworlds]] `QUESTS_ENGI 1–1`,
  [[sector-pirate-controlled-sector]] `QUESTS_PIRATE 0–1`,
  [[sector-rock-controlled-sector]] / [[sector-rock-homeworlds]] `QUESTS_ROCK 0–1`
- **`unique="false"`** — stated explicitly in the XML, unusually for a quest
  ([[source-events-xml]])
- Beacon: a ship is present and non-hostile, `<ship load="CIVILIAN_SHIP" hostile="false"/>`;
  [[source-fandom-escort-civilians]] marks `LRSmap=ship`

> ⚠️ **CONTRADICTION:** sector coverage.
> - Game files: `QUESTS` is allocated `min=1 max=1` in `STANDARD_SPACE`
>   ([[source-sector-data-xml]]), so [[sector-federation-space]] is in scope.
> - Fandom: lists six sectors and omits Federation space ([[source-fandom-escort-civilians]]).
>
> Trusting the game files (`high` vs `medium`); the same omission recurs on every
> `QUESTS`-list event.

## Text
The intro **varies**: `<text load="QUEST_ESCORT_TEXT"/>` draws from a 3-entry `textList`
([[source-events-xml]], [[source-text-events-xml]]). Example:

> After a short time you receive a message, "Hello. I hope it's not a bother, but I'm
> looking for an escort to a nearby system. This region is quite dangerous and our ship is
> not well-armed."

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Accept. | — | *"Great. Take this bit of fuel as a down-payment. We'll be one step behind you, following your jump signatures."* → `autoReward level="LOW"` **`fuel_only`** and `<quest event="QUEST_ESCORT_ARRIVE"/>`. | 100% |
| 2 | Decline. | — | *"We understand. Not everyone is confident they can survive in these hostile times…"* → nothing. | 100% |

[[source-fandom-escort-civilians]] renders the down-payment as 1–3 fuel; the XML states only
the `LOW fuel_only` tier, which is the game's own word for it.

### The destination — `eventList QUEST_ESCORT_ARRIVE`
Not a separate beacon page: it is the quest marker's event list, loaded by `<quest>`. It is
also loaded by [[event-escort-civilians-ftl-haywire]], the distress-list version of the same job
([[source-events-xml]]).

Assuming uniform selection across `eventList` entries ([[concept-event-list-weighting]]):

| Entry | Text | Effect | Odds (AE) | Odds (vanilla) |
|---|---|---|---|---|
| 1 | *"…Much to your dismay you are ambushed by a Rebel ship. You walked right into their trap!"* | `<ship load="REBEL" hostile="true"/>` — an ordinary [[event-rebel-fight]], which offers surrender at 50% ([[concept-surrender-offers]]) | 1/4 | 1/3 |
| 2 | *"Shortly after you arrive, the ship you were escorting jumps nearby. They thank you for your help and offer you a reward."* | `autoReward level="HIGH"` `standard` | 1/4 | 1/3 |
| 3 | *"Let my friends patch up some of your hull and show you their wares."* | `<damage amount="-5"/>` (5 hull repaired) **and `<store/>`** | 1/4 | 1/3 |
| 4 | *"We work at a nearby fusion power plant, we could try to improve your reactor's output…"* | `<upgrade amount="1" system="reactor"/>` — **+1 reactor bar** | 1/4 | — |

**Version note (rule 10).** Entry 4 is wrapped `<event><!--DLC!--> … </event>` in
`events.xml` ([[source-events-xml]]), so it is Advanced Edition content. The vanilla pool is
the first three entries only, which changes every probability in the table — hence
`version: both` with two odds columns.

## Blue Options
None. No choice in this event or its destination carries a `req` ([[source-events-xml]]).

## Rewards & Risks
- Guaranteed: `LOW fuel_only` for accepting, which alone makes it worth taking on a
  fuel-poor run.
- Destination: 3/4 (AE) chance of a strictly good outcome — `HIGH standard`, a store plus
  repairs, or a reactor upgrade.
- Risk: 1/4 (AE) / 1/3 (vanilla) chance of an ambush by a standard `REBEL` ship. There is no
  way to avoid the fight once you jump to the marker.

## Strategy Notes
- Good expected value: the only bad entry is a fight you would probably have taken anyway
  for the rewards, and three of four entries are pure upside. *(Opinion, derived from the
  table; no source gives a verdict.)*
- The store entry matters most on runs with scrap but nowhere to spend it, and the reactor
  upgrade is the strongest AE-only outcome for a low-power ship.
- Because the event is `unique="false"`, it can recur — and each instance rolls the
  destination table independently.

## Related
- [[event-escort-civilians-ftl-haywire]] — the distress-beacon version of the same job, sharing `QUEST_ESCORT_ARRIVE`
- [[event-rebel-fight]] — the ambush at the destination
- [[chain-escort-civilians]]
- [[concept-surrender-offers]]

## Open Questions
- [ ] Confirm `eventList` selection is uniform — every fraction above depends on it.
- [ ] Fandom gives the down-payment as 1–3 fuel; is that the definition of the
      `LOW fuel_only` tier, or measured from play?

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-fandom-escort-civilians]] (per raw/wiki/escort-civilians.md)
