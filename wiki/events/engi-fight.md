---
id: event-engi-fight
type: event
event_name: ZOLTAN_ENGI
sectors: [[[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [unique, default-rewards, forced-fight, engi, mistaken-identity]
---

# Engi fight — `ZOLTAN_ENGI`

## Summary
A mistaken-identity fight: an Engi escort blames you for a destroyed Zoltan cruiser and
refuses all hails. No choices, no way to talk it down, default rewards. Notable mainly
because Engi ships are drone-heavy, which makes this a different combat problem from the
sector's Zoltan fights.

## Trigger & Where It Appears
- Sectors: [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]
- Beacon: hostile; a ship is shown on Long-Ranged Scanners
  ([[source-fandom-engi-fight]]).
- Reached via `HOSTILE_ZOLTAN` (vanilla) / `OVERRIDE_HOSTILE_ZOLTAN` (AE), allocated
  `min=6 max=8` beacons in both Zoltan sectors ([[source-sector-data-xml]]).
- `unique="true"` — at most once per sector.
- Despite the page title, this event is **Zoltan-sector content**; the in-game id is
  `ZOLTAN_ENGI` and it does not appear in [[sector-engi-homeworlds]] event lists.

## Text
> You jump into a debris field that used to be a Zoltan cruiser. Unfortunately, its Engi
> escort takes you for the attacker and retaliates! They refuse all hails.

(`event_ZOLTAN_ENGI_text`, per [[source-text-events-xml]])

The "debris field" is flavour only — the event carries **no `<environment>` element**, so
there is no asteroid or debris hazard in the fight
([[source-events-zoltan]], per raw/gamedata/events_zoltan.xml).

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | None. | — | `<ship load="ENGI_SHIP" hostile="true"/>` — fight an Engi ship ([[entity-engi]]), **default rewards**. | 100% |

Fandom notes `ENGI_SHIP` has **no surrender or escape values specified** in
`events_ships.xml` ([[source-fandom-engi-fight]]).

## Blue Options
None. "They refuse all hails" is flavour rather than a gated option — there is no
diplomacy branch even with relevant crew or systems.

## Rewards & Risks
- **Rewards:** default rewards for an Engi ship at the current sector depth.
- **Risks:** Engi ships are typically drone-oriented, so expect combat and defence drones
  rather than heavy weapons. No source ingested here confirms the `ENGI_SHIP` loadout, so
  that expectation is unverified.
- No environment hazard, boarders, or scripted system damage.

## Strategy Notes
- *Opinion:* a favourable beacon in this sector. Without a Super Shield to strip, laser
  builds that struggle against [[event-zoltan-fight]] resolve this quickly.
- Engi crew are poor in melee, so this is a good boarding target if you want the
  crew-kill reward tier on a fight that offers only default rewards otherwise.

> ⚠️ **CONTRADICTION (version):** which event list supplies this event.
> - `HOSTILE_ZOLTAN` (raw/gamedata/events_zoltan.xml) — 7 entries.
> - `OVERRIDE_HOSTILE_ZOLTAN` (raw/gamedata/dlcEventsOverwrite.xml) — 8 entries, adds
>   `REBEL_PULSAR`, replaces `HOSTILE_ZOLTAN` when AE content is enabled
>   ([[source-events-zoltan]]).
>
> A genuine **vanilla-vs-AE difference, not an error**.

## Related
- [[event-zoltan-fight]], [[event-pirate-fight-zoltan]], [[event-mantis-fight-zoltan]],
  [[event-zoltan-fight-in-asteroid-field]] — the rest of the hostile pool
- [[entity-engi]] — the opponent

## Open Questions
- [ ] `ENGI_SHIP` blueprint loadout by sector depth.
- [ ] Is `ZOLTAN_ENGI` reused by any non-Zoltan sector's event lists? Nothing in the
      files ingested here suggests so.

## Sources
- [[source-events-zoltan]] (per raw/gamedata/events_zoltan.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-engi-fight]] (per raw/wiki/engi-fight.md)
