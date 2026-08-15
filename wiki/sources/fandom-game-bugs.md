---
id: source-fandom-game-bugs
type: source
source_kind: wiki
raw: raw/wiki/game-bugs.md
game_version: both
date: 2026-08-15
ingested: 2026-08-15
reliability: medium
tags: [bugs, store, save-reload, beacon]
---

# Fandom — "Game bugs"

## Summary
The community bug list, retrieved at revision 74618. Fetched as the page
[[source-fandom-stores-and-resources]] defers to for store bugs. Most of it is combat
minutiae; the sector-level content is the save-reload family and one useful marker
distinction.

## Key Takeaways
- **The map distinguishes fixed stores from event stores.** On the vanishing-store bug:
  *"When an 'extra' store is generated as the outcome of an event, reloading causes the store
  to vanish. **This does not apply to the 'fixed' stores that are labelled on the map.**"*
  So the STORE label belongs to allocated store beacons; an event-spawned store is a
  different object with different persistence.
- **Reload rules of thumb**, stated as the practical guidance: finish any fight or event
  before exiting; reloading at a store re-rolls crew skills and forces Drone Control to come
  with a Defence Drone Mk 1; never reload at an event-generated store. The only reliably safe
  reload point is **the start beacon of a sector** — "there are no known bugs that occur there".
- **The "mixed event bug"**: reloading can produce an outcome taken at random from a *different*
  event — the example given is reloading at a store and losing a crewmember to Giant Alien
  Spiders.
- Leaving the store interface to fight boarders can also delete an event store.
- Corroborates the Zoltan-Shield-without-Shields pulsar bug noted in
  [[source-fandom-environmental-hazards]].

## Events Covered
- By reference: [[event-giant-alien-spiders]], [[event-improve-reactor-for-supplies]],
  [[event-rock-live-mine]].

## Other Pages Touched
- [[concept-stores]], [[concept-hazards]], [[concept-start-beacons]]

## Reliability Notes
`medium`, and uneven: entries range from well-evidenced (video/screenshot links) to
explicitly untested — several carry inline `[occurrence: undefined]` markers and
commented-out author notes asking for testing. Cite individual bullets, not the page.

## Contradictions Flagged
None.

## Links
- Source URL: https://ftl.fandom.com/wiki/Game_bugs
- [[source-fandom-stores-and-resources]], [[source-fandom-environmental-hazards]]
