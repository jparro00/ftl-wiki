---
id: source-fandom-environmental-hazards
type: source
source_kind: wiki
raw: raw/wiki/environmental-hazards.md
game_version: both
date: 2026-08-15
ingested: 2026-08-15
reliability: medium
tags: [sector, hazard, nebula, pulsar, asb, asteroid, solar-flare]
---

# Fandom — "Environmental Hazards"

## Summary
The mechanics page for beacon hazards, retrieved at revision 74893. Covers red giants,
asteroid fields, pulsars, nebulas, ion/plasma storms and Anti-Ship Batteries, with
quantified timings and damage rules. It is the source for what a nebula actually does to a
run, which the sector pages currently list as an open question.

## Key Takeaways
- **Nebula**: disables Sensors entirely; Slug crew or the Lifeform Scanner still see enemy
  crew. Slows Rebel pursuit "by 50% in most sectors and by 20% inside nebula sectors".
  Nebulas do **not** count as an environmental hazard for the Tactical Approach achievement.
- **Ion/plasma storm**: reactor runs at half capacity (rounded up); Zoltan power and Backup
  Battery are unaffected. Power is stripped automatically on arrival, which can drop your
  shields — leave spare reactor before jumping. The enemy reactor is halved too and they
  will re-allocate mid-fight.
- **A fleet-taken nebula beacon always has an ion storm; a taken nebula *exit* beacon never
  does.** (Same rule as [[source-fandom-rebel-fleet]].)
- **ASB**: 3 damage, shield-piercing, always breaches, hits a random room; evadable but not
  shootable. Bypasses Zoltan Shields. First warning 15–20s after the fight starts, real shot
  5–10s later, cycling indefinitely; most visible shots are cosmetic fakes. Always present
  when the fleet overtakes you **except** at a nebula beacon or at the exit on Easy.
- **Red giant**: flare every 28–34s with a 5s warning. Shields up → 1–2 fires; shields down
  → 3–6 fires. Extra shield layers do not help. Each fire-bearing room has 33% (1 fire) or
  66% (2 fires) chance of 1 hull+system damage.
- **Pulsar**: **AE content only.** Ion pulse every 11–18s with 5s warning; ionises 2 systems
  on each ship for `1 + floor(0.5 × system power)`. Shields are always one of the two if
  powered — so depowering shields just before the pulse limits the damage. A single Zoltan
  Shield layer absorbs the whole pulse; but a Zoltan Shield on a ship with **no shield
  system** is ignored (stated as likely a bug). Reverse Ion Field makes it 2 or 0, never 1;
  two stacks give full immunity.
- **Asteroid field**: 1 shield layer or 1 hull+system damage per hit, small fire/breach
  chance, same effect on the enemy. Interval **scales with your own shield system level** —
  a highly upgraded shields system means more frequent asteroids, and the rate does not drop
  when your shields are knocked down, which makes enemy ion weapons especially dangerous here.
- **Hazard persistence**: a hazard beacon with no hostile ship loses its hazard on revisit —
  except a plain nebula, or a beacon the Rebels have taken.
- **`IN DANGER` lockout**: solar flares, asteroids, pulsars and ASBs block the ship menu, so
  no upgrades, no cargo swaps, no crew management while you sit there.

## Events Covered
- By reference: the `Red Giant`, `Asteroid Field`, `Pulsar`, `Nebula`, `Plasma Storm`,
  `Anti-Ship Battery hazard risk` and `Anti-Ship Battery support` categories, plus roughly
  20 named hazard-fight events already in `wiki/events/`.

## Other Pages Touched
- [[concept-nebula-mechanics]], [[sector-uncharted-nebula]], [[sector-slug-controlled-nebula]],
  [[sector-slug-home-nebula]], [[item-sensors]], [[item-reverse-ion-field]]

## Reliability Notes
`medium`, but higher than typical for this wiki: the flare and asteroid sections cite
reverse-engineered data (xftl), and the numbers are specific rather than remembered. The
pulsar AE-only restriction is consistent with `dlcEvents.xml` carrying the pulsar events.

## Contradictions Flagged
> ⚠️ **CONTRADICTION:** nebula-sector pursuit reduction. This page says nebulas slow the
> fleet "by 50% in most sectors and by 20% inside nebula sectors" — a *20% reduction*.
> [[source-fandom-rebel-fleet]] words the identical rule as reducing the rate "by 1/5 of
> regular beacon advance rate", which reads as reducing it *to* 20%. Unresolved; no game
> file in `raw/` carries pursuit rates.

## Links
- Source URL: https://ftl.fandom.com/wiki/Environmental_Hazards
- [[source-fandom-rebel-fleet]], [[source-fandom-sectors]], [[source-fandom-sensors]]
