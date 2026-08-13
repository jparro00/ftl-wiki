---
id: event-confused-mantis
type: event
event_name: CONFUSED_MANTIS
sectors: [[[sector-engi-controlled-sector]], [[sector-engi-homeworlds]]]
beacon_type: any
hostile: false
blue_options: [human crew, mantis crew, [[item-mind-control]]]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [engi, mantis, unique, blue-option, crew-reward, crew-risk, clone-bay, system-upgrade, ae]
---

# Confused Mantis — `CONFUSED_MANTIS`

## Summary
An Engi ship asks you to talk down a Mantis who believes he is human. Send an untrained
away team and you are gambling a crew member; send a **Human** crew member, or use
**Mind Control**, and the gamble disappears. The best branch ends at a Mantis mining
colony where you can recruit a named Mantis crew member (Robert Smith) or take a free
Engines upgrade. It is a free-to-enter, no-cost event whose entire risk profile is
decided by which option you pick.

## Trigger & Where It Appears
- Sectors: [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]] — the event is a
  member of `NEUTRAL_ENGI`, the Engi-specific neutral list, and of no other list
  ([[source-events-engi]]). `sector_data.xml` allocates `NEUTRAL_ENGI` at 4–6 beacons in
  the Engi Controlled Sector and 5–7 in the Engi Homeworlds
  ([[source-sector-data-xml]]).
- The event's own definition carries the dev comment `<!-- in Engi Neutrals only-->`
  ([[source-newevents]]).
- Beacon: an ordinary (neutral) beacon; no ship is staged, so it starts non-hostile.
- `unique="true"` — at most once per run.
- Prerequisites: none. The three gated options need crew or a system (see Blue Options).

## Text
> As soon as you jump into the system, you receive a hail from a nearby civilian Engi
> vessel. Their Captain appears on your screen: "Strange bug. Can you assist in
> debugging?"

(`event_CONFUSED_MANTIS_text`, per [[source-text-events-xml]])

Taking choice 1 prints the Engi captain's explanation before the real decision:

> "Found malfunctioning Mantis. Believes it is human. Will receive input only from human.
> Danger Evaluation: Extremely High. Provide assistance."

## Choices & Outcomes

Top level:

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Listen to their problem. | — | Prints the captain's explanation, then opens the five-option inner menu below. | 100% |
| 2 | Explain that you can't do any programming and leave. | — | Nothing happens. | 100% |

Inner menu (after choice 1):

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1a | Send a shuttle with an away team to help. | — | Loads `eventList CONFUSED_MANTIS_DEFAULT` (3 entries) — see below. | 1/3 each |
| 1b | Leave them, a cornered Mantis is too dangerous. | — | Nothing happens. | 100% |
| 1c | **(Human Crew)** Send your human crewmember to communicate with the Mantis. | `req="human"` | The Mantis introduces himself as Robert Smith and asks to be returned home → single follow-up choice "Return him home." → loads `CONFUSED_MANTIS_HOME`. **No risk.** | 100% |
| 1d | **(Mantis Crew)** Send your Mantis crewmember to communicate with the Mantis. | `req="mantis"` | The Mantis panics, attacks the Engi and is killed by your crew member. `autoReward level="LOW">standard` — the game's own words for the tier. | 100% |
| 1e | **(Mind Control)** Use your Mind control System to calm him down. | `req="mind" lvl="1"` | He calms down, is returned to the human colony, the Engi reward you. `autoReward level="MED">standard`. | 100% |

`CONFUSED_MANTIS_DEFAULT` — the unassisted away team, 3 entries:

| # | Outcome | Effect |
|---|---------|--------|
| 1 | *"After an hour of convincing, the Mantis finally calms down and introduces himself as Robert Smith…"* | Follow-up "continue" → loads `CONFUSED_MANTIS_HOME` (the good branch). |
| 2 | *"The cornered and frightened Mantis attacks as soon as you approach. One of your crew is eviscerated…"* | `removeCrew` with `<clone>true</clone>` — **lose a crew member**, revived if you have a [[item-clone-bay]] (*"Your crew's clone is waiting when you return to the ship."*). |
| 3 | *"…You're able to subdue him and leave him at a Mantis colony in a neighboring system."* | Nothing. |

**Assuming uniform selection across the three list entries**, that is 1/3 the good branch,
1/3 a crew loss, 1/3 nothing. The game files state no percentage; this fraction is derived
from the list membership only ([[source-newevents]]).

`CONFUSED_MANTIS_HOME` — the mining colony, reached from 1a-outcome-1 or from 1c. It is a
separate `<event>` rather than a list, so **both** of its options are always offered and
you pick one:

| # | Choice | Outcome |
|---|--------|---------|
| 1 | Offer him a position on your ship. | *"He graciously accepts, having always wanted to serve in the Federation."* → `crewMember amount="1" class="mantis" id="name_RobertSmith"` — a **named Mantis crew member, Robert Smith**. |
| 2 | Ask if they can take a look at your engines. | *"They are happy to take a look…"* → `upgrade system="engines" amount="1"`. |

## Blue Options
- **Human crew member** (`req="human"`) — removes the 1/3 crew-loss risk entirely and
  routes straight to the mining colony. [[source-fandom-confused-mantis]] claims this is
  the **only event in the game with a Human crew blue option**; that is a claim about the
  whole corpus and is not verifiable from any one game file.
- **Mantis crew member** (`req="mantis"`) — safe, but the worst payoff: the Mantis dies
  and you get `LOW` standard rewards. It forecloses the crew recruit.
- **[[item-mind-control]]**, level 1 (`req="mind" lvl="1"`) — safe, `MED` standard
  rewards. Also forecloses the crew recruit.

Note the ordering: the two "safe" species/system options give scrap, while the *risky*
away-team and the Human option are the only routes to Robert Smith.

## Rewards & Risks
- **Best case:** a free Mantis crew member (via 1c, guaranteed; or 1a, 1/3) — one of the
  cheapest crew acquisitions in the game, since the event costs nothing to enter.
- **Alternative payoff:** +1 Engines upgrade instead of the crew member, same branch.
- **Scrap:** `LOW` standard (Mantis crew) or `MED` standard (Mind Control). "Standard"
  is scrap with resources in the wiki's vocabulary ([[source-fandom-confused-mantis]]).
- **Risk:** exactly one — the 1/3 crew-loss entry on the unassisted away team, mitigated
  but not removed by a [[item-clone-bay]].
- No scrap, fuel or missile cost anywhere in the event.

## Strategy Notes
- With a Human crew member aboard, choice 1c is strictly dominant: no risk, and it reaches
  the recruit. Most starting ships have Human crew, so this is usually available.
- Without Human crew, the away team is a 1/3 chance of a crew member, 1/3 of losing one.
  With a Clone Bay the downside is largely neutralised and the gamble is worth taking;
  without one it is a coin-flip on a crew member's life for a crew member's life.
- If you have Mantis crew or Mind Control *and* no Human crew, those options trade the
  recruit for a guaranteed small-to-medium scrap payout — take them when your crew is
  already full or you cannot afford the risk. (Opinion, reasoned from the outcome table;
  no source ranks these.)
- Robert Smith is a Mantis, so he is a boarding asset, not a repair asset.

> ⚠️ **CONTRADICTION:** minor wording only, in the mining-colony prose.
> - Game files: *"Robert's family, the head engineers, are excited to see him, and **are**
>   very grateful for his return."* ([[source-text-events-xml]], per
>   `raw/gamedata/text_events.xml`)
> - Fandom: *"…excited to see him, and very grateful for his return."*
>   ([[source-fandom-confused-mantis]])
>
> Trusting the game files — reliability `high` vs `medium`, and they are the exact 1.6.x
> build being played. This looks like a transcription slip, not a version difference; no
> AE/vanilla split is plausible since the whole event is AE content.

## Related
- [[event-abandoned-station]] — another AE `newEvents.xml` neutral with a Clone Bay branch
- [[event-refueling-platform]] — the other `newEvents.xml` event in the Engi neutral list
- [[entity-engi]], [[entity-mantis]]
- [[item-mind-control]], [[item-clone-bay]], [[item-engines]]
- [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]]
- [[concept-blue-options]]

## Open Questions
- [ ] Whether `eventList` selection is uniform (the 1/3 figures depend on it).
- [ ] Actual scrap/resource values behind `LOW` and `MED` `standard` rewards.
- [ ] Whether the Human blue option really is unique in the game, as Fandom claims.
- [ ] Whether Robert Smith arrives with any non-default skill levels.

## Sources
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-events-engi]] (per raw/gamedata/events_engi.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-confused-mantis]] (per raw/wiki/confused-mantis.md)
