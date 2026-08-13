---
id: event-distress-engi-rebel-result
type: event
event_name: DISTRESS_ENGI_REBEL_RESULT
sectors: [[[sector-engi-controlled-sector]], [[sector-engi-homeworlds]]]
beacon_type: distress
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [orphan, trading, augment-reward, weapon-chance, drone-chance, scrap-cost]
---

# Distress Engi Rebel result — `DISTRESS_ENGI_REBEL_RESULT`

## Summary
The trading half of the Engi distress ambush. Having beaten the Rebel fighter, you can pay
the surviving Engi runabout for gear: 25 scrap buys a lottery ticket (two thirds of the
time a weapon or drone, one third nothing), while 40 scrap plus 2 missiles and 2 fuel
buys a **guaranteed** Engi Med-bot Dispersal augmentation.

## Trigger & Where It Appears
- **Not in any sector event list.** It is reached only as the continuation of
  [[event-engi-distress-rebel-fight]]: the `DISTRESS_ENGI_REBEL` ship's `destroyed` and
  `deadCrew` blocks both end in `<event load="DISTRESS_ENGI_REBEL_RESULT"/>`
  ([[source-events-xml]], per `raw/gamedata/events_ships.xml`).
- It therefore inherits that event's placement: the distress beacon in
  [[sector-engi-controlled-sector]] or [[sector-engi-homeworlds]].
- Fandom documents it as the "After the fight" section of the parent page rather than as a
  separate event ([[source-fandom-engi-distress-rebel-fight]]).

## Text
> The Engi vessel turns out to be very poorly equipped - barely a runabout, really.
> They're trying to outrun the Rebels, and need all the help they can get.

(`event_DISTRESS_ENGI_REBEL_RESULT_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Give them 25 scrap. | 25 scrap | Loads `DISTRESS_ENGI_REBEL_LIST1`, three entries, each costing `-25` scrap: (a) gratitude only, nothing gained; (b) **Healing Burst** (`<weapon name="BOMB_HEAL"/>`); (c) a **random drone schematic** (`<drone name="RANDOM"/>`). | unknown |
| 2 | Give them 40 scrap, 2 missiles and 2 fuel. | 40 scrap, 2 missiles, 2 fuel | `-40` scrap, `-2` fuel, `-2` missiles, and `<augment name="NANO_MEDBAY"/>` — the **Engi Med-bot Dispersal** augmentation. Deterministic: `DISTRESS_ENGI_REBEL_LIST2` is a single `<event>`, not a list. | 100% |
| 3 | Give them nothing. | — | "Engi can't feel fear, so they bear you no ill will…" → nothing gained, nothing lost. | 100% |

Choice 2's outcome text:

> They wouldn't get more than a few jumps with that load-out. You provide them with all the
> munitions and supplies they should need for the journey home. "Generosity magnitude
> unpredicted. Well-being syntax error [value too high]. Accept this token."

## Blue Options
None.

## Rewards & Risks
- **[[item-engi-med-bot-dispersal]]** (`NANO_MEDBAY`) — guaranteed, for 40 scrap + 2 missiles
  + 2 fuel.
- **[[item-healing-burst]]** (`BOMB_HEAL`) or a random drone schematic — two of the three
  25-scrap outcomes.
- Risk: the 25-scrap option can pay nothing at all. The resource cost is charged in every
  branch of the list ([[source-events-xml]]).

## Strategy Notes
- Choice 2 is the only deterministic reward in the event. Whether it is worth 2 missiles
  and 2 fuel on top of the scrap depends entirely on how thin your consumables are.
  *(Opinion.)*
- Choice 1 is a 25-scrap gamble with a stated one-in-three chance of nothing — the exact
  weighting of the three list entries is not given by any source here.

## Related
- [[event-engi-distress-rebel-fight]] — the fight that leads here; the only way to reach this
- [[item-engi-med-bot-dispersal]] — the guaranteed reward
- [[item-healing-burst]] — the weapon chance
- [[entity-engi]]

## Open Questions
- [ ] Relative weighting of the three `DISTRESS_ENGI_REBEL_LIST1` entries.
- [ ] What happens if you cannot afford a choice — is it hidden, or shown and refused?

## Sources
- [[source-events-xml]] (per `raw/gamedata/events_engi.xml`, `raw/gamedata/events_ships.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-engi-distress-rebel-fight]] (per `raw/wiki/engi-distress-rebel-fight.md`)
