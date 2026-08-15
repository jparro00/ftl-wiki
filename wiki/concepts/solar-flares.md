---
id: concept-solar-flares
type: concept
version: both
first_seen: 2026-08-13
last_updated: 2026-08-13
sources: 4
related_events: []
tags: [mechanics, environment, hazard, fire, rock-crew, shields]
---

# Solar flares — the `sun` hazard

## Definition & Context

`<environment type="sun"/>` — **7 uses**, the second rarest hazard in the game
([[source-events-xml]] and siblings). The engine's tooltip is unusually informative
([[source-text-tooltips]]):

> *"You're too close to a star. Solar flares will light the ship on fire. **Shields will reduce
> the effect.**"*

That last clause is **the only stated interaction between a hazard and a system anywhere in
`raw/gamedata/`** — every other hazard's tooltip describes an effect with no mitigation.

The map warning is separate ([[source-text-misc]]): *"Beacon coordinates appear to be very
close to a nearby sun."*, and in-fight the engine prints **`SOLAR FLARE IMMINENT!`** — a
warning, which makes this the one hazard you get advance notice of within the fight.

## How It Shows Up Across Sources

The sun events divide into two groups.

**Ordinary fights with a star added** — the same pattern as [[concept-asteroid-fields]]:
[[event-auto-ship-fight-near-sun]], [[event-mantis-fight-near-sun]],
[[event-boarders-humans-near-sun]], [[event-boarders-rockmen-near-sun]],
[[event-rock-pirates-fight-near-sun]].

**One fight where the star is the point:** [[event-rock-unlock2]], step 2 of
[[chain-rock-cruiser-unlock]]. The Rockmen challenge you to a duel beside an M-class star
specifically to see whether you can take the heat — *"Let's see how long your puny ship can
handle this heat!"* — and the chain's win condition is to **survive the flares for a
32-second escape timer without killing the enemy**. It is the only place in the game where a
hazard is the test rather than a complication.

## Implications For Play

- **Fire is the whole effect.** Flares do not damage hull or systems directly; they start
  fires, and the fires do the damage. That makes the counters different from every other
  hazard: door control, venting to space, and crew who can fight fires safely.
- **[[entity-rock-men]] are immune to fire.** A Rock crew turns this hazard from a crisis into
  a chore, which is exactly the irony of [[event-rock-unlock2]]: the ship you are trying to
  earn — the [[entity-rock-cruiser]], crewed entirely by Rockmen — is the ship that would find
  the test easy.
- **Shields reduce the effect**, per the tooltip. A ship that has invested in shields takes
  fewer fires, which makes the unshielded [[entity-stealth-cruiser]] the worst ship to meet a
  sun beacon in.
- **Venting is the general answer.** Open the doors to space and the fire goes out, at the cost
  of oxygen — see [[item-doors]].

## Where It Applies
The five ordinary sun fights above, plus [[event-rock-unlock2]]. Sun beacons appear
disproportionately in Rock space, which is thematically deliberate and mechanically an odd
choice — it is the sector whose natives care least.

## Related
- [[concept-hazards]] — the parent page and the full six-type census
- [[chain-rock-cruiser-unlock]] — the chain built around surviving one
- [[entity-rock-men]] — fire immunity
- [[entity-rock-cruiser]] — the fire-immune crew you win for passing the fire test
- [[item-doors]] — venting as the general fire answer
- [[concept-asteroid-fields]] — the hazard fire immunity does *not* answer

## Open Questions
- [ ] The flare interval and how many fires each starts — unquantified in `raw/gamedata/`.
- [ ] How much *"shields will reduce the effect"* reduces it, and whether shield **level**
      matters or merely having shields up.
- [ ] Whether the enemy ship catches fire on the same schedule — [[event-rock-unlock2]]'s
      Open Questions raise the possibility that flares could destroy the enemy hull for you and
      break the chain by accident.
- [ ] Whether the `SOLAR FLARE IMMINENT!` warning gives a fixed lead time.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-events-rock]] (per raw/gamedata/events_rock.xml)
- [[source-text-tooltips]] (per raw/gamedata/text_tooltips.xml)
- [[source-text-misc]] (per raw/gamedata/text_misc.xml)
