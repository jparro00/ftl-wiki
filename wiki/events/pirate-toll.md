---
id: event-pirate-toll
type: event
event_name: PIRATE_CHOICE
sectors: [[[sector-civilian-sector]], [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-federation-space]], [[sector-pirate-controlled-sector]]]
beacon_type: hostile
hostile: false
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 9
tags: [pirate, optional-fight, scrap-cost, default-rewards]
---

# Pirate toll — `PIRATE_CHOICE`

## Summary
A pirate ship is sitting at the beacon and wants a toll. Pay 15–25 scrap and nothing
happens; refuse and it becomes [[event-pirate-fight]] with the standard `PIRATE` ship.
The ship is loaded `hostile="false"`, so the decision is genuinely yours — the fight only
starts if you pick it.

## Trigger & Where It Appears
- Sectors: [[sector-civilian-sector]], [[sector-engi-controlled-sector]],
  [[sector-engi-homeworlds]], [[sector-federation-space]],
  [[sector-pirate-controlled-sector]]
- Event lists: `HOSTILE1` and `HOSTILE_CIVILIAN` ([[source-newevents]]), `HOSTILE_ENGI`
  ([[source-events-engi]]), `NEUTRAL_PIRATE` ([[source-events-pirate]]); under Advanced
  Edition also `OVERRIDE_HOSTILE1`, `OVERRIDE_HOSTILE2`, `OVERRIDE_HOSTILE_ENGI`
  ([[source-dlceventsoverwrite]]). Note it sits in both hostile and neutral pools.
  `HOSTILE1` and `HOSTILE_CIVILIAN` are what put it in [[sector-federation-space]], which
  [[source-fandom-pirate-toll]] omits.
- `unique="false"` — explicitly, so it can repeat within a sector
  ([[source-events-pirate]]; [[source-fandom-pirate-toll]] agrees)
- Long-range scanners show a ship ([[source-fandom-pirate-toll]], `LRSmap=ship`)
- Drawn with `<img planet="NONE"/>` — deep space, no planet
  ([[source-events-pirate]])

## Text
> Upon completing your jump, you receive a message from a nearby ship. "Greetings and
> welcome to our beacon! For a small fee, we'll let you continue on your way."

(`event_PIRATE_CHOICE_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Pay their toll. | — | *"You made the right decision, friend."* → `<item type="scrap" min="-25" max="-15"/>`, i.e. **lose 15–25 scrap**. No fight. | 100% |
| 2 | Reject their 'offer'. | — | *"Too bad... You will regret this decision!"* → `<ship hostile="true"/>`, the already-present `PIRATE` ship attacks. | 100% |

The event body loads `<ship load="PIRATE" hostile="false"/>` up front; choice 2 only flips
the hostility flag ([[source-events-pirate]]).

### The fight (choice 2)
Standard `<ship name="PIRATE">` — surrender `chance="0.5"` at 3–4 hull → `PIRATE_SURRENDER`
(accept: ship goes non-hostile, `autoReward level="RANDOM"` `stuff`), escape
`chance="0.5"` at 2–4 hull, `DESTROYED_DEFAULT` → MED `standard`, `DEAD_CREW_DEFAULT` →
the 9-entry table. Full profile on [[event-pirate-fight]] ([[source-events-ships]],
[[source-events-xml]]).

## Blue Options
None. Neither choice carries a `req=` attribute — unusually, there is no Piloting, Engines
or weapons gate on a toll event.

## Rewards & Risks
- **Choice 1:** a flat 15–25 scrap cost, no risk. There is no reward for paying.
- **Choice 2:** the full default-rewards table, at the cost of a fight you could have
  bought your way out of. Note the toll (15–25 scrap) is smaller than a MED `standard`
  reward, so refusing is scrap-positive if you win cleanly.

## Strategy Notes
- *(Opinion.)* Refusing is the default line for a healthy ship: the toll is real scrap and
  the fight pays more than it costs. Pay only when hull, drone parts or a broken weapon
  make the fight genuinely dangerous — the `PIRATE` ship has a 50/50 escape branch, so it
  can also deny you the kill reward after you have already taken damage.
- Because the event appears in `NEUTRAL_PIRATE` as well as the hostile lists, a Pirate
  sector can roll it in a beacon slot you were expecting to be safe.

## Related
- [[event-pirate-fight]] — what choice 2 becomes; full ship profile
- [[event-pirate-briber]] — the mirror image: the pirate pays *you* to stay out of it
- [[event-slaver-hostile]] — the other pirate "pay a price or fight" beacon, priced in crew
- [[entity-pirates]]
- [[sector-pirate-controlled-sector]], [[sector-civilian-sector]],
  [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]],
  [[sector-federation-space]]
- [[event-pirate-surrender]] — the shared `PIRATE_SURRENDER` aftermath this hull loads

## Open Questions
- [ ] Is the scrap cost scaled by sector? The `item_modify` range is fixed at 15–25 in the
      file, with no sector modifier.

## Sources
- [[source-events-pirate]] (per raw/gamedata/events_pirate.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml — `HOSTILE1`, `HOSTILE_CIVILIAN`)
- [[source-events-engi]] (per raw/gamedata/events_engi.xml — `HOSTILE_ENGI`)
- [[source-fandom-pirate-toll]] (per raw/wiki/pirate-toll.md)
