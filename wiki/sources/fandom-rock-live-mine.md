---
id: source-fandom-rock-live-mine
type: source
source_kind: wiki
raw: raw/wiki/rock-live-mine.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [rock, crew-risk, blue-option, bug-claim, clone-bay]
---

# Fandom — "Rock live mine"

## Summary
Community wiki page for `ROCK_STARSHIP_MINE`, retrieved via the MediaWiki API at revision
74671. The deepest choice tree of the Rock batch, fully transcribed including the Cut the
wire sub-page, plus two blue-option caveats and a confirmed code-typo bug.

## Key Takeaways
- **Names the in-game id**: *"This event is called 'ROCK_STARSHIP_MINE' in the
  datafiles."*
- Locations: Rock Controlled Sector, Rock Homeworlds; `LRSmap=noship`, `unique=true`.
- **Aggregates hull damage** where the game files split it across two `<damage>` tags:
  *"4 hull damage, 1 damage to a random system"* (files: `amount="3"` + a system damage)
  and *"6 hull damage, 1 damage with a breach to a random room"* (files: `amount="5"` +
  a breach). Both aggregates are consistent with system/room damage also costing hull.
  Recorded on [[event-rock-live-mine]].
- **Blue-option exclusions not in the game files** — the single most useful thing on the
  page, since `events_rock.xml` gives only opaque list names:
  - `WEAPONS_MISSILES`: *"bugged: Hull Missile doesn't count"*.
  - `COMBAT_BEAM_DRONE_LIST`: *"(Anti-Ship Fire Drone doesn't count)"*.
- **Confirmed code typo:** *"Due to a code error in the line `<item type="missile" min="-1"
  max="-1"/>` (instead of `missiles`) the missile weapon blue option does not waste a
  missile ammo."* The typo is directly verifiable in the game files; the consequence is
  Fandom's inference.
- Documents the **Clone Bay revival** on the wire-cut death, matching `<clone>true</clone>`
  in the files.
- Does **not** note that Red! and Blue! load the same event list — that finding comes from
  the game files alone.
- Categorised `Crew loss hazard`, `Clone Bay revival`, `Hull damage hazard`,
  `System damage hazard`, `Hull breach hazard`, `Missiles use Events`,
  `Drone Parts use Events`.

## Events Covered
- [[event-rock-live-mine]]

## Other Pages Touched
- [[item-engines]], [[item-missile-weapon]], [[item-beam-drone]], [[item-clone-bay]],
  [[concept-crew-loss-risk]]

## Reliability Notes
`medium`. No version stated — which matters here, because two of the damage tags are
marked `<!--DLC-->` in the game files. Fandom's damage totals match the **AE** values, so
the page is describing AE even though it does not say so.

## Contradictions Flagged
> ⚠️ Hull damage totals (4/6 aggregate vs. 3+1 / 5+1 split). Recorded on
> [[event-rock-live-mine]]; not a real disagreement, a difference in how damage is counted.

> ⚠️ Missile consumption typo — file confirms the typo, Fandom supplies the behaviour.

## Links
- Source URL: https://ftl.fandom.com/wiki/Rock_live_mine
- [[source-events-rock]], [[source-text-events-xml]]
