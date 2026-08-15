---
id: chain-rock-bride
type: chain
trigger_event: [[[event-rock-bride]]]
steps: [[[event-rock-bride]], [[event-rock-quest-marriage]]]
sectors: [[[sector-rock-controlled-sector]], [[sector-rock-homeworlds]]]
reward: "a random augment + low scrap, OR Ariadne (a named Rock crew member) and a fight"
version: both
first_seen: 2026-08-13
last_updated: 2026-08-13
sources: 4
tags: [quest, moral-choice, named-crew, rock, two-outcomes, combat]
---

# The Rock bride

## Summary
A courier job with a person as the cargo, and the only quest in the game whose final choice is
purely ethical: deliver the bride to her arranged marriage for **a random augment and a little
scrap**, or refuse and receive **Ariadne** — a named Rock crew member — and an immediate fight
with the Grand Basilisk's escort.

Nothing in the first beacon hints that a choice is coming. The passenger is silent for the
whole journey; she speaks for the first time in the last event, and only after you have
committed the jumps.

## How It Starts
- Trigger: [[event-rock-bride]] (`ROCK_QUEST_MARRIAGE_START`), `unique="true"`
  ([[source-events-rock]]). A Rock captain with broken engines asks you to carry his passenger
  to *"her new husband — the Grand Basilisk of Numa V."*
- **Accept** → `<quest event="ROCK_QUEST_MARRIAGE"/>`, and a detail the game does not repeat:
  *"She refuses to enter the main hold and prefers to wait in the cargo bay."*
- **Refuse** → *"Arranged marriages aren't on your list of worthy causes."* No cost, no reward.

## Steps

1. **[[event-rock-bride]]** — accept the passenger, take the marker.
2. **[[event-rock-quest-marriage]]** — Numa V. One forced continue, then the passenger finally
   speaks and pleads not to be handed over, while the Grand Basilisk's Chief Aid demands
   delivery. Two choices ([[source-events-rock]]):

   | Choice | Outcome |
   |---|---|
   | **Hand her over** | *"May your children erode into dust!"* → `<augment name="RANDOM"/>` + `autoReward LOW scrap_only` |
   | **Refuse to comply** | *"I will join you. But quickly, we must jump away…"* → `<crewMember amount="1" class="rock" id="name_Ariadne"/>` — **Ariadne**, a Rock crew member — and an immediate hostile `ROCK_QUEST_MARRIAGE` ship |

3. **The fight, if you refuse.** `auto_blueprint="SHIPS_ROCK"`, with only two resolutions
   defined and **no surrender and no escape** ([[source-events-rock]]):
   - `destroyed` → `autoReward MED standard`
   - `deadCrew` → `autoReward HIGH standard`

   Both branches share the same text: *"His escort eliminated, the Grand Basilisk dispatches
   his entire fleet. There's just time to take your pick from the wreck before you jump out of
   their reach."*

## Requirements
- None. No crew, system, augment or resource gate anywhere in the chain.
- Fuel for the extra jump.

## Reward
The two branches are not comparable in kind, which is the point:

- **Hand her over:** a *random* augment — see [[concept-blueprint-rarity]] for what the
  `RANDOM` sentinel draws from — plus `LOW scrap_only`. Guaranteed, no fight.
- **Refuse:** **Ariadne**, a permanent Rock crew member (fire-immune, high health — see
  [[entity-rock-men]]), plus `MED` or `HIGH standard` from the escort fight.

A named crew member with the Rock species traits is generally worth more than a random augment,
and the fight pays on top — but it is a real fight, entered at whatever hull you arrived with.

## Failure Modes
- **Losing the escort fight.** There is no surrender and no `gotaway` branch: once you refuse,
  the fight resolves one way or the other.
- The standard quest-marker losses — see [[concept-quest-beacon-placement]].
- No branch loses the passenger or damages you before the choice, so the chain is riskless up
  to the final decision.

## Strategy Notes
- *Opinion:* refuse, if your hull can take a `SHIPS_ROCK` fight. Ariadne is free crew of the
  best defensive species in the game, and the kill pays `MED`–`HIGH standard` anyway — the
  handover branch's random augment is the weaker half in most runs.
- If you are limping, hand her over: the augment-and-scrap branch involves no combat at all.
- Boarding the escort is worth it for the `HIGH standard` on `deadCrew` rather than `MED` on
  `destroyed` — a rare case where the crew-kill premium is stated outright.

## Related
- [[entity-rock-men]] — what Ariadne is, mechanically
- [[concept-blueprint-rarity]] — how `<augment name="RANDOM"/>` resolves
- [[concept-quest-beacon-placement]]
- [[chain-rock-cruiser-unlock]] — the other Rock quest line, in the same sectors
- [[event-rock-fight]] — the ordinary `SHIPS_ROCK` encounter this fight reuses

## Open Questions
- [ ] Whether Ariadne differs from a generic Rock crew member beyond her name — `id="name_Ariadne"`
      sets the display name, and no other attribute is present.
- [ ] What augment pool `<augment name="RANDOM"/>` draws from, and whether rarity 0 items are
      excluded.
- [ ] Whether the escort fight scales with sector depth like an ordinary `SHIPS_ROCK` draw.

## Sources
- [[source-events-rock]] (per raw/gamedata/events_rock.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
