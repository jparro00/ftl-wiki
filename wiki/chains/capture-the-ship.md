---
id: chain-capture-the-ship
type: chain
trigger_event: [[[event-capture-the-ship]]]
steps: [[[event-capture-the-ship]], [[event-quest-crewdead]]]
sectors: [[[sector-civilian-sector]], [[sector-federation-space]], [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]]]
reward: "autoReward HIGH weapon — but only if you kill the crew without destroying the hull"
version: ae
first_seen: 2026-08-13
last_updated: 2026-08-13
sources: 4
tags: [quest, crew-kill, blue-option-gated, inverted-win-condition, teleporter, punishing]
---

# Capture the ship intact

## Summary
The only quest in the game that is **invisible without the right equipment**. You overhear
merchants who need an enemy ship taken intact; unless you carry a Teleporter, an Anti-Bio Beam
or a Fire Bomb, they scan you, tell you that you are *"not properly equipped"*, and that is the
entire event.

If you do qualify, the payoff is a `HIGH weapon` reward — and the failure case is one of the
harshest in the game: **destroying the target hull costs 13 hull damage, a random system, and
sets every room on fire.** Like [[chain-rock-cruiser-unlock]], winning the fight the ordinary
way is how you lose.

## How It Starts
- Trigger: [[event-capture-the-ship]] (`QUEST_CREWDEAD_START`), `unique="true"`
  ([[source-events-xml]]). *"There is some unencrypted chatter between the ships, you tune in."*
- It continues into `QUEST_CREWDEAD_START_2`, where the gate sits. Five choices, and **three of
  them are blue**:

  | Choice | Requirement | Result |
  |---|---|---|
  | Offer your services | — | *"not properly equipped"* — **dead end** |
  | Leave them alone | — | nothing |
  | (Teleporter) Offer to board their ship | `req="teleporter" lvl="1"` | → `QUEST_CREWDEAD_CONTINUE` |
  | (Bio Beam) Offer to 'remove' their crew | `req="BEAM_BIO"` | → `QUEST_CREWDEAD_CONTINUE` |
  | (Fire Bomb) Offer to burn the crew out | `req="BOMB_FIRE"` | → `QUEST_CREWDEAD_CONTINUE` |

  All three blue options lead to exactly the same place. The requirement is not *a* piece of
  equipment but **any crew-killing method**, which is the same test the mission itself sets.

## Steps

1. **[[event-capture-the-ship]]** — overhear the merchants; pass the equipment gate.
2. **`QUEST_CREWDEAD_CONTINUE`** — the briefing. *"We need you to capture the ship intact…
   Remember, do NOT destroy that ship!"* Agreeing plants
   `<quest event="QUEST_CREWDEAD"/>`; declining ends the chain with no penalty.
3. **[[event-quest-crewdead]]** (`QUEST_CREWDEAD`, `unique="true"`) — the marked beacon. A
   forced fight with `PIRATE_QUEST_CREWDEAD` (`auto_blueprint="SHIPS_PIRATE"`,
   [[source-events-xml]]). Two outcomes and no others:

   | Resolution | Payload |
   |---|---|
   | **`deadCrew`** ✅ | *"You secure the ship… We would prefer if you did not speak of this to anyone."* → `autoReward HIGH weapon` |
   | **`destroyed`** ❌ | 13 hull damage, `<damage amount="1" system="random"/>` (AE only), and `<damage amount="1" system="room" effect="all"/>` — **fires throughout the ship** |

## Requirements
- **A crew-killing method, checked twice.** The gate at step 1 accepts a Teleporter,
  [[item-anti-bio-beam]] or a Fire Bomb; step 3 requires you to actually use it.
- Fuel for the extra jump.
- No scrap cost anywhere.

## Reward
`autoReward HIGH weapon` — a high-tier weapon roll, which for a two-beacon quest with no scrap
cost is a strong return. There is no scrap, no crew and no augment.

## Failure Modes
- **Destroying the hull.** Not merely a lost reward: it is a *net loss* of 13 hull, a damaged
  system, and fires in every room. This is one of the few events in the game whose bad branch
  can end a run outright.
- **Arriving without the means to finish.** The gate is checked when you accept, so selling the
  Teleporter or losing the Anti-Bio Beam between the briefing and the beacon leaves you at a
  fight you cannot win correctly.
- The standard quest-marker losses — see [[concept-quest-beacon-placement]].

## Strategy Notes
- *Opinion:* only take this with a Teleporter and boarders you trust, or with an
  [[item-anti-bio-beam]]. A Fire Bomb qualifies for the gate but is the least reliable way to
  clear a crew before your own damage output finishes the hull.
- **Turn your weapons off.** The failure branch triggers on hull destruction, so the safe play
  is to disable weapons entirely once boarders are aboard — the same discipline
  [[event-rock-unlock2]] demands.
- The dev note on the ship block reads `<!-- JUSTIN - TO DO - Start fires on the player ship -->`,
  and the shipped `destroyed` branch does exactly that, so the punishment is deliberate.

## Related
- [[chain-rock-cruiser-unlock]] — the other chain where destroying the target ends it
- [[item-teleporter]], [[item-anti-bio-beam]] — two of the three keys
- [[concept-blue-options]] — this is the clearest case of a gate that hides a whole quest
- [[concept-quest-beacon-placement]]
- [[entity-pirates]]

## Open Questions
- [ ] Whether the Fire Bomb gate (`req="BOMB_FIRE"`) checks the weapon or an inventory count —
      [[event-quest-mantis-invasion]]'s comparable option deducts 2 missiles, this one does not.
- [ ] What the merchants' ships are; they never appear as an entity.
- [ ] Whether `unique="true"` on both steps is per sector or per run — see
      [[concept-event-uniqueness]].

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
