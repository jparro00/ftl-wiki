---
id: event-lanius-ship-attacking-mantis
type: event
event_name: LANIUS_MANTIS_DISTRESS
sectors: [[[sector-abandoned-sector]]]
beacon_type: distress
hostile: false
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [lanius, mantis, distress, optional-fight, missiles, unique, advanced-edition]
---

# Lanius ship attacking Mantis — `LANIUS_MANTIS_DISTRESS`

## Summary
A Mantis ship is being mined for parts and its distress beacon is failing. You can save
the Mantis or let them be eaten. Saving them means a no-surrender Lanius fight followed by
a two-way aftermath roll — grateful missiles, or a wreck to strip.

## Trigger & Where It Appears
- Sector: [[sector-abandoned-sector]] only.
- List: `DISTRESS_BEACON_LANIUS`, allocated `min=1 max=2` per sector
  ([[source-sector-data-xml]]); twelve members → **1/12** *assuming uniform selection
  across list entries* ([[source-dlcevents-anaerobic]]).
- Carries `<distressBeacon/>`; `unique="true"`.
- Long-range scanners show **no** ship, despite two of them being present
  ([[source-fandom-lanius-ship-attacking-mantis]]) — the event defines its enemy inside a
  choice rather than up front.
- One of a family of four "Lanius eats a named species" distress events written by the
  same hand (the file comments them "Chris's"): Slug, Mantis, Rock and the generic trap.

> **AE-only** — Advanced Edition file and sector.

## Text
> The Mantis ship in this system looks like its distress beacon is malfunctioning...
> likely due to the Lanius ship mining their hull and sub-systems! It doesn't look like
> the Mantis ship will last much longer.

(`event_LANIUS_MANTIS_DISTRESS_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Attack the Lanius ship. | — | *"The Lanius don't seem to have noticed you yet - but they will…"* → combat with `LANIUS_MANTIS_DISTRESS_SHIP`. Destroyed **or** dead crew → `MED standard`, then **Contact the Mantis** below. | 100% |
| 2 | Leave the Mantis to their fate. | — | *"The Mantis ship is quickly overcome by the Lanius vessel, and you move away as the Lanius feed on the remains."* → nothing happens. | 100% |

### Contact the Mantis (`LANIUS_MANTIS_DISTRESS_END`)
Two members, **1/2** each *assuming uniform selection across list entries*
([[source-dlcevents-anaerobic]]):

| Result | Payload |
|---|---|
| The Mantis survive and pay you off in scrap and missiles they can no longer use | `autoReward MED missiles` — Fandom expands this as **2-4 missiles** plus scrap ([[source-fandom-lanius-ship-attacking-mantis]]) |
| No survivors; you strip the wreck | `autoReward MED standard` |

## Blue Options
None. There is no Lanius-crew de-escalation here, unlike
[[event-lanius-ship-attacking-civilian-distress]].

## Rewards & Risks
- The enemy `LANIUS_MANTIS_DISTRESS_SHIP` (`auto_blueprint="SHIPS_LANIUS"`) has **no
  surrender and no escape** entries — it is a fight to the finish
  ([[source-dlcevents-anaerobic]]).
- Unusually, destroyed and dead-crew pay the same (`MED standard`), so there is no reason
  to prefer boarding for reward's sake here.
- Guaranteed `MED` from the fight plus a guaranteed second `MED` from the aftermath list —
  this is one of the better-paying optional fights in the sector.
- Risk: the whole fight is optional; choice 2 costs nothing.

## Strategy Notes
- Both aftermath results pay, so the only question is whether your ship can take a
  no-surrender Lanius warship. If it can, this is worth taking — the payout is two medium
  rewards rather than one.
- Missile-hungry builds should note the 1/2 chance at a missile-flavoured payout.

## Related
- [[event-lanius-fight-distress]], [[event-lanius-ship-attacking-civilian-distress]],
  [[event-lanius-empty-distress-beacon-1]], [[event-lanius-empty-distress-beacon-2]] —
  the rest of the `DISTRESS_BEACON_LANIUS` pool covered so far
- [[entity-mantis]], [[entity-lanius]], [[sector-abandoned-sector]]

## Open Questions
- [ ] Numeric values behind `MED missiles` (Fandom says 2-4 missiles; the XML says only
      `MED`).
- [ ] Sibling events `LANIUS_SLUG_DISTRESS` and `LANIUS_ROCK_DISTRESS` are in the same
      list and not yet paged.

## Sources
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-lanius-ship-attacking-mantis]] (per raw/wiki/lanius-ship-attacking-mantis.md)
