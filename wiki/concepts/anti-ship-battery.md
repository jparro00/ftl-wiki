---
id: concept-anti-ship-battery
type: concept
version: both
first_seen: 2026-08-13
last_updated: 2026-08-13
sources: 4
related_events: []
tags: [mechanics, environment, hazard, pds, asb, one-sided]
---

# The Anti-Ship Battery — the `PDS` hazard

## Definition & Context

`<environment type="PDS"/>` — **16 uses**, the second most common hazard after nebulae
([[source-events-xml]] and siblings). A planet-side gun fires on ships at the beacon. The
files call it `PDS`; the engine's player-facing strings call it an **ASB** (Anti-Ship Battery),
and the wiki uses the player-facing name.

It is the **only hazard that can be one-sided**: 8 of the 16 uses carry `target="player"`,
meaning the battery shoots at you and not at your opponent. That makes it less an environment
than a third participant, and it is the only `target` attribute in the hazard system.

## What the game tells the player

There is **no in-fight tooltip** for `PDS` — unlike the other five hazards. Instead it is
announced on the **map, before you jump** ([[source-text-misc]]):

> *"Planet-side anti-ship batteries are detected in this system."*
>
> *"The fleet's anti-ship batteries will be firing on you at this location."*

and in-fight by two warnings rather than a description:

> **`ASB TARGET LOCKED!`** · **`ALLIES!`**

The map-first design fits a hazard that is genuinely avoidable: you can see an ASB beacon
coming and route around it, which is not true of a hazard revealed on arrival.

## The `ALLIES!` case

`warning_pds_allies` exists because the battery is not always hostile.
[[event-lanius-fight-with-friendly-asb-support]] is **the one encounter where the planetary
battery fires at your enemy instead of at you** — the mirror image of `target="player"`, and
the only place in the game where a hazard is an advantage.

The Rebel fleet also fields ASBs: `map_pds_fleet` describes batteries belonging to the fleet
rather than a planet, which is how the hazard appears in [[sector-rebel-stronghold]] and
during the endgame.

## Implications For Play

- **It is the most avoidable hazard.** Being map-announced means the decision happens at
  routing time, not in the fight. Where a beacon is optional, an ASB beacon is a good one to
  skip.
- **`target="player"` beacons are strictly bad.** There is no upside and no counterplay beyond
  winning quickly — the battery does not care about the fight's state.
- **It stacks with quest pressure.** [[chain-construction-yard]]'s Rebel-station fight adds
  `<environment type="PDS" target="player"/>` to an already hard engagement, and the quest
  gives you no way to see it coming.
- Cloaking is the one system that plausibly interacts with a targeted battery, but **no source
  in this repo establishes that it does.**

## Where It Applies
[[event-rebel-auto-pds]], [[event-rebel-pds]],
[[event-lanius-fight-with-friendly-asb-support]] (the friendly case),
[[chain-construction-yard]]'s first destination, and
[[event-space-station-under-construction]]'s follow-up. [[event-abandoned-station]] references
an ASB in prose without carrying the tag.

## Related
- [[concept-hazards]] — the parent page and the full six-type census
- [[event-lanius-fight-with-friendly-asb-support]] — the friendly-battery encounter
- [[chain-construction-yard]] — a quest that drops you into a targeted one
- [[sector-rebel-stronghold]] — where fleet batteries appear
- [[entity-rebels]]

## Open Questions
- [ ] Fire rate and damage per shot — unquantified anywhere in `raw/gamedata/`.
- [ ] Whether Cloaking prevents an ASB lock, as it does an enemy weapon lock. Plausible and
      widely assumed, but **not established by any source here**.
- [ ] Whether shields reduce ASB damage as they reduce solar-flare fires.
- [ ] Whether `ALLIES!` can fire at *both* ships, or only ever at one.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-text-misc]] (per raw/gamedata/text_misc.xml)
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml)
