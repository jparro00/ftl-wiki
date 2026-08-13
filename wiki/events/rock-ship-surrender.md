---
id: event-rock-ship-surrender
type: event
event_name: ROCK_SHIP_SURRENDER
sectors: []
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [surrender, aftermath, orphan, rock, shared-sub-event]
---

# Rock ship surrender — `ROCK_SHIP_SURRENDER`

## Summary
The surrender offer made by the standard Rock hull (`ROCK_SHIP`). It is the **stingiest
offer rate in the game** — the `ROCK_SHIP` block declares `chance="0.7"`, which under
[[concept-surrender-offers]] is a 30% surrender chance, the lowest of any ship that offers
at all. Accepting ends the fight for one `RANDOM`-level `stuff` payout.

## Trigger & Where It Appears
- **Not in any sector event list.** Reached only through `events_ships.xml`: the
  `ROCK_SHIP` hull declares
  `<surrender chance="0.7" min="3" max="4" load="ROCK_SHIP_SURRENDER"/>`
  ([[source-events-ships]]).
- Per [[concept-surrender-offers]], `chance` is the probability the ship **keeps
  fighting**, so `chance="0.7"` is a **30% surrender chance** once hull falls into the
  `min=3 max=4` band. Fandom's *Rock fight* page independently states 30%, which is the
  decisive evidence behind that concept page.
- Every hostile `ROCK_SHIP` encounter can reach it. The hull is loaded hostile by, among
  others ([[source-events-rock]], [[source-events-xml]], [[source-events-slug]],
  [[source-events-zoltan]]):
  - [[event-rock-fight]] (`ROCK_SHIP`), which sits in the Rock hostile pool
  - [[event-rock-nursery]] — the `ROCK_NURSERY_LOSE` branch
  - [[event-rock-bride]] → [[event-rock-quest-marriage]]'s refusal branch uses a *separate*
    `ROCK_QUEST_MARRIAGE` hull with no surrender block, so that fight cannot reach here
  - [[event-rock-and-slug-standoff]], [[event-zoltan-ship-follows-mantis-ship]] and other
    cross-sector events that stage a Rock hull
- Typical sectors are therefore [[sector-rock-controlled-sector]] and
  [[sector-rock-homeworlds]], plus wherever a Rock hull is staged. `sectors:` is left empty
  because the event itself has no allocation ([[concept-sector-event-allocation]]).
- No Fandom page joins this event directly; the community wiki folds it into *Rock fight*
  and its variants.

## Text
`<text load="ROCK_SHIP_SURRENDER"/>` — a 12-entry text list built from **three** distinct
strings, each repeated four times, so **1/3 each** assuming uniform selection across list
entries ([[concept-event-list-weighting]], [[source-events-rock]],
[[source-text-events-xml]]):

> The Rock ship hails: "Enough! We were told aliens were a threat to our ways, and you have
> proved as much. Take this and leave us in peace."

> Their systems suffering, the Rock ship attempts to make contact: "Alien vessel. Cease
> your attack. We will pay."

> The Rock ship moves into a defensive position and transmits a white flag signal. They
> seem willing to buy their lives.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Accept their offer. | — | `<ship hostile="false"/>` — the fight ends — plus `<autoReward level="RANDOM">stuff</autoReward>`. | 100% |
| 2 | We will not accept surrender! | — | Empty `<event/>`; the fight continues. | 100% |

## Blue Options
None. Neither choice carries a `req`.

## Rewards & Risks
- **Accepting:** one `RANDOM`-level `stuff` bundle; you forgo the `ROCK_SHIP` hull's
  `destroyed` / `deadCrew` payouts.
- **Refusing:** free.
- **Risk of waiting for it:** Rock hulls are heavily armoured and missile-armed. Pushing a
  fight to the 3–4 hull band hoping for a 30% offer is a poor trade against a ship that
  hits back that hard.

## Strategy Notes
- *Opinion:* do not play for this offer. At 30% it is the least likely surrender in the
  game, and by the time it can fire you are usually one volley from the kill and its
  larger scrap payout.
- Accept it when it does appear and you are damaged — Rock fights are attrition fights and
  a free exit is worth more than a marginal `standard` reward.

## Related
- [[event-rock-fight]] — the main fight that leads here
- [[event-rock-nursery]] — its losing branch stages the same hull
- [[event-pirate-surrender]], [[event-zoltan-surrender]], [[event-lanius-surrender]] — the
  other species-specific surrender events
- [[entity-rock-men]] — the faction
- [[concept-surrender-offers]] — why `chance="0.7"` is a 30% offer
- [[concept-event-list-weighting]] — basis for the 1/3 figures

## Open Questions
- [ ] What `RANDOM` `stuff` actually rolls in resources.
- [ ] Does refusing re-offer later in the same fight?

## Sources
- [[source-events-rock]] (per raw/gamedata/events_rock.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-fandom-rock-fight]] (per raw/wiki/rock-fight.md)
