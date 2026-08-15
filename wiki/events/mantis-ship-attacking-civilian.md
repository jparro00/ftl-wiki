---
id: event-mantis-ship-attacking-civilian
type: event
event_name: MANTIS_CIVILIAN
sectors: [[[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [mantis, moral-choice, optional-fight, crew-reward-chance]
---

# Mantis ship attacking civilian — `MANTIS_CIVILIAN`

## Summary
A Mantis warship is running down a civilian. You can intervene or jump on. Intervening is
a fully optional fight against a Mantis ship crewed 75% Mantis / 25% Engi, and winning it
opens a second roll on the shared "save the civilian" reward table — which can pay a crew
member, medium scrap, a weapon, or nothing at all. Walking away costs and gains nothing.

## Trigger & Where It Appears
- Sectors: [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]],
  [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]]
- Drawn from the `NEUTRAL_ENGI` and `NEUTRAL_MANTIS` event lists
  ([[source-events-xml]], per `raw/gamedata/events_mantis.xml`). Mantis sectors allocate
  `NEUTRAL_MANTIS` at `min=6 max=7` beacons ([[source-sector-data-xml]]).
- `unique="false"` — it can repeat within a sector.
- The event opens with `<ship load="MANTIS_CIVILIAN" hostile="false"/>`, so the Mantis
  ship is present but **not** shooting until you choose. Long-range scanners show a ship
  ([[source-fandom-mantis-ship-attacking-civilian]]).

## Text
The intro prose is drawn from the `MANTIS_CIVILIAN` text list and **varies** between five
strings ([[source-events-xml]], [[source-text-events-xml]]):

> A Mantis vessel flashes past your view-screen, weapons and engines at full. A tiny blip
> on the sensor readout marks its quarry.

> You spot a Mantis ship hunting in the distance.

> A Mantis ship engaging a civilian hails you. Sparks fly about his cockpit as he yells,
> "Stay out of this human! Else you are next!"

> Local sensors pick up two ships engaged in a heated battle. It seems the Mantis military
> ship will surely defeat its prey.

> You pick up a distress call from a civilian ship. It's being chased by a Mantis ship!

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Aid the civilian ship. | — | *"You frown, power up the weapons and prepare to engage the Mantis ship. Not today."* → the ship turns hostile. Fight it; on win, `autoReward level="MED"` `standard` **plus** a follow-up choice, *"Attempt to contact the civilian ship"* → rolls `SAVE_CIVILIAN_LIST` (see below). | 100% (deterministic) |
| 2 | Stay out of it. | — | Flavour text only, drawn from the `MANTIS_CIVILIAN_AVOID` list — **varies** between three strings. Nothing happens. | 100% |

### Choice 1 — the fight
`<ship name="MANTIS_CIVILIAN">` uses the `SHIPS_MANTIS` auto-blueprint and is crewed
`mantis` at `prop="0.75"` and `engi` at `prop="0.25"`
([[source-events-xml]], per `raw/gamedata/events_ships.xml`). It has no surrender or
escape branch — both the `destroyed` and `deadCrew` endings give `autoReward level="MED"`
`standard` and then offer the same follow-up choice.

- Destroyed: *"The Mantis ship breaks apart."*
- Crew killed: *"No more life signs detected on the pirate ship. You hasten to contact the
  civilian ship."* (the string says "pirate ship" — an in-file wording slip, quoted as-is)

### Choice 1 follow-up — `SAVE_CIVILIAN_LIST`
"Attempt to contact the civilian ship" loads the shared `SAVE_CIVILIAN_LIST` event list
(defined in `raw/gamedata/events_pirate.xml`, [[source-events-xml]]). Six entries, one
drawn at random; the file states no weights, so the odds are **unknown**:

| Entry | Result |
|---|---|
| 1 | Damaged survivor ship; one crew member offers to join → **+1 crew member** (unspecified species) if you accept, nothing if you decline |
| 2 | Science vessel thanks you → `autoReward level="MED"` `standard` |
| 3 | Crew did not survive; you loot the remains → `autoReward level="LOW"` `standard` |
| 4 | A shipwright offers to install equipment → `autoReward level="LOW"` `weapon` |
| 5 | They patch your hull → `<damage amount="-5"/>`, i.e. **5 hull repaired** |
| 6 | The civilian already fled → nothing |

### Choice 2 — the avoid texts
Drawn from `MANTIS_CIVILIAN_AVOID` ([[source-text-events-xml]]):

> Smoking, the civilian ship limps on. You set your sights on the future.

> The noise of the FTL spinning up almost drowns out the explosions. Almost.

> You let them pass and try not to think about it.

## Blue Options
None. Neither choice carries a `req=` attribute.

## Rewards & Risks
- **Reward path:** MED standard scrap-with-resources for the kill, then one roll on
  `SAVE_CIVILIAN_LIST` — best case a free crew member or a weapon, worst case nothing.
- **Risk:** a full Mantis-ship fight you did not have to take, against a crew that is
  three-quarters Mantis, with **no surrender and no escape branch** in the ship
  definition. If they board you, you are fighting Mantis melee.
- Choice 2 is mechanically free.

## Strategy Notes
- *(Opinion.)* The expected value on choice 1 is decent — MED standard rewards plus a
  second roll — but two of the six `SAVE_CIVILIAN_LIST` outcomes pay nothing or nearly
  nothing, so this is not a guaranteed-profit beacon. Take it when your weapons are ahead
  of the sector curve; skip it when hull is thin, because there is no surrender offer to
  bail you out mid-fight.
- The Engi-sector version is the same event id — the sector does not change the payload.

## Related
- [[event-mantis-fight]] — the unconditional version of the same fight
- [[event-mantis-fight-choice]] — the other "engage or avoid" Mantis beacon
- [[entity-mantis]], [[entity-engi]]
- [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]],
  [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]]

## Open Questions
- [ ] Weights inside `SAVE_CIVILIAN_LIST` — the file lists six entries with no `prop`.
- [ ] Which species the `SAVE_CIVILIAN_LIST` entry-1 crew member is (`<crewMember amount="1"/>`
      with no `class`).
- [ ] Exact scrap values behind `MED`/`LOW` `standard` `autoReward`.
- [ ] Is the "pirate ship" wording in `ship_MANTIS_CIVILIAN_deadCrew_text` a copy-paste
      artefact from the pirate version of this event?

## Sources
- [[source-events-xml]] (per raw/gamedata/events_mantis.xml, raw/gamedata/events_ships.xml,
  raw/gamedata/events_pirate.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-mantis-ship-attacking-civilian]] (per raw/wiki/mantis-ship-attacking-civilian.md)
