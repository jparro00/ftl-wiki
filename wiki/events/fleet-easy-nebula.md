---
id: event-fleet-easy-nebula
type: event
event_name: FLEET_EASY_NEBULA
sectors: []
beacon_type: unknown
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [nebula, plasma-storm, rebel-fleet, orphan, unreachable, no-choice, combat]
---

# Fleet takeover (nebula) — `FLEET_EASY_NEBULA`

## Summary
The nebula version of the "the Rebel fleet has caught you" fight. Fully authored — its own
prose string, an elite fleet ship, a plasma-storm environment — but **no file in
`raw/gamedata/` references it**. Its only appearance outside its own definition is in the
header comment of `events_nebula.xml`. Recorded here because it is shipped content, not
because it can be played.

## Trigger & Where It Appears
- **Orphan.** It is in no event list, no sector allocation, and no `load=` anywhere in
  `raw/gamedata/`. A grep for `FLEET_EASY_NEBULA` across every XML file returns only its
  own definition (`events_nebula.xml` line 97), the file's summary comment (line 16), and
  its text string in `text_events.xml` ([[source-events-nebula]],
  [[source-text-events-xml]]).
- **No Fandom page joins it** — the slug here comes from the in-game id.
- The XML comment above it states the intent: *"for when the fleet takes over a nebula
  beacon"* ([[source-events-nebula]]).
- The siblings that *do* handle fleet takeover all live in `events.xml` and all carry a
  `<fleet>rebel</fleet>` element that `FLEET_EASY_NEBULA` **lacks**
  ([[source-events-xml]]):

  | Event | `<fleet>` | Environment | Text |
  |---|---|---|---|
  | `FLEET_EASY` | `rebel` | `PDS` on the player | *"The Rebel fleet has found you, and a nearby scout turns to engage…"* |
  | `FLEET_EASY_DLC` | `rebel` | `PDS` on the player | identical string to `FLEET_EASY` |
  | `FLEET_EASY_BEACON` | `rebel` | none | *"You've found the exit beacon but the Rebels got here first!"* |
  | `FLEET_EASY_BEACON_DLC` | `rebel` | `PDS` on the player | identical string to `FLEET_EASY_BEACON` |
  | `FLEET_HARD` | `rebel` | — | *"The Rebel fleet has found you, and a nearby scout turns to engage. You must flee before their cruisers open fire!"* |
  | **`FLEET_EASY_NEBULA`** | **absent** | `storm` | its own unique string |
  | `FLEET_EASY_AGAIN` | `rebel` | — | **entire event commented out** |

  The missing `<fleet>` element is the strongest single piece of evidence that this event
  is not wired into the fleet-takeover machinery, whatever the comment intended.

Tagged `unreachable` per the shipped-but-unlisted rule. If the engine loads it by hardcoded
name when the fleet claims a nebula beacon, that would make it live — but nothing in
`raw/gamedata/` says so, and the missing `<fleet>` tag argues against it.

## Text
> An advanced Rebel hunter easily found your ship. You can't see it through the nebula, but
> you can assume the fleet is right on top of you. You need to escape quickly.

(`event_FLEET_EASY_NEBULA_text`, per [[source-text-events-xml]]. Unlike the `_DLC` variants
of its siblings, this string is unique — it is not a copy of any other fleet text.)

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(none — the event has no `<choice>` elements)_ | — | *If it ever fired:* immediate combat with `LONG_FLEET`, inside `<environment type="storm"/>`. | n/a — not referenced anywhere |

The `LONG_FLEET` ship, from `events_ships.xml` on the `SHIPS_REBEL_ELITE` blueprint pool
and marked `<!-- NEEDS ELITE BLUEPRINT -->` ([[source-events-ships]]):

- `<destroyed>` → `<item_modify><item type="fuel" min="1" max="1"/></item_modify>` — **+1
  fuel and nothing else**. No scrap, no `autoReward`.
- `<deadCrew>` → the identical +1 fuel.
- No surrender, no escape.

That reward shape is the tell that this is a survival encounter rather than a loot one: an
elite Rebel ship that pays a single unit of fuel is meant to be fled, not farmed. The
prose agrees — *"You need to escape quickly."*

## Blue Options
None.

## Rewards & Risks
- Reward if killed: **+1 fuel.**
- Risk: an elite Rebel warship in a plasma storm with sensors down, and by the framing of
  the event, more of them behind it.

## Strategy Notes
- Not applicable — the event is not reachable through any path recorded in the game files.
- Documented so the nebula event pool is complete and so the orphan is visible rather than
  quietly dropped.

## Related
- [[event-rebel-fight-in-plasma-storm]] — the reachable storm fight against a normal Rebel
  ship
- [[event-auto-ship-warning-in-nebula]] — the nebula event that *causes* fleet advance
- [[concept-rebel-fleet-advance]], [[concept-rebel-fleet-advance]]
- [[event-fleet-easy-again]] — the other commented-out member of the family

## Open Questions
- [ ] Does the engine load `FLEET_EASY_NEBULA` by hardcoded name when the Rebel fleet takes
      a nebula beacon? Nothing in `raw/gamedata/` references it, and it lacks the
      `<fleet>rebel</fleet>` element its siblings all carry.
- [ ] Was the missing `<fleet>` element an oversight, or is it absent because the engine
      supplies the fleet context itself in this case?
- [ ] Whether any FTL build ever used it.

## Sources
- [[source-events-nebula]] (per raw/gamedata/events_nebula.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
