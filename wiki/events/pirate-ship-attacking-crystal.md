---
id: event-pirate-ship-attacking-crystal
type: event
event_name: CRYSTAL_PIRATE_CRYSTAL
sectors: [[[sector-hidden-crystal-worlds]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [combat-optional, weapon-reward, pirate]
---

# Pirate ship attacking Crystal — `CRYSTAL_PIRATE_CRYSTAL`

## Summary
A pirate that followed you through the reopened Long-Range Beacon is about to hit a
Crystalline transport. Mechanically identical to
[[event-mantis-ship-attacking-crystal]]: optional fight, standard scrap, then the shared
`CRYSTAL_SAVED` reaction table. Its flavour text is the clearest in-game statement that
the outsiders in this sector are here because *you* opened the door.

## Trigger & Where It Appears
- Sector: [[sector-hidden-crystal-worlds]] only
- Pool: one of **10** entries in the `NEUTRAL_CRYSTAL` event list, allocated exactly **12**
  times per sector (`min=12 max=12`) ([[source-events-xml]], [[source-sector-data-xml]])
- `unique="false"` — it can recur in the same sector
- Beacon: shows **no ship** on Long-Range Scanners
  ([[source-fandom-pirate-ship-attacking-crystal]])

## Text
> A pirate ship jumps in right after you arrive at the beacon. It must have followed once
> the Long-Range Beacon was reactivated. It almost charges a small Crystalline transport
> ship, weapons armed.

(`event_CRYSTAL_PIRATE_CRYSTAL_text`, per [[source-text-events-xml]])

The "Long-Range Beacon was reactivated" is the ancient device at
[[event-ancient-device]] — the wormhole route into this sector.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Attack the pirate. | — | `ship load="PIRATE_CRYSTAL" hostile="true"` → fight a pirate ship. On win: `destroyed` → `autoReward level="MED"` **standard**; `deadCrew` → `autoReward level="HIGH"` **standard**. Both then load `CRYSTAL_SAVED`. | 100% |
| 2 | Ignore them. | — | *"You assume the Crystalline ship can handle itself. You have enough of your own problems."* Nothing happens. | 100% |

`PIRATE_CRYSTAL` (`auto_blueprint="SHIPS_PIRATE"`) has no surrender and no escape branch
([[source-events-xml]], per raw/gamedata/events_ships.xml).

### Sub-event: `CRYSTAL_SAVED` ("Contact the Crystal ship")
The same five-entry list shared with [[event-mantis-ship-attacking-crystal]] and
[[event-rebel-ship-attacking-crystal-ship]] ([[source-events-xml]]):

| Entry | Result |
|---|---|
| 1, 2 | Hostile brush-off — they blame you for the Rebels being here. Nothing. |
| 3, 4 | Thanks → `autoReward level="RANDOM"` **stuff**. |
| 5 | → `weapon name="WEAPONS_CRYSTAL"` — a **Crystal weapon**. |

The Fandom page uses the unexpanded `{{Crystal Ship Saved}}` template, so this breakdown
comes from the game files ([[source-fandom-pirate-ship-attacking-crystal]],
[[source-events-xml]]).

## Blue Options
- None.

## Rewards & Risks
- **Rewards:** medium (hull kill) / high (crew kill) scrap with resources, then a 3-in-5
  follow-up including a 1-in-5 Crystal weapon.
- **Risk:** a pirate warship fight with no surrender or escape. Declining is free.

## Strategy Notes
- Pirate ships are generally the softer of the sector's optional fights compared with the
  Crystal warships in `HOSTILE_CRYSTAL`, so this is a reasonable place to farm the
  `CRYSTAL_SAVED` weapon roll. *(Opinion — no source rates the ships against each other.)*

## Related
- [[sector-hidden-crystal-worlds]]
- [[event-mantis-ship-attacking-crystal]] — same structure
- [[event-rebel-ship-attacking-crystal-ship]] — same structure plus a third option
- [[event-ancient-device]] — the reactivated beacon the text refers to
- [[entity-pirates]], [[entity-crystal-men]]

## Open Questions
- [ ] Contents of the `WEAPONS_CRYSTAL` list.
- [ ] Fandom labels this simply "Pirate ship" with no surrender/escape footnote; the game
      file confirms no surrender block, but the pirate blueprint pool itself is not yet
      ingested.

## Sources
- [[source-events-xml]] (per raw/gamedata/events_crystal.xml, raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-pirate-ship-attacking-crystal]] (per raw/wiki/pirate-ship-attacking-crystal.md)
