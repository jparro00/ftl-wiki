---
id: event-zoltan-ship-follows-mantis-ship
type: event
event_name: ZOLTAN_DISTRESS_MANTIS
sectors: [[[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: distress
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unique, distress, asteroid-field, pick-a-side, scrap-reward]
---

# Zoltan ship follows Mantis ship — `ZOLTAN_DISTRESS_MANTIS`

## Summary
A distress beacon where the Zoltan explicitly ask you **not** to help. Both interference
options lead to the same reward tier, so this is a pick-a-side event with no mechanical
payoff difference — only a choice of opponent, fought inside an **asteroid field**.
Declining is free.

## Trigger & Where It Appears
- Sectors: [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]
- Beacon: **distress** (`<distressBeacon/>`) in an **asteroid field**
  (`<environment type="asteroid"/>`). Both interference branches re-apply the asteroid
  environment, so the hazard follows you into the fight
  ([[source-events-zoltan]], per raw/gamedata/events_zoltan.xml).
- Reached via the `DISTRESS_BEACON_ZOLTAN` event list, allocated `min=1 max=2` beacons in
  both Zoltan sectors ([[source-sector-data-xml]]).
- `unique="true"`. Long-Ranged Scanners show **no ship** plus an asteroid field
  ([[source-fandom-zoltan-ship-follows-mantis-ship]]).

## Text
> Your jump interrupts a Zoltan security ship as it follows a Mantis pirate into an
> asteroid field. They message you, "Your presence here will continue to be tolerated -
> but please, do not interfere."

(`event_ZOLTAN_DISTRESS_MANTIS_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Interfere and save the Mantis ship. | — | *"Sometimes you have to bet on the underdog - even on the rare occasions that the underdog is a Mantis warship. You set off for the heart of the asteroid field and engage the Zoltan there."* → `<ship load="ZOLTAN_SHIP_SAVE_MANTIS1" hostile="true"/>` + asteroid environment. | 100% |
| 2 | Interfere and help the Zoltan ship. | — | *"You overtake the Zoltan and catch up with the Mantis ship in the asteroid belt. Time to make some friends."* → `<ship load="ZOLTAN_SHIP_SAVE_MANTIS2" hostile="true"/>` + asteroid environment. Fandom: the Mantis ship has a **crew entirely composed of Mantis**. | 100% |
| 3 | Don't interfere. | — | *"The Zoltan know their business better than most - best to leave them to it. You prepare to jump."* Nothing happens. | 100% |

### Post-fight rewards

From [[source-fandom-zoltan-ship-follows-mantis-ship]] (`events_ships.xml` is not
ingested here):

| Path | Destroyed the ship | Killed the crew |
|------|--------------------|--------------------|
| **1 — fight the Zoltan** | *"The Mantis are so grateful that they only take three quarters of the loot, leaving the rest for you. How civilized."* → `low` scrap with resources | same text → `medium` scrap with resources |
| **2 — fight the Mantis** | *"As you're salvaging the Mantis wreck the Zoltan security patrol returns with three other ships. You quickly salvage what you can…"* → `low` scrap with resources | same text → `medium` scrap with resources |

**The reward tiers are identical on both paths.** Neither side gives you an augment,
weapon, or crew for choosing them.

## Blue Options
None. No `req` attribute on any choice.

## Rewards & Risks
- **Rewards:** `low` (hull destroyed) or `medium` (crew killed) scrap with resources,
  the same either way.
- **Risks:** the asteroid field runs for the whole fight — continuous random hull and
  system hits, and it will strip an unshielded ship. This is the dominant risk, not the
  enemy.
- No crew-loss, system-sabotage, or fleet-advance effects are scripted on any branch.

## Strategy Notes
- *Opinion:* because the payouts are equal, choose on opponent difficulty alone. The
  Zoltan ship brings a Super Shield (bad for lasers, fine for ion and beams once it is
  down); the Mantis ship brings an all-Mantis crew (bad news if it has a teleporter).
- *Opinion:* choice 3 is genuinely competitive here. A `low`/`medium` scrap payout is a
  modest return for a fight in an asteroid field, and the beacon costs nothing to skip.
- Killing the crew upgrades the tier on both paths, so boarding is worth more than
  hull damage — but boarding into an asteroid field with your own hull taking hits is
  its own risk.

## Related
- [[event-free-scrap-with-resources-zoltan]] — the other unique `DISTRESS_BEACON_ZOLTAN`
  member, and a strictly better one
- [[event-zoltan-fight-in-asteroid-field]] — the other Zoltan asteroid-field event
- [[entity-zoltan]], [[entity-mantis]] — the two opponents
- [[concept-asteroid-fields]] — the hazard

## Open Questions
- [ ] Loadouts of `ZOLTAN_SHIP_SAVE_MANTIS1` and `ZOLTAN_SHIP_SAVE_MANTIS2`.
- [ ] Surrender/escape behaviour of either ship.
- [ ] Does siding with the Mantis have any effect later in the sector? Nothing in the
      game files suggests so.

## Sources
- [[source-events-zoltan]] (per raw/gamedata/events_zoltan.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-zoltan-ship-follows-mantis-ship]] (per raw/wiki/zoltan-ship-follows-mantis-ship.md)
