---
id: event-lanius-surrender
type: event
event_name: LANIUS_SURRENDER
sectors: [[[sector-abandoned-sector]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [surrender, aftermath, orphan, lanius, advanced-edition, shared-sub-event]
---

# Lanius surrender — `LANIUS_SURRENDER`

## Summary
The surrender offer made by the standard Lanius hull, and the **most generous offer rate in
the game**: `LANIUS_SHIP` declares `chance="0.2"`, an 80% surrender chance under
[[concept-surrender-offers]]. Almost every Lanius fight pushed to low hull ends with this
prompt. The prose is the best joke in the file — a species with no shared language
improvising surrender.

## Trigger & Where It Appears
- **Not in any sector event list.** Reached only through the ship block: `LANIUS_SHIP`
  declares `<surrender chance="0.2" min="3" max="4" load="LANIUS_SURRENDER"/>`
  ([[source-dlcevents-anaerobic]]).
- Per [[concept-surrender-offers]], `chance` is the probability the ship **keeps fighting**,
  so `chance="0.2"` is an **80% surrender chance** once hull falls into the `min=3 max=4`
  band. Fandom independently states 80 for this hull — one of the pairs that settled that
  concept page.
- Every hostile `LANIUS_SHIP` encounter can reach it ([[source-dlcevents-anaerobic]]):
  - [[event-lanius-fight]] (`LANIUS_FIGHT`)
  - [[event-lanius-fight-in-asteroid-field]] (`LANIUS_FIGHT_ASTEROID`)
  - [[event-lanius-fight-near-pulsar]] (`LANIUS_FIGHT_PULSAR`)
  - [[event-lanius-fight-distress]] — the `LANIUS_DISTRESS_TRAP` ambush
  - [[event-lanius-ship-absorbing-rebel-base]] (`LANIUS_GROUP_AUTO`), and the several events
    that stage `LANIUS_SHIP` non-hostile and can turn on you
    ([[event-lanius-ship-salvager]], [[event-lanius-powered-down-ship]],
    [[event-lanius-ship-absorbing-jump-beacon]], [[event-lanius-lone-ship]])
- **Version:** `ae`. It lives in `dlcEvents_anaerobic.xml`; the Lanius and their hulls do
  not exist in vanilla.
- Sector: the Lanius pools are the [[sector-abandoned-sector]] content set.
- No Fandom page joins this event directly; the community wiki renders it as the surrender
  template on each Lanius fight page.

## Text
`<text load="LANIUS_SURRENDER_TEXT"/>` — **seven distinct strings, no repeats, so 1/7
each** assuming uniform selection across list entries ([[concept-event-list-weighting]],
[[source-dlcevents-anaerobic]], [[source-text-events-xml]]):

> An image of a silent Lanius captain appears on your monitor. Images of their well-filled
> cargo hold follow. You come to the conclusion that they are trying to barter for a
> cease-fire.

> The Lanius ship hails you. Your translator struggles, spurting out "Prevent death...
> Merciful... Penitent...". You believe they are surrendering.

> You receive a hail from the ship followed by a crude translation device spurting, "Stop.
> Stop. Stop."

> You receive an image of their captain, silhouetted by the destruction aboard their ship.
> It bows forward with the metallic appendages about its body doing the same. It appears to
> be requesting mercy.

> Your comms system receives a video feed of the enemy ship's crew waving small makeshift
> white flags. It appears they have taken research about your culture's customs quite
> literally.

> You receive a message from the enemy ship that your translator struggles to interpret,
> "Penitence for metal. Offering intention."

> You receive a one word message from the enemy ship, "Surrender." You assume they are
> asking to surrender rather than demanding your surrender.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Accept their offer. | — | `<ship hostile="false"/>` — the fight ends — plus `<autoReward level="RANDOM">stuff</autoReward>`. | 100% |
| 2 | We will not accept surrender! | — | Empty `<event/>`; the fight continues. | 100% |

## Blue Options
None. Neither choice carries a `req` — notably, **no Lanius-crew blue option**, even though
the prose is built around the translation problem a Lanius crew member would solve.

## Rewards & Risks
- **Accepting:** one `RANDOM`-level `stuff` bundle; you forgo the `LANIUS_SHIP` hull's
  `LANIUS_DESTROYED` / `LANIUS_DEAD_CREW` payouts.
- **Refusing:** free.
- **Note the escape block.** `LANIUS_SHIP` also declares
  `<escape chance="0.2" min="2" max="4" load="LANIUS_ESCAPE"/>`. Refusing a surrender leaves
  a ship that may then jump away with the scrap you were about to take.

## Strategy Notes
- *Opinion:* at 80% this is the offer you can actually plan around. If you are damaged, or
  the Lanius boarders are draining your oxygen, taking it is a reliable exit — but the
  `RANDOM` `stuff` bundle is usually worse than the kill.
- The oxygen drain is the real argument for accepting: Lanius fights get worse the longer
  they last, unlike most hulls.

## Related
- [[event-lanius-fight]], [[event-lanius-fight-in-asteroid-field]],
  [[event-lanius-fight-near-pulsar]], [[event-lanius-fight-distress]] — the fights that
  lead here
- [[event-pirate-surrender]], [[event-rock-ship-surrender]], [[event-zoltan-surrender]] —
  the other species-specific surrender events
- [[entity-lanius]] — the faction
- [[sector-abandoned-sector]] — where Lanius hulls live
- [[concept-surrender-offers]] — why `chance="0.2"` is an 80% offer
- [[concept-event-list-weighting]] — basis for the 1/7 figures

## Open Questions
- [ ] What `RANDOM` `stuff` rolls in resources.
- [ ] Why no `req="anaerobic"` blue option, given the translation gag?
- [ ] Does refusing re-offer later in the same fight?

## Sources
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-fandom-lanius-fight]] (per raw/wiki/lanius-fight.md)
