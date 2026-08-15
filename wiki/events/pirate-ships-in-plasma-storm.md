---
id: event-pirate-ships-in-plasma-storm
type: event
event_name: STORM_ZOLTAN_SUPPLY_CHOICE
sectors: [[[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: nebula
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unique, plasma-storm, fuel-reward, missile-reward, pirate, resource-choice]
---

# Pirate ships in plasma storm — `STORM_ZOLTAN_SUPPLY_CHOICE`

## Summary
Two pirate ships, one carrying fuel and one carrying ammunition — you pick which to
raid, or skip both. Fought inside a **plasma storm**, which halves your reactor output,
so this is a resource top-up that arrives under the worst possible power conditions.
Preserving the hull rather than destroying it roughly triples the payout.

## Trigger & Where It Appears
- Sectors: [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]
- Beacon: **plasma storm** — the event carries `<environment type="storm"/>`
  ([[source-events-zoltan]]). Long-Ranged Scanners show no ship plus a storm
  ([[source-fandom-pirate-ships-in-plasma-storm]]).
- Reached via the `NEBULA_ZOLTAN` event list, allocated `min=2 max=6` beacons in both
  Zoltan sectors ([[source-sector-data-xml]]).
- `unique="true"`. The source file carries the developer note
  `<!-- can also use this with other sectors?-->`, so this is a Zoltan-only event that
  was written to be portable.

## Text
> You spy two pirate ships lurking in the nebula here. They remain unaware of your
> presence; you're able to get your scanners to at least identify their cargo: One is
> carrying the fuel supplies, the other the ammunition. They begin to drift away from
> each other in the storm.

(`event_STORM_ZOLTAN_SUPPLY_CHOICE_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Secure the fuel supply. | — | *"You jet toward the pirate with the fuel supplies and engage - hopefully you can leave the ship in one piece!"* → `<ship load="STORM_PIRATE_SUPPLY_FUEL" hostile="true"/>`. | 100% |
| 2 | Secure the ammunition. | — | *"You jet toward the pirate with the ammunition and engage - hopefully you can leave the ship in one piece!"* → `<ship load="STORM_PIRATE_SUPPLY_AMMO" hostile="true"/>`. | 100% |
| 3 | Let them leave. | — | *"Sometimes discretion is the better part of valor."* Nothing happens. | 100% |

### Post-fight rewards

From [[source-fandom-pirate-ships-in-plasma-storm]] (these branches live in
`events_ships.xml`, not ingested here):

| Path | Destroyed the ship | Killed the crew (hull intact) |
|------|--------------------|-------------------------------|
| **1 — fuel** | *"The ship obliterated, only scant fuel canisters can be scavenged…"* → `low` fuel and scrap (Fandom glosses: **1–3 fuel**) | *"With the ship in one piece, you are able to salvage most of the fuel supplies…"* → `high` fuel and scrap (Fandom glosses: **3–6 fuel**) |
| **2 — ammunition** | *"…only scant ammunition crates can be scavenged…"* → `low` missiles and scrap (Fandom glosses: **1–2 missiles**) | *"With the ship in one piece, you are able to salvage most of the ammunition…"* → `high` missiles and scrap (Fandom glosses: **4–8 missiles**) |

Fandom also states that **both enemy ships have a 50% escape-attempt chance at 20–40%
hull and never surrender**. The reward tiers (`low`/`high`) are the game's own words;
the numeric ranges in brackets are Fandom's gloss, not values stated in the game files.

## Blue Options
None. No `req` attribute on any choice.

## Rewards & Risks
- **Rewards:** fuel or missiles plus scrap, with the tier depending entirely on whether
  you leave the hull intact.
- **Risks:**
  - The **plasma storm halves your reactor power** for the whole fight. Ships that rely
    on many simultaneously-powered systems are badly hurt here; ships running on
    missiles, drones, or a small number of high-value systems are barely affected.
  - The enemy may **escape at 20–40% hull** (50% chance), which forfeits the reward
    entirely. This is the main way the beacon disappoints.

## Strategy Notes
- *Opinion:* the storm makes this a poor fight for shield-and-laser builds and a good one
  for missile or boarding builds — which is convenient, since boarding is also how you
  reach the `high` reward tier.
- Choose by what you are short of, not by value: the `high` tiers are not directly
  comparable (fuel keeps you moving, missiles keep a launcher relevant).
- Because the enemy can flee at low hull, burst damage or a teleporter is worth more here
  than sustained chip damage.
- Choice 3 is free and is the correct answer if the storm would leave you unable to power
  shields.

## Related
- [[concept-nebula-mechanics]] — the halved-reactor hazard governing this fight
- [[event-zoltan-great-eye]], [[event-rock-fight-in-nebula]] — the other unique
  `NEBULA_ZOLTAN` members
- [[entity-pirates]] — the opponents

## Open Questions
- [ ] Loadouts of `STORM_PIRATE_SUPPLY_FUEL` and `STORM_PIRATE_SUPPLY_AMMO`.
- [ ] Confirm the `low`/`high` fuel and missile ranges against `autoReward` tables —
      Fandom's 1–3 / 3–6 / 1–2 / 4–8 figures are unsourced in the game files ingested here.
- [ ] Does the storm environment persist for the whole fight or only the approach?

## Sources
- [[source-events-zoltan]] (per raw/gamedata/events_zoltan.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-pirate-ships-in-plasma-storm]] (per raw/wiki/pirate-ships-in-plasma-storm.md)
