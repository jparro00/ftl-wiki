---
id: event-zoltan-quest-primitives
type: event
event_name: ZOLTAN_QUEST_PRIMITIVES
sectors: [[[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: quest
hostile: false
blue_options: []
chain: [[[chain-zoltan-primitives]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [unique, weapon-reward, rebel-fleet-risk, quest-marker, pick-a-side]
---

# Zoltan quest primitives — `ZOLTAN_QUEST_PRIMITIVES`

## Summary
A pick-a-side fight over an uncontacted primitive world. Siding with the Zoltan (attack
the Rebel) pays a **weapon plus scrap**; siding with the Rebels (make first contact) pays
less scrap and **doubles Rebel fleet pursuit for one jump**. Leaving is free. It is
reachable both as a standalone quest beacon and as the quest marker from
[[event-zoltan-trade-hub]].

## Trigger & Where It Appears
- Sectors: [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]
- **Two routes in:**
  1. Directly, via the `QUESTS_ZOLTAN` event list, allocated `min=0 max=1` beacons in
     both Zoltan sectors — so it is **not guaranteed** ([[source-sector-data-xml]]).
  2. As a quest marker from [[event-zoltan-trade-hub]], whose
     `ZOLTAN_TRADE_HUB_SUCCESS` list can fire `<quest event="ZOLTAN_QUEST_PRIMITIVES"/>`
     from the cantina branch ([[source-events-zoltan]],
     [[source-fandom-zoltan-trade-hub]]). The marker shows **no ship** on Long-Ranged
     Scanners.
- `unique="true"`.
- The intro assumes you heard about the planet "at the cantina" even when the event
  is rolled directly, which is a small narrative seam.

## Text
> You arrive at the primitive planet that you heard about at the cantina and are
> surprised to see a Zoltan ship facing off against a Rebel assault craft.

(`event_ZOLTAN_QUEST_PRIMITIVES_text`, per [[source-text-events-xml]])

The event opens with a forced continue (`<text id="continue"/>`) rather than a real
choice:

> You tap into their frequency and hear the Rebel captain yelling, "We are liberating
> this planet in the name of the new Galactic government! These aliens will not be left
> in ignorance where they cannot be of use!"

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Interfere - make first contact with the primitive aliens. | — | *"The local people - furry, one-eyed tree lizard things - begin chanting when they see you. Suddenly the sky is lit by laser fire - the Zoltan opened fire on your ship!"* → `<ship load="ZOLTAN_PRIMITIVES_ZOLTAN" hostile="true"/>`. | 100% |
| 2 | Protect the aliens' way of life - Attack the Rebel ship. | — | *"These creatures should be left to develop at their own pace. You direct all weapons on the Rebel ship and begin the firing sequence."* → `<ship load="ZOLTAN_PRIMITIVES_REBEL" hostile="true"/>`. | 100% |
| 3 | Leave. | — | *"You don't want to alert the Rebels of your presence and you don't want to anger the Zoltan in their territory. The best solution is to leave."* Nothing happens. | 100% |

### Post-fight results

These live in `events_ships.xml`, which is not ingested here — the following is entirely
from [[source-fandom-zoltan-quest-primitives]].

| Path | Win by destroying | Win by killing crew |
|------|-------------------|---------------------|
| **1 — fight the Zoltan** | Rebel fleet **pursuit doubled for 1 jump** + `low` scrap with resources | Rebel fleet **pursuit doubled for 1 jump** + a random amount of scrap with resources |
| **2 — fight the Rebel** | a **weapon** with `low` scrap | a **weapon** with `medium` scrap |

Path 1's Rebel captain signs off with *"Lovely, you've done our job for us! We'll let you
live as thanks. However, I can't promise the fleet will show you the same courtesy."*
Path 2's Zoltan hail with *"We were led to believe Federation ideals died along with the
Federation itself. Let us aid you a little, for old times' sake."*

## Blue Options
None. No `req` attribute on any choice.

## Rewards & Risks
- **Path 2 is strictly better on rewards:** a free weapon on both win conditions, and no
  fleet penalty.
- **Path 1 carries the only real risk beyond the fight itself** — doubled Rebel fleet
  advance for a jump, which can cost you a beacon's worth of exploration.
- Neither Fandom nor the game files here specify surrender or escape behaviour for
  `ZOLTAN_PRIMITIVES_ZOLTAN` or `ZOLTAN_PRIMITIVES_REBEL`; Fandom explicitly notes both
  ships have **no** surrender/escape values set in `events_ships.xml`.

## Strategy Notes
- *Opinion:* take choice 2 (attack the Rebel) unless you specifically want to avoid a
  Rebel-flagged kill. It is the same amount of combat for a weapon instead of a fleet
  penalty.
- Killing the enemy crew rather than destroying the hull upgrades the scrap tier on both
  paths, so boarding or an anti-personnel approach is worth more here than usual.

## Related
- [[chain-zoltan-primitives]] — the full quest line this belongs to
- [[event-zoltan-trade-hub]] — the other way to reach this beacon
- [[entity-zoltan]], [[entity-rebels]] — the two possible opponents
- [[concept-rebel-fleet-advance]] — what path 1 accelerates

## Open Questions
- [ ] Loadouts of `ZOLTAN_PRIMITIVES_ZOLTAN` and `ZOLTAN_PRIMITIVES_REBEL`.
- [ ] Which weapon pool path 2 draws from.
- [ ] Whether reaching it via [[event-zoltan-trade-hub]] changes any outcome (Fandom
      transcludes the identical text for both routes, suggesting not).

## Sources
- [[source-events-zoltan]] (per raw/gamedata/events_zoltan.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-zoltan-quest-primitives]] (per raw/wiki/zoltan-quest-primitives.md)
- [[source-fandom-zoltan-trade-hub]] (per raw/wiki/zoltan-trade-hub.md)
