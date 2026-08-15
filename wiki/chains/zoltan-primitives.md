---
id: chain-zoltan-primitives
type: chain
trigger_event: [[[event-zoltan-trade-hub]]]
steps: [[[event-zoltan-trade-hub]], [[event-zoltan-quest-primitives]]]
sectors: [[[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
reward: "a weapon roll — low/med for defending the planet, low/random scrap for siding against it"
version: both
first_seen: 2026-08-13
last_updated: 2026-08-13
sources: 4
tags: [quest, moral-choice, zoltan, rebels, overheard, three-way]
---

# The primitive planet

## Summary
A quest you are not offered but **overhear**. Visiting the cantina at a Zoltan trade hub, you
catch gossip about a newly discovered planet that has not had first contact, and note down its
location. When you arrive, a Zoltan ship and a Rebel assault craft are already facing off over
it — and you have to decide whose idea of "helping" these people you agree with.

It is the wiki's clearest three-way moral choice: side with the Zoltan's non-interference, side
with nobody, or make first contact yourself and discover that the Zoltan will shoot you for it.

## How It Starts
- Trigger: [[event-zoltan-trade-hub]] (`ZOLTAN_TRADE_HUB`). The marker is planted on the
  **success branch**, `ZOLTAN_TRADE_HUB_SUCCESS` ([[source-events-zoltan]]) — the cantina
  route, not the shop route: *"You head into the cantina for gossip… You overhear one group
  discussing a newly discovered planet yet to have first contact, and note down its
  location."*
- There is no accept/decline. Overhearing it **is** accepting it.

## Steps

1. **[[event-zoltan-trade-hub]]** — take the cantina branch; the marker is planted silently.
2. **[[event-zoltan-quest-primitives]]** (`ZOLTAN_QUEST_PRIMITIVES`, `unique="true"`) — the
   planet. A forced continue reveals the Rebel captain's position: *"We are liberating this
   planet in the name of the new Galactic government! These aliens will not be left in
   ignorance where they cannot be of use!"* Then three choices ([[source-events-zoltan]]):

   | Choice | What happens | Ship |
   |---|---|---|
   | **Interfere — make first contact** | *"The local people — furry, one-eyed tree lizard things — begin chanting when they see you. Suddenly the sky is lit by laser fire — the Zoltan opened fire on your ship!"* | `ZOLTAN_PRIMITIVES_ZOLTAN` |
   | **Protect the aliens' way of life — attack the Rebel** | *"These creatures should be left to develop at their own pace."* | `ZOLTAN_PRIMITIVES_REBEL` |
   | **Leave** | *"You don't want to alert the Rebels… and you don't want to anger the Zoltan in their territory."* | none |

3. **The two fights pay differently, and both reward boarding**
   ([[source-events-ships]]):

   | Ship | `destroyed` | `deadCrew` |
   |---|---|---|
   | `ZOLTAN_PRIMITIVES_ZOLTAN` (you made contact) | `LOW standard` | `RANDOM standard` |
   | `ZOLTAN_PRIMITIVES_REBEL` (you defended the planet) | `LOW weapon` | **`MED weapon`** |

   Killing the Zoltan leaves the Rebel free to take the planet, and the Rebel captain says so:
   *"Lovely, you've done our job for us! We'll let you live as thanks. However, I can't promise
   the fleet will show you the same courtesy."* Killing the Rebel earns a Zoltan thank-you —
   *"We were led to believe Federation ideals died along with the Federation itself."*

## Requirements
- None. No gates, no resource cost, no scrap.
- Fuel for the extra jump.

## Reward
Attacking the Rebel is the better branch on every axis: it pays a weapon rather than plain
scrap, it pays more, and it is the only outcome where the planet is left alone. Boarding
rather than shelling upgrades `LOW weapon` to `MED weapon`.

The first-contact branch is the deliberate trap — it looks like the curious, exploratory choice
and it turns the Zoltan hostile for `LOW standard`.

## Failure Modes
- **Leaving** ends the chain with nothing. No penalty, but no payment either.
- **Making first contact** costs you the good outcome and starts a fight with a Zoltan hull
  (shielded — see [[entity-zoltan]]) for the worst reward in the chain.
- The standard quest-marker losses — see [[concept-quest-beacon-placement]].

## Strategy Notes
- *Opinion:* attack the Rebel, and board if you can. It is the highest-paying branch and the
  only one that does not end with the planet in someone's hands.
- The trigger is easy to miss entirely: the marker is planted by a flavour branch of a
  trade-hub event, so a player who takes the shop route never learns the quest exists.
- Zoltan hulls carry a super-shield; a `LOW standard` reward is poor payment for one.

## Related
- [[entity-zoltan]] — whose territory this is, and whose ship shoots you for interfering
- [[entity-rebels]] — the other claimant
- [[chain-zoltan-cruiser-unlock]] — the other Zoltan quest line, also about non-interference
- [[concept-quest-beacon-placement]]

## Open Questions
- [ ] Whether `ZOLTAN_TRADE_HUB`'s cantina branch is the only planter — the success list has
      two entries and only one carries the `<quest>` tag.
- [ ] What `autoReward level="RANDOM"` resolves to in practice, here and elsewhere.
- [ ] Whether the primitives themselves ever recur; they appear in no other event.

## Sources
- [[source-events-zoltan]] (per raw/gamedata/events_zoltan.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
