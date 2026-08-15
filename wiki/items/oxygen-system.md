---
id: item-oxygen-system
type: item
item_kind: system
rarity: 1
unlocks_blue: [[[event-slug-hacker-oxygen]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-14
sources: 6
tags: [system, subsystem]
---

# Oxygen

## Summary
The `oxygen` subsystem — *"Refills the oxygen in the ship. Upgrading increases the rate of
refill."* ([[source-text-blueprints]]).

## Stats
- Blueprint `oxygen` (`<systemBlueprint>`), [[source-blueprints]].
- Power: `startPower` 1, `maxPower` 3.
- Purchase cost: **0** scrap — the only system in the file priced at zero.
- Upgrade costs: level 2 = 25, level 3 = 50, plus a 75-scrap entry the file annotates as an *"imaginary level 4"*.
- `rarity` 1.

### Refill rates
Not in `raw/gamedata/` — no XML in the game files states an oxygen rate. From
[[source-fandom-oxygen]] and [[source-xftl-oxygen-mechanics]], which agree:

| Level | Cost | Refill | Multiplier |
|---|---|---|---|
| 1 | — | 1.2 %/sec | ×1 |
| 2 | 25 scrap | 4.8 %/sec | ×4 |
| 3 | 50 scrap | 8.4 %/sec | ×7 |

The costs match this file's own `blueprints.xml` figures above, which is useful corroboration
that those sources describe this build.

**Level 1 exactly cancels the unpowered drain** (1.2%/sec each way) — it holds a sealed ship
steady and does nothing against breaches, fires or airlocks. Level 2 counters a single breach or
one Lanius, and outruns a Hacking-3 pulse. Full rate table and the venting model:
[[concept-oxygen-and-suffocation]].

> ⚠️ **CONTRADICTION — the game's own UI is wrong.** The ship upgrade menu advertises refill
> multipliers of **1/3/6**. Both external sources independently give **1/4/7**, with
> [[source-xftl-oxygen-mechanics]] naming 1/3/6 as *"the multipliers listed in the UI"* and
> incorrect. Not a source disagreement — a display bug. Levels 2 and 3 are better than advertised.

## How To Get It
- Present on every ship. Upgrades bought at stores.
- `TRADER_UPGRADES_LIST` and `HIGH_SCAN_TERRAFORMING` both grant `<upgrade system="oxygen" amount="1"/>` — [[event-trade-scrap-for-upgrades]] and [[event-terraforming-scan]] ([[source-newevents]]).

## Blue Options It Unlocks
- [[event-slug-hacker-oxygen]] — `NEBULA_SLUG_OXYGEN`, `lvl="2"` — the only genuine `req="oxygen"` blue option in the game
- `TRADER_UPGRADES_LIST` also uses `req="oxygen"`, but with `max_lvl` and `blue="false"` —
  an inverse gate hiding the "buy an upgrade" choice once Oxygen is already at that level.
  **Not** a blue option. ([[event-trade-scrap-for-upgrades]], [[source-newevents]])

## Strategy Notes
- One blue option in the entire game. Oxygen upgrades are bought for survivability, never
  for event access.
- [[item-emergency-respirators]] and [[item-lanius-crew]] both interact with low oxygen but
  satisfy different `req` values.
- **Free to buy, and level 2 is the real breakpoint.** The system costs 0 scrap — the only one
  in the file priced at zero — so the whole decision is the 25-scrap first upgrade, which is
  what converts Oxygen from "holds a sealed ship" to "beats a breach".

## Related
- [[concept-oxygen-and-suffocation]] — the rates, the venting model, and what suffocation costs
- [[item-emergency-respirators]] — halves suffocation damage (6.4 → 3.2 HP/sec)
- [[item-lanius-crew]] — drains oxygen at a breach's rate, immune to suffocation
- [[item-medbay]] — a powered level 1 negates suffocation damage outright in its room
- [[item-doors]] — venting is the usual reason oxygen matters
- [[item-hacking]] — a Hacking-3 pulse on this system is a drain level 2 can outrun

## Open Questions
- [ ] What the "imaginary level 4" upgrade entry is for. Neither external source mentions a
      level 4 — [[source-fandom-oxygen]]'s upgrade table stops at 3.
- [ ] Whether the 1/3/6 UI display bug has since been patched.

## Sources
- [[source-blueprints]] (per raw/gamedata/blueprints.xml)
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-fandom-oxygen]] (per raw/wiki/oxygen.md)
- [[source-xftl-oxygen-mechanics]] (per raw/modding/2026-08-14-xftl-oxygen-mechanics.txt)
