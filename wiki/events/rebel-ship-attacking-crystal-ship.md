---
id: event-rebel-ship-attacking-crystal-ship
type: event
event_name: CRYSTAL_REBEL_CRYSTAL
sectors: [[[sector-hidden-crystal-worlds]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [combat-optional, weapon-reward, fleet-advance, rebel]
---

# Rebel ship attacking Crystal ship — `CRYSTAL_REBEL_CRYSTAL`

## Summary
A three-way: a Rebel and a Crystalline ship are already shooting at each other. You can
help the Crystals (fight the Rebel, then roll the `CRYSTAL_SAVED` reaction table), turn on
the Crystals instead (a no-surrender fight **and** the Rebel escapes to report you,
advancing the fleet), or slip past for free.

## Trigger & Where It Appears
- Sector: [[sector-hidden-crystal-worlds]] only
- Pool: one of **10** entries in the `NEUTRAL_CRYSTAL` event list, allocated exactly **12**
  times per sector (`min=12 max=12`) ([[source-events-xml]], [[source-sector-data-xml]])
- `unique="false"` — it can recur in the same sector
- Beacon: shows **no ship** on Long-Range Scanners
  ([[source-fandom-rebel-ship-attacking-crystal-ship]])

## Text
> Crystal shards fly past the screen as soon as you arrive. Checking the scanners, it looks
> like a crystalline ship is engaged with a Rebel!

(`event_CRYSTAL_REBEL_CRYSTAL_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Attack the Rebel. | — | `ship load="REBEL_CRYSTAL_REBEL_CRYSTAL" hostile="true"` → fight a Rebel ship. `destroyed` → `autoReward level="MED"` **standard**; `deadCrew` → `autoReward level="HIGH"` **standard**. Both then load `CRYSTAL_SAVED`. | 100% |
| 2 | Attack the Crystalline ship. | — | The Rebel escapes to report you → `modifyPursuit amount="1"` (**Rebel fleet pursuit doubled for 1 jump**) **and** `ship load="CRYSTAL_SHIP_NO_SURRENDER" hostile="true"` — a fight with no surrender and no escape, **default rewards**. | 100% |
| 3 | Ignore them. | — | *"With the two ships engaged in combat, you sneak by unnoticed."* Nothing happens. | 100% |

Fandom notes the Rebel ship here uses **the same text for both the destroyed and the
crew-kill outcome**, which the game file confirms — both branches point at
`ship_REBEL_CRYSTAL_REBEL_CRYSTAL_destroyed_text`, only the reward level differs
([[source-fandom-rebel-ship-attacking-crystal-ship]], [[source-events-xml]]).

### Sub-event: `CRYSTAL_SAVED` ("Contact the Crystal ship")
The shared five-entry reaction list, also used by
[[event-mantis-ship-attacking-crystal]] and [[event-pirate-ship-attacking-crystal]]
([[source-events-xml]]):

| Entry | Result |
|---|---|
| 1, 2 | They blame you for bringing the Rebels here. Nothing. |
| 3, 4 | Thanks → `autoReward level="RANDOM"` **stuff**. |
| 5 | → `weapon name="WEAPONS_CRYSTAL"` — a **Crystal weapon**. |

## Blue Options
- None.

## Rewards & Risks
- **Choice 1:** medium/high scrap with resources plus a 3-in-5 follow-up (1-in-5 Crystal
  weapon). Strictly the better fight.
- **Choice 2:** default rewards, **plus** a jump of doubled Rebel pursuit, **plus** the
  enemy cannot surrender or flee. Pure downside relative to choice 1.
- **Choice 3:** free.

## Strategy Notes
- There is no sourced reason to take choice 2 — it costs fleet position and gives a
  strictly worse fight than choice 1, which targets a Rebel you were going to have to
  fight sooner or later. *(Opinion, built on the reward levels and `modifyPursuit` above.)*
- Compare [[event-crystal-fight-choice]] (`CRYSTAL_REBEL_CRYSTAL2`), which looks like the
  same setup but gives you no way to actually help the Crystals.

## Related
- [[sector-hidden-crystal-worlds]]
- [[event-crystal-fight-choice]] — the near-identical premise with a nastier resolution
- [[event-mantis-ship-attacking-crystal]], [[event-pirate-ship-attacking-crystal]] — same
  `CRYSTAL_SAVED` follow-up
- [[event-crystalline-ship-messaging-about-rebels]], [[event-crystalline-men-buried]] — the
  sector's other pursuit-modifying events
- [[concept-rebel-fleet-advance]], [[entity-crystal-men]]
- [[concept-rebel-fleet-advance]]

## Open Questions
- [ ] Whether `REBEL_CRYSTAL_REBEL_CRYSTAL` has a surrender or escape branch — the game
      file shows only `destroyed`/`deadCrew` nodes, and Fandom marks its footnote
      `verify`.
- [ ] Contents of the `WEAPONS_CRYSTAL` list.

## Sources
- [[source-events-xml]] (per raw/gamedata/events_crystal.xml, raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-rebel-ship-attacking-crystal-ship]] (per raw/wiki/rebel-ship-attacking-crystal-ship.md)
