---
id: event-lanius-powered-down-ship
type: event
event_name: LANIUS_DORMANT_EVENT
sectors: [[[sector-abandoned-sector]]]
beacon_type: any
hostile: false
blue_options: [lanius crew, piloting 2]
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [lanius, optional-fight, blue-option, piloting, unique, advanced-edition]
---

# Lanius powered-down ship — `LANIUS_DORMANT_EVENT`

## Summary
A hibernating Lanius vessel, undamaged and unpowered. Poking it wakes it up; investigating
carefully opens a second menu with two blue options — a Lanius crew member who can loot it
quietly, or Piloting 2 to strip the hull on autopilot. The event is a small decision tree
where almost every unskilled route ends in the same `LANIUS_SHIP` fight.

## Trigger & Where It Appears
- Sector: [[sector-abandoned-sector]] only.
- List: `NEUTRAL_LANIUS`, allocated `min=5 max=6` beacons per sector
  ([[source-sector-data-xml]]); thirteen members → **1/13** *assuming uniform selection
  across list entries* ([[source-dlcevents-anaerobic]]). The file comments it "From Chris".
- `unique="true"` — at most once per sector.
- Spawns `<ship load="LANIUS_SHIP" hostile="false"/>`; long-range scanners show a ship
  ([[source-fandom-lanius-powered-down-ship]]).

> **AE-only** — Advanced Edition file, sector, and (for one blue option) species.

## Text
> You have picked up a Lanius vessel drifting in this sector. There is no damage to the
> hull, and it appears to be powered down.

(`event_LANIUS_DORMANT_EVENT_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Scan the ship for lifeforms. | — | *"…the scan frequencies awaken the Lanius crew from hibernation - and they're hungry for raw materials!"* → combat with `LANIUS_SHIP`. | 100% |
| 2 | Power weapons to attack. | — | Loads `LANIUS_DORMANT_WEAPONS` (two members): (a) *"…the Lanius ship does the same!"* → combat; (b) *"You power up your weapons, but don't get a response"* → a second menu: **Investigate the vessel** (below) or *"Destroy and scrap it"*, which wakes them → combat. | **1/2** each *(assuming uniform selection across list entries)* |
| 3 | Investigate the vessel. | — | Loads the `LANIUS_DORMANT_INVESTIGATE` sub-event below. | 100% |

### Investigate the vessel (`LANIUS_DORMANT_INVESTIGATE`)
> The vessel appears to be dormant. It is likely there are Lanius on board, but they may be
> in hibernation until the ship comes within range of new materials.

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| a | Ignore the vessel. | — | Nothing happens. | 100% |
| b | **(Lanius Crew)** Send over a Lanius crewmember to plunder the ship of resources. | `req="anaerobic"` | *"Your crewmember manages to salvage some resources without waking the hibernating crew."* → `autoReward MED` **`stuff`** — the resources-with-some-scrap payout, not the standard one. | 100% |
| c | Navigate carefully around the ship and strip what materials from the hull you can. | — | Loads `LANIUS_DORMANT_PILOT` (two members): (a) your piloting isn't up to it → combat with `LANIUS_SHIP`; (b) *"You clumsily manage to strip some hull plating…"* → `autoReward LOW scrap_only`. | **1/2** each *(assuming uniform selection across list entries)* |
| d | **(Advanced Piloting)** Engage the autopilot to strip the ship safely. | `req="pilot" lvl="2"` | *"The computer matches the rotation and speed of the target ship… You get an excellent haul!"* → `autoReward MED standard`, no fight. | 100% |

Note the labelling quirk: the choice text calls this "(Advanced Piloting)" but the gate is
`lvl="2"`, which the rest of the file (e.g.
[[event-lanius-ship-in-rich-debris-field]]) calls *Improved* Piloting. Fandom renders it
as "Piloting 2+" ([[source-fandom-lanius-powered-down-ship]]).

## Blue Options
- **Lanius crew member** (`req="anaerobic"`) — the only fight-free way to loot the ship
  without a Piloting upgrade. Pays `MED stuff`: Fandom expands the "stuff" reward type as
  *fuel 2-4, missiles 2-4, drone parts 1* — resources rather than scrap
  ([[source-fandom-lanius-powered-down-ship]]); the XML says only `MED` and `stuff`.
- **Piloting level 2** (`req="pilot" lvl="2"`) — `MED standard`, no fight, and strictly
  better than gambling on choice (c).

## Rewards & Risks
- Every fight branch is against `LANIUS_SHIP`, whose tables (surrender 0.2, escape 0.2,
  and the 1/8 free crew member on dead crew) are on [[event-lanius-fight]].
- Unskilled play is genuinely dangerous here: choice 1 is a guaranteed fight, choice 2 is
  a coin flip, and choice (c) is another coin flip.
- Skilled play is entirely safe: (b) and (d) both end the event with a reward and no
  combat.

## Strategy Notes
- With either blue option, take it; there is no reason to gamble.
- With neither, "Investigate → Ignore" is a free exit, and choice (c) is the only way to
  get paid — at 50/50 odds of a warship fight.
- *Opinion:* if you are hunting the free crew member on the `LANIUS_DEAD_CREW` table,
  choice 1 is the most reliable way in the sector to start a `LANIUS_SHIP` fight on your
  own terms.

## Related
- [[event-lanius-ship-in-rich-debris-field]] — the other Piloting-gated Lanius salvage
- [[event-lanius-fight]] — the enemy definition and its reward tables
- [[event-lanius-ship-absorbing-jump-beacon]] — the other Lanius-crew trade opportunity
- [[entity-lanius]], [[sector-abandoned-sector]]

## Open Questions
- [ ] Numeric values behind `MED stuff` (Fandom's fuel/missile/drone breakdown is not in
      the XML).
- [ ] Why the level-2 gate is labelled "Advanced Piloting" here and "Improved Piloting"
      elsewhere.

## Sources
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-lanius-powered-down-ship]] (per raw/wiki/lanius-powered-down-ship.md)
