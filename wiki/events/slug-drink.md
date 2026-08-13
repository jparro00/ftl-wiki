---
id: event-slug-drink
type: event
event_name: SLUG_DRINK
sectors: [[[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: nebula
hostile: false
blue_options: [rock crew]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unique, nebula, blue-option, hull-repair, store-chance, scrap-loss-risk, default-rewards]
---

# Slug drink — `SLUG_DRINK`

## Summary
A Slug captain boards your ship uninvited with a flask and a toast. Drinking is a coin
flip: 10 hull repaired plus a store, or waking up 25–35 scrap lighter. Refusing guarantees
a fight. A Rockman posing as captain shifts the coin flip's downside from theft to combat —
and keeps the same upside.

## Trigger & Where It Appears
- Sectors: [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]] — via the
  `NEBULA_NEUTRAL_SLUG` event list (`min 3 / max 5` per sector)
  ([[source-events-slug]], [[source-sector-data-xml]])
- Beacon: nebula (`<environment type="nebula"/>`), `unique="true"`
- A `JELLY` ship is present **non-hostile** from arrival ([[source-events-slug]])

## Text
> A Slug captain hails and invites himself aboard your ship to present a flask of something
> slimy. "Now, most gracioussss captain, you must join me please in a drink to our
> alliance!"

(`event_SLUG_DRINK_text`, per [[source-text-events-xml]])

## Choices & Outcomes

All three choices are `hidden="true"`.

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Drink. | — | Rolls `SLUG_DRINK_DRINK` — 2 entries, below. | see below |
| 2 | Refuse. | — | "The Slug feigns offense…" → `<ship hostile="true"/>` — the waiting `JELLY` attacks. Default rewards. | 100% |
| 3 | **(Rock Crew)** Have your Rockman pose as captain. | `req="rock"` | Rolls `SLUG_DRINK_ROCK` — 2 entries, below. | see below |

### `SLUG_DRINK_DRINK` (choice 1)

| Entry | Text | Effect |
|---|---|---|
| 1 | "It's foul, but doesn't do any lasting damage… this Slug actually seems to be trustworthy." | `<damage amount="-10"/>` — **+10 hull** — and `<store/>` opens |
| 2 | "You take one gulp and wake up with the rest of the crew in the cargo hold…" | `<item_modify steal="true"><item type="scrap" min="-35" max="-25"/></item_modify>` — **lose 25–35 scrap** |

### `SLUG_DRINK_ROCK` (choice 3)

| Entry | Text | Effect |
|---|---|---|
| 1 | "…you doubt it would affect the Rock digestive system." | `<damage amount="-10"/>` — **+10 hull** — and `<store/>` opens |
| 2 | "Your crewmember is able to identify a heavy anaesthetic… His ruse discovered, the Slug immediately returns to his ship and opens fire." | `<ship hostile="true"/>` — default rewards |

## Blue Options
- **Rock crew member** (`req="rock"`) — same 50/50 on the good outcome, but the bad half
  becomes a default-rewards fight instead of an unavoidable 25–35 scrap theft. Since you
  keep whatever the fight pays, it strictly dominates choice 1 unless your ship cannot
  afford another fight.

## Rewards & Risks
- Upside (both drink paths): **10 hull repaired and a store** — one of the better free
  outcomes available in Slug space.
- Downside without a Rockman: 25–35 scrap stolen, flagged `steal="true"`.
- Downside with a Rockman, or on refusing: a `JELLY` fight at default rewards (50%
  surrender / 50% escape at low hull, per [[source-events-ships]]).

## Strategy Notes
- With a Rock crew member this is a clearly positive event: half a free repair-plus-store,
  half a fight you are paid for. *(Opinion, comparing the two lists in
  [[source-events-slug]].)*
- Without one, weigh 25–35 scrap against a store opening — early, the store is usually
  worth more than the scrap at risk.
- Refusing is the choice that guarantees the fight without any chance of the repair. It is
  only correct if you want the fight.

## Related
- [[event-slug-store-ship]], [[event-slug-repair-station]] — the other Slug hospitality
  traps in these sectors
- [[event-store-in-nebula-slug]] — the honest Slug store
- [[entity-rock-men]], [[entity-slugs]]

## Open Questions
- [ ] Whether the two entries in each list are equally weighted.

## Sources
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-fandom-slug-drink]] (per raw/wiki/slug-drink.md)
