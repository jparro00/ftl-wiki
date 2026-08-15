---
id: concept-hazards
type: concept
version: both
first_seen: 2026-08-13
last_updated: 2026-08-13
sources: 4
related_events: []
tags: [mechanics, environment, combat, beacon-types, parent-page]
---

# Beacon hazards — the `<environment>` tag

## Definition & Context

A hazard is one XML element: `<environment type="X"/>` on an event. It changes the conditions
a fight happens under without changing the fight itself — the same enemy hull, the same
choices, a different beacon.

There are **exactly six types and 91 uses** across the event files, and the whole system is
that closed set ([[source-events-xml]] and siblings):

| Type | Uses | What it does | Detail page |
|---|---|---|---|
| `nebula` | 42 | sensors stop working; the Rebel fleet advances more slowly | [[concept-nebula-mechanics]] |
| `PDS` | 16 | a planetary Anti-Ship Battery fires on ships at the beacon | [[concept-anti-ship-battery]] |
| `asteroid` | 14 | rocks strike both ships throughout the fight | [[concept-asteroid-fields]] |
| `storm` | 8 | plasma storm — your reactor output is halved | [[concept-nebula-mechanics]] |
| `sun` | 7 | solar flares set fires periodically | [[concept-solar-flares]] |
| `pulsar` | 4 | EM pulses disrupt systems | — |

**The engine states five of the six in its own words.** `text_tooltips.xml` carries the
in-beacon tooltip for each, which is the most authoritative description this repo holds —
it is what the game tells the player ([[source-text-tooltips]]):

> **asteroid** — *"You're in an asteroid field. Periodically asteroids will strike your ship."*
>
> **sun** — *"You're too close to a star. Solar flares will light the ship on fire. **Shields
> will reduce the effect.**"*
>
> **pulsar** — *"You're close to a pulsar. Periodic waves of electromagnetic energy will
> disrupt your systems."*
>
> **nebula** — *"You're inside a nebula. Your sensors will not function, but the Rebel fleet
> will advance more slowly towards you."*
>
> **storm** — *"This section of the nebula is experiencing a plasma storm. Your main reactor
> can only function at half capacity."*

`PDS` has no tooltip; it is described on the **map** instead, which fits a hazard you are meant
to see before you jump ([[source-text-misc]]):

> *"Planet-side anti-ship batteries are detected in this system."* · *"The fleet's anti-ship
> batteries will be firing on you at this location."*

The sun tooltip's *"Shields will reduce the effect"* is the only interaction between a hazard
and a system stated anywhere in the files.

## The `target` attribute

Eight of the 16 `PDS` uses carry `target="player"` — the battery shoots **only at you**. This
is the one hazard that can be one-sided, and it is the difference between a hazard and a second
enemy. The reverse case exists too, as an event rather than an attribute:
[[event-lanius-fight-with-friendly-asb-support]] is the single encounter where the battery
fires at your opponent instead.

## How It Shows Up Across Sources

- **A hazard is a property of the beacon, not the enemy.** The great majority of hazard events
  are ordinary fights with one line added — [[event-lanius-fight-in-asteroid-field]] and
  [[event-lanius-fight-near-pulsar]] are byte-for-byte identical to
  [[event-lanius-fight]] except for the `<environment>` line. This is why the wiki has so many
  near-duplicate combat pages: the game genuinely defines them separately.
- **Hazards stack with everything.** Nothing in the schema prevents a hazard on an event that
  also has boarders, a quest marker or a store.
- **A hazard is not always announced in the prose.** [[chain-construction-yard]]'s Rebel
  station fight adds `<environment type="PDS" target="player"/>` and mentions it only in the
  choice text; other events say nothing at all.

## Implications For Play

- **Hazards punish slow kills.** Every one of the six does damage or degrades you over time, so
  the ship that wins fast takes less of it. This is the mechanical argument against attrition
  builds in hazard-heavy sectors.
- **Crew species matter more here than anywhere else.** [[entity-rock-men]] are immune to fire,
  which is most of what `sun` does; [[entity-lanius]] do not breathe, which changes how hull
  breaches play out.
- **Some hazards are why a blue option exists.** Sensors gates cluster around `nebula` events,
  because that is where sensors stop working — see [[concept-nebula-mechanics]].

## Where It Applies
Every event whose page carries a **Hazard** note. The largest families are the nebula and
plasma-storm events ([[concept-nebula-mechanics]] enumerates them), the asteroid-field fights
([[concept-asteroid-fields]]), and the sun fights ([[concept-solar-flares]]).

## Related
- [[concept-nebula-mechanics]] — nebula and storm, the two commonest, documented in depth
- [[concept-asteroid-fields]], [[concept-solar-flares]], [[concept-anti-ship-battery]]
- [[concept-event-tree-grammar]] — where `<environment>` sits in the grammar
- [[concept-sector-event-allocation]] — which sectors draw hazard-bearing events

## Open Questions
- [ ] **Pulsar has no page of its own** — 4 uses, and the tooltip's *"disrupt your systems"* is
      the most precise statement available. Which systems, and how, is unrecorded.
- [ ] The damage rate of each hazard, in any unit. None of the six is quantified anywhere in
      `raw/gamedata/` — only the sun's shield interaction is even qualitatively described.
- [ ] Whether `target="player"` exists for hazards other than `PDS` (8 of 16 PDS uses carry it;
      no other type does in this build).
- [ ] Whether hazards affect enemy ships symmetrically when `target` is absent.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-events-nebula]] (per raw/gamedata/events_nebula.xml)
- [[source-text-tooltips]] (per raw/gamedata/text_tooltips.xml)
- [[source-text-misc]] (per raw/gamedata/text_misc.xml)
