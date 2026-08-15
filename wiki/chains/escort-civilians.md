---
id: chain-escort-civilians
type: chain
trigger_event: [[[event-escort-civilians]], [[event-escort-civilians-ftl-haywire]]]
steps: [[[event-escort-civilians]], [[event-escort-civilians-ftl-haywire]]]
sectors: [[[sector-civilian-sector]], [[sector-federation-space]], [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]]]
reward: "1 of 4: high scrap · a store plus 5 hull · +1 reactor bar (AE) · or a Rebel ambush"
version: both
first_seen: 2026-08-13
last_updated: 2026-08-13
sources: 4
tags: [quest, one-hop, escort, two-triggers, shared-destination, blue-option]
---

# Escorting civilians

## Summary
Two different beacons ask you to escort a civilian ship, and both resolve to the **same
destination list**, `QUEST_ESCORT_ARRIVE`. Like [[chain-hidden-federation-base]] it is a
one-hop quest whose interest is entirely in the payoff table — except here one of the four
outcomes is **an ambush**, and the down-payment you are given up front is the game quietly
telling you the odds are not all good.

The second trigger carries the only way to skip the escort entirely: **Advanced FTL
Navigation** solves the civilians' problem on the spot for a `HIGH standard` reward and no
quest at all.

## How It Starts

Two triggers, both planting `<quest event="QUEST_ESCORT_ARRIVE"/>` ([[source-events-xml]]):

| Trigger | Framing | Down-payment |
|---|---|---|
| [[event-escort-civilians]] (`QUEST_ESCORT`, `unique="false"`) | A lightly-armed civilian ship asks for an escort | `autoReward LOW fuel_only` |
| [[event-escort-civilians-ftl-haywire]] (`ESCORT_BEACON`, `unique="true"`) | A **distress beacon** — their FTL navigation has failed and they need leading to a depot | `autoReward LOW scrap_only` |

Both park a non-hostile `CIVILIAN_SHIP` at the beacon while you decide. Declining costs
nothing on either.

**`QUEST_ESCORT` is `unique="false"`** — it is one of the few quest triggers that can come up
more than once, so the destination table can be rolled repeatedly in a single run.

## Steps

1. **Accept at either beacon** — take the down-payment, get the marker.
2. **The marked beacon** resolves `QUEST_ESCORT_ARRIVE`, 4 entries. Per
   [[concept-event-list-weighting]] each is **25%** — except the fourth is `<!--DLC!-->`, so
   in vanilla the table is 3 entries at 33%:

   | # | Outcome | Payload | Version |
   |---|---|---|---|
   | 1 | *"You are ambushed by a Rebel ship. You walked right into their trap!"* | forced fight, `REBEL` | both |
   | 2 | They jump in behind you and pay up | `autoReward HIGH standard` | both |
   | 3 | *"Let my friends patch up some of your hull and show you their wares"* | **5 hull repaired** + **a store opens** | both |
   | 4 | *"We work at a nearby fusion power plant"* | **+1 reactor bar** (`<upgrade amount="1" system="reactor"/>`) | **AE only** |

## The blue option that skips the quest

[[event-escort-civilians-ftl-haywire]] alone carries
`<choice req="FTL_JUMPER">` — [[item-ftl-jumper]], Advanced FTL Navigation. Uploading a route
to their ship pays `autoReward HIGH standard` **immediately**, plants no marker, and costs no
jumps. It converts a two-beacon quest with a 25% ambush into a guaranteed one-beacon reward.

## Requirements
- None to start or finish.
- [[item-ftl-jumper]] for the skip, on the distress-beacon trigger only.
- Fuel for the extra jump.

## Reward
Genuinely good three times in four. Entry 3 is the standout — **a store where there was no
store**, which in a sector that rolled badly can matter more than the scrap. Entry 4 is a
permanent reactor bar, one of the few free power upgrades in the game.

## Failure Modes
- **The 25% Rebel ambush**, which arrives with no warning and no avoid option.
- The standard quest-marker losses — see [[concept-quest-beacon-placement]].
- Nothing punishes abandoning the escort; you simply keep the down-payment.

## Strategy Notes
- *Opinion:* accept freely. The down-payment covers the fuel, and a 75% shot at high scrap,
  a store, or a reactor bar beats an ordinary beacon comfortably.
- With [[item-ftl-jumper]] aboard, always take the blue option on the distress version — it
  is strictly better than the quest.
- Because `QUEST_ESCORT` is not unique, a civilian-heavy sector can hand you this table
  several times.

## Related
- [[chain-hidden-federation-base]] — the other multi-trigger, one-hop quest
- [[item-ftl-jumper]] — the skip
- [[concept-quest-beacon-placement]], [[concept-event-list-weighting]], [[concept-stores]]
- [[entity-rebels]]

## Open Questions
- [ ] Whether the vanilla table really is 3 entries, or whether the DLC entry replaced
      something — the file shows an addition, not a substitution.
- [ ] Whether the escorted ship is modelled at all between beacons, or purely narrative.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
