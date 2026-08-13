---
id: event-engi-smashed-ships
type: event
event_name: ENGI_SEX
sectors: [[[sector-engi-controlled-sector]], [[sector-engi-homeworlds]]]
beacon_type: any
hostile: true
blue_options: [engi crew]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unique, dlc, blue-option, trap, forced-fight-optional]
---

# Engi smashed ships — `ENGI_SEX`

## Summary
Two Engi ships are stuck together and it looks like a rescue. Helping starts a fight that
pays **nothing at all** on victory. An Engi crewmember instead explains what is actually
happening — the ships are mating — and gets you paid for looking away. A rare case where
the blue option is the only branch with a reward and the "helpful" branch is a pure trap.

## Trigger & Where It Appears
- Sectors: [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]]
- Beacon: ordinary — no `<distressBeacon/>` or `<store/>` tag ([[source-events-xml]], per
  `raw/gamedata/events_engi.xml`)
- Event list: `NEUTRAL_ENGI`, allocated `min=4 max=6` in Engi Controlled Sector and
  `min=5 max=7` in Engi Homeworlds ([[source-sector-data-xml]])
- Marked in the file as DLC-added content ([[source-events-xml]])
- `unique="true"` — at most once per run

## Text
> What appeared to be a single damaged ship is in fact two ships that have smashed into each
> other... there is a flurry of comm signals and damage, and it's hard to determine what
> occurred. The vessels appear to be... Engi? They look locked together by the impact and
> can't free themselves.

(`event_ENGI_SEX_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Attempt to help the ships by prying them apart. | — | *"To your surprise, one of the Engi vessels attacks!…"* → fight `ENGI_SEX_SHIP` (`auto_blueprint="SHIPS_CIRCLE"`). On **destroyed** or **dead crew** → `ENGI_SEX_SHIP_DONE`: *"Apparently, you interrupted the equivalent of a 'consolidation'…"* → **nothing**. The ship's outcome blocks contain no `autoReward`. | 100% |
| 2 | Ignore the damaged vessels. | — | Empty `<event/>` — nothing happens. | 100% |
| 3 | **(Engi Crew)** Have your Engi crewmember hail the vessel and assess the damage. | `req="engi"` | Your Engi refuses and explains the ships are "achieving a union"; continue → *"You elect to leave the two Engi ships... to their 'business.' … you do manage to salvage what scrap parts you can from the perimeter"* → `<autoReward level="MEDIUM">stuff</autoReward>`. | 100% |

## Blue Options
- **Engi crewmember** (`req="engi"`) — any Engi crew satisfies it. It is the **only** branch
  of this event that awards anything ([[source-events-xml]]). It also skips the fight
  entirely, so it costs no hull.

## Rewards & Risks
- Choice 3: a `stuff` reward — resources with some scrap, per
  [[source-fandom-engi-smashed-ships]].
- Choice 1: an unavoidable fight once chosen, with **no victory reward**. Confirmed on both
  sides: the `ENGI_SEX_SHIP` `destroyed` and `deadCrew` blocks carry only text and a
  continue-choice ([[source-events-xml]]), and Fandom records the outcome as "Nothing
  happens" ([[source-fandom-engi-smashed-ships]]).
- Choice 2: no cost, no reward.

> ⚠️ **CONTRADICTION (data vs. schema):** the choice-3 reward is written
> `<autoReward level="MEDIUM">stuff</autoReward>`, but `MEDIUM` is not one of the levels the
> game's other events use (`LOW` / `MED` / `HIGH` / `RANDOM`).
> - Game files: the literal string is `MEDIUM` ([[source-events-xml]], per
>   `raw/gamedata/events_engi.xml`).
> - Fandom: annotates this as a typo for `MED` and states that the game "treats this as a
>   `RANDOM` value" ([[source-fandom-engi-smashed-ships]]).
>
> The typo is a verified fact; the *consequence* is a Fandom claim about engine behaviour
> that the game files do not state, so it is recorded as `medium` reliability rather than
> asserted. The same `MEDIUM` string appears four more times in
> [[event-the-engi-virus]].

## Strategy Notes
- With any Engi aboard, take choice 3 — it is free resources and the only paying branch.
  *(Opinion, but the outcome table leaves little room.)*
- Without an Engi, choice 2 is correct. Choice 1 is a fight for zero reward; the only thing
  it can give you is hull damage. *(Opinion, derived from the ship's empty outcome blocks.)*

## Related
- [[event-the-engi-virus]] — the other DLC `NEUTRAL_ENGI` unique with an Engi-crew blue option
- [[event-engi-surrender]] — the other "leave them alone" Engi judgement call
- [[entity-engi]]
- [[concept-blue-options]]

## Open Questions
- [ ] Does the engine really fall back to `RANDOM` on an unrecognised `autoReward` level?
      Only Fandom asserts this.
- [ ] What does a `stuff` reward contain, as distinct from `standard`?

## Sources
- [[source-events-xml]] (per `raw/gamedata/events_engi.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-engi-smashed-ships]] (per `raw/wiki/engi-smashed-ships.md`)
