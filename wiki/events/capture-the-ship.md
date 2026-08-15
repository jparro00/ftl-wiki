---
id: event-capture-the-ship
type: event
event_name: QUEST_CREWDEAD_START
sectors: [[[sector-civilian-sector]], [[sector-federation-space]], [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]], [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: quest
hostile: false
blue_options: [[[item-teleporter]], [[item-anti-bio-beam]], [[item-fire-bomb]]]
chain: [[[chain-capture-the-ship]]]
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [quest-start, unique, blue-option, boarding, weapon-reward, hull-damage-risk]
---

# Capture the ship — `QUEST_CREWDEAD_START`

## Summary
A quest start that is **gated entirely behind crew-killing equipment**. Without a
Teleporter, Anti-Bio Beam or Fire Bomb the beacon is a dead end that pays nothing; with
one, it opens a marker where you must kill an enemy crew **without destroying their ship**
for a `HIGH weapon`. Blowing the target up instead is the single most damaging outcome in
the game.

## Trigger & Where It Appears
- Event lists: `QUESTS`, `QUESTS_ROCK`, `QUESTS_ZOLTAN`, and `OVERRIDE_QUESTS` under AE
  ([[source-newevents]], [[source-dlceventsoverwrite]])
- Sector allocations ([[source-sector-data-xml]]):
  [[sector-federation-space]] `QUESTS 1–1`, [[sector-civilian-sector]] `QUESTS 0–2`,
  [[sector-rock-controlled-sector]] / [[sector-rock-homeworlds]] `QUESTS_ROCK 0–1`,
  [[sector-zoltan-controlled-sector]] / [[sector-zoltan-homeworlds]] `QUESTS_ZOLTAN 0–1`
- `unique="true"` ([[source-events-xml]])
- Beacon: no ship staged; [[source-fandom-capture-the-ship]] marks `LRSmap=noship`

> ⚠️ **CONTRADICTION:** sector coverage.
> - Game files: `QUESTS` is allocated `min=1 max=1` in `STANDARD_SPACE`
>   ([[source-sector-data-xml]]), so [[sector-federation-space]] is in scope.
> - Fandom: lists five sectors and omits Federation space ([[source-fandom-capture-the-ship]]).
>
> Trusting the game files (`high` vs `medium`); consistent with the same omission on every
> other `QUESTS`-list event.

## Text
> You arrive to find a number of ships convening around a station. There is some unencrypted
> chatter between the ships, you tune in and listen for anything interesting.

(`event_QUEST_CREWDEAD_START_text`, per [[source-text-events-xml]])

A single unlabelled `continue` choice loads the named event `QUEST_CREWDEAD_START_2` — not
an event list, so this step is deterministic ([[source-events-xml]]).

## Choices & Outcomes

### `QUEST_CREWDEAD_START_2`
> Overhearing their conversation, it seems that they need to take possession of an enemy
> ship intact.

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Offer your services. | — | *"They briefly scan your ship and inform you that you are not 'properly equipped' for this type of mission."* → nothing. | 100% |
| 2 | Leave them alone. | — | *"If they wanted your help they would surely ask for it. You prepare to leave."* → nothing. | 100% |
| 3 | **(Teleporter)** Offer to board their ship. | `req="teleporter" lvl="1"` | → `QUEST_CREWDEAD_CONTINUE` | 100% |
| 4 | **(Bio Beam)** Offer to 'remove' their crew. | `req="BEAM_BIO"` | → `QUEST_CREWDEAD_CONTINUE` | 100% |
| 5 | **(Fire Bomb)** Offer to burn the crew out. | `req="BOMB_FIRE"` | → `QUEST_CREWDEAD_CONTINUE` | 100% |

All five are `hidden="true"`. The three blue options are interchangeable — they load the
same follow-up with no difference in text or reward ([[source-events-xml]]).

### `QUEST_CREWDEAD_CONTINUE`
> They quickly scan your ship and say, "It appears you could help. A bandit has made off
> with some very important cargo, though I doubt they have any understanding of what it is
> they stole. We need you to capture the ship intact.

| # | Choice | Outcome |
|---|---|---|
| 1 | Agree to capture the ship. | *"Great, we'll relay their coordinates. Remember, do NOT destroy that ship!…"* → `<quest event="QUEST_CREWDEAD"/>` — a quest marker is added. See [[event-quest-crewdead]]. |
| 2 | Decline. | *"We understand. Hopefully we can find a solution to this on our own."* → nothing. |

**Nothing is paid up front.** The `<quest>` tag is the only effect on the accept branch
([[source-events-xml]]).

## Blue Options
- **[[item-teleporter]]** (`req="teleporter" lvl="1"`) — level 1 is enough; the gate is
  merely having the system.
- **[[item-anti-bio-beam]]** (`req="BEAM_BIO"`) — the weapon, not a system.
- **[[item-fire-bomb]]** (`req="BOMB_FIRE"`) — the weapon, not a system.

Any one of the three unlocks the quest, and all three lead to the identical branch. Without
one, choices 1 and 2 both do nothing — the beacon is a complete write-off.

## Rewards & Risks
- Here: no reward and no risk either way.
- At the marker ([[event-quest-crewdead]]): `autoReward level="HIGH"` **`weapon`** for
  killing the crew, or the worst hull-damage result in the game for destroying the ship.
- The gating equipment is the same equipment you need to *win* the quest, which is the
  point of the gate — you cannot accept a job you have no way of completing.

## Strategy Notes
- Only accept if the tool you were gated on can realistically clear an enemy crew. A
  Teleporter with two crew is a very different proposition from an Anti-Bio Beam, and
  overshooting into a hull kill is punished hard. *(Opinion, from the reward/damage split
  below; no source states it.)*
- [[source-fandom-capture-the-ship]] notes the destroy outcome deals more damage to the
  player ship than any other event in the game.

## Related
- [[event-quest-crewdead]] — the quest marker this places
- [[item-teleporter]], [[item-anti-bio-beam]], [[item-fire-bomb]] — the three gates
- [[chain-capture-the-ship]]
- [[entity-pirates]]

## Open Questions
- [ ] Is there any difference at all between the three blue routes? Nothing in the XML
      distinguishes them, but the target ship's behaviour under each is untested.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-fandom-capture-the-ship]] (per raw/wiki/capture-the-ship.md)
