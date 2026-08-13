---
id: source-fandom-rock-war-vessel-encounter
type: source
source_kind: wiki
raw: raw/wiki/rock-war-vessel-encounter.md
game_version: unknown
ingested: 2026-08-09
reliability: medium
tags: [rock, ship-unlock, quest]
---

# Fandom — *Rock war vessel encounter*

## Summary
The FTL Fandom wiki page covering the **entire Rock Cruiser unlock quest** as one article:
the opening challenge in the Rock Homeworlds, the "Sun Quest Marker" fight beside an M-class
star, and the "Shipyard Quest Marker" payoff. Retrieved 2026-08-09, revision 73856.

## Key Takeaways
- Declares the datafile id as **"ROCK_UNLOCK"** in its Trivia section — a family name, not
  an exact id. The three stages map to `ROCK_UNLOCK1`, `ROCK_UNLOCK2` and `ROCK_UNLOCK3`.
- Confirms the sector: **Rock Homeworlds**, `unique`, LRS shows a ship.
- Confirms the Sun Quest Marker fight is the **Rock Assault (Elite)** hull, matching
  `auto_blueprint="ROCK_ASSAULT_ELITE"` in `events_ships.xml`, and states the escape
  countdown as **32 seconds** — matching `escape timer="32"`.
- States that the *"got away"* branch is the one that relays coordinates and adds the next
  quest marker; destroyed and dead-crew branches pay `MED` / `HIGH` scrap with resources and
  **end the chain**.
- Confirms the step-3 payoff: Rock Cruiser unlock, **Rock Plating** augment (glossed as
  *Titanium System Casing*), and 29 hull repairs.
- Also notes the Rock Cruiser can be unlocked by winning a run with the Slug Cruiser.

## Events Covered
- [[event-rock-unlock1]] — stage 1
- [[event-rock-unlock2]] — stage 2 (the Sun Quest Marker)
- [[event-rock-unlock3]] — stage 3 (the Shipyard Quest Marker)

## Other Pages Touched
- [[chain-rock-cruiser-unlock]]
- [[sector-rock-homeworlds]]
- [[entity-rock-men]]

## Contradictions Flagged
- **Hull repair — no conflict.** The page's *"29 repairs"* matches `<damage amount="-29"/>`
  exactly ([[source-events-rock]]). Recorded on [[event-rock-unlock3]] as corroboration.
- **Augment link anchor is wrong.** The reward is named *"Rock Plating"* but linked to
  `Augmentations#Titanium_System_Casing`. `ROCK_ARMOR` ("Rock Plating") and `SYSTEM_CASING`
  ("Titanium System Casing") are separate augments ([[source-blueprints]],
  [[source-text-blueprints]]). Flagged on [[event-rock-unlock3]]; the visible name is right.
- **Datafile id is imprecise.** Trivia says the event *"is called `ROCK_UNLOCK`"*; no such
  id exists — the datafiles use `ROCK_UNLOCK1` / `2` / `3` ([[source-events-rock]]). Flagged
  on [[event-rock-unlock1]].
- **Slug-Cruiser-victory unlock is unverified.** The lede claims the Rock Cruiser can also be
  unlocked by winning with the Slug Cruiser. `achievements.xml` contains no unlock-condition
  entries whatsoever ([[source-achievements]]), so this raw set neither supports nor refutes
  it. Recorded as Fandom-only on [[event-rock-unlock1]]. Same shape as the
  Zoltan-Cruiser-victory claim on [[event-legendary-thief-kazaaakplethkilik]].
- ~~[[event-rock-unlock1]] and [[event-rock-unlock3]] state that no Fandom page covers
  them.~~ **Resolved 2026-08-09** — both pages now cite this one.

## Links
- https://ftl.fandom.com/wiki/Rock_war_vessel_encounter
- raw/wiki/rock-war-vessel-encounter.md
