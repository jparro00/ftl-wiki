---
id: event-zoltan-wise-man
type: event
event_name: ZOLTAN_RIFT_FIGHT
sectors: [[[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: any
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unique, choose-your-enemy, scrap-reward, cut-content]
---

# Zoltan wise man — `ZOLTAN_RIFT_FIGHT`

## Summary
A mad Zoltan opens a wormhole and lets you **pick your opponent** — Mantis, Slug, or
Rock. There is no way out; all three choices are fights. The payoff is unusually good
for a forced fight: the normal ship reward *plus* a second `HIGH` scrap-with-resources
payout from the wise man detonating himself afterwards.

## Trigger & Where It Appears
- Sectors: [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]
- Beacon: ordinary, no ship shown on Long-Ranged Scanners
  ([[source-fandom-zoltan-wise-man]]).
- Reached via the `NEUTRAL_ZOLTAN` event list, allocated `min=5 max=6` beacons in both
  Zoltan sectors ([[source-sector-data-xml]]) — despite being a guaranteed fight.
- `unique="true"`.

## Text
> You come to a quiet part of Zoltan space and encounter an ancient Zoltan wise man who
> has managed to harness the power of a spatial rift, but seems to have been driven
> completely mad by the power. "Choose your doom," he demands. This is all part of a
> day's work.

(`event_ZOLTAN_RIFT_FIGHT_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Mantis. | — | *"'You like a challenge. So be it!' A wormhole forms and a confused, angry Mantis ship hurtles toward you!"* → `<ship load="ZOLTAN_RIFT_MANTIS" hostile="true"/>`. Fandom adds: crew **entirely composed of Mantis**. | 100% |
| 2 | Slug. | — | *"'Do not be fooled, Federation, by a soft underbelly.' …a Slug ship is attacking from the other direction!"* → `<ship load="ZOLTAN_RIFT_SLUG" hostile="true"/>`. | 100% |
| 3 | Rockmen. | — | *"'A hardened foe for a hardened veteran.' …a Rock ship appears with guns blazing."* → `<ship load="ZOLTAN_RIFT_ROCK" hostile="true"/>`. | 100% |

**There is no "leave" option.** Once you arrive, one of the three fights happens.

### After the fight

All three paths converge on the same reward structure
([[source-fandom-zoltan-wise-man]] for the ship rewards,
[[source-events-zoltan]] for the follow-up event):

| Win condition | Ship reward | Then |
|---------------|-------------|------|
| Destroyed the ship | `low` scrap with resources | → `ZOLTAN_RIFT_SUCCESS` |
| Killed the crew | `medium` scrap with resources | → `ZOLTAN_RIFT_SUCCESS` |

`ZOLTAN_RIFT_SUCCESS`:
> When he sees you have emerged victorious, the Zoltan wise man enters a rage. Rifts
> threaten to tear space apart until, instead, the Zoltan implodes, sending a blast wave
> of scrap and salvage dragged here from distant worlds in your direction.

`autoReward level="HIGH"` `standard` — **high scrap with resources on top of the ship
reward, regardless of how you won** ([[source-events-zoltan]], per
raw/gamedata/events_zoltan.xml).

## Blue Options
None. No `req` attribute on any choice.

## Cut content
The game file contains a **fourth, commented-out option** to fight a Crystalline ship:

> `<text>Crystalline Beings.</text>` … *"The Zoltan is quiet for a moment, and then
> whispers, 'Are you sure? Well, so be it then.' A huge wormhole opens, and from within
> it looms a Crystalline ship, prepared for war."* … `<ship load= ?!?!  JUSTIN DO THIS
> STILL!!!!!!! JUSTIN - TO DO`

The `<ship load=` was never filled in. Both sources agree the option is unfinished and
disabled ([[source-events-zoltan]], [[source-fandom-zoltan-wise-man]]). It is not reachable
in play.

## Rewards & Risks
- **Reward:** `low`/`medium` scrap with resources from the ship, **plus** `HIGH` scrap
  with resources from `ZOLTAN_RIFT_SUCCESS`. This is a double payout and is the reason
  to like the beacon.
- **Risk:** one unavoidable ship fight against a sector-scaled enemy. No crew-loss or
  system-damage effects are scripted.

## Strategy Notes
- *Opinion:* pick the opponent your build handles best, not the one that sounds easiest.
  A Mantis ship arrives with an all-Mantis crew, which is the worst case for boarding
  defence but the best case for a ship that just wants to shoot; a Rock ship is the
  tankiest hull; a Slug ship is the least predictable. No source here gives the three
  ships' loadouts, so this is a judgement call rather than a sourced ranking.
- Killing the crew rather than destroying the hull upgrades the first reward tier
  (`low` → `medium`) and does not affect the second.

## Related
- [[entity-mantis]], [[entity-slugs]], [[entity-rock-men]] — the three
  opponents
- [[event-zoltan-security-checkpoint]], [[event-zoltan-retake-the-ship]] — the other
  unique `NEUTRAL_ZOLTAN` members in this batch
- [[concept-cut-content]] — the unfinished Crystalline branch

## Open Questions
- [ ] Loadouts of `ZOLTAN_RIFT_MANTIS`, `ZOLTAN_RIFT_SLUG`, `ZOLTAN_RIFT_ROCK` (needs
      `events_ships.xml`) — needed to rank the three choices properly.
- [ ] Do any of the three ships offer surrender or escape?
- [ ] Does fleeing the fight forfeit the `ZOLTAN_RIFT_SUCCESS` payout?

## Sources
- [[source-events-zoltan]] (per raw/gamedata/events_zoltan.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-zoltan-wise-man]] (per raw/wiki/zoltan-wise-man.md)
