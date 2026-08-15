---
id: event-rock-ship-in-plasma-storm
type: event
event_name: NEBULA_ROCK_RACIST
sectors: [[[sector-uncharted-nebula]]]
beacon_type: nebula
hostile: false
blue_options: [rock crew]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [plasma-storm, rock, blue-option, crew-gate, optional-fight, unique]
---

# Rock ship in plasma storm — `NEBULA_ROCK_RACIST`

## Summary
A lost Rock transport insults you and tells you to leave. With a Rock crew member you can
escort them out for the **highest single payout in the nebula file** — `autoReward
level="HIGH"` with the `standard` payload. Without one, your options are to swallow it or
start a fight for ordinary rewards.

## Trigger & Where It Appears
- Beacon: **plasma storm** — `<environment type="storm"/>`, despite the `NEBULA_` prefix on
  the event id. This is why Fandom titles the page "in plasma storm"
  ([[source-fandom-rock-ship-in-plasma-storm]]).
- `unique="true"` — once per run.
- **[[sector-uncharted-nebula]] only.** Its single list is `NEBULA_NEUTRAL`
  ([[source-events-nebula]]), allocated 7–8 per `NEBULA_SECTOR`
  ([[source-sector-data-xml]]). Fandom agrees.
- Arrives non-hostile: `<ship load="ROCK_SHIP" hostile="false"/>`. Long-range scanners show
  a ship in a plasma storm.
- Flagged `NEW` in the file's header comment — a later addition to the nebula pool.

## Text
> A Rock armoured transport nearby looks to have lost its bearings, but when you hail they
> grow suspicious: "Whatever life-form you are, we find you repugnant. We seek no aid.
> Leave. Now."

(`event_NEBULA_ROCK_RACIST_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Leave. | — | Empty `<event/>` — nothing happens. | 100% |
| 2 | Repugnant?! Arm the weapons! | — | `<ship hostile="true"/>` — fight the `ROCK_SHIP`. | 100% |
| 3 | **(Rock crewmember)** Offer to lead them out of the nebula. | `req="rock"`, `hidden="true"` | *"The Rock grudgingly transfer control of their helm to you and you steer them to a thinner part of the nebula. They're not sure what to think, but transfer over some supplies all the same."* → `autoReward level="HIGH"`, payload **`standard`**. | 100% |

### The `ROCK_SHIP`
`events_ships.xml`, on the `SHIPS_ROCK` blueprint pool, with the developer note
`<!-- JUSTIN - MAKE A SURRENDER!!-->` ([[source-events-ships]]):
- `<surrender chance="0.7" min="3" max="4" load="ROCK_SHIP_SURRENDER"/>` — a **70%**
  surrender chance, the highest of any ship referenced by this batch. Accepting pays
  `autoReward level="RANDOM">stuff` and turns the ship non-hostile
  ([[source-events-rock]]).
- `<destroyed load="DESTROYED_DEFAULT"/>` → `MED` / `standard`.
- `<deadCrew load="DEAD_CREW_DEFAULT"/>`.
- No escape element — it cannot flee.

## Blue Options
- **Rock crew member** (`req="rock"`) — any Rock crew member satisfies it; the XML sets no
  count or level. It is the only `HIGH`-level `autoReward` reachable in
  `events_nebula.xml` outside the `STORM_ITEMS` damage branch, and it costs nothing at all.

## Rewards & Risks
- Choice 3: `HIGH` / `standard`, free, no fight. Unambiguously the best outcome in the
  event.
- Choice 2: `MED` / `standard` on a kill, or a `RANDOM` / `stuff` roll if the 70% surrender
  fires and you accept — plus the risk of a Rock warship in a plasma storm, an environment
  that periodically ignites fires aboard both ships.
- Choice 1: nothing, no risk.

## Strategy Notes
- With a Rock crew member this is one of the best free beacons in the game. It is a
  standing argument for keeping a Rock crew member alive through
  [[sector-uncharted-nebula]].
- Without one, the 70% surrender rate makes attacking less bad than it looks — but a plasma
  storm is a poor place to fight a Rock ship, since Rock ships characteristically field
  fire weapons and the storm compounds fire risk. *(That last point is about the
  `SHIPS_ROCK` blueprint pool, not this event, and is not stated in the sources read here.)*

## Related
- [[event-mantis-fight-choice-in-nebula]] — the same "fight or move on" shape, no blue
  option
- [[event-rock-fight-in-nebula]] — a different Rock nebula encounter
- [[entity-rock-men]], [[concept-blue-options]], [[sector-uncharted-nebula]]
- [[event-rock-ship-surrender]] — the `ROCK_SHIP_SURRENDER` aftermath this hull loads

## Open Questions
- [ ] Numeric values behind `autoReward level="HIGH">standard`.
- [ ] Whether the `req="rock"` gate accepts a Crystal crew member (Crystals descend from
      Rock in FTL's fiction; the XML says only `rock`).

## Notes on transcription
> ⚠️ **CONTRADICTION (wording):** Fandom transcribes choice 2 as *"Repugnant? Arm the
> weapons!"* and writes "rock" in lower case throughout
> ([[source-fandom-rock-ship-in-plasma-storm]]); the game strings read *"Repugnant?! Arm
> the weapons!"* and capitalise "Rock" ([[source-text-events-xml]]). Trusting the game
> files. Cosmetic, and almost certainly a wiki slip rather than a version difference.

## Sources
- [[source-events-nebula]] (per raw/gamedata/events_nebula.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-events-rock]] (per raw/gamedata/events_rock.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-fandom-rock-ship-in-plasma-storm]] (per raw/wiki/rock-ship-in-plasma-storm.md)
