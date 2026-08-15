---
id: event-slug-home-nebula-surrender
type: event
event_name: NEBULA_SLUG_FIGHT_UNLOCK
sectors: [[[sector-slug-home-nebula]]]
beacon_type: nebula
hostile: true
blue_options: [slug crew, sensors lvl 2, cloaking]
chain: [[[chain-slug-cruiser-unlock]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-13
sources: 4
tags: [unique, guaranteed, ship-unlock, combat, quest-marker, blue-option]
---

# Slug Home Nebula surrender — `NEBULA_SLUG_FIGHT_UNLOCK`

## Summary
A guaranteed beacon in [[sector-slug-home-nebula]] that is deliberately disguised as an
ordinary [[event-slug-fight-in-nebula]] — same intro text, same ship blueprint. The only
tell is the surrender: this ship's surrender block leads to the **Slug Cruiser unlock
chain**, offering either an Anti-Bio Beam or a quest marker to the cruiser's construction
platform.

## Trigger & Where It Appears
- Sector: [[sector-slug-home-nebula]] **only**
- **Guaranteed:** `<event name="NEBULA_SLUG_FIGHT_UNLOCK" min="1" max="1"/>` in the
  `SLUG_HOME` sector description — exactly one per Slug Home Nebula
  ([[source-sector-data-xml]])
- Beacon: nebula (`<environment type="nebula"/>`), `unique="true"`
  ([[source-events-slug]])
- Fandom notes the Slug Cruiser can also be unlocked by winning with the Mantis Cruiser —
  this event is not the only route ([[source-fandom-slug-home-nebula-surrender]])

## Text
Loads the **same text list as [[event-slug-fight-in-nebula]]** (`<text load="NEBULA_SLUG_FIGHT"/>`)
— five variants, quoted in full on that page. This is the reason the two events cannot be
told apart on arrival. ([[source-events-slug]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | (none) | — | `<ship load="JELLY_UNLOCK1" hostile="true"/>` — a Slug ship on the same `SHIPS_JELLY` blueprint, with a special surrender. | 100% |

### The enemy — `JELLY_UNLOCK1`

```
<surrender chance="0" min="3" max="4" load="SLUG_UNLOCK_SURRENDER"/>
<escape    chance="0.5" min="3" max="4" load="PIRATE_ESCAPE"/>
<destroyed load="DESTROYED_DEFAULT"/>
<deadCrew  load="DEAD_CREW_DEFAULT"/>
```
([[source-events-ships]])

> ⚠️ **CONTRADICTION:** the surrender probability.
> - Game files: `chance="0"` ([[source-events-ships]]).
> - Fandom: "surrender offer: **100% chance** at 30–40% hull"
>   ([[source-fandom-slug-home-nebula-surrender]]) — and it quotes the very same
>   `chance="0"` line in its own reference notes.
>
> Fandom applies the same reading to `QUEST_SLUG_PIRATE_TRAP1`, which is also `chance="0"`
> and which it describes as simply "surrenders at 30–40% hull". So `chance="0"` appears to
> mean *this ship always takes the scripted surrender branch* rather than *never
> surrenders*. ~~Recorded, not resolved: no source here documents the attribute's
> semantics.~~
>
> **RESOLVED (lint, 2026-08-13).** The reading above is correct and now sourced:
> [[concept-surrender-offers]] establishes `chance` as the probability the ship **keeps
> fighting**, making `chance="0"` a guaranteed offer — Fandom's 100%. This event and
> `QUEST_SLUG_PIRATE_TRAP1` are two of the four `chance="0"` ships, and all four are built
> around an offer that must fire, which is itself part of the evidence. No contradiction
> remains: **100%**, both sources agreeing.

### `SLUG_UNLOCK_SURRENDER` — the tell

> "You have besssted us! Will you accept what is in our storeesss in exchange for our
> livess?"

| # | Choice | Outcome |
|---|--------|---------|
| 1 | Let them live. | → "Take thisss newly developed weapon we're transporting…" then: |
| 1a | Accept the prototype weapon. | `<weapon name="BEAM_BIO"/>` — the [[item-anti-bio-beam]]; ship becomes non-hostile |
| 1b | We don't want the weapon, we want information. | `<quest event="SLUG_UNLOCK_1"/>` — a quest marker to the construction platform; ship non-hostile |
| 2 | We will not accept surrender! | Nothing — the fight continues |

(`SLUG_UNLOCK_SURRENDER` is loaded from the **ship** block, not from this event's choices;
it carries its own `event_name` and is documented at [[event-slug-unlock-surrender]].)

### The quest marker — `SLUG_UNLOCK_1` / `SLUG_UNLOCK_2`

Documented at [[event-slug-unlock-1]] (which also covers `SLUG_UNLOCK_2` as a
sub-event — it has no page of its own). In outline, per
[[source-events-slug]] and [[source-fandom-slug-home-nebula-surrender]]:

- Charging in fights `JELLY_UNLOCK2` (blueprint `JELLY_TRUFFLE`, a Slug Assault) —
  `HIGH standard` on a kill, but the platform escapes and there is **no unlock**.
- Tailing them can end in the same assault-ship fight, in nothing at all, or — with a
  **Slug crew member** (`req="slug"`) or **Sensors level 2+** (`req="sensors" lvl="2"`) — in
  a fight with `JELLY_UNLOCK3` (blueprint `JELLY_BUTTON`, a Slug Interceptor).
- Destroying `JELLY_UNLOCK3` gives `<unlockShip id="5"/>`, `HIGH standard`, and
  `<augment name="SLUG_GEL"/>` — the [[item-slug-repair-gel]]. That ship starts an escape
  with a 35-second timer, so it can get away and you get nothing.
  ([[source-events-ships]])

The event definition also contains a **commented-out** older version of `SLUG_UNLOCK_1`
with `req="cloaking"` and `req="pilot" lvl="2"` options and a dev note "Changed this part
to be easier" — those blue options are **not live** in this build ([[source-events-slug]]).

## Blue Options
- **Slug crew member** (`req="slug"`, at `SLUG_UNLOCK_2`) — monitors life signatures so the
  escort jumps away, leaving only the weak interceptor: the path that actually unlocks the
  ship.
- **Sensors level 2+** (`req="sensors" lvl="2"`, at `SLUG_UNLOCK_2`) — same payoff by a
  different route.
- **Cloaking / Piloting 2** — present only in commented-out code; not available.

## Rewards & Risks
- [[item-anti-bio-beam]] (`BEAM_BIO`) for taking the weapon and ending the chain there.
- Or: the Slug Cruiser unlock, `HIGH standard`, and [[item-slug-repair-gel]] — but only if
  you reach and kill `JELLY_UNLOCK3` before its 35-second escape timer runs out.
- Fandom flags a bug: if the `standard` reward roll happens to include an augment, it
  **overwrites** the guaranteed Slug Repair Gel
  ([[source-fandom-slug-home-nebula-surrender]]).
- Risk: destroying the ship outright, or letting it escape (50%), forfeits the whole chain.

## Strategy Notes
- In the Slug Home Nebula, treat **every** Slug nebula fight as a possible unlock: shoot
  the ship down to low hull and wait for a surrender offer rather than finishing it.
  ([[source-fandom-slug-home-nebula-surrender]])
- The escape roll and the surrender roll sit in the same hull band, so if the ship tries to
  run first you must land more damage to trigger the surrender
  ([[source-fandom-slug-home-nebula-surrender]]).
- Taking the Anti-Bio Beam ends the chain. If the cruiser is the goal, refuse the weapon.

## Related
- [[event-slug-fight-in-nebula]] — the ordinary fight this is disguised as
- [[event-slug-unlock-surrender]], [[event-slug-unlock-1]] — the
  rest of the chain
- [[chain-slug-cruiser-unlock]]
- [[item-anti-bio-beam]], [[item-slug-repair-gel]]
- [[sector-slug-home-nebula]], [[entity-slugs]]
- [[event-pirate-escape]] — the shared `PIRATE_ESCAPE` aftermath this hull loads

## Open Questions
- [x] ~~What `chance="0"` actually means in a `<surrender>` block.~~ A **guaranteed** offer —
      `chance` is the probability the ship keeps fighting ([[concept-surrender-offers]]).
- [ ] Whether the augment-overwrite bug Fandom describes is present in this 1.6.x build.

## Sources
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-slug-home-nebula-surrender]] (per raw/wiki/slug-home-nebula-surrender.md)
