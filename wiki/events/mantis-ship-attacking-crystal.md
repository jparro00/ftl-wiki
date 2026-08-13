---
id: event-mantis-ship-attacking-crystal
type: event
event_name: CRYSTAL_MANTIS_CRYSTAL
sectors: [[[sector-hidden-crystal-worlds]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [combat-optional, weapon-reward, mantis]
---

# Mantis ship attacking Crystal — `CRYSTAL_MANTIS_CRYSTAL`

## Summary
A Mantis raider is picking on Crystalline civilians. Intervene and you fight a Mantis ship
for standard scrap, then the rescued Crystal ship reacts — sometimes with a reward,
sometimes with open resentment that you brought the war here in the first place.

## Trigger & Where It Appears
- Sector: [[sector-hidden-crystal-worlds]] only
- Pool: one of **10** entries in the `NEUTRAL_CRYSTAL` event list, allocated exactly **12**
  times per sector (`min=12 max=12`) ([[source-events-xml]], [[source-sector-data-xml]])
- `unique="false"` — it can recur in the same sector
- Beacon: shows **no ship** on Long-Range Scanners
  ([[source-fandom-mantis-ship-attacking-crystal]])

## Text
> You discover a number of civilian ships fleeing the area. Shots are fired and you find
> the assailant; a Mantis ship is attacking one of the smaller ships!

(`event_CRYSTAL_MANTIS_CRYSTAL_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Attack the Mantis. | — | `ship load="MANTIS_CRYSTAL" hostile="true"` → fight a Mantis ship. On win: `destroyed` → `autoReward level="MED"` **standard**; `deadCrew` → `autoReward level="HIGH"` **standard**. Both then load `CRYSTAL_SAVED`. | 100% |
| 2 | Ignore them. | — | *"You try to keep a low profile and quickly prepare to jump."* Nothing happens. | 100% |

`MANTIS_CRYSTAL` has no surrender and no escape branch — it is a fight to the finish
([[source-events-xml]], per raw/gamedata/events_ships.xml).

### Sub-event: `CRYSTAL_SAVED` ("Contact the Crystal ship")
Shared by this event, [[event-pirate-ship-attacking-crystal]] and
[[event-rebel-ship-attacking-crystal-ship]]. Five entries
([[source-events-xml]], [[source-text-events-xml]]):

| Entry | Result |
|---|---|
| 1 | *"It seems you have brought war to our doorstep… I should kill you myself..."* Nothing. |
| 2 | *"Bastards, my home was just overrun by your 'Rebels'. Just leave us in peace!"* Nothing. |
| 3 | *"Thank you for your assistance… Take this as a reward."* → `autoReward level="RANDOM"` **stuff**. |
| 4 | *"It's a good thing you came when you did… Please take this for your help."* → `autoReward level="RANDOM"` **stuff**. |
| 5 | *"We will give you one of our weapons if you intend on assisting our kind in the future."* → `weapon name="WEAPONS_CRYSTAL"` — a **Crystal weapon**. |

2 of 5 give nothing, 2 of 5 give random stuff, 1 of 5 gives a Crystal weapon. The Fandom
page renders this as a `{{Crystal Ship Saved}}` template that is **not expanded** in the
retrieved dump, so the breakdown above comes from the game files only
([[source-fandom-mantis-ship-attacking-crystal]], [[source-events-xml]]).

## Blue Options
- None.

## Rewards & Risks
- **Rewards:** medium (hull kill) or high (crew kill) scrap with resources, then a 3-in-5
  chance of a follow-up — including a 1-in-5 Crystal weapon.
- **Risk:** a Mantis warship fight with no surrender or escape. Mantis ships are the
  boarding-heavy archetype, so expect crew combat.
- Declining is entirely free.

## Strategy Notes
- Killing the crew rather than destroying the hull upgrades MED → HIGH, same as the other
  intervention events in this sector. *(Reward levels sourced; the recommendation is
  opinion.)*
- The 1-in-5 Crystal weapon is the reason to take these fights at all — it is one of the
  few free weapon sources in the sector alongside [[event-crystalline-cache]].
  *(Opinion.)*

## Related
- [[sector-hidden-crystal-worlds]]
- [[event-pirate-ship-attacking-crystal]] — same shape, pirate aggressor
- [[event-rebel-ship-attacking-crystal-ship]] — same shape, Rebel aggressor, plus the
  option to side against the Crystals
- [[event-crystal-ship-attacking-federation-loyalists]] — the mirror case, Crystals as
  aggressor
- [[entity-mantis]], [[entity-crystal-men]]

## Open Questions
- [ ] Contents of the `WEAPONS_CRYSTAL` list (blueprints.xml not yet ingested).
- [ ] Whether the `CRYSTAL_SAVED` entries are drawn with equal weight (the list shows each
      once).

## Sources
- [[source-events-xml]] (per raw/gamedata/events_crystal.xml, raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-mantis-ship-attacking-crystal]] (per raw/wiki/mantis-ship-attacking-crystal.md)
