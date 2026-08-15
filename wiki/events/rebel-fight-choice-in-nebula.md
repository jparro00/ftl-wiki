---
id: event-rebel-fight-choice-in-nebula
type: event
event_name: NEBULA_REBEL_UNDETECTED
sectors: [[[sector-civilian-sector]], [[sector-federation-space]], [[sector-pirate-controlled-sector]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]], [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]], [[sector-uncharted-nebula]], [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: nebula
hostile: false
blue_options: [[[item-cloaking]], [[item-engines]]]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 10
tags: [nebula, rebel, blue-option, cloaking, engines, fleet-advance, optional-fight, unique]
---

# Rebel fight choice in nebula — `NEBULA_REBEL_UNDETECTED`

## Summary
A Rebel picket is waiting for you and hasn't seen you yet. Attack, hide, or cloak. Hiding
is a three-way roll whose worst branch advances the fleet — but its *first* branch drops
you into a second decision where high-level Engines get you out clean. Cloaking skips the
whole tree.

## Trigger & Where It Appears
- Beacon: nebula (`<environment type="nebula"/>`).
- `unique="true"` — once per run.
- Lists: `NEBULA_NEUTRAL`, `NEBULA_NEUTRAL_SLUG`, `NEBULA_PIRATE`, `NEBULA_REBEL`
  ([[source-events-nebula]], [[source-events-slug]], [[source-events-pirate]],
  [[source-events-rebel]]) — the second-widest reach in the file after
  [[event-nebula-lost-ship]].
- Arrives non-hostile: `<ship load="REBEL" hostile="false"/>`. Long-range scanners show a
  ship ([[source-fandom-rebel-fight-choice-in-nebula]]).
- Carries the developer note `<!-- give player option to hide, -->`
  ([[source-events-nebula]]).

## Text
> Your ship emerges quite far away from the beacon. You see a Rebel ship waiting nearby,
> undoubtedly stationed to look for you.

(`event_NEBULA_REBEL_UNDETECTED_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Attack the ship. | — | `<ship hostile="true"/>` — fight the `REBEL` ship, default rewards. | 100% |
| 2 | Attempt to remain concealed. | — | `NEBULA_REBEL_UNDETECTED_LIST`, three entries — see below. | unknown (3-entry list) |
| 3 | **(Cloaking)** Cloak to stay hidden. | `req="cloaking"`, `hidden="true"` | *"You use your cloaking system to slip further into the nebula undetected."* — nothing happens, guaranteed. | 100% |

### Choice 2 — `NEBULA_REBEL_UNDETECTED_LIST`

| Entry | Text | Effect |
|---|---|---|
| 1 | *"You immediately slip further into the clouds, but not quickly enough. The Rebel catches sight of you and moves in to engage!"* | **Opens a second choice**: *Prepare to fight* → `<ship hostile="true"/>`; or **(Engines, level 4+, `hidden="true"`)** *"Your powerful engines allow you to out-distance the ship and eventually lose it within the nebula."* → nothing happens. |
| 2 | *"You power down non-essential systems and slip into the cloud. The ship never noticed you."* | Nothing happens. |
| 3 | *"The ship spots you and gives chase. After some quick maneuvering you were able to lose your pursuers in the clouds. You expect they warned the fleet of your position, however."* | `<modifyPursuit amount="1"/>` — the fleet advances. |

The nested **Engines level 4** gate is the detail the parsed preview drops entirely; it
lives inside entry 1 of the sub-list, not on the parent event
([[source-events-nebula]], and correctly nested on
[[source-fandom-rebel-fight-choice-in-nebula]]).

The `REBEL` ship: `<surrender chance="0.5" min="2" max="3" load="PIRATE_SURRENDER"/>`,
`<escape chance="0.5" min="3" max="4" load="PIRATE_ESCAPE"/>`,
`<destroyed load="DESTROYED_DEFAULT"/>` → `MED` / `standard` ([[source-events-ships]]).

## Blue Options
- **[[item-cloaking]]** (`req="cloaking"`, no level) — a top-level, guaranteed clean exit.
  Any level of Cloaking works.
- **[[item-engines]] level 4** (`req="engines" lvl="4"`) — **nested**, and only ever
  offered if choice 2 rolls entry 1. It rescues the one branch of hiding that would
  otherwise force a fight. It does not protect against entry 3's fleet advance, because
  that branch never presents the choice.

## Rewards & Risks
- There is **no reward path that isn't a fight**. Every non-combat outcome is "nothing
  happens". This event is purely about avoiding cost.
- Best outcome: nothing (choice 3, or choice 2 → entry 2, or choice 2 → entry 1 → Engines).
- Worst outcome: choice 2 → entry 3, a fleet advance with no compensation.
- Choice 1 gives `MED` / `standard` on a kill if you want the scrap.

## Strategy Notes
- With Cloaking, choice 3 is free and ends the event. Without it, the decision is whether
  an ordinary Rebel fight is worth more than a one-in-three chance of a fleet advance.
- On a strong ship, **attacking is the cleaner line**: it converts an uncertain cost into a
  certain payout, and the `REBEL` ship can surrender or flee. *(Opinion; no source
  recommends a line.)*
- Engines 4 is a common early investment, so choice 2's worst *immediate* branch is often
  already covered — but note the fleet-advance branch is the one it cannot cover.

## Related
- [[event-rebel-fight-chance-in-nebula]] — the mirror image, where *you* have the drop
- [[event-auto-ship-warning-in-nebula]] — the other nebula fleet-advance event
- [[item-cloaking]], [[item-engines]], [[concept-rebel-fleet-advance]],
  [[concept-rebel-fleet-advance]]
- [[sector-uncharted-nebula]], [[sector-slug-home-nebula]]
- [[event-pirate-surrender]] — the shared `PIRATE_SURRENDER` aftermath this hull loads
- [[event-pirate-escape]] — the shared `PIRATE_ESCAPE` aftermath this hull loads

## Open Questions
- [ ] Weights inside `NEBULA_REBEL_UNDETECTED_LIST` (3 entries, none stated).
- [ ] What `modifyPursuit amount="1"` does mechanically.

## Notes on the pursuit gloss
> ⚠️ **CONTRADICTION (internal to Fandom):** this page renders
> `<modifyPursuit amount="1"/>` as *"Rebel Fleet pursuit is doubled **for 1 jump**"*
> ([[source-fandom-rebel-fight-choice-in-nebula]]), while
> [[source-fandom-auto-ship-warning-in-nebula]] and
> [[source-fandom-rebel-fight-chance-in-nebula]] gloss the identical element as simply
> *"doubled"*. The game files state only `amount="1"` with no unit
> ([[source-events-nebula]]). Trusting the game files for what is recorded; both Fandom
> readings are unverified interpretations of the same value, and at most one can be right.

## Sources
- [[source-events-nebula]] (per raw/gamedata/events_nebula.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-rebel-fight-choice-in-nebula]] (per raw/wiki/rebel-fight-choice-in-nebula.md)
