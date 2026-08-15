---
id: chain-hidden-federation-base
type: chain
trigger_event: [[[event-asteroid-belt-distress]], [[event-rebel-ship-attacking-federation-loyalists]], [[event-encrypted-federation-signal]], [[event-engi-ship-attacked-by-mantis-ship]]]
steps: [[[event-asteroid-belt-distress]], [[event-rebel-ship-attacking-federation-loyalists]], [[event-encrypted-federation-signal]], [[event-engi-ship-attacked-by-mantis-ship]]]
sectors: [[[sector-civilian-sector]], [[sector-federation-space]], [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-pirate-controlled-sector]], [[sector-rebel-controlled-sector]]]
reward: "1 of 5: high drone reward · free crew · 35 hull repair · a gated scrap/weapon roll · an auto-ship fight"
version: both
first_seen: 2026-08-13
last_updated: 2026-08-13
sources: 5
tags: [quest, one-hop, federation, multi-trigger, shared-destination]
---

# The hidden Federation base

## Summary
The most widely-reachable quest in the game and the shortest: **four different beacons, across
six sector types, all plant the same marker**, and that marker resolves in a single jump to a
five-outcome table. There is no second stage. What makes it a chain rather than an outcome is
[[concept-quest-beacon-placement]] — the payoff happens at a *different beacon*, one or more
jumps later, and can be lost entirely if the run ends first.

It is also the game's best illustration of why a quest marker is not a reward: three of the
five destinations are excellent (a high-tier drone, a free crew member, a 35-point hull
repair), one is a gated consolation prize, and one is **a fight you did not ask for**.

## How It Starts

Four independent triggers, five planting sites. Every one uses
`<quest event="HIDDEN_FEDERATION_BASE_LIST"/>` ([[source-events-xml]],
[[source-events-engi]]):

| Trigger | Where the marker is planted | Sectors |
|---|---|---|
| [[event-asteroid-belt-distress]] (`CIVILIAN_ASTEROIDS_BEACON`) | via `CIVILIAN_ASTEROIDS_BEACON_LIST2`, after rescuing the miner | 8 sector types |
| [[event-rebel-ship-attacking-federation-loyalists]] (`REBEL_VS_FEDERATION`) | via `REBEL_VS_FEDERATION_SAVED_LIST` — **three separate sites**, including a Teleporter branch and an AE-only Healing Burst branch | 5 sector types |
| [[event-encrypted-federation-signal]] (`FEDERATION_PLANET_SIGNAL`) | via `FEDERATION_PLANET_SIGNAL_LIST` | 9 sector types |
| [[event-engi-ship-attacked-by-mantis-ship]] (`ENGI_STATION_DISTRESS`) | via `SAVE_ENGI_STATION` | Engi space only |

The common thread is doing a favour for the Federation or its civilians. There is no crew,
system or resource gate on *receiving* the marker from any of the four.

## Steps

1. **Any of the four trigger beacons above** — help the Federation ship, station, miner or
   signal, and the base coordinates go onto your map.
2. **The base beacon** — resolves `HIDDEN_FEDERATION_BASE_LIST`, a 5-entry list
   ([[source-events-xml]]). Per [[concept-event-list-weighting]] the engine selects uniformly,
   so each is **20%**:

   | # | What you find | Payload |
   |---|---|---|
   | 1 | *"We'll bring you up some supplies."* | `autoReward HIGH drone` |
   | 2 | A well-disguised outpost; someone offers to join | `autoReward LOW standard` **+ 1 crew** |
   | 3 | The hidden space-dock | `autoReward MED standard` **+ 35 hull repaired** (`<damage amount="-35"/>`) |
   | 4 | *"Your search yields no results."* | nothing — **unless gated**, see below |
   | 5 | `FEDERATION_BASE_ASSIST` | **a hostile auto-ship**, `AUTO_FEDERATION_BASE` or `AUTO_FEDERATION_BASE2` |

3. **Entry 4 is the one place equipment pays.** The empty-handed result carries three
   mutually-exclusive blue options (`max_group="0"` on the first two), all of which convert
   "nothing" into a reward ([[source-events-xml]]):
   - **Sensors 2** — `autoReward MED standard`. Marked `<!--DLC!-->`, so **AE only**.
   - **Sensors 3** — `autoReward MED weapon`.
   - **[[item-long-ranged-scanners]]** (`req="ADV_SCANNERS"`) — `autoReward MED weapon`.

## Requirements
- **None to start or to finish.** Every gate in the chain is optional upside.
- Fuel and jumps to reach the marked beacon before the run moves on — the only real cost.

## Reward
Expected value is high and the variance is entirely in which of the five you draw. Two
outcomes (crew, 35 hull) are worth more than most events in the game; one is a fight against
an automated ship with the usual default rewards.

The 35-hull repair on entry 3 is worth noting on its own: it is larger than a Rock Cruiser's
entire hull, so at low health this beacon is effectively a free repair station.

## Failure Modes
- **The marker is planted in sector 7.** Per [[concept-quest-beacon-placement]], a quest that
  cannot be placed in the current sector is pushed to the next one — and sector 8 allows no
  quests at all, so the quest is **cancelled outright**. Accepting any of these four late in
  sector 7 is worth nothing.
- Jumping past the marked beacon, or the Rebel fleet reaching it first.
- Drawing entry 5 at low hull — the one branch that costs rather than pays.

## Strategy Notes
- *Opinion:* take the marker every time. There is no cost to accepting, four of five outcomes
  are neutral-to-excellent, and the one fight is an ordinary auto-ship.
- If you carry Sensors 3 or [[item-long-ranged-scanners]], the worst outcome (entry 4) stops
  being empty, which materially improves the table — one of the few places
  [[item-sensors]] pays a concrete dividend.
- The dev comment on the list — `<!-- JUSTIN - USE THIS ELSEWHERE -->` — suggests the
  destination was written as reusable, which is exactly how it ended up being used.

## Related
- [[concept-quest-beacon-placement]] — why a sector-7 acceptance is thrown away
- [[concept-event-list-weighting]] — why each destination is 20%
- [[chain-escort-civilians]] — the other quest with several triggers feeding one destination
- [[item-long-ranged-scanners]], [[item-sensors]] — the gates on entry 4
- [[entity-federation]], [[entity-rebels]]

## Open Questions
- [ ] Whether all four triggers can fire in one run, and whether the destination is
      `unique` across them — the list itself carries no `unique` attribute, and the four
      trigger events each carry their own.
- [ ] `AUTO_FEDERATION_BASE` vs `AUTO_FEDERATION_BASE2` — what distinguishes the two hulls.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-events-engi]] (per raw/gamedata/events_engi.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
