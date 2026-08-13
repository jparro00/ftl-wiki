---
id: chain-zoltan-cruiser-unlock
type: chain
trigger_event: [[[event-unarmed-zoltan-transport]]]
steps: [[[event-unarmed-zoltan-transport]], [[event-zoltan-peace-quest2]]]
sectors: [[[sector-zoltan-homeworlds]]]
reward: Zoltan Cruiser unlock + Zoltan Shield augment or the crew member Envoy
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [ship-unlock, zoltan-cruiser, dialogue-puzzle, two-step, guaranteed-start, no-combat]
---

# Zoltan Cruiser unlock

## Summary
The shortest ship-unlock chain in the game: two beacons, no fight, no equipment
requirement, no crew requirement. A Zoltan peace envoy asks you to hear them out, then
tests whether you meant it. Say the right two things at the second beacon and the
**Zoltan Cruiser** is yours. Say anything else and the test collapses into an ordinary
Rebel fight. ([[source-events-zoltan]], [[source-text-events-xml]])

Its difficulty is entirely conversational — which makes it the one unlock chain you can
fail with a perfect ship and complete with a broken one.

## How It Starts
- Trigger: [[event-unarmed-zoltan-transport]] (`ZOLTAN_PEACE_QUEST`), a **guaranteed**
  beacon in [[sector-zoltan-homeworlds]].
- `sector_data.xml` allocates it directly on the `ZOLTAN_HOME` sector description at
  `min="1" max="1"` and nowhere else — not in `ZOLTAN_SECTOR`, and not through any
  `eventList` ([[source-sector-data-xml]]). Entering the Zoltan Homeworlds guarantees the
  chain is offered exactly once.
- `ZOLTAN_HOME` is `unique="true"` with `minSector="2"`, so the chain can start no earlier
  than sector 3 and at most once per run ([[source-sector-data-xml]]).
- The event is `unique="true"` ([[source-events-zoltan]]).

## Steps

1. **[[event-unarmed-zoltan-transport]]** — `ZOLTAN_PEACE_QUEST` (raw: events_zoltan.xml)
   An unarmed Zoltan transport hails you. Three choices:
   - *Attack them* → loads the `ZOLTAN_PEACE_QUEST_ATTACK` list (one unarmed ship, one
     with a Zoltan defence escort). **Chain over.**
   - *Hear them out* → forced continue → `<quest event="ZOLTAN_PEACE_QUEST2"/>`. **The
     only advancing choice**, and it is free — no cost, no combat, no gate.
   - *Leave* → nothing happens; the quest marker is never placed. **Chain over.**

2. **[[event-zoltan-peace-quest2]]** — `ZOLTAN_PEACE_QUEST2` (raw: events_zoltan.xml)
   The quest marker. It looks like a Rebel ambush, but the ship loads
   `hostile="false"` — the fight is opt-in, which is the mechanical tell that this is a
   scripted test ([[source-events-zoltan]]). The winning line is three choices deep:

   > **Attempt to hail them** → **"Perhaps there could be a reconciliation of our ideals
   > without war?"** → **"True progress can only be achieved without bloodshed."**

   That path loads `ZOLTAN_PEACE_QUEST_REWARD`. **Every** other reply — *Attack*, the
   *"Surrender"* line, the *"Unity is the only option"* line, and the *"The galaxy is
   huge"* line at the final split — sets `<ship hostile="true"/>` and turns the beacon
   into an ordinary Rebel fight with default rewards. The unlock is not recoverable that
   run.

There is no third beacon. `ZOLTAN_PEACE_QUEST_REWARD` is an `eventList` resolved in place
at step 2, not a separate jump ([[source-events-zoltan]]).

## Requirements
- **Routing:** the [[sector-zoltan-homeworlds]] must appear on your map and you must enter
  it. That is the whole requirement.
- **No crew, system, augment or weapon gate anywhere in the chain.** Neither event carries
  a single `req=` attribute ([[source-events-zoltan]]) — unusual for a ship-unlock line,
  and the reason this chain is reachable on any hull.
- Fuel for one extra jump to the marker.

## Reward
`ZOLTAN_PEACE_QUEST_REWARD` has two entries; both call `<unlockShip id="7"/>`, so **the
unlock itself is guaranteed** once you reach the winning line — only the bonus differs
([[source-events-zoltan]]):

| Entry | Payload |
|-------|---------|
| 1 | Zoltan Cruiser unlock + `<augment name="ENERGY_SHIELD"/>` ([[item-zoltan-shield]]) + `autoReward level="LOW"` `scrap_only` |
| 2 | Zoltan Cruiser unlock + `<crewMember amount="1" class="energy" all_skills="2" id="name_Envoy"/>` (a Zoltan named **Envoy**) + `autoReward level="HIGH"` `standard` |

Ship id `7` → Zoltan Cruiser is corroborated by the ship's own unlock hint,
*"Learn from the Zoltan that sometimes diplomacy works."*
(`ship_PLAYER_SHIP_ENERGY_unlock`, [[source-text-blueprints]]), which describes this
chain and no other.

> ⚠️ **CONTRADICTION:** the split between the two entries.
> - Fandom states an explicit **50% / 50%** ([[source-fandom-unarmed-zoltan-transport]]).
> - The game files give an unweighted two-entry `eventList` with no stated odds
>   ([[source-events-zoltan]]).
>
> Compatible if `eventList` selection is uniform, but the file does not say so. Recorded
> as Fandom's claim, not as fact. Trusting the files on what the payloads are, Fandom on
> nothing else. Full detail on [[event-zoltan-peace-quest2]].

## Failure Modes
- **The Zoltan Homeworlds never appear.** `ZOLTAN_HOME` is `unique="true"`; if the sector
  map does not offer it, the chain does not exist that run ([[source-sector-data-xml]]).
- **Attacking the transport at step 1.** Trades the entire chain for one small fight.
- **Leaving at step 1.** No marker is placed, so there is nothing to return to.
- **Any wrong reply at step 2.** Four of the five conversational endpoints lose the
  unlock, and the mistake is invisible until the ship turns hostile.
- **Not reaching the marker before the Rebel fleet does.**

## Strategy Notes
- *Opinion:* this is the highest-value-per-risk chain in the game. Step 1 costs nothing,
  step 2 costs one jump, and neither has a combat requirement. If the Zoltan Homeworlds
  are on your route, take it regardless of ship state.
- The step-2 marker shows a **ship present** on Long-Ranged Scanners, so it reads as a
  hostile beacon on the map — do not skip it for that reason
  ([[source-fandom-unarmed-zoltan-transport]]).
- Memorise the line. It is a pure dialogue puzzle with no in-game hint, and the
  sympathetic-sounding *"The galaxy is huge — you can find a place for your ideals
  elsewhere"* is a **losing** reply.
- Fandom notes the Zoltan Cruiser can alternatively be unlocked by winning a run with the
  Federation Cruiser ([[source-fandom-unarmed-zoltan-transport]]); nothing in
  `achievements.xml` in this raw set states that condition, so it is Fandom-only.

## Related
- [[sector-zoltan-homeworlds]] — the only sector the chain runs in
- [[chain-crystal-cruiser-unlock]] — the other Zoltan-sector quest line, and the
  route-dependent opposite of this one
- [[item-zoltan-shield]] — one of the two payouts
- [[concept-blue-options]] — notable here for its complete absence

## Open Questions
- [ ] Confirm the 50/50 reward split from the engine's `eventList` selection logic.
- [ ] The `ZOLTAN_PEACE_QUEST_REWARD` list carries a `<!--DLC2 DLC3-->` annotation
      ([[source-events-zoltan]]). The events themselves carry no DLC marker and sit in a
      base file, so the chain is recorded here as `both` — but the **vanilla payout is
      unknown**, and that annotation is the only hint it may have differed.
- [ ] Both step pages currently record `version: ae`; this page records `both` on the
      grounds that neither event is DLC-gated and neither is overridden in
      `dlcEvents*.xml`. Needs a lint decision.
- [ ] Is `all_skills="2"` the skill cap, i.e. is Fandom's "maxed" exact?
- [ ] Can the step-2 marker be reached after leaving the Zoltan Homeworlds?

## Sources
- [[source-events-zoltan]] (per raw/gamedata/events_zoltan.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-fandom-unarmed-zoltan-transport]] (per raw/wiki/unarmed-zoltan-transport.md)
