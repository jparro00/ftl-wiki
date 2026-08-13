---
id: event-plagued-station
type: event
event_name: DONOR_PLAGUE
sectors: [[[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: any
hostile: false
blue_options: [[[item-medbay]]]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [slug, unique, donor-event, filler, crew-loss-risk, crew-reward-chance, clone-bay, blue-option, gamble]
---

# Plagued station — `DONOR_PLAGUE`

## Summary
A gamble at an abandoned station: board it for a one-in-three shot at a free Human crew
member, a one-in-three shot at losing a crew member to disease, and a one-in-three shot at
nothing but low scrap — or skip the risk entirely and take a random scrap payout for
free. A level-2 Medbay removes the downside of the bad roll.

## Trigger & Where It Appears
- Sectors: [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]
- Pooled in the base `NEUTRAL` and `NEUTRAL_EXIT` lists (`newEvents.xml`, the names
  `sector_data.xml` actually references) and in their Advanced Edition replacements
  `OVERRIDE_NEUTRAL` / `OVERRIDE_NEUTRAL_EXIT` (`dlcEventsOverwrite.xml`). It is in the
  pool in **both editions**; only the size of the pool around it changes, since the
  `OVERRIDE_` lists add nine further AE entries ([[source-newevents]],
  [[source-dlceventsoverwrite]], [[source-sector-data-xml]]).
- The `_EXIT` lists are the engine's **filler** pool — the comment on `NEUTRAL_EXIT` reads
  *"This event list is hardcoded to fill out a sector if it ran out of all other calls for
  that sector"* ([[source-newevents]]). Fandom marks the event `alsooccur=exitandfiller`,
  which is the same fact ([[source-fandom-plagued-station]]).
- `unique="true"` — at most once per run.
- No ship at the beacon; Long-Range Scanners show nothing
  ([[source-fandom-plagued-station]]).

## Text
> You arrive near a damaged and dilapidated space station. It appears to be abandoned but
> you detect faint life signatures on board.

(`event_DONOR_PLAGUE_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Board the station and look for survivors. | — | Loads `DONOR_PLAGUE_LIST` — three outcomes, below. | see below |
| 2 | Scrap some of the debris. | — | *"While waiting for the FTL drive to charge, you skirt around the edge of the station and collect some scrap."* → `autoReward level="RANDOM"` type `scrap_only`. | 100% |

`RANDOM` is the game's own word for choice 2's reward level — it rolls a tier rather than
naming one ([[source-events-xml]]). Fandom renders it as *"a random amount of scrap"*
([[source-fandom-plagued-station]]).

### `DONOR_PLAGUE_LIST` — the boarding outcomes

Three distinct members, none duplicated. **Assuming uniform selection across list entries,
each is 1/3.** The game files state no percentage; this is derived from list membership
only ([[source-events-xml]]).

| Odds | Outcome |
|---|---|
| 1/3 | *"All around you is the stench of death and decay. The life sign readings must have been malfunctioning…"* → `autoReward level="LOW"` type `scrap_only`. **Low scrap, nothing else.** |
| 1/3 | *"Human corpses are scattered across the station. You find the source of the signal, a lone survivor…"* → `autoReward level="LOW"` type `scrap_only` **plus** `<crewMember amount="1" class="human"/>`. **A free Human crew member with low scrap.** |
| 1/3 | *"All around you is the stench of death and decay. Suddenly, one of your crew bends over and starts retching violently…"* → `autoReward level="LOW"` type `scrap_only`, then a follow-up screen (below). |

The disease outcome's follow-up:

| # | Choice | Requirement | Outcome |
|---|---|---|---|
| a | Continue... | — | *"Your crewmember insists you leave them behind, not wanting to endanger the rest of the crew."* → `<removeCrew><clone>false</clone></removeCrew>` — **lose a crew member permanently.** |
| b | **(Improved Medbay)** Try to cure the disease. | `req="medbay" lvl="2"` | *"Your advanced medical suite is able to isolate the cause of the problem and administer an antidote. That was a close one."* → **nothing is lost.** |

`<clone>false</clone>` is the important flag: it suppresses the Clone Bay revival. The
Clone Bay text reads *"You stop your crew's clone from forming, knowing that the disease
would follow into his next life"* — Fandom marks this **[no effect]**, i.e. a Clone Bay
does **not** save this crew member ([[source-fandom-plagued-station]],
[[source-text-events-xml]]).

## Blue Options
- **[[item-medbay]] at level 2 or higher** (`req="medbay" lvl="2"`) — the only gate in the
  event, and it appears only on the third boarding outcome. It converts a permanent,
  clone-proof crew loss into no effect at all. Note that a level-1 Medbay does not
  qualify, and a [[item-clone-bay]] is not a substitute — this is one of the events where
  the Clone Bay is explicitly worse than the Medbay.

## Rewards & Risks
- Best case (choice 1): a **Human crew member** plus low scrap.
- Worst case (choice 1): **a dead crew member**, unrecoverable even with a Clone Bay,
  offset by low scrap — unless you are carrying a level-2+ Medbay.
- Choice 2: a random tier of scrap, no risk, no ship, no combat.

## Strategy Notes
- With a level-2 Medbay the boarding branch has no downside at all: two-thirds a free
  crew member or low scrap, one-third low scrap and a cured crew member. Take it.
  *Opinion*, derived from the outcome table.
- Without one, it is a 1/3 chance of losing a crew member for a 1/3 chance of gaining one —
  and the crew you gain is a Human, the cheapest kind. Early with a thin crew, choice 2 is
  the defensible pick.
- Running a Clone Bay does not change the calculus here; the `<clone>false</clone>` flag
  specifically defeats it.

## Related
- [[event-intelligent-ponies]] — the other Slug-nebula donor event, the mirror case where
  the Clone Bay *does* revive the lost crew member
- [[item-medbay]] — the gate
- [[item-clone-bay]] — explicitly defeated here
- [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]
- [[concept-crew-loss-risk]]

## Open Questions
- [ ] The actual distribution across `DONOR_PLAGUE_LIST` — the 1/3 figures assume uniform
      selection across list entries, which the files do not confirm.
- [ ] What scrap `autoReward level="RANDOM"` actually rolls, and over which tiers.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-plagued-station]] (per raw/wiki/plagued-station.md)
