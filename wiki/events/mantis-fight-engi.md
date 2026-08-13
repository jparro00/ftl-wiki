---
id: event-mantis-fight-engi
type: event
event_name: ENGI_MANTIS_FIGHT
sectors: [[[sector-engi-controlled-sector]], [[sector-engi-homeworlds]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [forced-fight, default-rewards, no-choice, varies-text]
---

# Mantis fight (Engi) — `ENGI_MANTIS_FIGHT`

## Summary
A forced Mantis fight, flavoured for Engi space. No choices — the event exists to put a
generic Mantis ship in front of you with default rewards. One of the three Engi-specific
entries in the `HOSTILE_ENGI` pool, which is the largest allocation in the sector.

## Trigger & Where It Appears
- Sectors: [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]]
- Beacon: hostile — the event loads a hostile ship on arrival
- Event lists: `HOSTILE_ENGI` and `OVERRIDE_HOSTILE_ENGI`. `HOSTILE_ENGI` is allocated
  `min=5 max=7` in both Engi sectors — the single biggest event allocation there
  ([[source-sector-data-xml]])
- Not unique — it can recur within a run

## Text
The prose **varies**: the event uses `<text load="ENGI_MANTIS_FIGHT"/>`, drawing one of four
entries from `textList ENGI_MANTIS_FIGHT` ([[source-events-xml]], per
`raw/gamedata/events_engi.xml`). The four variants, per
[[source-fandom-mantis-fight-engi]]:

> A mixed radar signal turns out to be a Mantis attack ship scavenging the remains of an
> Engi carrier. They turn and fight.

> You come across a Mantis raider taking pot shots at a defenceless Engi supply station.
> Discovering its weapons aren't much of a match for the station's armour, it turns on your
> ship. Battle stations!

> The area looks clear, and you prepare to jump off, but a Mantis scout jumps in behind
> you! They're as surprised as you are, but their weapons are already online.

> You find a Mantis ship harrying a small squad of Engi. They make it to the node and jump
> off, leaving you toe to toe with their pursuer!

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none — forced fight)* | — | `<ship load="MANTIS_FIGHT" hostile="true"/>` — the generic Mantis ship, with **default rewards**. | 100% |

Fandom records that this ship neither surrenders nor escapes
([[source-fandom-mantis-fight-engi]]).

## Blue Options
None.

## Rewards & Risks
- Default rewards on victory; no source here states the amounts.
- Risk: a Mantis ship in Engi space is a boarding threat, and the crew you would be
  fighting are the game's best melee species. Nothing in this event mitigates that.

## Strategy Notes
- Nothing to decide — the value of this page is knowing that up to seven of the beacons in
  an Engi sector come from `HOSTILE_ENGI`, and this is one of the three Engi-flavoured
  entries in it ([[source-sector-data-xml]]). *(Opinion: Engi sectors are not the soft
  option their reputation suggests.)*

## Related
- [[event-pirate-fight-engi]], [[event-rebel-fight-engi]] — the other two `HOSTILE_ENGI` Engi entries
- [[event-engi-ship-attacked-by-mantis-ship]] — a Mantis fight you can decline
- [[entity-mantis]]

## Open Questions
- [ ] What "default rewards" resolve to numerically at a given sector depth.
- [ ] What `OVERRIDE_HOSTILE_ENGI` changes relative to `HOSTILE_ENGI`.

## Sources
- [[source-events-xml]] (per `raw/gamedata/events_engi.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-mantis-fight-engi]] (per `raw/wiki/mantis-fight-engi.md`)
