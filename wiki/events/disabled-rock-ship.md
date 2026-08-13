---
id: event-disabled-rock-ship
type: event
event_name: ROCK_LOOTING
sectors: [[[sector-rock-controlled-sector]], [[sector-rock-homeworlds]]]
beacon_type: any
hostile: false
blue_options: [[[item-slug-crew]]]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [rock, salvage, blue-option, scrap-reward, unique, known-bug]
---

# Disabled Rock ship — `ROCK_LOOTING`

## Summary
A salvage-or-walk-away beacon. Strip a derelict Rock transport for scrap at a 50% risk of
a Rock patrol jumping you, or leave and still eat a 1-in-3 chance of being attacked
anyway. A Slug crew member removes the risk entirely and keeps the scrap — one of the
cleanest Slug blue options in the game.

## Trigger & Where It Appears
- Sectors: [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]]
- Event list: `NEUTRAL_ROCK`, allocated `min="7" max="8"` per Rock sector
  ([[source-sector-data-xml]])
- Beacon: **no ship present on arrival** ([[source-fandom-disabled-rock-ship]],
  `LRSmap=noship`) — the event has no `<ship>` element of its own; ships only appear
  inside branches ([[source-events-rock]])
- `unique="true"` — at most once per sector ([[source-events-rock]])

## Text
> You find a disabled rock transport floating near the beacon. You consider stripping it
> of useful parts but are uncertain why it's there in the first place.

(`event_ROCK_LOOTING_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Strip the ship. | — | Loads `eventList ROCK_LOOTING_STRIP` (2 entries) — see below. Scrap either way; a fight in one of the two. | 1/2 fight |
| 2 | Leave it alone. | — | Loads `eventList ROCK_LOOTING_LEAVE` (3 entries) — see below. No scrap either way; a fight in one of the three. | 1/3 fight |
| 3 | **(Slug Crew)** Check for lifeforms and keep a lookout for ships while looting the wreck. | `req="slug"` | Loads `eventList ROCK_LOOTING_SLUG` (2 entries). **Both** give scrap; **neither** gives a fight. | 100% scrap, 0% fight |

### Choice 1 — `ROCK_LOOTING_STRIP`
| Entry | Text | Effect |
|---|---|---|
| 1 | *"You salvage what you can from the ship. No one bothers you during the operation."* | `<autoReward level="low">standard</autoReward>` |
| 2 | *"A Rock patrol ship jumps in while you are salvaging the ship. They message you, 'Filthy pirates! Prepare to die!'…"* | `<ship load="ROCK_SHIP" hostile="true"/>` **and** `<autoReward level="low">standard</autoReward>` |

You get the salvage in **both** cases — the fight is on top of the reward, not instead of
it ([[source-events-rock]]).

### Choice 2 — `ROCK_LOOTING_LEAVE`
| Entry | Text | Effect |
|---|---|---|
| 1 | *"The Rock people are not known for setting traps but you hasten to leave anyway."* | nothing |
| 2 | **identical text id to entry 1** | nothing |
| 3 | *"Before you have a chance to leave, a Rock patrol ship arrives… 'Their killing spree ends now!'"* | `<ship load="ROCK_SHIP" hostile="true"/>`, **no reward** |

[[source-fandom-disabled-rock-ship]] independently tags the "nothing" outcome
`{{DuplicateEvent|2}}`, agreeing that it fills two of the three slots.

### Choice 3 — `ROCK_LOOTING_SLUG`
| Entry | Text | Effect |
|---|---|---|
| 1 | *"You salvage what you can from the ship. No lifeforms or ships are detected nearby."* | `<autoReward level="low">standard</autoReward>` |
| 2 | *"You begin the salvage operation but before long your crew warns you of an approaching ship. You hasten to leave before they get within firing range."* | `<autoReward level="low">standard</autoReward>` |

Different prose, identical mechanics. There is no downside branch.

## Blue Options
- **Slug crew member** (`req="slug"`) — any Slug aboard. It is a strict superset of choice
  1: same reward, zero fight risk. Thematically the Slug's mind-reading spots both the
  absent lifeforms and the incoming patrol ([[source-events-rock]],
  [[source-fandom-disabled-rock-ship]]).

## Rewards & Risks
- Reward: `autoReward level="low"` of type `standard` — the game's own word is **`low`**,
  which is scrap plus resources ("scrap with resources" in Fandom's vocabulary).
- Risk: a `ROCK_SHIP` fight, which carries the usual
  `<surrender chance="0.7" min="3" max="4">` branch — see [[event-rock-fight]].

> ⚠️ **CONTRADICTION / suspected bug:** the reward level's case.
> - Game files: `<autoReward level="low">standard</autoReward>` — **lowercase**, in all
>   five reward branches of this event ([[source-events-rock]], per
>   `raw/gamedata/events_rock.xml`). Everywhere else in the same file the levels are
>   uppercase (`LOW`, `MED`, `HIGH`, `RANDOM`).
> - [[source-fandom-disabled-rock-ship]] asserts in an HTML comment that this is a typo
>   and that *"the game treats this as `RANDOM`"*, and describes the payout as
>   "a random amount of scrap with resources" rather than a low amount.
>
> The file's literal content is not in dispute; what is in dispute is the *runtime
> behaviour* of an unrecognised level string, which no source here demonstrates. Fandom's
> claim is plausible and specific, but it is `medium` reliability and untested. Recorded
> as-is: the file says `low`, Fandom says it behaves as `RANDOM`. **Do not** convert
> either to a scrap number.

## Strategy Notes
- With a Slug: always choice 3. Free scrap, no risk.
- Without a Slug: choice 1 dominates choice 2 on expectation — choice 1 pays scrap in
  100% of outcomes and fights in 50%; choice 2 pays nothing in 100% and still fights in
  33%. Leaving is only correct if you are too damaged to survive a Rock ship at all.
  *(Opinion, but the outcome tables above are the whole argument.)*

## Related
- [[event-rock-fight]] — the `ROCK_SHIP` fight both risky branches load
- [[event-rock-atheists]] — the other `NEUTRAL_ROCK` blue-option beacon
- [[item-slug-crew]] — the gate on choice 3
- [[concept-auto-rewards]] — how `autoReward` levels resolve

## Open Questions
- [ ] Does an unrecognised `autoReward level` string genuinely fall through to `RANDOM`?
      This needs either a decompile or a controlled run to settle.
- [ ] Whether `eventList` selection is uniform (the 1/2 and 1/3 figures depend on it).

## Sources
- [[source-events-rock]] (per raw/gamedata/events_rock.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-disabled-rock-ship]] (per raw/wiki/disabled-rock-ship.md)
