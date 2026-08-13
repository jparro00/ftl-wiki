---
id: event-rebel-fight-in-nebula
type: event
event_name: NEBULA_REBEL
sectors: [[[sector-civilian-sector]], [[sector-federation-space]], [[sector-pirate-controlled-sector]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]], [[sector-uncharted-nebula]], [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: nebula
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [nebula, rebel, no-choice, combat, unreachable, name-collision, shipped-but-dead]
---

# Rebel fight in nebula — `NEBULA_REBEL`

## Summary
Seven flavour texts and a Rebel ship — and the single most structurally important dead
event in the nebula file. `NEBULA_REBEL` is *also* the name of an eventList in
`events_rebel.xml`, and that list is what the game loads. Every `NEBULA_REBEL` entry
scattered through the nebula pools is therefore not a Rebel fight but a **re-roll into an
eleven-entry nebula table** — which is why so many nebula events reach so many sectors.

## Trigger & Where It Appears
- Referenced from `NEBULA` ([[source-newevents]]), `NEBULA_HOSTILE`
  ([[source-events-nebula]]), `NEBULA_PIRATE` ([[source-events-pirate]]),
  `NEBULA_ZOLTAN` ([[source-events-zoltan]]) and from the shadowing `NEBULA_REBEL`
  eventList itself.
- No `unique` attribute; `<environment type="nebula"/>` present.
- **The name collision.** `raw/gamedata/events_rebel.xml` line 78 defines
  `<eventList name="NEBULA_REBEL">` with eleven entries: `NEBULA_EMPTY`, **`NEBULA_REBEL`
  (itself)**, `NEBULA_AUTO`, `NEBULA_AUTO_WARNING`, `NEBULA_AUTO_DEFENSE_ITEM`,
  `NEBULA_TRADER`, `STORM_REBEL`, `STORM_AUTO`, `STORM_ITEMS`,
  `NEBULA_REBEL_UNDETECTED`, `NEBULA_LOST_SHIP`, `NEBULA_REBEL_BOARDING`
  ([[source-events-rebel]]). [[source-fandom-rebel-fight-in-nebula]] states the eventList
  wins over the event, so the fight *"can never happen"*.
- Note the **self-reference**: the list contains its own name, so rolling that entry
  re-enters the same table.

> As with [[event-pirate-fight-in-nebula]], the collision itself is verifiable in the game
> files; the resolution order is engine behaviour asserted only by Fandom (reliability
> `medium`). The `unreachable` tag depends on that assertion.

## Text
The prose comes from the `NEBULA_REBEL_LIST` text list and varies across seven strings
([[source-text-events-xml]]); all seven are transcribed on
[[source-fandom-rebel-fight-in-nebula]].

> A ship bearing Rebel colors can be seen waiting near the beacon. They must have been
> waiting for you, since they engage immediately.

> The Rebels must have anticipated you would try to lose them within the nebula. A scout is
> waiting for you at the beacon.

> Newton-knows what brings this Rebel ship so far out; its captain hails, but does a double
> take when he identifies your ship. They open fire.

Its first string, *"You cross paths with an advance scout of the Rebel fleet searching this
section of the nebula for your ship,"* is **byte-identical** to
`text_NEBULA_AUTO_LIST_1` used by [[event-auto-ship-fight-in-nebula]] — so that one line of
prose does still reach players, just from the other event.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(none — the event has no `<choice>` elements)_ | — | *If it ever fired:* immediate combat with a `REBEL` ship, default rewards. | n/a — the event is shadowed |

The `REBEL` ship definition ([[source-events-ships]]):
`<surrender chance="0.5" min="2" max="3" load="PIRATE_SURRENDER"/>`,
`<escape chance="0.5" min="3" max="4" load="PIRATE_ESCAPE"/>`,
`<destroyed load="DESTROYED_DEFAULT"/>` (`MED` / `standard`),
`<deadCrew load="DEAD_CREW_DEFAULT"/>`.

## Blue Options
None.

## Rewards & Risks
Not applicable in practice.

## Strategy Notes
- The knock-on effect matters more than the event does. Because `NEBULA_REBEL` appears in
  four separate nebula pools and resolves to an eleven-entry table each time, events such as
  [[event-auto-ship-fight-in-nebula]], [[event-auto-ship-warning-in-nebula]],
  [[event-trade-resources-in-nebula]] and [[event-plasma-storm-incapacitated-ships]] are
  reachable from far more sectors than their own list membership suggests. Any sector-reach
  figure for a nebula event has to be traced through this indirection.
- A player still fights plenty of Rebel ships at nebula beacons — via
  [[event-rebel-fight-in-plasma-storm]], [[event-rebel-fight-choice-in-nebula]] and
  [[event-rebel-fight-chance-in-nebula]] — just never through this event.

## Related
- [[event-pirate-fight-in-nebula]] — the identical name-collision bug
- [[event-rebel-fight-in-plasma-storm]], [[event-rebel-fight-choice-in-nebula]],
  [[event-rebel-fight-chance-in-nebula]] — the Rebel nebula fights that do fire
- [[concept-rebel-fleet-advance]], [[sector-uncharted-nebula]]
- [[event-pirate-surrender]] — the shared `PIRATE_SURRENDER` aftermath this hull loads
- [[event-pirate-escape]] — the shared `PIRATE_ESCAPE` aftermath this hull loads

## Open Questions
- [ ] Confirm the engine's event-vs-eventList resolution order from a non-Fandom source.
- [ ] Whether the self-referencing `NEBULA_REBEL` entry inside its own eventList can
      recurse indefinitely or is depth-limited.

## Sources
- [[source-events-nebula]] (per raw/gamedata/events_nebula.xml)
- [[source-events-rebel]] (per raw/gamedata/events_rebel.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-fandom-rebel-fight-in-nebula]] (per raw/wiki/rebel-fight-in-nebula.md)
