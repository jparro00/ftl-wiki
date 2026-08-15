---
id: event-pirate-ship-attacking-civilian-distress
type: event
event_name: PIRATE_CIVILIAN_BEACON
sectors: [[[sector-civilian-sector]], [[sector-federation-space]], [[sector-pirate-controlled-sector]], [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]], [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]], [[sector-uncharted-nebula]]]
beacon_type: distress
hostile: true
blue_options: [[[item-weapons]]]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 7
tags: [distress, pirate-fight, blue-option, crew-reward, weapon-reward, bugged]
---

# Pirate ship attacking civilian distress — `PIRATE_CIVILIAN_BEACON`

## Summary
A distress-list encounter where a pirate is chasing a civilian. Killing the pirate opens the
shared `SAVE_CIVILIAN_LIST` rescue table — the same six-outcome pool used by every
"save the civilian" event in the game, which can hand you a crew member, a weapon, hull
repairs or nothing. With **Weapons level 6** you get a blue option that can scare the pirate
off outright and skip the fight entirely.

## Trigger & Where It Appears
- Event lists: `DISTRESS_BEACON`, `DISTRESS_BEACON_PIRATE`, `DISTRESS_BEACON_ROCK`,
  `DISTRESS_BEACON_SLUG` ([[source-newevents]], [[source-events-pirate]])
- Sector allocations for those lists ([[source-sector-data-xml]]):
  [[sector-federation-space]] `DISTRESS_BEACON 1–2`, [[sector-civilian-sector]] `1–2`,
  [[sector-uncharted-nebula]] (`NEBULA_SECTOR`) `1–3`,
  [[sector-pirate-controlled-sector]] `DISTRESS_BEACON_PIRATE 1–2`,
  [[sector-rock-controlled-sector]] / [[sector-rock-homeworlds]] `DISTRESS_BEACON_ROCK 1–2`,
  [[sector-slug-controlled-nebula]] / [[sector-slug-home-nebula]] `DISTRESS_BEACON_SLUG 3–4`
- Not `unique` — it can repeat ([[source-events-xml]])

**It is not actually flagged as a distress beacon.** The event definition contains **no
`<distressBeacon/>` element** ([[source-events-xml]]), even though it sits in the distress
lists and its own text calls out a distress beacon. [[source-fandom-pirate-ship-attacking-civilian-distress]]
records this as a bug: *"This event is meant to occur at a distress beacon but won't because
the `<distressBeacon/>` tag is missing in its definition."* Both sources agree; the beacon
icon on your map will not show the distress marker. Fandom likewise marks it `LRSmap=noship`.

> ⚠️ **CONTRADICTION:** sector coverage.
> - Game files: `DISTRESS_BEACON` is allocated `min=1 max=2` in `STANDARD_SPACE`
>   ([[source-sector-data-xml]]), so [[sector-federation-space]] is in scope.
> - Fandom: lists seven sectors and omits Federation space
>   ([[source-fandom-pirate-ship-attacking-civilian-distress]]).
>
> Trusting the game files (`high` vs `medium`). Same omission pattern as other
> `DISTRESS_BEACON` events; reads as a wiki template convention, not a version difference.

## Text
> The distress beacon is coming from a civilian ship. It appears it is being chased by a
> pirate.

(`event_PIRATE_CIVILIAN_BEACON_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Aid the civilian ship. | — | *"You power up your weapons and engage the pirate ship."* → `<ship load="PIRATE_CIVILIAN" hostile="true"/>`. Win → rescue table, below. | 100% |
| 2 | Stay out of it. | — | *"The fight brings them out of your immediate scanning range; however, after a time the distress calls stop."* → nothing. | 100% |
| 3 | **(Improved Weapons)** Fire a warning shot from your strongest weapon. | `req="weapons" lvl="6"` | Loads `eventList PIRATE_CIVILIAN_BEACON_BEAM` — 2 entries, **1/2** each. | see below |

### Choice 3 — `eventList PIRATE_CIVILIAN_BEACON_BEAM` (2 entries)
Assuming uniform selection across `eventList` entries ([[concept-event-list-weighting]]):

| Entry | Outcome | Odds |
|---|---|---|
| 1 | *"Detecting the greater threat (and potential reward), they turn and engage your ship."* → the same `PIRATE_CIVILIAN` fight as choice 1. | 1/2 |
| 2 | *"It seems the pirate wasn't looking for a fight with someone who could fight back. They leave and you move to contact the civilian ship."* → straight to the rescue table, **no fight, no combat reward**. | 1/2 |

### Fighting `PIRATE_CIVILIAN`
([[source-events-ships]]) — **no `<surrender>` and no `<escape>`**: it will not give up and
cannot flee. Both win conditions then offer a hidden "Contact the civilian ship" choice
into `SAVE_CIVILIAN_LIST`:

| Result | Text | Reward |
|---|---|---|
| `destroyed` | *"The pirate ship breaks apart. You hasten to contact the civilian ship."* | `autoReward level="MED"` `standard` |
| `deadCrew` | *"No more life signs detected on the pirate ship. You hasten to contact the civilian ship."* | `autoReward level="HIGH"` `standard` |

Boarding to kill the crew pays a full tier more than blowing the ship up.

### The rescue table — `eventList SAVE_CIVILIAN_LIST` (6 entries)
Defined in `events_pirate.xml` and shared by many events ([[source-events-pirate]]).
Assuming uniform selection, **1/6** each:

| Entry | Text | Effect |
|---|---|---|
| 1 | *"…One offers to join your crew."* | **Welcome aboard!** → `<crewMember amount="1"/>`; **Decline their request** → nothing |
| 2 | *"Apparently the ship that was being assaulted was a science vessel…"* | `autoReward level="MED"` `standard` |
| 3 | *"It seems the crew did not survive the assault. You take what you can…"* | `autoReward level="LOW"` `standard` |
| 4 | *"I'm a shipwright and I'd like to help you like you helped me."* | → `autoReward level="LOW"` **`weapon`** |
| 5 | *"I think my crew can patch up some of your hull damage as thanks."* | `<damage amount="-5"/>` — **5 hull repaired** |
| 6 | *"The civilian ship wisely made a fast retreat while you distracted the hostile ship."* | nothing |

## Blue Options
- **[[item-weapons]] level 6** (`req="weapons" lvl="6"`) — a **1/2 chance to skip the fight
  entirely** and go straight to the rescue table. The gate is the *system level*, not a
  particular weapon. [[source-fandom-pirate-ship-attacking-civilian-distress]] adds a detail
  the XML does not carry: on the scare-off branch the reward preview is shown before you
  commit, which does not happen on the other routes into the rescue table.

## Rewards & Risks
- Best case: `HIGH standard` from a boarding kill, then a crew member or a weapon from the
  rescue table.
- The blue option's good half trades the combat reward for zero risk — you get the rescue
  table but not the `MED`/`HIGH standard`.
- Risk: a pirate ship that cannot be made to surrender or run. Choice 2 is a clean opt-out
  with no penalty.

## Strategy Notes
- The `deadCrew` vs `destroyed` gap (`HIGH` vs `MED`) makes this a good beacon for a
  boarding ship. *(Read off the ship definition; no source states the advice.)*
- Fandom notes this event is very similar to [[event-pirate-ship-attacking-civilian]], with
  the Weapons-6 blue option being the distinguishing feature.

## Related
- [[event-pirate-ship-attacking-civilian]] — the near-identical `NEUTRAL`-list version, no blue option
- [[event-pirate-ship-attacking-civilian-lanius]] — the Lanius-sector variant
- [[event-pirate-surrender-civilan]] — an unreferenced surrender event written for this scenario
- [[item-weapons]], [[entity-pirates]]

## Open Questions
- [ ] Confirm `eventList` selection is uniform — the 1/2 and 1/6 splits depend on it.
- [ ] Is the missing `<distressBeacon/>` tag also absent in vanilla, or an AE regression?
      Only the AE build was extracted here.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-events-pirate]] (per raw/gamedata/events_pirate.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-pirate-ship-attacking-civilian-distress]] (per raw/wiki/pirate-ship-attacking-civilian-distress.md)
