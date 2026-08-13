---
id: event-lanius-ship-in-rich-debris-field
type: event
event_name: LANIUS_HARVESTER
sectors: [[[sector-abandoned-sector]]]
beacon_type: hostile
hostile: false
blue_options: [piloting 2, piloting 3]
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [lanius, optional-fight, blue-option, piloting, unique, advanced-edition]
---

# Lanius ship in rich debris field — `LANIUS_HARVESTER`

## Summary
A Lanius vessel is harvesting a rich debris field and you want a share. Greed without
piloting skill starts a fight; **Piloting level 2 or 3** takes the loot with no fight at
all, scaling from `MED` to `HIGH`. It is the only member of `HOSTILE_LANIUS` that can be
resolved without combat, and the graded blue options make it a direct payoff for having
upgraded the helm.

## Trigger & Where It Appears
- Sector: [[sector-abandoned-sector]] only.
- List: `HOSTILE_LANIUS`, allocated `min=5 max=6` beacons per sector
  ([[source-sector-data-xml]]); six members → **1/6** *assuming uniform selection across
  list entries* ([[source-dlcevents-anaerobic]]). The file comments it "From Chris".
- `unique="true"` — at most once per sector.
- The event body spawns no ship, so long-range scanners show **no** ship despite this
  being on the hostile list ([[source-fandom-lanius-ship-in-rich-debris-field]]).

> **AE-only** — Advanced Edition file and sector.

## Text
> Your scans have picked up a Lanius vessel in this system: it appears to be navigating a
> rich debris field, harvesting the minerals.

(`event_LANIUS_HARVESTER_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Attempt to harvest some for yourself. | — | *"…you come too close to the Lanius ship - and they proceed to try to harvest you!"* → combat with `LANIUS_HARVESTER_SHIP`. | 100% |
| 2 | **(Improved Piloting)** Engage the auto-pilot and safely harvest the debris. | `req="pilot" lvl="2"` | No fight. `autoReward MED standard`. | 100% |
| 3 | **(Advanced Piloting)** Engage the auto-pilot and safely harvest the debris. | `req="pilot" lvl="3"` | No fight. `autoReward HIGH standard`. | 100% |
| 4 | Attack the vessel. | — | *"You go on the offensive and power up your weapons…"* → the same `LANIUS_HARVESTER_SHIP` fight as choice 1. | 100% |
| 5 | Ignore the vessel. | — | *"You charge up your drive and prepare to make the next jump…"* → nothing happens. | 100% |

Choices 2 and 3 carry `max_group="0"` in the XML, the same flag the game uses elsewhere to
keep graded blue options from crowding out the normal choices
([[source-dlcevents-anaerobic]]).

### Winning the fight — then Investigate the debris
`LANIUS_HARVESTER_SHIP` (`auto_blueprint="SHIPS_LANIUS"`) has **no surrender and no
escape**. Destroyed **or** dead crew both pay `MED standard`, then offer *"Investigate the
debris"* → `LANIUS_HARVESTER_SHIP_LIST`, three members, **1/3** each *assuming uniform
selection across list entries*:

| Result | Payload |
|---|---|
| The Lanius already took most of it | `autoReward LOW standard` |
| You scavenge what you can | `autoReward MED standard` |
| You interrupted them early — a good haul | `autoReward HIGH standard` |

## Blue Options
- **Piloting level 2** (`req="pilot" lvl="2"`) — skip the fight for `MED standard`.
- **Piloting level 3** (`req="pilot" lvl="3"`) — skip the fight for `HIGH standard`.
  Both appear together when eligible; level 3 strictly dominates
  ([[source-fandom-lanius-ship-in-rich-debris-field]]).

## Rewards & Risks
- Fighting pays `MED` guaranteed plus a `LOW`/`MED`/`HIGH` roll on top — in expectation
  more than the level-2 blue option, and comparable to level 3, but only if you win a
  no-surrender fight without hull loss.
- The no-fight routes are risk-free.
- Choice 5 is a free exit.

## Strategy Notes
- With Piloting 3, take choice 3: `HIGH standard` for nothing.
- With Piloting 2 only, the choice is real — the fight's expected payout (`MED` plus a
  three-way roll) beats a flat `MED`, at the cost of a warship engagement.
- With no piloting upgrade, this is the sector's only hostile-list beacon you can simply
  decline.

## Related
- [[event-lanius-powered-down-ship]] — the other Piloting-gated Lanius salvage event
- [[event-lanius-fight]], [[event-pirate-fight-lanius]], [[event-rebel-fight-lanius]] —
  the rest of `HOSTILE_LANIUS`
- [[entity-lanius]], [[sector-abandoned-sector]]

## Open Questions
- [ ] Numeric values behind `LOW` / `MED` / `HIGH standard`.
- [ ] Whether the three debris-list entries are genuinely equally weighted.

## Sources
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-lanius-ship-in-rich-debris-field]] (per raw/wiki/lanius-ship-in-rich-debris-field.md)
