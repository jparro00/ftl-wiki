---
id: source-fandom-rebel-transport-ship
type: source
source_kind: wiki
raw: raw/wiki/rebel-transport-ship.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [rebel, timed-escape, item-reward, filler]
---

# Fandom — "Rebel transport ship"

## Summary
The community wiki page for `REBEL_TRANSPORT`. Retrieved via the MediaWiki API at revision
73819. Short, because it delegates the fifteen reward outcomes to a shared
`{{Pirate Smuggler / Rebel Transport}}` template — but its Trivia section carries three
useful mechanical claims.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'REBEL_TRANSPORT' in the datafiles."*
- Locations: Civilian Sector, Mantis Controlled Sector, Mantis Homeworlds, Rebel Controlled
  Sector, Rebel Stronghold, Slug Controlled Nebula, Slug Home Nebula, with
  `alsooccur=exitandfiller`, `LRSmap=ship`, `unique=true`. Omits
  [[sector-federation-space]].
- Cites the enemy as `SQUAT_TRANSPORT` in `events_ships.xml`, gives the escape timer as
  **40**, and states **no surrender** — matching the file.
- **Trivia claims, all consistent with the files:**
  - *"Despite the flavor text, this ship isn't generated any differently than any other
    Rebel ship."* — the blueprint is `SHIPS_REBEL`, same as every other Rebel ship.
  - *"The rewards given by this event are identical to those of Pirate smuggler ship."*
  - *"If the enemy escapes, the Rebel Fleet pursuit is **not** doubled."* — borne out by
    the absence of a `<gotaway>` block on `SQUAT_TRANSPORT`.
- Categorised `Random_Events`, `Unique_Events`, `Filler_Events`, `Ship escape Events`.

## Events Covered
- [[event-rebel-transport-ship]]

## Other Pages Touched
- [[event-rebel-ship-warning]], [[concept-rebel-fleet-advance]]

## Reliability Notes
`medium`. Version unstated. Everything it asserts checks out against `events_ships.xml`.
The reward tables themselves live behind a template, so this page is not the transcription
source for `REBEL_TRANSPORT_DESTROYED` / `REBEL_TRANSPORT_CAPTURED` —
[[source-events-rebel]] is.

## Contradictions Flagged
- Sector reach narrower than the event lists support.

## Links
- Source URL: https://ftl.fandom.com/wiki/Rebel_transport_ship
- [[source-events-rebel]], [[source-events-ships]], [[source-text-events-xml]]
