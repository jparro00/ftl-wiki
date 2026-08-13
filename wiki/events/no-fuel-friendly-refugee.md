---
id: event-no-fuel-friendly-refugee
type: event
event_name: NO_FUEL_REFUGEE_FRIENDLY
sectors: []
beacon_type: any
hostile: false
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [out-of-fuel, refugee, free-reward, no-choice, advanced-edition, derived-odds]
---

# No fuel: friendly refugee — `NO_FUEL_REFUGEE_FRIENDLY`

## Summary
Pure charity, and the only unconditional-gain draw in the distress-beacon-**off**
out-of-fuel pool. A refugee ship that has been quietly following you turns up, recognises
the Federation colours, and splits its fuel with you. No choices, no ship, no catch.
Advanced Edition only.

## Trigger & Where It Appears
- **Not a sector event.** Member of the `NO_FUEL` list — the distress-beacon-**off**
  out-of-fuel pool ([[source-events-fuel]]). Fandom marks it `outoffuel=distressoff`
  ([[source-fandom-no-fuel-friendly-refugee]]).
- Prerequisites: 0 fuel, distress beacon off, and you choose to wait.

**Version: `ae`.** Its entry in the `NO_FUEL` list is annotated
`<event load="NO_FUEL_REFUGEE_FRIENDLY"/> <!-- DLC - below -->`, and the event itself sits
under the file's `DLC!!! / Events added with the DLC` header ([[source-events-fuel]]). It
does not exist in vanilla.

**Derived odds.** 1/11 (~9.1%) per wait, from the 11-entry AE `NO_FUEL` list. *Assumes
uniform selection across list entries.* Adding this entry is also what shifts every other
member of that list from 1/10 to 1/11 — the AE and vanilla out-of-fuel odds differ purely
because of this event and its distress-on counterpart.

## Text
> A refugee ship fleeing the Rebel advance enters the system. It seems surprised to see you
> stranded, and admits it was following you from afar in the hopes of you leading it to
> Federation space. While it doesn't have much fuel to spare, it recognizes you are part of
> the Federation and offers to split its remaining fuel with you.

(`event_NO_FUEL_REFUGEE_FRIENDLY_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none — a `<text>` plus an `<autoReward>`)* | — | `autoReward level="MED"` **fuel_only**. Fandom reads `MED` fuel_only as **2–4 fuel** ([[source-fandom-no-fuel-friendly-refugee]]). | 100% |

No `<ship>` tag — the refugee vessel never appears as a combat target.

## Blue Options
None.

## Rewards & Risks
- `MED` fuel_only, free, guaranteed. No scrap, no risk, no branch.
- Note it is a **fuel_only** reward, so unlike the `fuel` variant used elsewhere in this
  file it carries no scrap component.

## Strategy Notes
- *Opinion:* one of two reasons the distress-off pool is not simply worse than distress-on
  — the other being [[event-no-fuel-rebel-fleet-delay]]. Between them, roughly 2/11 of
  distress-off waits are strictly good, against a distress-on pool where the equivalent
  friendly-refugee outcome is only 1/36 and pays the smaller `LOW` tier.
- Nothing to play — it resolves itself.

## Related
- [[event-no-fuel-refugee-damaged]], [[event-no-fuel-refugee-pirate]] — the two AE refugee
  events on the distress-on side, both of which *do* have catches
- [[event-no-fuel-rebel-fleet-delay]] — the other purely good distress-off draw
- [[concept-out-of-fuel]]

## Open Questions
- [ ] Exact fuel value of `autoReward level="MED"` fuel_only — Fandom's 2–4 is the only
      figure any source gives.

## Sources
- [[source-events-fuel]] (per raw/gamedata/events_fuel.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-fandom-no-fuel-friendly-refugee]] (per raw/wiki/no-fuel-friendly-refugee.md)
