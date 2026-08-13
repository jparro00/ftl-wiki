---
id: event-merchant-s-request
type: event
event_name: MERCHANT_REQUEST
sectors: [[[sector-civilian-sector]], [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-federation-space]], [[sector-pirate-controlled-sector]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]]]
beacon_type: quest
hostile: false
blue_options: []
chain: [[[chain-merchant-s-request]]]
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [quest-start, unique, drone-parts, trading]
---

# Merchant's request — `MERCHANT_REQUEST`

## Summary
A quest-start beacon that branches into one of two errands: a **delivery job** (you are
handed 5 drone parts and a marker, and get paid on arrival) or an **investigation job**
(find a missing freighter). Both are pure quest-marker starts — the delivery branch is the
only one that pays anything up front, and it pays in drone parts rather than scrap.

## Trigger & Where It Appears
- Event lists: `QUESTS`, `QUESTS_ENGI`, `QUESTS_PIRATE`, `QUESTS_REBEL`, and
  `OVERRIDE_QUESTS` under AE ([[source-newevents]], [[source-dlceventsoverwrite]])
- Sectors and quest-slot allocations ([[source-sector-data-xml]]):
  [[sector-federation-space]] `QUESTS 1–1`, [[sector-civilian-sector]] `QUESTS 0–2`,
  [[sector-engi-controlled-sector]] / [[sector-engi-homeworlds]] `QUESTS_ENGI 1–1`,
  [[sector-pirate-controlled-sector]] `QUESTS_PIRATE 0–1`,
  [[sector-rebel-controlled-sector]] / [[sector-rebel-stronghold]] `QUESTS_REBEL 0–2`
- `unique="true"` ([[source-events-xml]])
- Beacon: no ship staged; `<img planet="PLANET_POPULATED_SMALL"/>`.
  [[source-fandom-merchant-s-request]] marks `LRSmap=noship`.

> ⚠️ **CONTRADICTION:** sector coverage.
> - Game files: `QUESTS` is allocated `min=1 max=1` in `STANDARD_SPACE`
>   ([[source-sector-data-xml]]), so [[sector-federation-space]] is in scope.
> - Fandom: lists six sectors, omitting Federation space
>   ([[source-fandom-merchant-s-request]]).
>
> Trusting the game files (`high` vs `medium`) — the same omission recurs on every
> `QUESTS`-list event and looks like a wiki template convention.

## Text
> You arrive at a populated sector. One merchant seems to be mass-broadcasting a request
> for a mercenary ship to aid him. Shall we respond?

(`event_MERCHANT_REQUEST_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Yes. | — | Loads `eventList MERCHANT_REQUEST_LIST` — 2 entries, below. | see below |
| 2 | No. | — | Nothing happens. | 100% |

### `eventList MERCHANT_REQUEST_LIST` (2 entries)
Assuming uniform selection across `eventList` entries ([[concept-event-list-weighting]]),
each errand is offered **1/2** of the time.

**Entry 1 — the delivery**
> "Great, I was worried no one would respond. My usual carrier is days late. I need you to
> deliver this cargo of drone parts to a small station a few jumps from here. We can't
> afford to pay another carrier, but they will surely tip you generously."

| Choice | Outcome |
|---|---|
| Accept. | *"Great! I uploaded their location to your star map…"* → **+5 drone parts** (`<item type="drones" min="5" max="5"/>`) and `<quest event="MERCHANT_DELIVER"/>`. See [[event-merchant-deliver]]. |
| Decline. | *"Fine, I'll keep looking for someone who wishes to make some easy money..."* → nothing. |

**Entry 2 — the investigation**
> "Your ship seems reasonably equipped... A freighter carrying a shipment of my goods is a
> week late. The fools flew through a pirate-filled sector in their haste and I fear for
> the cargo's safety. I'm looking for a less incompetent captain to investigate."

| Choice | Outcome |
|---|---|
| Accept. | *"At least you're confident, for what little that's worth. Here is their last known location."* → `<quest event="MERCHANT_INVESTIGATE"/>`, **no up-front payment**. See [[event-merchant-investigate]]. |
| Decline. | *"At least YOU are willing to admit your incompetence…"* → nothing. |

> ⚠️ **CONTRADICTION:** entry-1 prose.
> - Game files: *"**We can't afford to pay another carrier**, but they will surely tip you
>   generously."* (`event_MERCHANT_REQUEST_LIST_1_text`, [[source-text-events-xml]])
> - Fandom: *"**I'll pay you a bit of scrap now**, but they will surely tip you
>   generously."* ([[source-fandom-merchant-s-request]])
>
> Trusting the game files (`high` vs `medium`). The wiki's wording would imply a scrap
> payment that the XML does not contain — the only up-front effect is `+5 drone parts`.
> Most likely pre-AE wording that was rewritten when the reward changed; not confirmed as
> a version difference.

## Blue Options
None on this event. The blue options in this quest line all sit on the destination events —
Mind Control and Weapons 6 on [[event-merchant-deliver]], Teleporter on
[[event-merchant-investigate]].

## Rewards & Risks
- Entry 1: **+5 drone parts** immediately. The parts are consumed on delivery (all payout
  branches at [[event-merchant-deliver]] take `drones -5`), so treat them as cargo, not
  income — spending them elsewhere forfeits the payout.
- Entry 2: nothing up front; the reward is whatever [[event-merchant-investigate]] rolls,
  which can include a free crew member or a free weapon.
- Risk: neither branch is dangerous *here*. The danger is at the destinations — one
  `MERCHANT_INVESTIGATE` outcome is an unavoidable pirate fight.

## Strategy Notes
- If you take the delivery, **do not spend the 5 drone parts**. Every paying branch at the
  destination deducts exactly 5. *(Read off `<item type="drones" min="-5" max="-5"/>` on
  each payout branch, [[source-events-xml]]; no source states the warning.)*
- The investigation branch has the higher ceiling (crew member, random weapon, `HIGH
  standard`) and the higher variance.

## Related
- [[event-merchant-deliver]] — entry 1's quest marker
- [[event-merchant-investigate]] — entry 2's quest marker
- [[event-merchant-investigate-deliver]] — the follow-on marker from the investigation
- [[event-research-station-with-no-response]] — the "station doesn't respond" sub-tree reused by the delivery
- [[chain-merchant-s-request]]

## Open Questions
- [ ] Confirm `eventList` selection is uniform — the 1/2 split depends on it.
- [ ] Is the Fandom entry-1 wording a genuine pre-AE string, or a transcription error?

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-fandom-merchant-s-request]] (per raw/wiki/merchant-s-request.md)
