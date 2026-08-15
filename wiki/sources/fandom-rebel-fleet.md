---
id: source-fandom-rebel-fleet
type: source
source_kind: wiki
raw: raw/wiki/rebel-fleet.md
game_version: both
date: 2026-08-15
ingested: 2026-08-15
reliability: medium
tags: [sector, rebel-fleet, pursuit, nebula, asb, routing]
---

# Fandom — "Rebel Fleet"

## Summary
The page for the pursuing fleet, retrieved at revision 73264. Short, and the densest
routing-relevant source in this batch: it enumerates every known modifier to the fleet
advance rate and every rule governing what happens on a beacon the fleet has taken.

## Key Takeaways
- **Baseline**: the fleet advances one step per jump you make. Its current extent is the
  red shading; the red "warning" line is where it will be after one more jump.
- **Advance-rate modifiers** (the routing payload):
  - a nebula beacon **in a non-nebula sector halves** that turn's advance;
  - a nebula beacon **in a nebula sector reduces it only by 1/5** — "the Rebel Fleet was
    prepared for the nebula" (also stated on [[source-fandom-sectors]] and
    [[source-fandom-environmental-hazards]]);
  - letting a Rebel scout or automated ship escape, or not jumping before it does,
    **doubles** the advance for one turn;
  - the Rebel *transport* ship does **not** accelerate pursuit;
  - hiring the Mercenary **delays** the advance by 2 turns;
  - Distraction Buoys **postpone** the start-of-sector advance by 1 turn;
  - other events add or subtract turns (the `Rebel Fleet Advancement Events` and `Rebel
    Fleet delay Rewards` categories).
- **Being caught**: fighting the Rebel Elite Fighter yields **1 fuel** and nothing else —
  no scrap, because the armada prevents salvage. The advice given is to disable its weapons
  and wait out the FTL charge rather than kill it.
- **Out of fuel** changes this: destroying the Elite Fighter then gives **4 fuel**. A glitch
  makes that beacon never an ion storm and repeatable for 4 fuel each visit.
- **Overtaking rewrites the beacon**: it replaces the previous event *and* any environmental
  hazard.
- **Nebula interaction**: a taken nebula beacon always gains an ion storm, **except** nebula
  exit beacons. Nebula beacons never have ASBs — unless you are out of fuel and *waiting*,
  in which case the nebula is stripped and an ASB appears.
- **ASB**: 3 hull damage plus a guaranteed breach, evadable (cloaking at 100% evasion is
  certain) or outrun by jumping first. **ASBs never occur at exit beacons on Easy.** Present
  whether or not AE content is on.

## Events Covered
- By reference only: the `Rebel Fleet advancement hazard`, `Rebel Fleet Advancement Events`
  and `Rebel Fleet delay Rewards` categories; [[event-rebel-transport-ship]],
  [[event-the-mercenary]].

## Other Pages Touched
- All of `wiki/sectors/`, [[concept-nebula-mechanics]], [[item-distraction-buoys]],
  [[entity-rebels]]

## Reliability Notes
`medium`. The 50% / 20% nebula figures are corroborated by two other Fandom pages in this
batch ([[source-fandom-sectors]], [[source-fandom-environmental-hazards]]) but by nothing
in `raw/gamedata/` — `sector_data.xml` carries no pursuit data at all. The
"halves"/"1/5" phrasing is loose about whether it scales the step or the distance; the page
does not resolve this.

## Contradictions Flagged
> ⚠️ **CONTRADICTION (internal, minor):** this page says a nebula beacon in a nebula sector
> "reduces the Rebel advance rate only partially (by 1/5 of regular beacon advance rate)",
> which reads as *cutting the advance to 1/5*. [[source-fandom-environmental-hazards]] and
> [[source-fandom-sectors]] both phrase the same rule as a **20% reduction** — i.e. leaving
> 80%. These are very different numbers and the wiki does not reconcile them. Nothing in
> `raw/gamedata/` settles it. Flagged unresolved.

## Links
- Source URL: https://ftl.fandom.com/wiki/Rebel_Fleet
- [[source-fandom-sectors]], [[source-fandom-beacons]],
  [[source-fandom-environmental-hazards]], [[source-fandom-stores-and-resources]]
