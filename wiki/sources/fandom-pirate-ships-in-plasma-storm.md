---
id: source-fandom-pirate-ships-in-plasma-storm
type: source
source_kind: wiki
raw: raw/wiki/pirate-ships-in-plasma-storm.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [zoltan, plasma-storm, fuel-reward, missile-reward]
---

# Fandom — "Pirate ships in plasma storm"

## Summary
The community wiki page for `STORM_ZOLTAN_SUPPLY_CHOICE`. Retrieved via the MediaWiki API
at revision 73778. The game file for this event ends at the two ship loads; every reward
figure here comes from Fandom.

## Key Takeaways
- **Names the in-game id explicitly**: *"This event is called
  'STORM_ZOLTAN_SUPPLY_CHOICE' in the datafiles."*
- **Supplies what the game files do not:** the win-condition reward split, which is the
  whole point of the event.
  - Fuel path: `low` (glossed **1–3 fuel**) if destroyed, `high` (glossed **3–6 fuel**)
    if you kill the crew and leave the hull intact.
  - Ammo path: `low` (glossed **1–2 missiles**) if destroyed, `high` (glossed
    **4–8 missiles**) if the hull survives.
- States both enemy ships have a **50% escape-attempt chance at 20–40% hull and never
  surrender** — the main way the beacon fails to pay out.
- Carries HTML comments naming the ship blueprints (`STORM_PIRATE_SUPPLY_FUEL`,
  `STORM_PIRATE_SUPPLY_AMMO`) and their source file (`events_ships.xml`).
- Locations template: both Zoltan sectors, `plasmastorm=true`, `unique=true`, Long-Ranged
  Scanners `noship+plasmastorm`.
- Categorised `Fuel reward opportunity`, `Missiles reward opportunity`,
  `Pirate ship fights`.

## Events Covered
- [[event-pirate-ships-in-plasma-storm]]

## Other Pages Touched
- [[entity-pirates]], [[concept-nebula-mechanics]]

## Reliability Notes
`medium`. States no game version. The bracketed numeric ranges (1–3, 3–6, 1–2, 4–8) are
the wiki's own gloss on the `low`/`high` reward tiers and are **not** stated in the game
files — recorded on the event page as Fandom's figures rather than as data.

## Contradictions Flagged
None. Intro, choice, and outcome texts match `text_events.xml` where they overlap.

## Links
- Source URL: https://ftl.fandom.com/wiki/Pirate_ships_in_plasma_storm
- [[source-events-zoltan]], [[source-text-events-xml]]
