---
id: event-boarders-crystal
type: event
event_name: BOARDERS_CRYSTAL
sectors: [[[sector-hidden-crystal-worlds]]]
beacon_type: any
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [boarders, crew-risk, no-choices]
---

# Boarders: Crystal — `BOARDERS_CRYSTAL`

## Summary
The [[sector-hidden-crystal-worlds]] boarding event. No choices, no enemy ship — 2–3
Crystalline boarders simply teleport aboard and you fight them in your own corridors.
Crystal boarders are the hardest boarding party in the game to handle because
[[entity-crystal-men]] can lock a room down, so this is the sector's main crew-loss
threat outside of ship combat.

## Trigger & Where It Appears
- Sector: [[sector-hidden-crystal-worlds]] only
- Allocation: `BOARDERS_CRYSTAL` is placed `min=1 max=2` per sector
  ([[source-sector-data-xml]])
- `unique="false"` — it can fire at more than one beacon in the same sector
  ([[source-events-xml]])
- Beacon: an ordinary beacon; the Fandom page records it as showing **no ship** on
  Long-Range Scanners despite the boarding ([[source-fandom-boarders-crystal]])

## Text
The intro text **varies** — `<text load="BOARDERS_CRYSTAL"/>` draws from the three-entry
`BOARDERS_CRYSTAL` text list ([[source-events-xml]]). All three variants
([[source-text-events-xml]]):

> You detect a heavily armed Crystalline ship escorting some sort of prison vessel. Scans
> indicate there are a number of non-Crystal based life forms aboard; they must be
> rounding up all of the intruders in their space! Before you can react, you hear the
> telltale sounds of a teleporter going off.

> You arrive near a small settlement and a lone guard ship moves to intercept you. You try
> to contact them but they are refusing all hails. Suddenly you hear lasers ricocheting
> from within the ship. You've been boarded!

> You pick up chatter from a nearby ship, "Yes... Here are some interesting specimens. Try
> to take them alive this time, there's a lot of money to be had on aliens." Scanners
> indicate a remote teleporter was just used.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _none — the event has no choice nodes_ | — | `<boarders min="2" max="3" class="crystal"/>` → 2–3 Crystalline boarders teleport aboard | 100% |

The number of boarders inside the 2–3 band is not weighted in the file.
([[source-events-xml]])

## Blue Options
- None. There is no `req` on this event at all.

## Rewards & Risks
- **Reward:** none directly. Killing the boarders yields nothing beyond the usual
  no-reward boarding resolution — the event has no `autoReward`.
- **Risk:** crew loss, hull damage from the fight, and system damage in whatever room the
  boarders land in.

## Strategy Notes
- There is nothing to decide here, so the whole event is your standing anti-boarding
  setup: doors level, medbay, and where your crew is parked when you jump.
- Because the sector allocates 1–2 of these on top of 6–10 hostile beacons, arriving in
  [[sector-hidden-crystal-worlds]] with a weak crew-combat answer is the main way the
  sector kills a run. *(Opinion, inferred from the allocation in
  [[source-sector-data-xml]] — no source states it.)*

## Related
- [[sector-hidden-crystal-worlds]] — the only sector this appears in
- [[entity-crystal-men]] — the boarders
- [[event-crystalline-cache]] — a different route to the same 2–3 Crystal boarders
- [[event-crystalline-ship-messaging-about-rebels]] — 1–2 Crystal boarders on a bad outcome

## Open Questions
- [ ] Whether the three text variants are drawn evenly (the list has three distinct
      entries with no repeats, unlike most FTL text lists).
- [ ] Whether Crystal boarders here can use lockdown (not stated in any source ingested).

## Sources
- [[source-events-xml]] (per raw/gamedata/events_crystal.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-boarders-crystal]] (per raw/wiki/boarders-crystal.md)
