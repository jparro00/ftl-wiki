---
id: event-refugee-comms-down
type: event
event_name: REFUGEE_GHOST
sectors: [[[sector-civilian-sector]], [[sector-federation-space]], [[sector-pirate-controlled-sector]], [[sector-uncharted-nebula]]]
beacon_type: distress
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [distress, crew-risk, crew-reward, boarding-risk, clone-bay, refugee, advanced-edition]
---

# Refugee comms down — `REFUGEE_GHOST`

## Summary
The grim member of the refugee family. Same drifting ship, same dead beacon, but the comms
are out — so there is no hailing and no trade, only a boarding party. Five outcomes, one
of which gives you a free crew member and two of which are cannibals. Unlike every other
refugee event, this one can cost you a crew member outright.

## Trigger & Where It Appears
- Beacon: **distress signal** (`<distressBeacon/>`, [[source-newevents]]).
- Reached through the `DISTRESS_BEACON` event list, the entry immediately above
  `REFUGEE_DISTRESS`:

  ```xml
  <event load="REFUGEE_GHOST"/><!--DLC CHRIS - down below-->
  <event load="REFUGEE_DISTRESS"/> <!--DLC - down below-->
  ```

  ([[source-newevents]], lines 217–218) — both marked as DLC additions, so the vanilla
  `DISTRESS_BEACON` pool did not contain them.
- `DISTRESS_BEACON` is allocated in `STANDARD_SPACE` ([[sector-federation-space]],
  `min=1 max=2`), `CIVILIAN_SECTOR` (`min=1 max=2`) and `NEBULA_SECTOR`
  ([[sector-uncharted-nebula]], `min=1 max=3`) ([[source-sector-data-xml]]), and is also an
  entry inside `NEUTRAL_CIVILIAN` ([[source-newevents]]) and `NEUTRAL_PIRATE`
  ([[source-events-pirate]]) — the latter is how it reaches
  [[sector-pirate-controlled-sector]].
- Not `unique`.

> ⚠️ **CONTRADICTION:** sector scope.
> - Fandom lists Civilian Sector, Pirate Controlled Sector and Uncharted Nebula
>   ([[source-fandom-refugee-comms-down]]).
> - `sector_data.xml` also allocates `DISTRESS_BEACON` in `STANDARD_SPACE`
>   ([[source-sector-data-xml]]) — [[sector-federation-space]].
>
> Trusting the game files (`high` vs `medium`).

## Text
> You have encountered a refugee ship drifting in space. It looks as if it was fleeing the
> Rebel advance and ran out of fuel. Its distress beacon is active, but you're not sure
> anyone is on board, and its communications seem to be down.

(`event_REFUGEE_GHOST_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Prepare to board and investigate. *(hidden)* | — | Loads `REFUGEE_GHOST_LIST` — five entries, below. | — |
| 2 | Ignore the ship. | — | `<event/>` — nothing happens. | 100% |

Choice 1 is `hidden="true"`, so the result text is not previewed before you commit.

### `REFUGEE_GHOST_LIST` — the boarding pool
Five distinct entries, no duplicates. **Assuming uniform selection across list entries**
(the files state no weights), each is 1/5:

| # | Text | Effect |
|---|------|--------|
| 1 | *"The ship is completely abandoned. There is no trace of the crew or any cargo. Mystified, you leave the ghost ship and continue on."* | Nothing. |
| 2 | *"…It looks like it ran out of fuel... and the crew ran out of food not long after. Despite the grisly scene that remains, you are able to scavenge some supplies from the cargo hold."* | `autoReward level="MED"` **`missiles`** |
| 3 | *"…you find one surviving crewman locked in the freezer, almost perfectly preserved and apparently overlooked by the starving crew."* | `crewMember amount="1"` — a free crew member |
| 4 | *"As you investigate the ship, you are attacked by the now-cannibalistic crew!… one of your crew falls to the crazed attackers, and you are forced to leave them behind…"* | `removeCrew` with `<clone>true</clone>` — **lose a crew member**, but a Clone Bay brings them back: *"Your abandoned crewmember is waiting on the ship when you return…"* |
| 5 | *"As you approach the ship, the other ship's transporters suddenly power up, and your decks swarm with now-cannibalistic refugees!"* | `boarders min="2" max="4" class="human"` — 2–4 human boarders |

([[source-newevents]], [[source-text-events-xml]]) Derived from list contents, not a
stated percentage.

Fandom reads the `MED` `missiles` reward as **2–4 missiles** plus scrap
([[source-fandom-refugee-comms-down]]); the game files only say `MED`, so the exact number
is not confirmed here.

## Blue Options
None.

## Rewards & Risks
- **Reward:** a free crew member (1/5), or a medium missile payout (1/5).
- **Risk:** losing a crew member (1/5, recoverable with a Clone Bay), or 2–4 human
  boarders (1/5). No fight against a ship — the danger is entirely on your decks.
- 1/5 is a clean no-op.

## Strategy Notes
- *(Opinion, from the pool shape.)* With a Clone Bay the downside of outcome 4 evaporates,
  which makes boarding a clearly positive gamble: 2/5 upside, 1/5 neutralised, 1/5 a
  boarding fight you can usually win, 1/5 nothing.
- Without a Clone Bay and on a small crew, outcome 4 is a permanent loss — this is one of
  the few distress beacons where "Ignore the ship" is the disciplined play.
- 2–4 **human** boarders are the mildest boarder class in the game, which softens outcome
  5 considerably compared to a Mantis or Rock boarding event.

## Related
- [[event-refugee-distress]] — the other refugee entry in the `DISTRESS_BEACON` pool
- [[event-refugee]] — the non-distress version, which does have a trade branch
- [[item-clone-bay]] — turns outcome 4 from a loss into a scare
- [[concept-blue-options]]

## Open Questions
- [ ] Whether event-list selection is truly uniform.
- [ ] Exact missile count behind `autoReward level="MED"` `missiles`.
- [ ] What species the free crew member in outcome 3 can be — `crewMember amount="1"` has
      no `class` attribute, so it is presumably random, but no source states the pool.

## Sources
- [[source-newevents]] (per `raw/gamedata/newEvents.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-events-pirate]] (per `raw/gamedata/events_pirate.xml`)
- [[source-events-xml]] (per `raw/gamedata/events.xml`)
- [[source-fandom-refugee-comms-down]] (per `raw/wiki/refugee-comms-down.md`)
