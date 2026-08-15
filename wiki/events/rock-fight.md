---
id: event-rock-fight
type: event
event_name: ROCK_SHIP
sectors: [[[sector-rock-controlled-sector]], [[sector-rock-homeworlds]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-13
sources: 6
tags: [combat, rock, default-rewards, surrender, reused-as-subevent]
---

# Rock fight — `ROCK_SHIP`

## Summary
The baseline Rock combat encounter and the single most-reused Rock event in the game. It
is an unavoidable fight with no choices: you jump in, a Rock ship is hostile, you fight.
Beyond its own slot in `HOSTILE_ROCK` it is loaded as the punishment branch of half a
dozen other Rock events, so most Rock-sector fights you see are literally this event.

## Trigger & Where It Appears
- Sectors: [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]]
- Event list: `HOSTILE_ROCK`, which both Rock sectors allocate at `min="6" max="8"`
  ([[source-sector-data-xml]], per `raw/gamedata/sector_data.xml`)
- Beacon: hostile, ship present ([[source-fandom-rock-fight]], `LRSmap=ship`)
- Not `unique` — it can and does repeat within a sector ([[source-events-rock]])
- **Also loaded from other events**, not just the sector list: the "strip the ship" and
  "leave it alone" branches of [[event-disabled-rock-ship]], the hostile branch of
  [[event-rock-atheists]] (via a `<ship hostile="true"/>` on the pre-loaded `ROCK_SHIP`),
  the scrap-it branch of [[event-ancient-device]], and the losing branch of
  [[event-rock-nursery]] ([[source-events-rock]]).

## Text
Varies — `<text load="ROCK_SHIP"/>` over an **8**-entry `textList`
([[source-events-rock]]). The framings range from a botched trade hail, to an excavation
project you jumped into, to a Rock vessel that objects to the contents of your computer
("Why do you fill your computer with lies?! These are not the holy words!").
[[source-fandom-rock-fight]] transcribes all eight.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(no choices)_ | — | Fight a Rock ship (`<ship load="ROCK_SHIP" hostile="true"/>`). Default rewards on victory. | 100% |

### Surrender branch — `ROCK_SHIP_SURRENDER`
The enemy ship definition carries a surrender offer:
`<surrender chance="0.7" min="3" max="4" load="ROCK_SHIP_SURRENDER"/>`
([[source-events-ships]]) — a **30%** offer, since `chance` is the probability the ship
*keeps fighting* ([[concept-surrender-offers]]). If it fires:

| # | Choice | Outcome |
|---|--------|---------|
| 1 | Accept their offer. | Ship becomes non-hostile; `<autoReward level="RANDOM">stuff</autoReward>` — the game's own word is `RANDOM`, so the payout tier is not fixed. |
| 2 | We will not accept surrender! | The fight continues. |

Surrender flavour text also varies, over a three-entry `textList` repeated four times in
the file ([[source-events-rock]]).

## Blue Options
None. `ROCK_SHIP` has no `req` on anything — there is no talking your way out of it.

## Rewards & Risks
- Victory: **default rewards** for a Rock ship
  ([[source-fandom-rock-fight]]); the event itself specifies no `autoReward`, so the
  payout comes from `DESTROYED_DEFAULT` / `DEAD_CREW_DEFAULT`
  ([[source-events-ships]]).
- Accepting surrender: `RANDOM`-level "stuff" and no further damage taken.
- Risk: a Rock crew is hard to board and hard to burn out — Rockmen are fire-immune —
  and the ship blueprint is `SHIPS_ROCK`, not a pushover. See [[entity-rock-men]].

## Strategy Notes
- With `HOSTILE_ROCK` at 6–8 beacons per sector and `ROCK_SHIP` one of five entries in
  that list, expect to see this several times per Rock sector
  ([[source-sector-data-xml]]).
- The surrender offer is the reason to bring the enemy low rather than alpha-striking it:
  accepting converts a hull-damage race into free `RANDOM` loot. Whether accepting is
  worth more than a kill is not stated by any source here — treat it as open.

> ⚠️ **CONTRADICTION:** the surrender numbers.
> - Game files: `chance="0.7" min="3" max="4"` ([[source-events-rock]], per
>   `raw/gamedata/events_ships.xml`).
> - Fandom passes `{{SurrenderEscape(alt)|surrenderofferchance|ROCK_SHIP|events_ships.xml|30|30-40|3-4}}`
>   on [[source-fandom-disabled-rock-ship]] — a **30** where the file says `0.7`.
>
> ~~We only have the unrendered wikitext, so what those template slots mean (offer chance
> vs. hull threshold vs. scrap) cannot be settled from the raw here. Trusting the game
> files (`high` vs `medium`): `chance="0.7"`, `min/max 3–4`. Flagged rather than resolved.~~
>
> **RESOLVED (lint, 2026-08-13) — both sources were right about different quantities.**
> Per [[concept-surrender-offers]], `chance` is the probability the ship **keeps fighting**,
> so `chance="0.7"` is a **30%** surrender offer — exactly Fandom's 30. `ROCK_SHIP` is in
> fact one of the two decisive rows in that finding (the other being `CRYSTAL_SHIP` at
> 0.6 → 40), because 0.7 reads differently under the two conventions and only `1 − chance`
> matches. The remaining template slots parse as `30-40` = hull-percentage band and `3-4` =
> the `min`/`max` hull points, whose units are still open.

## Related
- [[event-rock-pirates-fight]] — the pirate-flavoured twin, uses `ROCK_PIRATE` instead
- [[event-rock-fight-in-asteroid-field]] — same fight in an asteroid environment
- [[event-rock-fight-with-boarders]] — same fight plus 1–3 boarders
- [[event-disabled-rock-ship]], [[event-ancient-device]], [[event-rock-nursery]] — events
  that load this one as a branch
- [[entity-rock-men]]
- [[event-rock-ship-surrender]] — the `ROCK_SHIP_SURRENDER` aftermath this hull loads

## Open Questions
- [ ] Exact scrap/resource values of "default rewards" for `SHIPS_ROCK`.
- [x] ~~What `chance="0.7"` denotes precisely (offer probability vs. hull threshold) and how
      Fandom's `30` maps onto it.~~ It is the probability the ship **keeps fighting**, so the
      offer is 30% — Fandom's number ([[concept-surrender-offers]]).
- [ ] What `autoReward level="RANDOM"` resolves to in practice.

## Sources
- [[source-events-rock]] (per raw/gamedata/events_rock.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-rock-fight]] (per raw/wiki/rock-fight.md)
- [[source-fandom-disabled-rock-ship]] (per raw/wiki/disabled-rock-ship.md) — for the
  surrender-template numbers only
