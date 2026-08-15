---
id: concept-oxygen-and-suffocation
type: concept
version: both
first_seen: 2026-08-14
last_updated: 2026-08-14
sources: 5
related_events: [[[event-slug-hacker-oxygen]], [[event-slug-hacker-choice]], [[event-terraforming-scan]], [[event-trade-scrap-for-upgrades]]]
tags: [mechanics, oxygen, suffocation, venting, breach, boarding, lanius, crystal]
---

# Oxygen and suffocation — the rates

## Definition & Context

Oxygen is the one system whose numbers appear **nowhere in `raw/gamedata/`**. `blueprints.xml`
gives the [[item-oxygen-system]] its power, cost and upgrade prices; `text_tooltips.xml` says
only *"Most crew need oxygen to live."* Every rate on this page therefore comes from outside the
game files — [[source-fandom-oxygen]] and [[source-xftl-oxygen-mechanics]] — and inherits their
`medium` reliability. That is a real step down from the rest of this wiki, and it is why the
page exists: to keep the numbers together with the caveat attached to them.

**The headline figure: suffocating crew take 6.4 HP per second**, starting at **≤5% O₂ in the
room they occupy** ([[source-fandom-oxygen]]).

## The rate table

Everything below is per second. Rates that both sources agree on are marked **✓✓**.

| Effect | Rate | Scope | Source |
|---|---|---|---|
| Crew suffocation damage | **6.4 HP/sec** | per crew member at ≤5% O₂ | Fandom only |
| Oxygen system unpowered / hacked | 1.2% ✓✓ | every room | both |
| Oxygen level 1 refill | 1.2% ✓✓ | every room | both |
| Oxygen level 2 refill | 4.8% (×4) ✓✓ | every room | both |
| Oxygen level 3 refill | 8.4% (×7) ✓✓ | every room | both |
| Hull breach | 8% ✓✓ | breached room, ×`0.75^distance` outward | xftl (Fandom: unquantified) |
| Lanius crew | 8% — *engine-identical to a breach* ✓✓ | same propagation | xftl |
| Open airlock door | 16% each | same propagation | xftl |
| Each fire | 0.96% ✓✓ | its own room only | both |
| Redistribution between open rooms | 8% of the gap to the chunk average | distance-independent | xftl |

**Level 1 exactly cancels the unpowered drain** — 1.2% against 1.2%. A level-1 Oxygen system
does not fight breaches, fires or airlocks at all; it only holds a sealed ship at equilibrium.
That single coincidence explains why the first 25-scrap upgrade feels so much larger than a
"+1 level" ought to.

## The modifiers

| Crew | Suffocation damage taken |
|---|---|
| Standard | 100% — 6.4 HP/sec |
| With [[item-emergency-respirators]] | 50% — 3.2 HP/sec |
| [[entity-crystal-men]] | 50% — 3.2 HP/sec |
| Crystal **+** Respirators | 25% — 1.6 HP/sec |
| [[entity-lanius]] | none — exempt, and drains instead |
| Anyone in a powered level-1 [[item-medbay]] | **none** — fully negated |
| Drones (crew / boarding) | none — no oxygen requirement |

The Respirators entry is the first time this wiki can say what the augment's
`<value>0.5</value>` in `dlcBlueprints.xml` is 0.5 *of*. It also works while boarding an enemy
ship ([[source-fandom-oxygen]]).

The Medbay line is the sharper one: **a powered level-1 Medbay makes its room immune to
suffocation entirely**, and level 2 heals through it. Venting the whole ship is survivable if
the crew are standing in the Medbay.

## How It Shows Up Across Sources

The two sources were fetched together and agree on everything they both cover, which is most of
it. Their division of labour is clean: Fandom has the crew-facing consequences (damage,
thresholds, AI behaviour, race modifiers), xftl has the engine model (the propagation rule, the
chunk model, the constants). Where they overlap they corroborate.

The one thing neither pins down is what this ingest was run for. **6.4 HP/sec rests on Fandom
alone** — xftl documents air, never crew health.

> ⚠️ **CONTRADICTION:** airlock speed. Fandom says an open airlock *"instantly drains the O₂ in
> the room it is opened in"* ([[source-fandom-oxygen]]). xftl reads 16%/sec per airlock door out
> of `OxygenSystem::ComputeAirLoss` ([[source-xftl-oxygen-mechanics]]) — fast, roughly six
> seconds for a full room, not instant. Trust xftl: it is reading the engine, and Fandom's own
> tactical advice (open *every* airlock to vent faster) presupposes a finite rate.

> ⚠️ **CONTRADICTION — and the game is the one that's wrong.** The ship upgrade menu advertises
> Oxygen refill multipliers of **1/3/6**. Both external sources independently state the real
> values are **1/4/7**, with xftl naming the UI figures explicitly as the incorrect ones. This
> is not source disagreement; it is a display bug in the shipped game. Level 3 is meaningfully
> better than the store claims.

## Implications For Play

- **Venting works because of the 5% floor, not because of zero.** Crew start dying at 5%, and
  boarders start *leaving* at 10% ([[source-fandom-oxygen]]) — so a room drifting down through
  10% pushes boarders out before it hurts them. Venting kills only what cannot path away.
- **The asymmetry is the whole tactic.** Redistribution ignores distance; breach loss decays at
  `0.75^distance`. So to *save* a breached room, close its neighbours and let air snake in from
  far away; to *vent* a room, open every airlock on the ship regardless of where they are. xftl
  measures the payoff: 3.5s versus 5.2s on the Kestrel teleporter.
- **Oxygen-2 is the real breakpoint.** At 4.8%/sec it counters a single breach or one Lanius
  (with doors managed), counters a Hacking-3 disruption pulse, and outpaces four fires — which
  means it also **prevents fires from dying out**, an occasionally unwanted side effect.
  Oxygen-3 beats a breach with all doors shut.
- **Jumping does not pause suffocation.** During an FTL jump the Oxygen system is ignored and
  rooms stop equalising, but airlocks, breaches and fires keep draining **and crew keep taking
  6.4 HP/sec** ([[source-fandom-oxygen]]). Jumping away from a boarding fight with a vented ship
  does not save the crew standing in the vacuum.
- **Fires and oxygen are coupled in both directions.** Fires eat 0.96%/sec each and die below
  10% O₂ — venting is the general fire answer ([[concept-solar-flares]], [[item-doors]]) — but a
  level-2 Oxygen system refills fast enough to keep feeding them.
- **The "O2 LOW!" warning is not the danger line.** It triggers on *ship-total* O₂ below 25%;
  crew die on *per-room* O₂ below 5%. A ship can show the warning with nobody at risk, or kill a
  crew member in one vented room while the total looks fine.

## Where It Applies

- [[item-oxygen-system]] — the system these rates belong to
- [[item-doors]] — airlocks and the door-management half of every tactic here
- [[item-emergency-respirators]], [[item-medbay]] — the two mitigations
- [[item-lanius-crew]] / [[entity-lanius]], [[entity-crystal-men]] — the two races with
  non-standard suffocation behaviour
- [[item-hacking]] — a Hacking-3 pulse on Oxygen is a drain that Oxygen-2 can outrun
- [[event-slug-hacker-oxygen]] — Oxygen offline, or halved via the blue option; the halving is
  now quantifiable
- [[event-slug-hacker-choice]] — the "choose suffocation" branch
- [[event-terraforming-scan]], [[event-trade-scrap-for-upgrades]] — the two events that upgrade
  Oxygen, now with a known payoff

## Related
- [[concept-crew-loss-risk]] — suffocation as a crew-loss vector
- [[concept-hazards]] / [[concept-solar-flares]] — fire, the other reason to vent
- [[concept-blue-options]] — the Oxygen-gated options

## Open Questions
- [ ] **Corroborate 6.4 HP/sec.** It is single-sourced. A timed run note in `raw/runs/` — vent a
      room, count seconds to death — would confirm it cheaply.
- [ ] **Time-to-death is not yet derivable.** At 6.4 HP/sec a 100-HP crew member would die in
      ~15.6s, but baseline crew HP is *not* directly sourced in this repo: it is inferred from
      [[item-rock-crew]]'s *"Max Health is increased to 150"*. Confirm the 100 baseline before
      quoting the 15.6s.
- [ ] Whether Rock crew's 150 HP extends survival proportionally (~23s), or whether the damage
      rate scales too.
- [ ] Whether enemy mind-controlled crew benefit from your Respirators — flagged as an untested
      `@to-do` on the Fandom page itself.
- [ ] The exact O₂ cut-off below which redistribution between rooms stops — also an open
      `@to-do` upstream.
- [ ] Whether the 1/3/6 UI display bug was ever patched; both sources may predate a fix.
- [ ] The fire-mechanics Pastebin cited by [[source-fandom-oxygen]] (https://pastebin.com/iP6EnKm4)
      was not retrieved — likely holds the fire/O₂ interaction in detail.

## Sources
- [[source-fandom-oxygen]] (per raw/wiki/oxygen.md)
- [[source-xftl-oxygen-mechanics]] (per raw/modding/2026-08-14-xftl-oxygen-mechanics.txt)
- [[source-blueprints]] (per raw/gamedata/blueprints.xml) — upgrade costs, corroborating
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml) — the Respirators 0.5 value
- [[source-text-tooltips]] (per raw/gamedata/text_tooltips.xml) — the non-answer that made this
  page necessary
