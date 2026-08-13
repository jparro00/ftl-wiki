---
id: event-crystal-fight-with-surrender-offer-hull-repairs
type: event
event_name: CRYSTAL_CONVOY
sectors: [[[sector-hidden-crystal-worlds]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unique, combat, surrender, hull-repair, no-choices]
---

# Crystal fight with surrender offer (hull repairs) — `CRYSTAL_CONVOY`

## Summary
A forced fight against a convoy escort that, once beaten down, offers a truce worth
**8 hull repairs** plus fuel and scrap. That makes it the best-value fight in
[[sector-hidden-crystal-worlds]] — provided you can damage it without killing it.

## Trigger & Where It Appears
- Sector: [[sector-hidden-crystal-worlds]] only
- Pool: one of **7** entries in the `HOSTILE_CRYSTAL` event list, allocated `min=6 max=10`
  per sector ([[source-events-xml]], [[source-sector-data-xml]])
- `unique="true"` — at most once per run ([[source-events-xml]])
- Beacon: shows a **ship** on Long-Range Scanners
  ([[source-fandom-crystal-fight-with-surrender-offer-hull-repairs]])

## Text
> A large convoy of lumbering civilian ships appears to be passing through this region. You
> show no hostile intentions, but they are taking no chances, immediately sending their
> escort to attack!

(`event_CRYSTAL_CONVOY_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _none — the event has no choice nodes_ | — | `<ship load="CRYSTAL_CONVOY" hostile="true"/>` → immediate combat | 100% |

### Sub-outcome: they offer to stop the fight
Defined on the `CRYSTAL_CONVOY` ship entry, `<surrender chance="0" min="3" max="4">`
([[source-events-xml]], per raw/gamedata/events_ships.xml):

> Their ship seems severely damaged and they look to be reconsidering the fight. Should you
> power down your weapons and explain that you mean no threat?

| # | Choice | Outcome(s) |
|---|--------|-----------|
| 1 | Stop the fight. | Ship becomes non-hostile; they turn out to be miners and colonists fleeing pirate and Rebel attacks → `autoReward level="LOW"` **fuel** (Fandom: 1–3 fuel and scrap) and `damage amount="-8"` → **8 hull repairs**. |
| 2 | Finish them off. | The fight continues. |

### Sub-outcome: you win outright
Both `destroyed` and `deadCrew` give `autoReward level="MED"` **standard** — medium scrap
with resources — with flavour noting the rest of the convoy escaped in the meantime.
([[source-events-xml]], [[source-fandom-crystal-fight-with-surrender-offer-hull-repairs]])

## Blue Options
- None.

## Rewards & Risks
- **Best case:** 8 hull repairs + low fuel-and-scrap. Hull repair is otherwise only
  purchasable, and this sector has no repair-station allocation of its own beyond
  `ITEMS_CRYSTAL`.
- **Alternative:** medium scrap with resources for a kill.
- **Risk:** a live warship fight. Killing it too fast forfeits the repairs entirely.

## Strategy Notes
- If your hull is low, this is the beacon you want to *win slowly*: stop firing once the
  surrender prompt appears rather than pushing through to the kill.
  *(Opinion — sourced only as the mechanical trade-off above.)*
- The surrender branch is a strict upgrade over the kill when your hull is more than ~8
  short, since medium standard scrap does not buy 8 repairs at typical store prices.
  *(Opinion, not sourced.)*

> ⚠️ **CONTRADICTION:** the surrender-offer chance.
> - Game files: `<surrender chance="0" min="3" max="4">` on `CRYSTAL_CONVOY`
>   ([[source-events-xml]], per raw/gamedata/events_ships.xml).
> - Fandom: its `SurrenderEscape` footnote for `CRYSTAL_CONVOY` is flagged
>   `surrenderofferchance100`, i.e. the offer is claimed to be **guaranteed**
>   ([[source-fandom-crystal-fight-with-surrender-offer-hull-repairs]]) — and the page
>   title itself is "…with surrender offer".
> Read literally the file says the offer never fires, which cannot be right given the page
> exists and is named for the offer; the likeliest explanation is that the engine treats
> `chance="0"` on a surrender block as "always" rather than "never", but **no ingested
> source states that**. Recording both; the behavioural claim (Fandom) is the one to plan
> around, the raw attribute is the one to re-check.

## Related
- [[sector-hidden-crystal-worlds]]
- [[event-crystal-fight]] — `CRYSTAL_SHIP`, the surrender that can give crew
- [[event-crystal-fight-with-surrender-offer-human-crew]] — `CRYSTAL_HUNTER`
- [[entity-crystal-men]]
- [[concept-surrender-offers]]

## Open Questions
- [ ] Resolve `chance="0"` vs the "always offered" claim above.
- [ ] Whether the 8 repairs are capped by your current hull deficit.
- [ ] Exact scrap in "low fuel and scrap" (`autoReward LOW fuel`).

## Sources
- [[source-events-xml]] (per raw/gamedata/events_crystal.xml, raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-crystal-fight-with-surrender-offer-hull-repairs]] (per raw/wiki/crystal-fight-with-surrender-offer-hull-repairs.md)
