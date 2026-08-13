---
id: event-pirate-fight
type: event
event_name: PIRATE
sectors: [[[sector-civilian-sector]], [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-federation-space]], [[sector-pirate-controlled-sector]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 12
tags: [pirate, unavoidable-fight, default-rewards]
---

# Pirate fight — `PIRATE`

## Summary
The plain pirate ambush: you jump in, a pirate ship is hostile, there is no choice and no
way out but through. It is the baseline pirate encounter — several other events in this
batch are this fight wrapped in an environment hazard or a decision. The ship it loads,
`<ship name="PIRATE">`, is also the ship most other pirate events use, so its surrender /
escape / destroyed profile is documented in full here and referenced elsewhere.

## Trigger & Where It Appears
- Sectors: [[sector-civilian-sector]], [[sector-engi-controlled-sector]],
  [[sector-engi-homeworlds]], [[sector-federation-space]],
  [[sector-pirate-controlled-sector]]
- Event lists: `HOSTILE_PIRATE` ([[source-events-pirate]]), `HOSTILE_CIVILIAN`
  ([[source-newevents]]), `HOSTILE_ENGI` ([[source-events-engi]]), and under Advanced
  Edition also `OVERRIDE_HOSTILE2`, `OVERRIDE_HOSTILE_ENGI`, `OVERRIDE_HOSTILE_PIRATE`
  ([[source-dlceventsoverwrite]]). `HOSTILE_CIVILIAN` is what puts it in
  [[sector-federation-space]] (`min=4 max=6` there, [[source-sector-data-xml]]).
- Pirate sectors allocate `HOSTILE_PIRATE` at `min=6 max=8` beacons
  ([[source-sector-data-xml]])
- Not `unique` — the event element carries no `unique` attribute, so it can repeat within
  a sector ([[source-events-pirate]]; [[source-fandom-pirate-fight]] agrees,
  `unique=false`)
- Long-range scanners show a ship at the beacon ([[source-fandom-pirate-fight]],
  `LRSmap=ship`)

## Text
Varies — `<text load="PIRATE"/>` over a five-entry `textList`
([[source-events-pirate]]). All five, per [[source-text-events-xml]]:

> As you jump into the system a pirate advances on your position. They are refusing all
> hails. Prepare for a fight.

> Soon after arriving in the system you are hailed by a small cruiser. "What good fortune
> that we happen to run into each other. Nothing personal, but you have some information
> we need!"

> At first it appears you've arrived in an empty system, but a ship appears from behind a
> planet and hails you: "Haha! I am the dread pirate Tuco, prepare to die!"

> The only other ship at this beacon messages you: "Finally, after months of waiting,
> someone has fallen into our trap!"

> You barely have time to register jump completion before your ship warns you of an
> incoming ship with weapons hot.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(no choices)_ | — | `<ship load="PIRATE" hostile="true"/>` — combat starts immediately. | 100% |

The whole event body is a `<text>` and a hostile `<ship>` ([[source-events-pirate]]).

### The `PIRATE` ship
`<ship name="PIRATE" auto_blueprint="SHIPS_PIRATE">` ([[source-events-ships]]):

| Branch | Trigger in the file | Result |
|---|---|---|
| Surrender | `chance="0.5" min="3" max="4"` → loads `PIRATE_SURRENDER` | Offer at 3–4 hull remaining. Accept → ship becomes non-hostile, `autoReward level="RANDOM"` `stuff`. Refuse → fight continues. |
| Escape | `chance="0.5" min="2" max="4"` → loads `PIRATE_ESCAPE` | At 2–4 hull it spins up its FTL: *"The enemy ship appears to be powering up its FTL. It's trying to escape!"* |
| Got away | — | *"The pirate jumped away."* No reward. |
| Destroyed | loads `DESTROYED_DEFAULT` | *"The ship explodes, leaving behind a substantial collection of useful scrap material."* → `autoReward level="MED"` `standard`. Both entries of that 2-member list are identical, so this is deterministic. |
| Crew killed | loads `DEAD_CREW_DEFAULT` | 9-entry list, see below. |

`PIRATE_SURRENDER`, `PIRATE_ESCAPE`, `DESTROYED_DEFAULT` and `DEAD_CREW_DEFAULT` all live
in `raw/gamedata/events.xml` ([[source-events-xml]]).

### `DEAD_CREW_DEFAULT` — killing the crew instead of the ship
Nine entries with repeats. Weightings below are **derived from how many times each entry
appears in the list and assume uniform selection across list entries**
([[source-events-xml]]):

| Result | Entries | Share |
|---|---|---|
| *"There are no more life-signs remaining on the ship. You strip it of useful materials."* → `autoReward level="MED"` `standard` | 3 | 3/9 |
| Same text → `autoReward level="HIGH"` `standard` | 2 | 2/9 |
| *"With the crew dead, you are able to take the fuel out of storage…"* → `autoReward level="HIGH"` `fuel` | 2 | 2/9 |
| *"…you find a prisoner who offers to join your crew."* → **+1 crew member** and `autoReward level="LOW"` `scrap_only` | 1 | 1/9 |
| *"You find a weapon system on their ship…"* → `autoReward level="LOW"` `weapon` | 1 | 1/9 |

## Blue Options
None. The event has no `req=` gates at all.

## Rewards & Risks
- **Reward:** the "default rewards" profile — MED `standard` on a kill, or the
  `DEAD_CREW_DEFAULT` table (which is strictly better on average, and can pay a free crew
  member or a weapon) if you kill the crew and leave the hull intact.
- **Surrender** pays `RANDOM` `stuff` (resources plus some scrap) and ends the fight
  early — usually the safe line if your hull is thin.
- **Risk:** an unavoidable fight. There is no bribe, no run, no blue option.

> ⚠️ **CONTRADICTION (systematic, affects every pirate ship page):** the meaning of the
> `chance` attribute on `<surrender>` / `<escape>`.
> - Game files: `<surrender chance="0.5" …/>`, `<escape chance="0.5" …/>`
>   ([[source-events-ships]]).
> - Fandom reports "50% chance at 30-40% hull" for surrender and "50% chance at 20-40%
>   hull" for escape ([[source-fandom-pirate-toll]], which annotates this same `PIRATE`
>   ship).
>
> For `PIRATE` the two readings coincide because the value is 0.5. They do **not**
> coincide for other ships: Fandom reports `PIRATE_BRIBER`'s `chance="0.3"` surrender as
> **70%** and its `chance="0.4"` escape as **60%**, and `JELLY_PIRATE_WITHBOARDERS`'s
> `chance="0.3"` escape as **70%** ([[source-fandom-pirate-briber]],
> [[source-fandom-destroyed-cargo-ship]]). Fandom is consistently reporting `1 − chance`,
> which implies the attribute is the chance the ship *keeps fighting*, not the chance it
> surrenders. The raw attribute values here are game-file facts (`high`); the semantics
> are Fandom's interpretation (`medium`) and are recorded, not resolved.
>
> Separately, `min`/`max` are **hull points**, not percentages — Fandom renders them as
> percentages with its own tooltip conceding "actual in-game value may be 3-4 hull".

## Strategy Notes
- *(Opinion.)* Boarding rather than blowing the ship up is worth it when you can do it
  safely: `DEAD_CREW_DEFAULT` beats `DESTROYED_DEFAULT` on every entry, and 1/9 of the
  time it hands you a crew member.
- Accepting the surrender forfeits both of those tables in exchange for a `RANDOM`
  `stuff` payout, which is resource-heavy and scrap-light.

## Related
- [[event-pirate-fight-in-asteroid-field]], [[event-pirate-fight-near-sun]] — the same
  fight with an environment hazard
- [[event-pirate-toll]] — the same ship, with a chance to pay it off instead
- [[event-pirate-engine-hacker]] — a pirate fight with a different ship and a system debuff
- [[event-destroyed-cargo-ship]] — one of its branches loads this ship
- [[entity-pirates]]
- [[sector-pirate-controlled-sector]], [[sector-civilian-sector]],
  [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]],
  [[sector-federation-space]]
- [[event-pirate-surrender]] — the shared `PIRATE_SURRENDER` aftermath this hull loads
- [[event-pirate-escape]] — the shared `PIRATE_ESCAPE` aftermath this hull loads

## Open Questions
- [ ] Exact scrap values behind `LOW`/`MED`/`HIGH`/`RANDOM` `autoReward` levels.
- [ ] Whether `chance` is P(surrender) or P(keep fighting) — see the contradiction above.
- [ ] Whether the five text variants are weighted evenly.

## Sources
- [[source-events-pirate]] (per raw/gamedata/events_pirate.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml — `HOSTILE_CIVILIAN`)
- [[source-events-engi]] (per raw/gamedata/events_engi.xml — `HOSTILE_ENGI`)
- [[source-fandom-pirate-fight]] (per raw/wiki/pirate-fight.md)
- [[source-fandom-pirate-toll]], [[source-fandom-pirate-briber]],
  [[source-fandom-destroyed-cargo-ship]] — cited only for the `chance` contradiction above
