---
id: event-rebel-fight-chance
type: event
event_name: ROGUE_REBEL
sectors: [[[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: any
hostile: false
blue_options: [sensors lvl 2, sensors lvl 3]
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [rebel, filler, blue-option, sensors, fleet-advance-risk, advanced-edition]
---

# Rebel fight chance — `ROGUE_REBEL`

## Summary
An optional Rebel hunt. Searching blind is a gamble — you may not find him, and one branch
costs you fleet-pursuit time — while Sensors turns the whole event into a clean fight, and
Sensors 3 turns it into a fight against a ship that cannot run. One of the clearest
demonstrations in the game of what an upgraded Sensors subsystem buys you outside combat.

## Trigger & Where It Appears
- Event lists: `NEUTRAL` and `NEUTRAL_EXIT` in `newEvents.xml`, tagged
  `<!--DLC matt - down below-->` ([[source-newevents]]), plus `OVERRIDE_NEUTRAL` and
  `OVERRIDE_NEUTRAL_EXIT` ([[source-dlceventsoverwrite]]).
- Universal filler / exit pools, so it can appear in any sector that falls back to generic
  neutrals. Fandom scopes it to the two Slug sectors as an exit-and-filler event
  ([[source-fandom-rebel-fight-chance]]).
- Not `unique`.
- Beacon: ordinary; no distress flag, no environment.

## Text
`[varies: textList ROGUE_REBEL_TEXT]` — four variants
([[source-newevents]], [[source-text-events-xml]]). All four report a Rebel ship preying on
local civilians. One sample:

> You jump into a field of debris. It appears a battle recently took place here, and the
> loser seems to have been a civilian ship. A message was left on repeat before it was
> destroyed: "Rebels attacking, please send aid!" The responsible Rebels are likely still
> nearby.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Go looking for the Rebel ship. | — | Loads `ROGUE_REBEL_SEARCH` — four entries, below. | — |
| 2 | No time to search, you prepare to jump away. | — | `<event/>` — nothing happens. | 100% |
| 3 | **(Improved Sensors)** Perform a scan of the area. | `req="sensors" lvl="2" max_group="0"` | *"You quickly find the Rebel ship's location and move to intercept."* → fight `REBEL`. | 100% |
| 4 | **(Advanced Sensors)** Pinpoint the Rebel's location. *(hidden)* | `req="sensors" lvl="3" max_group="0"` | *"You find the Rebel ship hiding on a nearby asteroid. You are able to get a shot off and permanently disable their engines before they notice you."* → fight `REBEL` **plus** `<status type="limit" target="enemy" system="engines" amount="0"/>`. | 100% |

### `ROGUE_REBEL_SEARCH` — the blind-search pool
Four entries, two of which are functionally the same fight. **Assuming uniform selection
across list entries:**

| Outcome | Entries | Share |
|---|---|---|
| *"You spend some time looking around but your scanners cannot pick up any trace of the Rebel ship. You prepare to move on."* → nothing | 1 | 1/4 |
| *"After a short search you find the Rebel ship…"* **or** *"You are able to quickly track down the Rebel…"* → fight `REBEL` | 2 | 2/4 |
| *"After far too much time spent searching, you are finally able to track him down. You go into the fight pondering just how much of a head start you've lost on the Rebel Fleet..."* → `<modifyPursuit amount="1"/>` **then** fight `REBEL` | 1 | 1/4 |

([[source-newevents]], [[source-text-events-xml]]) Derived from list contents, not a stated
percentage. Fandom independently marks the two find-him entries as a duplicate pair
(`{{DuplicateEvent|2}}`, [[source-fandom-rebel-fight-chance]]), which agrees with the XML.

### The `REBEL` ship
`auto_blueprint="SHIPS_REBEL"`, 50% surrender chance (`min=2 max=3`), 50% escape chance
(`min=3 max=4`), `DESTROYED_DEFAULT` / `DEAD_CREW_DEFAULT` — default rewards
([[source-events-ships]]). The Sensors-3 branch's
`status type="limit" target="enemy" system="engines" amount="0"` caps enemy engine power at
zero for the fight, which removes their dodge and makes the 50% escape branch unreachable
in practice.

> ⚠️ **CONTRADICTION:** the pursuit penalty.
> - Game files: `<modifyPursuit amount="1"/>` ([[source-newevents]]).
> - Fandom: *"Rebel Fleet pursuit is doubled for 1 jump"*
>   ([[source-fandom-rebel-fight-chance]]).
>
> These are descriptions of the same tag at different levels — `modifyPursuit amount="1"`
> is the raw instruction, "doubled for one jump" is Fandom's account of what the engine
> does with it. Recorded rather than resolved; the game files are the higher-reliability
> statement of *what is written*, Fandom of *what it feels like*.

## Blue Options
- **[[item-sensors]] level 2** (`req="sensors" lvl="2"`, `max_group="0"`) — replaces the
  gamble with a guaranteed fight: no wasted jump, no pursuit risk. Not `hidden`, so it is
  visible whenever you qualify.
- **[[item-sensors]] level 3** (`req="sensors" lvl="3"`, `hidden="true"`) — the same fight,
  against an enemy whose engines are permanently disabled. This is the best outcome
  available at the beacon.

`max_group="0"` on both means the requirement is checked against the subsystem's own level
rather than a grouped alternative.

## Rewards & Risks
- Default Rebel-fight rewards on every branch that produces a fight.
- Risk on the blind search: 1/4 nothing at all (a wasted beacon), 1/4 a fleet-pursuit
  advance on top of the fight.
- No risk at all on choice 2, or on either Sensors branch.

## Strategy Notes
- *(Opinion.)* This event is the argument for buying Sensors 2 early: it converts a 1/4
  chance of losing tempo to the Rebel fleet into a clean, chosen engagement.
- Without Sensors, whether to search depends entirely on how healthy you are — the expected
  value is a Rebel fight three times out of four, which is normal filler-event value, but
  the pursuit branch is a real cost in a sector you are trying to leave.
- Sensors 3 is the rare case where a blue option makes a fight *strictly* easier rather
  than just skipping it — a disabled-engine enemy cannot dodge or flee.

## Related
- [[event-rebel-checkpoint]] — the other Rebel filler event from the same DLC batch
- [[event-rebel-ship-supplying-civilians]] — the third of the batch
- [[event-rebel-fight-chance-in-nebula]] — the nebula-sector counterpart
- [[item-sensors]], [[entity-rebels]], [[concept-rebel-fleet-advance]]

## Open Questions
- [ ] Whether event-list selection is truly uniform.
- [ ] Exactly what `modifyPursuit amount="1"` costs in jumps — see the contradiction above.
- [ ] The full sector reach of `NEUTRAL` / `NEUTRAL_EXIT` placement.

## Sources
- [[source-newevents]] (per `raw/gamedata/newEvents.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-events-ships]] (per `raw/gamedata/events_ships.xml`)
- [[source-dlceventsoverwrite]] (per `raw/gamedata/dlcEventsOverwrite.xml`)
- [[source-fandom-rebel-fight-chance]] (per `raw/wiki/rebel-fight-chance.md`)
