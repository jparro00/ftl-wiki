---
id: event-rebel-fight-with-boarders
type: event
event_name: BOARDERS_REBEL_SHIP
sectors: [[[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [rebel, boarding, no-choice, default-rewards, combat]
---

# Rebel fight with boarders — `BOARDERS_REBEL_SHIP`

## Summary
A Rebel ship fight with 2–3 human boarders already on your deck when the event resolves.
One of only two entries in the `BOARDERS_REBEL` list, which every Rebel sector allocates
exactly once — so if you clear a Rebel sector you have a coin-flip chance of seeing this
specific event.

## Trigger & Where It Appears
- Sectors: [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]].
- Beacon: hostile.
- Event list: `BOARDERS_REBEL`, whose only two entries are `BOARDERS_SUN` and this event
  ([[source-events-rebel]]). `BOARDERS_REBEL` is allocated **`min=1 max=1`** in both Rebel
  sector types ([[source-sector-data-xml]]) — exactly one boarding beacon per Rebel sector.
- The `textList` carries `unique="false"`, and the event itself declares no `unique`
  attribute — it can repeat ([[source-events-rebel]],
  [[source-fandom-rebel-fight-with-boarders]]).
- Long-range scanners show a ship ([[source-fandom-rebel-fight-with-boarders]]).

## Text
Drawn from the `BOARDERS_REBEL_SHIP` text list — **four variants**
([[source-events-rebel]], [[source-text-events-xml]]):

> You receive a message from a nearby Rebel station, "You have a lot of guts passing
> through our space, I'll give you that." He turns giving an order, "Kill their crew, I
> want that ship intact."

> Your sensors warn of an incoming Rebel ship at the same time as you hear the telltale
> signs of a teleporter. You hear someone taunt from within the ship, "Ready to die? I sure
> am ready to get a promotion!"

> Incoming message, "Hello Captain," says a Rebel in an officer's garb. "How very generous
> of you to turn yourself in. Prepare to be boarded. Come quietly and we may be lenient."

> You receive a message on a low-band channel. "You're surrounded, just like the last of
> your Federation friends. Just die already." The enemy has teleported onto your ship!

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none — the event has no `<choice>` elements)* | — | `<boarders min="2" max="3" class="human"/>` beam aboard **and** you fight `<ship load="REBEL" hostile="true"/>` — the generic Rebel warship, with **default rewards**. | 100% |

The boarder count is 2–3 and the species is fixed to `human` — Fandom agrees
([[source-fandom-rebel-fight-with-boarders]]).

### The `REBEL` ship
Same definition as [[event-rebel-fight]]: `SHIPS_REBEL` blueprint, 50% surrender chance
(`PIRATE_SURRENDER`) at hull 2–3, 50% escape chance (`PIRATE_ESCAPE`) at hull 3–4,
`DESTROYED_DEFAULT` / `DEAD_CREW_DEFAULT` payouts ([[source-events-ships]],
[[source-events-xml]]).

## Blue Options
None.

## Rewards & Risks
- Reward: default rewards only — `autoReward level="MED"` `standard` on destruction, a
  `MED`/`HIGH` roll on crew kill ([[source-events-xml]]).
- Risk: **human boarders arrive before you can react**. 2–3 attackers is enough to lose a
  system room or a crew member on a small ship, and you are simultaneously being shot at.
  The event gives no chance to prepare — no choice, no blue option, no doors warning.

## Strategy Notes
- *(Opinion.)* This is the encounter that justifies keeping a spare crew member off the
  helm in Rebel space, and the strongest argument for upgraded Doors before entering a
  Rebel sector — the sector guarantees one boarding beacon, and half the pool is this event.
- Killing the *enemy* crew ends nothing on your ship; the boarders must still be dealt with.
- Because the enemy ship can surrender at 50%, the fight may end while boarders are still
  aboard. The files do not state what happens to boarders on surrender — untested here.

## Related
- [[event-rebel-fight]] — the same `REBEL` ship without boarders
- [[event-boarders-rebels-in-nebula]] — Rebel boarders with **no** enemy ship to shoot back at
- [[event-boarders-mantis]], [[event-boarders-crystal]] — the other faction boarding events
- [[concept-rebel-fleet-advance]]
- [[event-pirate-surrender]] — the shared `PIRATE_SURRENDER` aftermath this hull loads
- [[event-pirate-escape]] — the shared `PIRATE_ESCAPE` aftermath this hull loads

## Open Questions
- [ ] What happens to boarders already aboard if the enemy ship surrenders.
- [ ] Numeric values behind "default rewards".
- [ ] Whether `BOARDERS_SUN` and this event are equally weighted in `BOARDERS_REBEL`.

## Sources
- [[source-events-rebel]] (per `raw/gamedata/events_rebel.xml`)
- [[source-events-ships]] (per `raw/gamedata/events_ships.xml`)
- [[source-events-xml]] (per `raw/gamedata/events.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-rebel-fight-with-boarders]] (per `raw/wiki/rebel-fight-with-boarders.md`)
