---
id: concept-asteroid-fields
type: concept
version: both
first_seen: 2026-08-13
last_updated: 2026-08-13
sources: 4
related_events: []
tags: [mechanics, environment, hazard, combat, defense-drone]
---

# Asteroid fields

## Definition & Context

`<environment type="asteroid"/>` — **14 uses** across the event files, the third most common
hazard after nebulae and Anti-Ship Batteries ([[source-events-xml]] and siblings). The engine's
own tooltip is the clearest statement of what it does ([[source-text-tooltips]]):

> *"You're in an asteroid field. Periodically asteroids will strike your ship."*

Unlike a nebula, an asteroid field does not disable anything. It simply adds a second source of
damage that neither ship can turn off, and it runs for as long as the fight does.

## How It Shows Up Across Sources

**Almost every asteroid event is an ordinary fight plus one line.** The pattern is consistent
enough to be a naming convention:

| Hazard event | Identical to | Adds |
|---|---|---|
| [[event-lanius-fight-in-asteroid-field]] | [[event-lanius-fight]] | `<environment type="asteroid"/>` |
| [[event-auto-ship-fight-in-asteroid-field]] | [[event-auto-ship-fight]] | the same |
| [[event-rock-fight-in-asteroid-field]] | [[event-rock-fight]] | the same |
| [[event-zoltan-fight-in-asteroid-field]] | the Zoltan fight | the same |

This is why the wiki carries so many near-duplicate combat pages — the game defines them
separately, so they are paged separately, with the hazard as the only difference.

**Asteroids are also a setting, not just a hazard.** A separate family of events uses asteroid
fields as scenery for non-combat encounters:
[[event-large-asteroid-field]] (the game's most widely distributed filler event),
[[event-dense-asteroid-field-distress]] (step 1 of [[chain-crystal-cruiser-unlock]], and the
beacon that can hand you the Damaged Stasis Pod), [[event-asteroid-belt-distress]],
[[event-crushed-pirate]] and [[event-asteroid-mining-colony]]. These carry no
`<environment>` tag — the asteroids are in the prose, not in the mechanics.

> The distinction matters when reading a page: **"asteroid" in a title does not imply the
> hazard.** Only the `<environment type="asteroid"/>` line does.

## Implications For Play

- **A Defense Drone Mark I shoots asteroids down.** This is the one hazard with a direct
  hard counter, which is most of why [[item-defense-drone-mark-i]] is valued —
  see [[item-defense-drone]].
- **Asteroid fights punish long engagements** in the same way every hazard does: the damage is
  time-based, so a slow attrition win costs hull the fast win does not.
- **Shields absorb asteroid hits**, so an unshielded ship — notably the
  [[entity-stealth-cruiser]], which starts with no shield system at all — is in real danger
  here in a way it is not in a nebula.
- Rock crew do not help. Asteroids cause hull and system damage, not fire, so
  [[entity-rock-men]]'s fire immunity is irrelevant — unlike at a
  [[concept-solar-flares]] beacon.

## Where It Applies
The four hazard fights listed above, plus [[event-rock-fight-with-boarders-in-asteroid-field]]
and [[event-rock-pirates-fight-in-asteroid-field]]. The non-hazard asteroid *settings* are
listed above and are much the larger group.

## Related
- [[concept-hazards]] — the parent page and the full six-type census
- [[item-defense-drone-mark-i]], [[item-defense-drone]] — the counter
- [[concept-solar-flares]] — the hazard that fire immunity *does* answer
- [[chain-crystal-cruiser-unlock]] — begins at an asteroid beacon
- [[entity-stealth-cruiser]] — the ship with most to fear here

## Open Questions
- [ ] The strike rate and damage per asteroid — unquantified anywhere in `raw/gamedata/`.
- [ ] Whether a Defense Drone intercepts asteroids at a stated rate or probabilistically.
- [ ] Whether asteroid damage can breach hulls or start fires, or only damage systems.
- [ ] Whether the enemy ship takes asteroid damage on the same schedule.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-events-rock]] (per raw/gamedata/events_rock.xml)
- [[source-text-tooltips]] (per raw/gamedata/text_tooltips.xml)
- [[source-text-misc]] (per raw/gamedata/text_misc.xml)
