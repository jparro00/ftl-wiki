---
id: event-store-rescue
type: event
event_name: STORE_RESCUE
sectors: []
beacon_type: quest
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [unique, orphan, unreachable, quest-giver, store, shipped-but-unused]
---

# Store rescue — `STORE_RESCUE`

## Summary
A fully authored quest-giver: a shuttle begs you to save its family's space dock from a
Rebel attacker, and accepting plants a quest marker that leads to a fight and then a
**store with free hull repairs**. It is complete, `unique="true"`, listed in the file's own
table of contents — and **no event list anywhere in the game data loads it**. Its payload
survives only because a different event hands out the same quest.

## Trigger & Where It Appears
- **Not in any sector event list.** `grep` across every file in `raw/gamedata/` finds
  `STORE_RESCUE` only in (a) the summary comment at the top of `events.xml`, (b) its own
  `<event name="STORE_RESCUE" unique="true">` definition, and (c) its text entries
  ([[source-events-xml]], [[source-text-events-xml]]). There is no `<event
  load="STORE_RESCUE"/>` and no commented-out one either — it is simply never wired up.
  The live `QUESTS` and `OVERRIDE_QUESTS` pools do not contain it
  ([[source-newevents]], [[source-dlceventsoverwrite]]).
- Tagged `unreachable`. Not tagged `cut-content`: `events.xml`'s own structure comment still
  lists it under *Special* as
  `STORE_RESCUE   (contains other quest events) / QUEST_STORE / QUEST_STORE_RESCUE`, which
  reads as an intended-but-unhooked event rather than a deliberately removed one
  ([[source-events-xml]]).
- Its quest destination **is** reachable: `MERCENARY_WORK_LIST` (under
  [[event-settlement-mercenary-work]]) also fires `<quest event="QUEST_STORE_RESCUE"/>`, so
  players do meet the follow-up without ever meeting this event
  ([[source-events-xml]]).
- Carries `<img planet="PLANET_POPULATED"/>` — it was written to appear at a populated
  planet.
- No Fandom page joins this event.

## Text
> Once you arrive at this populated region, you immediately pick up a distress signal. A
> small shuttle is asking anyone who'll listen for help protecting their family from a
> Rebel ship. Unsurprisingly, no one has yet responded to their request.

(`event_STORE_RESCUE_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | See if you can assist them. | — | *"It seems that a small space dock has done something to anger the Rebels. The store there is run by his family and he pleads that you rescue them. He uploads the coordinates of the station to your navigation system."* → `<quest event="QUEST_STORE_RESCUE"/>` — a quest marker is placed in the sector. | 100% |
| 2 | Ignore their pleas. | — | *"You block the channel and prepare to jump as soon as possible."* Nothing else. | 100% |

### The quest destination — `QUEST_STORE_RESCUE`

Documented here for context; it has its own `event_name` and is reachable independently, so
it belongs on [[event-quest-store-rescue]] rather than being folded in.

> Once you arrive at the beacon you detect a Rebel scout assaulting a compound on a nearby
> desolate moon.

| Choice | Outcome |
|--------|---------|
| Engage the Rebel and rescue the space dock. | `<ship load="SQUAT_STORE_RESCUE" hostile="true"/>` — a forced fight. |
| Avoid a fight. | *"After a time the ship powers down its weapons and jumps away. No life-signs are detected on the moon."* Nothing gained. |

**`SQUAT_STORE_RESCUE`** (`auto_blueprint="SHIPS_REBEL"`, [[source-events-ships]]) has
**no `<surrender>` and no `<escape>` block** — it will not give up and will not run. Both
`destroyed` and `deadCrew` pay the same:

- `autoReward level="MED"` `scrap_only`
- `<damage amount="-5"/>` — **5 hull repaired**
- `<store/>` — **the beacon becomes a store**

> The outpost hails you, "Thank you! I don't know what we did to anger the Rebels, but they
> were ready to kill us. I'll show you our goods and patch up your hull."

## Blue Options
None. Neither choice carries a `req`.

## Rewards & Risks
- Choice 1 costs a jump and commits you to a Rebel fight if you follow the marker through.
- Full payoff (via the quest): MED `scrap_only`, 5 hull repaired, and a store where there
  was none — a strong result, and the reason the quest survives elsewhere in the data.
- Choice 2 is free.

## Version differences
No `<!--DLC-->` marker on the event, the quest event, or the ship block
([[source-events-xml]], [[source-events-ships]]). It is equally unreachable in both
editions — `dlcEventsOverwrite.xml` redefines `QUESTS` as `OVERRIDE_QUESTS` and still does
not include it ([[source-dlceventsoverwrite]]).

## Strategy Notes
Not playable, so there is nothing to plan around. The practical note is the inverse: if you
see the *"Rebel scout assaulting a compound"* beacon in a run, it came from
[[event-settlement-mercenary-work]], not from this event.

## Related
- [[event-quest-store-rescue]] — the destination beacon (reachable; needs its own page)
- [[event-settlement-mercenary-work]] — `MERCENARY_WORK_START`, the live source of the same
  quest
- [[entity-rebels]]

## Open Questions
- [ ] Was `STORE_RESCUE` ever live in a shipped build, or unhooked from the start? The
      file's table of contents suggests it was meant to be in `QUESTS`.
- [ ] Does `QUEST_STORE` (defined next to it, a plain `<store/>` event with the comment
      "Can be used elsewhere") have any live reference?
- [ ] Exact scrap value of `MED scrap_only`.

## Sources
- [[source-events-xml]] (per `raw/gamedata/events.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-events-ships]] (per `raw/gamedata/events_ships.xml`)
- [[source-newevents]] (per `raw/gamedata/newEvents.xml`)
- [[source-dlceventsoverwrite]] (per `raw/gamedata/dlcEventsOverwrite.xml`)
</content>
