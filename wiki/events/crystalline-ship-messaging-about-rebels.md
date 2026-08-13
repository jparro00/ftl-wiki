---
id: event-crystalline-ship-messaging-about-rebels
type: event
event_name: CRYSTAL_REQUEST
sectors: [[[sector-hidden-crystal-worlds]]]
beacon_type: any
hostile: false
blue_options: [[[item-distraction-buoys]]]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unique, blue-option, scrap-reward, fleet-advance, fleet-delay, boarding-risk]
---

# Crystalline ship messaging about Rebels — `CRYSTAL_REQUEST`

## Summary
The Crystals will pay you **high scrap** for your flight plan so they can hand it to the
Rebels and get the fleet out of their space. Honest dealing costs you a jump of fleet
progress; lying is a coin flip between *delaying* the fleet and a boarded fight; and with
Distraction Buoys you get the good half of that coin flip guaranteed. It is the sector's
best scrap event and its only fleet-delay opportunity.

## Trigger & Where It Appears
- Sector: [[sector-hidden-crystal-worlds]] only
- Pool: one of **10** entries in the `NEUTRAL_CRYSTAL` event list, allocated exactly **12**
  times per sector (`min=12 max=12`) ([[source-events-xml]], [[source-sector-data-xml]])
- `unique="true"` — at most once per run
- Beacon: shows a **ship** on Long-Range Scanners — `<ship
  load="CRYSTAL_SHIP_NO_SURRENDER" hostile="false"/>` is present from the start
  ([[source-events-xml]], [[source-fandom-crystalline-ship-messaging-about-rebels]])

## Text
> The moment you arrive you notice a Crystalline ship in the vicinity keeping its distance.
> They message you, "The 'Rebels' that are trying to hunt YOU down are creating havoc
> everywhere they go."

Then, on Continue:

> "To minimize their impact on our people, we would like you to give them your flight path
> out of our sector. We would like to remain civil and are willing to pay you in 'scrap'
> for the increased danger it poses.

(`event_CRYSTAL_REQUEST_text` / `_c1_text`, per [[source-text-events-xml]]. The unclosed
quotation mark is in the shipped string.)

## Choices & Outcomes
The top level is a single `continue` node; the real decision is the four-way below.

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Give them your flight plans. | — | `autoReward level="HIGH"` **scrap_only** + `modifyPursuit amount="1"` → **high scrap, Rebel pursuit doubled for 1 jump**. | 100% |
| 2 | Accept the scrap but give them false flight plans. | — | Loads `CRYSTAL_REQUEST_LIST` — two entries, below. | — |
| 3 | **(Distraction Buoy)** Accept the scrap but give them falsified flight plans. | `req="FLEET_DISTRACTION"` | `autoReward level="HIGH"` **scrap_only** + `modifyPursuit amount="-1"` → **high scrap and the fleet delayed by 1 jump**. | 100% |
| 4 | Refuse. | — | *"They seem to understand, and break the comm link to set about preparing defenses."* Nothing happens. | 100% |

### Sub-event: `CRYSTAL_REQUEST_LIST` (choice 2)
Two entries ([[source-events-xml]],
[[source-fandom-crystalline-ship-messaging-about-rebels]]):

| Entry | Result |
|---|---|
| 1 | The deception works → `autoReward level="HIGH"` **scrap_only** + `modifyPursuit amount="-1"` — identical to the blue option. |
| 2 | *"They take one look at your fake telemetry and realize what you've done."* → `ship hostile="true"` (the `CRYSTAL_SHIP_NO_SURRENDER` already at the beacon, **default rewards**) **and** `boarders min="1" max="2" class="crystal"` — 1–2 Crystal boarders. |

So lying is a 1-in-2 shot at the best outcome in the event against a boarded no-surrender
fight.

## Blue Options
- **Distraction Buoys** (`req="FLEET_DISTRACTION"`) — marked `<!--DLC-->` in the source, so
  Advanced Edition content ([[source-events-xml]]). It converts the 50/50 gamble of choice
  2 into the guaranteed good half: high scrap **and** a jump of fleet delay, with no fight.

## Rewards & Risks
- **Best:** high scrap (`scrap_only`) plus a **−1** pursuit, i.e. the fleet loses a jump.
  Available guaranteed via the blue option, or at 1-in-2 without it.
- **Worst:** a `CRYSTAL_SHIP_NO_SURRENDER` fight with 1–2 Crystal boarders already aboard.
- **Safe-but-costly:** choice 1 pays the same high scrap but pushes the fleet a jump
  closer.
- **Free:** refusing costs nothing.

## Strategy Notes
- With Distraction Buoys this is unambiguously the best beacon in the sector: maximum
  scrap category, fleet delay, no risk.
- Without them, choice 1 vs choice 2 is a straight read on how much fleet slack you have:
  choice 1 trades a jump for guaranteed scrap; choice 2 risks a boarded fight to *gain* a
  jump. *(Opinion, built on the sourced effects.)*
- Note that both fleet-modifying paths use the same `modifyPursuit` magnitude in opposite
  directions, so the swing between choice 1 and a successful choice 2/3 is two jumps.

## Related
- [[sector-hidden-crystal-worlds]]
- [[item-distraction-buoys]] — unlocks choice 3
- [[event-crystalline-men-buried]] — the sector's other pursuit-modifying event (costs
  jumps)
- [[event-rebel-ship-attacking-crystal-ship]] — also advances the fleet on one branch
- [[event-boarders-crystal]] — the same Crystal boarding hazard standalone
- [[entity-crystal-men]], [[concept-rebel-fleet-advance]]
- [[concept-rebel-fleet-advance]], [[concept-blue-options]]

## Open Questions
- [ ] Exact scrap value of `autoReward HIGH scrap_only`.
- [ ] Whether `modifyPursuit amount="-1"` is exactly the inverse of `amount="1"` in effect
      (Fandom describes them as "doubled for 1 jump" and "delayed for 1 jump" respectively,
      which are not obviously symmetric).

## Sources
- [[source-events-xml]] (per raw/gamedata/events_crystal.xml, raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-crystalline-ship-messaging-about-rebels]] (per raw/wiki/crystalline-ship-messaging-about-rebels.md)
