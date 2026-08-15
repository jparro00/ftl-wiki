---
id: chain-mantis-war-camp
type: chain
trigger_event: [[[event-mantis-war-camp]]]
steps: [[[event-mantis-war-camp]], [[event-quest-mantis-invasion]]]
sectors: [[[sector-civilian-sector]], [[sector-federation-space]], [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
reward: "med scrap up front; then nothing, a fight, or (2 Fire Bombs) high stuff + a free Engi crew member"
version: ae
first_seen: 2026-08-13
last_updated: 2026-08-13
sources: 4
tags: [quest, blue-option, fire-bomb, missile-weapon, reconnaissance, paid-up-front]
---

# The Mantis war camp

## Summary
A settlement asks you to scout a Mantis war camp, pays you **before** you go, and then the
destination turns out to be exactly what you were told: far too many Mantis to fight. The
honest outcome is to leave.

What makes it worth a page is the **Fire Bomb branch** — the single best-paying blue option of
any non-unlock quest in the game, handing you `HIGH stuff` *and* a free Engi crew member for
2 missiles. The missile-weapon branch, by contrast, is a trap that costs a missile and starts a
fight.

## How It Starts
- Trigger: [[event-mantis-war-camp]] (`QUEST_MANTIS_INVASION_START`), `unique="true"`
  ([[source-events-xml]]). *"All of our military ships have been destroyed or damaged during
  the rebellion. However, there have been reports of a Mantis war camp only a few jumps from
  us. Can you help?"*
- **Pledge to do what you can** → `<quest event="QUEST_MANTIS_INVASION"/>` **and**
  `autoReward MED scrap_only`. The payment is unconditional and arrives immediately — you keep
  it whatever you do at the destination.
- **Apologize and decline** → *"There's no way you are crazy enough to want to take on a Mantis
  war-band."*

## Steps

1. **[[event-mantis-war-camp]]** — accept, take the `MED scrap_only` up front.
2. **[[event-quest-mantis-invasion]]** (`QUEST_MANTIS_INVASION`, `unique="true"`) — the camp.
   *"There are far too many of them to count accurately… It would be suicide to attack
   directly."* Three choices ([[source-events-xml]]):

   | Choice | Requirement | Outcome |
   |---|---|---|
   | Leave before they notice you | — | `MANTIS_LANDING_PARTY_LEAVE` |
   | (Missile Weapon) Bombard their key structures | `req="WEAPONS_MISSILES"` | **−1 missile**, a planetary defence system shreds the shot, and a `MANTIS_LANDING_PARTY` patrol attacks |
   | (2 Fire Bombs) Teleport fire bombs into key structures | `req="BOMB_FIRE"` | **−2 missiles**, then `autoReward HIGH stuff` **+ 1 Engi crew member** |

3. **The Fire Bomb branch in full.** The bombs land in a fuel depot and the barracks; *"Mantis
   comm channels fill with panicked chatter."* A forced continue then reads: *"With most of
   their ships and forces focused on the chaos, you slip undetected to a nearby depot. You find
   some useful resources and an Engi slave who gladly accepts your liberation."* →
   `<autoReward level="HIGH">stuff</autoReward>` and `<crewMember amount="1" class="engi"/>`.

## Requirements
- Nothing to reach the destination — the scrap is paid regardless.
- **A Fire Bomb and 2 missiles** for the only branch that pays at the camp.
- A missile weapon is *not* useful here despite being a listed gate; see Failure Modes.

## Reward
- **Guaranteed:** `MED scrap_only`, paid at the first beacon.
- **With a Fire Bomb:** `HIGH stuff` plus a free crew member, for 2 missiles. Engi crew are
  the fastest repairers in the game ([[entity-engi]]), so this is a substantial upgrade for a
  trivial cost.
- **Otherwise:** nothing further.

## Failure Modes
- **The missile-weapon option is worse than leaving.** It costs a missile, achieves nothing —
  *"a shot from the surface rips the missile to shreds"* — and hands you an unplanned fight
  against a `MANTIS_LANDING_PARTY`. The blue colouring makes it look like the clever play; it
  is the only branch that is strictly negative.
- The standard quest-marker losses — see [[concept-quest-beacon-placement]].

## Strategy Notes
- *Opinion:* always accept the job — it is free scrap with no obligation. Then take the Fire
  Bomb branch if you have one and **leave** if you do not. Never take the missile option.
- This is a strong argument for keeping a Fire Bomb aboard even on a non-boarding run: two
  missiles for a crew member and a `HIGH` roll is the best conversion rate in the quest pool.
- The event carries a dev note, `<!-- ADD PDS ENVIRONMENT -->`, that was never actioned — the
  planetary defence system exists in the missile branch's *prose* but not as an
  `<environment type="PDS"/>` on the beacon.

## Related
- [[entity-mantis]] — whose camp this is
- [[entity-engi]] — what the freed slave is worth
- [[concept-blue-options]] — a case where one gated option is a trap and another is the payoff
- [[concept-quest-beacon-placement]]
- [[chain-settlement-mercenary-work]] — the other "a settlement hires you" quest

## Open Questions
- [ ] Whether `req="BOMB_FIRE"` checks for the weapon or for 2 missiles in the hold; the branch
      deducts 2 missiles but the requirement names the bomb.
- [ ] What `MANTIS_LANDING_PARTY_LEAVE` contains — the leave branch is not expanded here.
- [ ] Why the event is AE-only when its trigger sectors are not.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
