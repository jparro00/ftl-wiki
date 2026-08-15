---
id: chain-rebel-defector
type: chain
trigger_event: [[[event-rebel-defector]]]
steps: [[[event-rebel-defector]]]
sectors: [[[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]]]
reward: "a human crew member, then high stuff or low scrap at the stash — if the defector was genuine"
version: both
first_seen: 2026-08-13
last_updated: 2026-08-13
sources: 4
tags: [quest, betrayal, crew-gain, boarders, gamble, clone-bay]
---

# The Rebel defector

## Summary
A Rebel offers to defect, join your crew, and lead you to a hoard of supplies. Accepting rolls
a **six-entry table**, and only half of it is the offer being honest. The other half is an
ambush: he can steal your ship data and teleport away, detonate charges and beam boarders in,
or come aboard and immediately **eviscerate one of your crew**.

The quest marker is only planted on the honest outcomes — so the chain either continues to a
supply stash or never begins, and you find out which by taking the gamble.

## How It Starts
- Trigger: [[event-rebel-defector]] (`ALISON_DEFECTOR`) ([[source-events-xml]]).
- Accepting the defection loads `ALISON_DEFECTOR_HELP_2`, a **6-entry list** — so **1 in 6**
  each, per [[concept-event-list-weighting]]:

  | # | What actually happens | Payload |
  |---|---|---|
  | 1 | *"The dishonorable Rebel has deceived you. He damages your ship and steals ship information before teleporting away."* | 2 hull, **1 engine damage** (AE), **fleet advances 1 jump** |
  | 2 | *"Your new crew-member smiles, then reveals a small remote trigger…"* | 2 hull, **1 piloting damage** (AE), **2 human boarders** |
  | 3, 4, 5 | *"Relieved and light-headed, your new crewmember gets to work as the Rebel ship attacks."* | **+1 human crew** and `<quest event="ALISON_DEFECTOR_QUEST"/>` |
  | 6 | *"The Rebel makes to take his assigned station, then suddenly turns and eviscerates the nearest crew-member. Red Alert!"* | **1 human boarder**, and `<removeCrew>` — **you lose a crew member** |

- **Three of the six entries are identical**, which per [[concept-event-list-weighting]] is how
  the files express a weight: the defection is genuine **50%** of the time.

## Steps

1. **[[event-rebel-defector]]** — accept the defection and roll the table above.
2. **On entries 3–5 only:** +1 human crew and the stash marker.
3. **The stash beacon** resolves `ALISON_DEFECTOR_QUEST`, a 2-entry list — **50/50**
   ([[source-events-xml]]):

   | Outcome | Payload |
   |---|---|
   | *"you find a sizable stash of useful materials"* | `autoReward HIGH stuff` |
   | *"it was not quite as large as advertised"* | `autoReward LOW scrap_only` |

## The Clone Bay line

Entry 6's `<removeCrew>` carries `<clone>true</clone>` ([[source-events-xml]]) — the murdered
crew member **is** revived if you have a Clone Bay. This is the opposite of the case recorded
on [[event-unknown-disease-on-mining-colony]], where `<clone>false</clone>` means no revive,
and the pair is why the extractor has to read the element's value rather than its presence.

## Requirements
- None. No gates.
- Fuel for one extra jump, on the branches that plant a marker.

## Reward
Expected value is positive but the variance is high. A 50% shot at a free human crew member
plus a coin-flip stash (`HIGH stuff` or `LOW scrap_only`), against a 50% chance of hull damage,
boarders, a fleet advance, or a dead crew member.

## Failure Modes
- **Entry 6 kills a crew member outright** unless you run a Clone Bay.
- **Entry 1 advances the Rebel fleet** on top of the damage — see
  [[concept-rebel-fleet-advance]].
- **Entries 1 and 2 damage a system**, and in AE specifically the engines or piloting — the two
  systems you most want intact when boarders arrive.
- The stash itself can disappoint: half the time it is `LOW scrap_only`.
- The standard quest-marker losses — see [[concept-quest-beacon-placement]].

## Strategy Notes
- *Opinion:* a coin flip with a bad tail. Take it with a Clone Bay, a strong crew, or good
  door control; skip it on a fragile run in [[sector-rebel-stronghold]], where a fleet advance
  costs the most.
- The three-identical-entries construction is worth knowing on its own: **the game is telling
  you the odds are exactly 50/50** without printing a number.

## Related
- [[concept-event-list-weighting]] — the duplicated-entry weighting this event demonstrates
- [[concept-rebel-fleet-advance]] — entry 1's hidden cost
- [[event-unknown-disease-on-mining-colony]] — the `<clone>false</clone>` counterpart
- [[item-clone-bay]]
- [[entity-rebels]]

## Open Questions
- [ ] Whether the defector's own ship remains hostile through the honest branches — the text
      says *"as the Rebel ship attacks"* but no `<ship>` state change is recorded here.
- [ ] Whether the `<!--DLC2-->` marker on entry 1's text denotes a second-pass DLC edit
      distinct from the ordinary `<!--DLC-->` markers; it appears rarely.
- [ ] What `autoReward level="HIGH">stuff` resolves to numerically.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
