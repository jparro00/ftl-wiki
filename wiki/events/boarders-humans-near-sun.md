---
id: event-boarders-humans-near-sun
type: event
event_name: BOARDERS_SUN
sectors: [[[sector-federation-space]], [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]], [[sector-pirate-controlled-sector]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]]]
beacon_type: any
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 7
tags: [pirate, boarding-hazard, sun-hazard, no-enemy-ship, unique]
---

# Boarders: Humans near sun — `BOARDERS_SUN`

## Summary
Desperate pirates whose own ship is dying next to a star decide to take yours. 2–4 human
boarders beam aboard and there is **no enemy ship to shoot** — the entire encounter is
fought inside your own hull, while a solar flare hazard cooks your rooms. No choices, no
rewards, `unique="true"`.

## Trigger & Where It Appears
- Sectors: [[sector-federation-space]], [[sector-mantis-controlled-sector]],
  [[sector-mantis-homeworlds]], [[sector-pirate-controlled-sector]],
  [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]]
- Event lists: `BOARDERS_PIRATE` ([[source-events-pirate]]), `BOARDERS_MANTIS`
  ([[source-events-mantis]]), `BOARDERS_REBEL` ([[source-events-rebel]]) and
  `HOSTILE_BOARDING` ([[source-newevents]])
- Allocation: `BOARDERS_PIRATE` `min=1 max=1` in Pirate sectors, `BOARDERS_REBEL`
  `min=1 max=1` in the two Rebel sectors, `BOARDERS_MANTIS` `min=1 max=2` in the two
  Mantis sectors ([[source-sector-data-xml]]). **`HOSTILE_BOARDING` is dead in
  `sector_data.xml`** — `min="0" max="0"` in `STANDARD_SPACE` and commented out in
  `CIVILIAN_SECTOR` — which is why [[source-fandom-boarders-humans-near-sun]] lists Mantis,
  Pirate and Rebel sectors but **not** Federation Space.
- `unique="true"` — once per run ([[source-events-pirate]]; Fandom agrees)
- Environment: `<environment type="sun"/>`
- Long-range scanners show **no ship** and the red giant
  ([[source-fandom-boarders-humans-near-sun]], `LRSmap=noship+redgiant`)

## Text
> You arrive to find yourself extremely close to a star. You receive a message from a
> pirate ship, "I'm glad you arrived; our ship is damaged and we were getting
> desperate... I hope you don't mind if we take yours." Hostiles detected on board our
> ship!

(`event_BOARDERS_SUN_text`, per [[source-text-events-xml]]. Fandom transcribes it
identically.)

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(no choices)_ | — | `<boarders min="2" max="4" class="human"/>` with `<environment type="sun"/>` — **2–4 human boarders** aboard, under solar flare damage. | 100% |

The event body is a `<text>`, a `<boarders>` tag and an `<environment>` tag. There is **no
`<ship>` element**, no `<autoReward>`, and no outcome branch of any kind
([[source-events-pirate]]).

## Blue Options
None.

## Rewards & Risks
- **Reward: none.** The event defines no `autoReward`, no scrap and no items. Killing the
  boarders ends the encounter and that is all.
- **Risk:** 2–4 human boarders inside your ship, plus the sun hazard setting fires in the
  rooms they are fighting in. Because there is no enemy ship, weapons are useless and the
  fight is entirely crew-vs-crew (or airlock-vs-boarders).

## Strategy Notes
- *(Opinion.)* The sun makes the usual "vent the boarders" answer more complicated: fires
  started by flares spread in the same rooms you are trying to depressurise, and you may
  need the oxygen for your own crew afterwards.
- With no enemy ship there is nothing to shoot and nothing to win — the goal is to get
  through it having spent as little hull and crew health as possible, then jump.
- Human boarders are the weakest boarder class in the game, which is the one mercy here.

## Related
- [[event-boarders-asteroid]] — the same 2–4 human boarders in an asteroid field
- [[event-destroyed-cargo-ship]] — the other `BOARDERS_PIRATE` event that beams human
  boarders aboard
- [[event-pirate-fight-near-sun]] — the same star hazard, with a ship to shoot at
- [[entity-pirates]]
- [[sector-pirate-controlled-sector]], [[sector-mantis-controlled-sector]],
  [[sector-mantis-homeworlds]], [[sector-rebel-controlled-sector]],
  [[sector-rebel-stronghold]], [[sector-federation-space]]

## Open Questions
- [ ] Is the boarder count uniform over 2–4? The file gives `min`/`max` only.
- [ ] Solar flare tick rate / damage is not defined in this event.
- [ ] Can this event actually appear in [[sector-federation-space]]? Its only route there
      is `HOSTILE_BOARDING`, which that sector allocates at `min=0 max=0`.

## Sources
- [[source-events-pirate]] (per raw/gamedata/events_pirate.xml)
- [[source-events-mantis]] (per raw/gamedata/events_mantis.xml — `BOARDERS_MANTIS`)
- [[source-events-rebel]] (per raw/gamedata/events_rebel.xml — `BOARDERS_REBEL`)
- [[source-newevents]] (per raw/gamedata/newEvents.xml — `HOSTILE_BOARDING`)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-boarders-humans-near-sun]] (per raw/wiki/boarders-humans-near-sun.md)
