---
id: event-remote-settlement
type: event
event_name: PIRATE_STATION_CROPS
sectors: [[[sector-civilian-sector]], [[sector-federation-space]]]
beacon_type: any
hostile: false
blue_options: [[[item-fire-beam]], [[item-fire-bomb]]]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [unique, blue-option, drone-schematic, pirate-fight, moral-choice, missile-cost]
---

# Remote settlement — `PIRATE_STATION_CROPS`

## Summary
A pirate is shaking down a farming settlement. You can fight the pirate for a modest,
multi-stage reward — or, with a **Fire Beam** or **Fire Bomb**, join in and torch the
settlement yourself for a **drone schematic with high scrap**, which is by a wide margin the
best outcome available. One of the game's clearest "the evil option pays better" beacons.

## Trigger & Where It Appears
- Event list: `NEUTRAL_CIVILIAN` only ([[source-newevents]]). `dlcEventsOverwrite.xml` does
  not redefine that list, so the AE and vanilla pools are identical here
  ([[source-dlceventsoverwrite]]).
- Sector allocations of `NEUTRAL_CIVILIAN` ([[source-sector-data-xml]]):
  [[sector-federation-space]] (`STANDARD_SPACE`) `2–4`, [[sector-civilian-sector]] `2–4`
- `unique="true"` — at most once per run ([[source-events-xml]])
- Beacon: a pirate ship is present but **non-hostile on arrival**,
  `<ship load="PIRATE_STATION_CROPS" hostile="false"/>`;
  [[source-fandom-remote-settlement]] marks `LRSmap=ship`

> ⚠️ **CONTRADICTION:** sector coverage.
> - Game files: `NEUTRAL_CIVILIAN` is allocated `min=2 max=4` in **both** `STANDARD_SPACE`
>   and `CIVILIAN_SECTOR` ([[source-sector-data-xml]]).
> - Fandom: lists Civilian Sector only ([[source-fandom-remote-settlement]]).
>
> Trusting the game files (`high` vs `medium`) — the same Federation-space omission recurs
> across this wiki's location templates.

## Text
> Scans show a remote settlement being blockaded by a pirate ship. The ship hastily
> messages you, "Stay out of this, or you'll be next!...Concentrate fire on..."

(`event_PIRATE_STATION_CROPS_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Attack the pirate. | — | *"'You asked for it!' They pull away from the planet and move in to engage."* → `<ship hostile="true"/>`. See the fight table below. | 100% |
| 2 | Ignore them. | — | *"It's just not possible to save every civilian affected by this war. You prepare to jump."* → nothing. | 100% |
| 3 | **(Fire Beam)** Show the pirate how to intimidate settlers: burn their crops! | `req="BEAM_FIRE"` | *"…In a few moments the settlement surrenders, offering tribute to leave them alone. The pirate seems impressed."* → `autoReward level="HIGH"` **`drone`** — a drone schematic with high scrap. | 100% |
| 4 | **(Fire Bomb)** Show the pirate how to intimidate settlers: start fires in their crude dwellings. | `req="BOMB_FIRE"` | *"…the pirate seems impressed with your tactics and agrees to share the settlement's 'tribute'."* → `autoReward level="HIGH"` **`drone`**, and **−1 missile**. | 100% |

All four choices are `hidden="true"` — no outcome preview ([[source-events-xml]]).

### Fighting `PIRATE_STATION_CROPS`
The ship definition lives in `events.xml` rather than `events_ships.xml`
([[source-events-xml]]):

| Branch | Trigger | Outcome |
|---|---|---|
| `surrender` | `chance="0.5" min="2" max="4"` → a **50%** surrender offer, since `chance` is the probability the ship keeps fighting ([[concept-surrender-offers]]) | *"Alright! We give up! We're terrible at this pirating thing anyway..."* → **Let them go**: `<ship hostile="false"/>` + `autoReward level="MED"` `stuff`; **Piracy cannot be forgiven. Attack!**: the fight continues |
| `escape` | `chance="0.5" min="3" max="4"` → a **50%** escape attempt | *"They look like they don't want to fight. They are trying to escape."* |
| `gotaway` | they get away | loads `PIRATE_STATION_CROPS_RESULT` — see below |
| `destroyed` / `deadCrew` | — | *"You pick through the remains and contact the settlement."* → `autoReward level="MED"` `standard`, then a hidden continue into `PIRATE_STATION_CROPS_RESULT` |

**`PIRATE_STATION_CROPS_RESULT`** — the settlement's thank-you:
> With the pirates gone you signal the station. "We appreciate what you've done, but there'll
> just be another ship looking to profit from our isolation soon enough. Sorry we can't give
> you more."

→ `autoReward level="LOW"` `stuff` ([[source-events-xml]]).

Fandom's percentages agree with the `1 − chance` reading: it states a 50% escape attempt at
30–40% hull and a 50% surrender offer at 20–40% hull
([[source-fandom-remote-settlement]]).

## Blue Options
- **[[item-fire-beam]]** (`req="BEAM_FIRE"`) — `HIGH drone` for free, no fight, no cost.
- **[[item-fire-bomb]]** (`req="BOMB_FIRE"`) — the same `HIGH drone` for **1 missile**.
  Mechanically identical to the Fire Beam option minus the missile, so if you have both,
  take the beam.

Both requirements name a weapon *type*, not a system, so they are satisfied by owning the
weapon regardless of whether it is powered.

## Rewards & Risks
- Blue options: `HIGH drone` (a drone schematic plus high scrap) with **zero risk**.
- Fighting: `MED standard` + `LOW stuff`, or `MED stuff` if you accept the surrender, or
  just `LOW stuff` if they escape.
- Ignoring: nothing, but also no risk.
- The pirate is a `SHIPS_PIRATE` auto-blueprint hull with both surrender and escape
  branches, so the fight is the ordinary pirate fight with a small tail-end bonus.

## Strategy Notes
- If you have either fire weapon, take it. The blue outcome beats every fight branch and
  carries no combat risk at all — the reward tiers are not close. *(Comparison derived from
  the `autoReward` tags above; no source ranks them.)*
- Without a fire weapon, fighting is worth it mainly for the extra `LOW stuff` tacked on
  after the normal kill reward.
- Accepting the surrender (`MED stuff`) forfeits the `MED standard` + `LOW stuff` you would
  get from finishing them. Whether that trade is worth it depends on whether you need
  resources or scrap.

## Related
- [[event-pirate-fight]] — the baseline pirate encounter
- [[event-pirate-ship-attacking-civilian]] — the other "pirate bullying civilians" beacon in the same list
- [[item-fire-beam]], [[item-fire-bomb]] — the two gating weapons
- [[concept-surrender-offers]] — how the 50% figures are derived
- [[entity-pirates]]

## Open Questions
- [ ] The `min`/`max` on `<surrender>` and `<escape>` are read by Fandom as hull-percentage
      thresholds (20–40% and 30–40%). The game files do not label them; confirm.
- [ ] Does the settlement-burning outcome have any downstream consequence, or is the drone
      schematic the end of it?

> ⚠️ **CONTRADICTION:** choice-4 outcome wording.
> - Game files: *"…you teleport an incendiary explosive into **the** settlement… Forcing
>   their surrender was **laughably easy**…"* ([[source-text-events-xml]])
> - Fandom: *"…into **their** settlement… Forcing their surrender was **almost laughably
>   easy**…"* ([[source-fandom-remote-settlement]])
>
> Trusting the game files (`high` vs `medium`). Cosmetic; most likely pre-AE wording, not
> confirmed as a version difference.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-fandom-remote-settlement]] (per raw/wiki/remote-settlement.md)
