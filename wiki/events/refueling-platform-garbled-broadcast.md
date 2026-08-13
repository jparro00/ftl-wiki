---
id: event-refueling-platform-garbled-broadcast
type: event
event_name: LANIUS_FUELING_STATION
sectors: [[[sector-abandoned-sector]]]
beacon_type: any
hostile: false
blue_options: [blast doors 2, sensors 2, sensors 3]
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [lanius, fuel, blue-option, boarding-risk, hull-damage-risk, unique, advanced-edition]
---

# Refueling platform garbled broadcast — `LANIUS_FUELING_STATION`

## Summary
A refuelling platform is broadcasting nonsense. Hail it and it turns out to be a Lanius
ship in disguise; dock with it and you get a three-way roll between a clean refuel and two
different ambushes. **Blast Doors 2** skips the roll entirely for a flat 5 fuel, and
**Sensors 2/3** top up the good result. Deepest choice tree of any event in this batch and
the sector's main fuel source.

## Trigger & Where It Appears
- Sector: [[sector-abandoned-sector]] only.
- List: `NEUTRAL_LANIUS`, allocated `min=5 max=6` beacons per sector
  ([[source-sector-data-xml]]); thirteen members → **1/13** *assuming uniform selection
  across list entries* ([[source-dlcevents-anaerobic]]). The file comments it "From Chris".
- `unique="true"` — at most once per sector.
- No ship is spawned by the event body, so long-range scanners show **no** ship
  ([[source-fandom-refueling-platform-garbled-broadcast]]) — which is exactly the trap.

> **AE-only** — Advanced Edition file and sector.

## Text
> You detect a refueling platform near the beacon, although its broadcast signal is
> garbled, and you can't make out the message.

(`event_LANIUS_FUELING_STATION_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Hail the platform and attempt to communicate. | — | *"…The platform suddenly begins to move, revealing itself to be a Lanius ship!"* → combat with `LANIUS_FUELING_STATION_SHIP`. | 100% |
| 2 | Dock with the platform. | — | *"Your ship enters one of the refueling station berths, grateful for a rest."* → a second menu: **Signal for a refuel** (the three-way roll below) or the **Blast Doors** blue option. | 100% |
| 3 | Ignore the platform. | — | *"You leave the platform alone, and prepare to jump."* → nothing happens. | 100% |

### Signal for a refuel (`LANIUS_FUELING_STATION_LIST`)
Three members, **1/3** each *assuming uniform selection across list entries*
([[source-dlcevents-anaerobic]]):

| Result | Payload |
|---|---|
| Hidden Lanius board you | combat with `LANIUS_FUELING_STATION_SHIP` **+** `<boarders breach="true" min="1" max="1" class="anaerobic"/>` — **1 Lanius boarder and a hull breach** |
| Engine-room explosion, then a cruiser | combat with `LANIUS_FUELING_STATION_SHIP` **+** `<damage amount="3" system="engines"/>` — **3 damage to Engines** |
| Station abandoned; you empty its tanks | **+3-5 fuel**, then optional Sensors blue options below |

On the good result:

| # | Choice | Requirement | Outcome(s) |
|---|--------|-------------|-----------|
| a | Continue… | — | Nothing further. |
| b | **(Improved Sensors)** Run another scan at maximum sensitivity. | `req="sensors" lvl="2"` | **+1-3 fuel**. |
| c | **(Advanced Sensors)** Run another scan at maximum sensitivity. | `req="sensors" lvl="3"` | **+2-3 fuel and +1-3 drone parts**. |

### After winning the fight
`LANIUS_FUELING_STATION_SHIP` (`auto_blueprint="SHIPS_LANIUS"`) has **no surrender and no
escape**. Destroyed **or** dead crew both pay `MED standard` and then offer *"Investigate
the fueling platform"* → `LANIUS_FUELING_STATION_END`: **+3-5 fuel**, guaranteed
([[source-dlcevents-anaerobic]]).

## Blue Options
- **Blast Doors level 2** (`req="doors" lvl="2"`, on the docking menu) — *"Your reinforced
  doors save you from an attempted ambush…"* → a flat **+5 fuel** with no roll and no
  fight. Strictly the best line in the event.
- **Sensors level 2** (`req="sensors" lvl="2"`) — **+1-3 fuel** on top of the clean
  refuel; `max_group="0"`.
- **Sensors level 3** (`req="sensors" lvl="3"`) — **+2-3 fuel and +1-3 drone parts**;
  `max_group="0"`.

Fandom's quantities match the XML `item_modify` ranges exactly
([[source-fandom-refueling-platform-garbled-broadcast]]).

## Rewards & Risks
- Fuel is the point: 5 guaranteed with Blast Doors, 3-5 (plus sensor bonuses) on the good
  docking roll, or 3-5 after winning a fight you started by hailing.
- Risks, all on the docking roll: a hull breach plus a Lanius boarder, or 3 engine damage
  — each **alongside** a no-surrender warship fight.
- Choice 3 is a clean, free exit.

## Strategy Notes
- With Blast Doors 2, dock and use the blue option: guaranteed fuel, zero risk.
- Without it, docking is a 1/3 chance of clean fuel against a 2/3 chance of a fight you
  enter already damaged or already boarded. If you are not short of fuel, choice 3 is the
  disciplined play.
- Hailing (choice 1) is the *cleanest* way to get the fight, since you take it undamaged
  and still collect 3-5 fuel afterwards — better than being ambushed into the same fight.

## Related
- [[event-lanius-fight]] — for comparison, the surrender-capable `LANIUS_SHIP`; this
  event's enemy is not
- [[event-refueling-platform]], [[event-refueling-station]] — the non-Lanius refuelling
  events elsewhere in the game
- [[entity-lanius]], [[sector-abandoned-sector]]

## Open Questions
- [ ] Numeric value of `MED standard` from the fight.
- [ ] Whether the three docking outcomes are genuinely equally weighted.

## Sources
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-refueling-platform-garbled-broadcast]] (per raw/wiki/refueling-platform-garbled-broadcast.md)
