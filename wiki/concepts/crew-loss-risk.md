---
id: concept-crew-loss-risk
type: concept
version: both
first_seen: 2026-08-13
last_updated: 2026-08-13
sources: 4
related_events: []
tags: [mechanics, crew, risk, clone-bay, away-teams, boarders]
---

# Crew-loss risk

## Definition & Context

Losing a crew member is the most expensive thing an FTL event can do to you short of ending the
run. Crew do not regenerate, they carry accumulated skill, and each one is a system you can no
longer staff.

The files express crew loss in exactly two ways ([[source-events-xml]] and siblings):

| Form | Uses | Meaning |
|---|---|---|
| `<removeCrew>` | 32 | a specific, scripted loss — usually an away team that does not come back |
| `<crewMember amount="-1"/>` | 5 | a signed decrement, the same tag used for gains |

Against **121 `<crewMember>` uses overall**, the great majority of which are gains. Crew loss is
rare, and that is what makes it memorable: [[event-giant-alien-spiders]] is the most notorious
event in the game because of one `<removeCrew>`.

## The Clone Bay decides most of them

**21 of the 32 `<removeCrew>` elements carry `<clone>true</clone>` and 11 carry
`<clone>false</clone>`** ([[source-events-xml]]). The value is not decoration — it decides
whether a [[item-clone-bay]] brings the crew member back.

> ⚠️ **A wrong reading of this cost the card pipeline a false claim.** The extractor originally
> set `clone` from the *presence* of a `<clone>` child, so all 32 read as revivable. But
> `<clone>false</clone>` exists and means the opposite: [[event-unknown-disease-on-mining-colony]]
> states in its own prose that *"it would be against Federation regulation to create a clone"*
> while the card promised a revive. Fixed on 2026-08-10; the spec had documented the
> presence rule, so spec and code agreed with each other and both disagreed with the game.

So a Clone Bay covers **roughly two-thirds** of scripted crew losses, not all of them. The
[[chain-rebel-defector]] murder is a `true` case; the mining-colony disease is a `false` one.

## The three ways crew die

1. **Away teams that do not come back.** The classic shape: an event offers to send a crew
   member somewhere, and one branch does not return them.
   [[event-giant-alien-spiders]], [[event-crystalline-research-facility]],
   [[event-crystalline-men-buried]], [[event-plagued-station]].
2. **Boarders.** **56 `<boarders>` elements** — 25 human, then slug and mantis at 6 each. These
   do not remove crew directly; they create a fight aboard your ship that may. Several arrive
   with **no enemy ship at all** and no choices, e.g.
   [[event-boarders-humans-in-nebula]], [[event-boarders-rockmen-near-sun]].
3. **Betrayal.** A crew member you gained turns on you — [[chain-rebel-defector]]'s entry 6,
   where the new recruit *"eviscerates the nearest crew-member"*, and `STATION_SICK`'s traitor.

## The signed-amount trap

`<crewMember amount="-1" class="traitor"/>` uses the *same tag* as a crew gain. The card
pipeline rendered it as **"+-1 traitor crew" in green** until 2026-08-10 — making a
Teleporter blue option look like a pure win when it costs a crewman. This was the fourth
sign-blind bug found in the effect table, after `autoReward` tiers, `modifyPursuit` and
resource ranges; the rule that came out of it is that **wherever a value's sign changes the
meaning, the vocabulary needs one entry per sense**.

## Implications For Play

- **A Clone Bay changes which events are safe**, but only for the two-thirds of losses that
  allow it. It is not a general licence to take away-team gambles.
- **Read the branch, not the flavour.** Events that *sound* dangerous frequently are not, and
  the pure-upside crew gains ([[event-crew-hiring-station]], [[chain-hidden-federation-base]]'s
  entry 2) outnumber the losses considerably.
- **Species matters for what a loss costs.** Losing the Engi on the
  [[entity-mantis-cruiser]] removes the ship's only competent repairer; losing one of four on
  the [[entity-federation-cruiser]] removes a capability outright.

## Where It Applies
The away-team events listed above, the 56 boarding events, and the betrayal cases. Event pages
carrying real crew-loss risk are tagged `crew-risk`.

## Related
- [[item-clone-bay]], [[item-medbay]] — the two answers, and only one of them applies here
- [[event-giant-alien-spiders]] — the archetype
- [[chain-rebel-defector]] — the betrayal case, with a `<clone>true</clone>`
- [[event-unknown-disease-on-mining-colony]] — the `<clone>false</clone>` counterpart
- [[concept-blue-options]] — most crew-risk events have a gate that removes the risk

## Open Questions
- [ ] Whether `<removeCrew>` picks the crew member randomly or by role.
- [ ] Whether a Clone Bay revive preserves accumulated skill levels.
- [ ] What the `traitor` and `ghost` crew classes are, mechanically — 2 and 1 uses respectively.
- [ ] Whether boarder counts scale with sector depth.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
