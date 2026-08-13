---
id: event-rebel-fight-lanius
type: event
event_name: LANIUS_REBEL_FIGHT
sectors: [[[sector-abandoned-sector]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [lanius, rebel, combat, no-choice, default-rewards, advanced-edition]
---

# Rebel fight (Lanius) — `LANIUS_REBEL_FIGHT`

## Summary
A standard Rebel fight with Abandoned Sector flavour text. The enemy is the generic
`REBEL` ship definition; everything sector-specific is in the six intro strings, which
between them are the best in-fiction account of how the Rebellion is coping with the
Lanius incursion — badly, and while still prioritising hunting you.

## Trigger & Where It Appears
- Sector: [[sector-abandoned-sector]] only.
- List: `HOSTILE_LANIUS`, allocated `min=5 max=6` beacons per sector
  ([[source-sector-data-xml]]); six members → **1/6** *assuming uniform selection across
  list entries* ([[source-dlcevents-anaerobic]]). Note the same list also contains the
  plain `REBEL` and `REBEL_AUTO` events, so Rebel ships are over-represented among this
  sector's fights relative to Lanius ones.
- No `unique` attribute → repeats freely.
- Long-range scanners show a ship ([[source-fandom-rebel-fight-lanius]]).

> **AE-only** as an event; the `REBEL` enemy itself is vanilla content.

## Text
`[varies: textList LANIUS_REBEL_FIGHT_TEXT]` — six strings,
`text_LANIUS_REBEL_FIGHT_TEXT_1` through `_6`, none duplicated → **1/6** each *assuming
uniform selection across list entries* ([[source-dlcevents-anaerobic]],
[[source-text-events-xml]]). All six are transcribed on
[[source-fandom-rebel-fight-lanius]]. For example:

> You intercept discussions between a Rebel patrol and a human mining colony, "... we
> realize you're scared but all reports indicate the metal bastards target abandoned
> settlements only. If we relocated our fleets based on every request from backwater...
> wait, what's that..." Before you can react, the channel is cut and the Rebel ship moves
> in to attack.

> You arrive at the beacon and notice a small Rebel ship chasing Lanius scavengers away
> from a wrecked Rebel battleship. As soon as the Rebel notices you and moves in to attack,
> the Lanius ships return to their prey like flies on garbage.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(none)_ | — | Immediate combat with the standard `REBEL` ship; **default rewards**. | 100% |

The `REBEL` definition ([[source-events-ships]]): surrender `chance="0.5" min="2" max="3"`
→ `PIRATE_SURRENDER`; escape `chance="0.5" min="3" max="4"` → `PIRATE_ESCAPE`; destroyed →
`DESTROYED_DEFAULT`; dead crew → `DEAD_CREW_DEFAULT`.

## Blue Options
None.

## Rewards & Risks
- Reward: default rewards.
- Risk: an ordinary Rebel warship, sector-scaled. No avoid option.

## Strategy Notes
- Nothing to decide. Worth noting only that three of `HOSTILE_LANIUS`'s six members are
  Rebel or Rebel-auto ships, so the "Lanius sector" fights Rebels about as often as it
  fights Lanius.

## Related
- [[event-lanius-fight]], [[event-pirate-fight-lanius]] — the other flavoured fights in
  `HOSTILE_LANIUS`
- [[event-lanius-ship-absorbing-automated-scout]],
  [[event-lanius-ship-absorbing-rebel-base]] — the events where the Lanius eat Rebel
  hardware instead
- [[entity-rebels]], [[sector-abandoned-sector]]
- [[event-pirate-surrender]] — the shared `PIRATE_SURRENDER` aftermath this hull loads
- [[event-pirate-escape]] — the shared `PIRATE_ESCAPE` aftermath this hull loads

## Open Questions
- [ ] Numeric values behind "default rewards".

## Sources
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml — the `REBEL` ship)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-rebel-fight-lanius]] (per raw/wiki/rebel-fight-lanius.md)
