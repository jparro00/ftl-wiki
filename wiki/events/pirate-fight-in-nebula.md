---
id: event-pirate-fight-in-nebula
type: event
event_name: NEBULA_PIRATE
sectors: [[[sector-pirate-controlled-sector]], [[sector-uncharted-nebula]]]
beacon_type: nebula
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 7
tags: [nebula, pirate, no-choice, combat, unreachable, name-collision, shipped-but-dead]
---

# Pirate fight in nebula — `NEBULA_PIRATE`

## Summary
A complete, fully authored pirate ambush — five flavour texts, a `PIRATE` ship, default
rewards — that **almost certainly never fires**. An `eventList` in `events_pirate.xml`
carries the same name, and every reference to `NEBULA_PIRATE` in the nebula pools resolves
to that list instead of to this event. Shipped content, effectively dead.

## Trigger & Where It Appears
- Listed in `NEBULA_HOSTILE` ([[source-events-nebula]]), which
  `sector_data.xml` allocates 5–6 per [[sector-uncharted-nebula]]; and reachable in
  principle from [[sector-pirate-controlled-sector]] through the `NEBULA_PIRATE`
  allocation ([[source-sector-data-xml]]).
- No `unique` attribute.
- **The name collision.** `raw/gamedata/events_pirate.xml` line 87 defines
  `<eventList name="NEBULA_PIRATE">` with twelve entries (`NEBULA_EMPTY`, `NEBULA_REBEL`,
  `NEBULA_PIRATE_SMUGGLE`, `NEBULA_TRADER`, `NEBULA_LOST_SHIP` ×2, `NEBULA_BOARDING`,
  `NEBULA_REBEL_UNDETECTED`, `NEBULA_REBEL_BOARDING`, `STORM_ITEMS` ×2, and a
  commented-out `STORM_BOARDING`) ([[source-events-pirate]]).
  [[source-fandom-pirate-fight-in-nebula]] states that when both an event and an eventList
  share a name, **the eventList wins**, so this event *"can never happen"*.
- **Missing environment tag.** Uniquely among the nebula events in this file,
  `NEBULA_PIRATE` has **no `<environment type="nebula"/>`**. Fandom flags the consequence:
  *"although the beacon is in a nebula on the map, the nebula environment will be missing
  upon arrival."* Verified — the event body is only `<text>` and `<ship>`
  ([[source-events-nebula]]).

> The existence of the shadowing eventList is verifiable in `raw/gamedata/`. The
> *resolution order* — eventList beats event — is engine behaviour that no game file
> states; it rests on [[source-fandom-pirate-fight-in-nebula]] alone (reliability
> `medium`). The `unreachable` tag reflects that, and would be wrong if the engine
> resolved the other way.

## Text
The prose is drawn from the `NEBULA_PIRATE` text list — **a third thing with the same
name**, this one a `textList` in `events_nebula.xml` — and varies across five strings
([[source-text-events-xml]]). The list carries the author note `<!-- JUSTIN - ADD MORE -->`.

> As you drift through the nebula an unmarked vessel descends from the clouds and into your
> wake. Their weapons come online.

> A pirate ship pulls out of the ether and hails: "You know what I love about this part of
> the galaxy? The explorers! You always carry such fine loot." They lock weapons.

> You try to read the ID of a ship ahead in the fog, but it's too thick to penetrate. You
> have your answer when the ship turns, weapons hot!

All five are transcribed on [[source-fandom-pirate-fight-in-nebula]].

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(none — the event has no `<choice>` elements)_ | — | *If it ever fired:* immediate combat with a `PIRATE` ship, default rewards, **without** the nebula environment. | n/a — the event is shadowed |

The `PIRATE` ship definition ([[source-events-ships]]):
`<surrender chance="0.5" min="3" max="4" load="PIRATE_SURRENDER"/>`,
`<escape chance="0.5" min="2" max="4" load="PIRATE_ESCAPE"/>`,
`<destroyed load="DESTROYED_DEFAULT"/>` (`MED` / `standard`),
`<deadCrew load="DEAD_CREW_DEFAULT"/>`. Accepting the surrender pays
`autoReward level="RANDOM">stuff` ([[source-events-xml]]).

## Blue Options
None.

## Rewards & Risks
Not applicable in practice. If it fired: default pirate-fight rewards, with the notable
oddity that the fight would happen in clear space at a beacon drawn on the map as a nebula.

## Strategy Notes
- Nothing actionable. Recorded so the event pool is complete and so the shadowing is
  documented rather than silently dropped.
- The practical effect of the collision is the opposite of a loss: every slot that *should*
  have been a pirate fight instead re-rolls into a twelve-entry table containing empties,
  traders and boarders. It makes [[sector-pirate-controlled-sector]] nebula beacons more
  varied and less dangerous than the design implies.

## Related
- [[event-rebel-fight-in-nebula]] — the identical bug, one file over
- [[event-pirate-smuggler]] — the pirate encounter that *does* fire in nebula space
- [[event-pirate-ship-selling-weapon]] — the other `PIRATE`-ship nebula event
- [[sector-pirate-controlled-sector]], [[sector-uncharted-nebula]]
- [[event-pirate-surrender]] — the shared `PIRATE_SURRENDER` aftermath this hull loads
- [[event-pirate-escape]] — the shared `PIRATE_ESCAPE` aftermath this hull loads

## Open Questions
- [ ] Confirm the engine's event-vs-eventList resolution order from a non-Fandom source.
- [ ] Whether the missing `<environment>` tag is deliberate or the same oversight as the
      name collision.
- [ ] Whether any FTL build ever resolved `NEBULA_PIRATE` to the event.

## Sources
- [[source-events-nebula]] (per raw/gamedata/events_nebula.xml)
- [[source-events-pirate]] (per raw/gamedata/events_pirate.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-fandom-pirate-fight-in-nebula]] (per raw/wiki/pirate-fight-in-nebula.md)
