---
id: event-lanius-ship-attacking-civilian
type: event
event_name: LANIUS_CIVILIAN
sectors: [[[sector-abandoned-sector]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [lanius, civilian-rescue, optional-fight, crew-reward-chance, unique, advanced-edition]
---

# Lanius ship attacking civilian — `LANIUS_CIVILIAN`

## Summary
The optional-fight version of the Lanius-versus-civilians encounter: a Lanius ship is
tearing into a civilian vessel and you may intervene or leave. Winning runs the shared
"save the civilian" reward list. Unlike its distress-beacon twin
([[event-lanius-ship-attacking-civilian-distress]]) there is **no** Lanius-crew blue
option here.

## Trigger & Where It Appears
- Sector: [[sector-abandoned-sector]] only.
- List: `NEUTRAL_LANIUS`, allocated `min=5 max=6` beacons per sector — the sector's
  joint-largest allocation ([[source-sector-data-xml]]). That list has thirteen members,
  none duplicated → **1/13** *assuming uniform selection across list entries*
  ([[source-dlcevents-anaerobic]]).
- `unique="true"` — at most once per sector.
- The enemy spawns as `<ship load="LANIUS_CIVILIAN" hostile="false"/>`: present but not
  shooting until you choose to fight.
- Long-range scanners show a ship ([[source-fandom-lanius-ship-attacking-civilian]]).

> **AE-only** — Advanced Edition file and sector.
>
> Naming trap: `LANIUS_CIVILIAN` is both this **event** id and the id of the **enemy ship
> definition** it uses. [[event-lanius-ship-attacking-civilian-distress]] loads that same
> ship without being this event.

## Text
`[varies: textList LANIUS_CIVILIAN_TEXT]` — three strings, `text_LANIUS_CIVILIAN_TEXT_1`
through `_3`, none duplicated → **1/3** each *assuming uniform selection across list
entries* ([[source-dlcevents-anaerobic]], [[source-text-events-xml]]). All three are
transcribed on [[source-fandom-lanius-ship-attacking-civilian]]. For example:

> You immediately receive a message upon arrival, "Help! These metal bastards have gone
> crazy!" The communication originates from the hull of a partially dismantled ship which
> lies among a number of other destroyed ships. The violent Lanius ship responsible for
> this carnage is advancing on the survivors.

> You scan the area after arriving at this system. A Lanius ship is in fast pursuit of an
> unarmed civilian ship. It's hard to say if it's truly a threat since its weapons are not
> charging.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Attack the Lanius ship. | — | *"You charge your weapons, which quickly gets the Lanius ship's attention."* → combat with `LANIUS_CIVILIAN`. Destroyed → `MED standard`; dead crew → `HIGH standard`; then **Contact the civilian ship** (`SAVE_CIVILIAN_LIST`). | 100% |
| 2 | Avoid the conflict. | — | *"Unfortunately it is not your mission to save every person affected by this war or the Lanius invasion."* → nothing happens. | 100% |

### Contact the civilian ship (`SAVE_CIVILIAN_LIST`)
Six members, **1/6** each *assuming uniform selection across list entries*
([[source-events-pirate]]): a survivor who can **join your crew**; `MED standard`;
`LOW standard`; `LOW weapon`; **5 hull repaired** (`damage amount="-5"`); or nothing.
Documented in full on [[event-lanius-ship-attacking-civilian-distress]].

## Blue Options
None — which is itself notable, because the near-identical distress version has a Lanius
crew option and this one does not ([[source-dlcevents-anaerobic]]).

## Rewards & Risks
- `LANIUS_CIVILIAN` as an enemy has **no surrender and no escape** branches — once you
  commit, it is a fight to the finish.
- Dead-crew wins pay `HIGH` where hull kills pay `MED`.
- Risk: entirely optional. Choice 2 is a clean exit with no penalty.

## Strategy Notes
- Straight risk/reward: a no-surrender warship fight in exchange for one roll on the
  rescue list. Early in a run, with a weak ship, choice 2 costs you nothing.
- The Lanius crew you might want for the blue options elsewhere in this sector is not
  usable here.

## Related
- [[event-lanius-ship-attacking-civilian-distress]] — the distress-beacon variant, same
  enemy ship, plus a Lanius blue option
- [[event-pirate-ship-attacking-civilian-lanius]] — same structure with a pirate attacker
- [[event-lanius-fight]] — the `LANIUS_SHIP` reward tables, for comparison
- [[entity-lanius]], [[sector-abandoned-sector]]

## Open Questions
- [ ] Numeric values behind `LOW` / `MED` / `HIGH`.
- [ ] Why the distress variant has a Lanius blue option and this one does not — design
      choice or oversight.

## Sources
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-pirate]] (per raw/gamedata/events_pirate.xml — `SAVE_CIVILIAN_LIST`)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-lanius-ship-attacking-civilian]] (per raw/wiki/lanius-ship-attacking-civilian.md)
