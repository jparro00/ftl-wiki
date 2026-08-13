---
id: event-fleet-easy-again
type: event
event_name: FLEET_EASY_AGAIN
sectors: []
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [unreachable, cut-content, orphan, rebel-fleet, structural, engine-event, no-choice, combat]
---

# Rebel fleet takeover, repeat — `FLEET_EASY_AGAIN`

## Summary
The "you stayed too long *again*" event: a second Rebel scout jumping in on a beacon the
fleet already owns. **Its entire definition is commented out in `events.xml`**, so the event
does not exist in the shipped game — it is not merely unlisted, it is not parsed at all. It
is recorded here so the id resolves and so the gap in the `FLEET_EASY` family is documented.

## Trigger & Where It Appears
- **Cut. The `<event>` element itself is inside an XML comment**
  ([[source-events-xml]], events.xml lines 337–343):

  ```xml
  <!--
  <event name = "FLEET_EASY_AGAIN">
      <fleet>rebel</fleet>
      <text>Another ship approaches, the reinforcements seem endless! You must jump away!</text>
      <ship load = "LONG_FLEET" hostile ="true"/>
  </event>  -->
  ```

- This is stronger evidence than the usual "commented-out list entry" case: there is no
  definition for a list to point at. A search of every `.xml` finds the id **exactly once**,
  on that commented line. No `load=`, no `sector_data.xml` allocation, nothing.
- It sat between `FLEET_EASY_DLC` and `FLEET_EASY_BEACON` in the fleet-progression block, so
  it was written as part of that family and disabled in place.
- Had it been live it would have been a **structural event** the engine calls by name, like
  its siblings, rather than a sector-pool entry — hence `sectors: []`
  ([[concept-sector-event-allocation]]).
- **Version:** `both` in the trivial sense — `events.xml` is a base file with no DLC markers
  — but the event runs in neither edition.
- No Fandom page exists for it.

## Text
Written inline rather than as a `text_events.xml` id, which is itself a sign the event never
reached a shipping state — every live member of the family uses a localised string id:

> Another ship approaches, the reinforcements seem endless! You must jump away!

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none — the body is `<fleet>`, `<text>` and `<ship>`)* | — | Would have staged another `LONG_FLEET` hostile — the same elite Rebel scout used by [[event-fleet-easy]] and [[event-fleet-easy-beacon]]. | n/a |

Notably it does **not** carry `<environment type="PDS" target="player"/>`, which
[[event-fleet-easy]] and [[event-fleet-easy-dlc]] both do. Whatever it was for, it was not
meant to add a second planetary-defence barrage on top of the first.

## Blue Options
None.

## Rewards & Risks
Not applicable. It has no `autoReward` of its own; the `LONG_FLEET` hull's own blocks would
have applied.

## Strategy Notes
None — the event cannot occur. Repeatedly lingering on a fleet-held beacon re-triggers
[[event-fleet-easy]] / [[event-fleet-easy-dlc]], not this.

## Related
- [[event-fleet-easy]], [[event-fleet-easy-dlc]] — the live takeover events
- [[event-fleet-easy-beacon]], [[event-fleet-easy-beacon-dlc]] — the exit-beacon variants
- [[event-fleet-easy-nebula]] — the other unreachable member of the family
- [[event-fleet-hard]] — the escalated version
- [[entity-rebels]], [[concept-sector-event-allocation]]

## Open Questions
- [ ] What distinguished this from a second firing of `FLEET_EASY` — the prose implies a
      repeat trigger, but nothing in the data says the engine tracked repeats.
- [ ] Whether it predates or postdates the `_DLC` split of the family.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
