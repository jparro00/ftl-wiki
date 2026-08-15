---
id: event-the-mercenary
type: event
event_name: MERCENARY
sectors: [[[sector-civilian-sector]], [[sector-federation-space]], [[sector-pirate-controlled-sector]], [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]], [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [scrap-cost, fleet-delay, map-reveal, filler, pirate-fight]
---

# The mercenary — `MERCENARY`

## Summary
A pirate-marked ship sells you one of two services for scrap: **two turns of Rebel fleet
delay**, or a **full sector map reveal**. It is one of very few events that lets you buy
fleet delay outright, which makes it disproportionately valuable when the fleet is
breathing down your neck. You can also just fight it — it is an ordinary `PIRATE` ship
with default rewards.

## Trigger & Where It Appears
- Event lists: `NEUTRAL`, `NEUTRAL_CIVILIAN`, `NEUTRAL_PIRATE`, `NEUTRAL_ROCK`, and
  `OVERRIDE_NEUTRAL` under AE ([[source-newevents]], [[source-dlceventsoverwrite]])
- Sectors: [[sector-civilian-sector]], [[sector-federation-space]],
  [[sector-pirate-controlled-sector]], [[sector-rock-controlled-sector]],
  [[sector-rock-homeworlds]], [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]
- `NEUTRAL` / `OVERRIDE_NEUTRAL` are the **hardcoded fill lists** — the game's own comment
  reads *"This event list is hardcoded to fill out a sector if it ran out of all other
  calls for that sector"* ([[source-newevents]]). That is why the event turns up as
  filler rather than at a guaranteed count; [[source-fandom-the-mercenary]] tags it
  `alsooccur=filler`.
- Not `unique` — it can repeat within a sector ([[source-events-xml]]).
- Beacon: a ship is present and **non-hostile** on arrival,
  `<ship load="PIRATE" hostile="false"/>`; [[source-fandom-the-mercenary]] marks
  `LRSmap=ship`.

## Text
The intro **varies**: `<text load="MERCENARY"/>` draws from a 6-entry `textList`
([[source-events-xml]], [[source-text-events-xml]]). One variant is planet-gated
(`text_MERCENARY_3`, `planet="PLANET_POPULATED"`). Example:

> A mercenary hails you: "Greetings, friend! We've heard tell of your quest and are here
> to offer our valuable services."

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Hire the mercenary to delay the Rebels. | — | *"The mercenary ship masks its jump signature to mimic your own…"* → **−10 to −25 scrap**, `<modifyPursuit amount="-2"/>` — the Rebel fleet is pushed back 2 turns. | 100% |
| 2 | Hire the mercenary to scout the sector. | — | *"Your map has been updated."* → **−10 to −20 scrap**, `<reveal_map/>` — the whole sector map is revealed. | 100% |
| 3 | Fight the ship. | — | *"Mercenaries are worse than Rebels. The only honorable course is to engage the mercenary in battle."* → `<ship hostile="true"/>` on the already-loaded `PIRATE` ship. Default rewards. | 100% |
| 4 | You have no need of his services. | — | Nothing happens. | 100% |

Scrap costs are `<item_modify>` ranges, so the exact price is rolled: 10–25 for the delay,
10–20 for the map ([[source-events-xml]]; [[source-fandom-the-mercenary]] gives the same
ranges).

### If you fight (choice 3)
The `PIRATE` ship definition ([[source-events-ships]]):

- `<surrender chance="0.5" min="3" max="4" load="PIRATE_SURRENDER"/>` — a **50%** surrender
  offer, because `chance` is the probability the ship *keeps fighting*
  ([[concept-surrender-offers]]). Accepting gives `autoReward level="RANDOM"` `stuff`.
- `<escape chance="0.5" min="2" max="4" load="PIRATE_ESCAPE"/>` — a **50%** escape attempt.
- `destroyed` / `deadCrew` load `DESTROYED_DEFAULT` / `DEAD_CREW_DEFAULT` — this is the
  plain [[event-pirate-fight]] reward profile.

## Blue Options
None. No choice in this event carries a `req` ([[source-events-xml]]).

## Rewards & Risks
- **Buying**: you pay scrap and get a non-material benefit. No risk, no combat.
- Choice 1 is one of the few purchasable `modifyPursuit` effects in the game.
  [[source-fandom-the-mercenary]] notes it has **no effect in [[sector-the-last-stand]]**,
  where the fleet mechanic is different — the game files do not state this, so it is a
  Fandom-only claim.
- Choice 3 risks an ordinary pirate fight for ordinary pirate rewards.

## Strategy Notes
- Fleet delay is worth far more than 10–25 scrap on any run where you are being chased
  through a sector you still want to farm. Map reveal is worth less, since it only saves
  scouting jumps. *(Opinion; the sources give values, not a ranking.)*
- Fighting is strictly a scrap-for-risk trade with no bonus over any other pirate beacon —
  there is no extra reward for killing the mercenary specifically ([[source-events-xml]]).

## Related
- [[event-pirate-fight]] — the same `PIRATE` ship and reward profile
- [[event-pirate-briber]] — the other "pay a pirate scrap" beacon in the same lists
- [[concept-surrender-offers]] — how the 50% figure is derived
- [[entity-pirates]]
- [[event-pirate-surrender]] — the shared `PIRATE_SURRENDER` aftermath this hull loads
- [[event-pirate-escape]] — the shared `PIRATE_ESCAPE` aftermath this hull loads

## Open Questions
- [ ] Is [[source-fandom-the-mercenary]]'s "no effect in The Last Stand" claim verifiable
      from the game files? `modifyPursuit` carries no sector condition in the XML.
- [ ] Fandom's sector list omits [[sector-federation-space]] even though `NEUTRAL` /
      `OVERRIDE_NEUTRAL` reaches it as filler. Probably a listing convention, not a
      disagreement.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-fandom-the-mercenary]] (per raw/wiki/the-mercenary.md)
