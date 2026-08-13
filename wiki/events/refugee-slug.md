---
id: event-refugee-slug
type: event
event_name: REFUGEE_NO_DISTRESS_SLUG
sectors: [[[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: nebula
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [trading, ambush-risk, refugee, slug, nebula, advanced-edition]
---

# Refugee (Slug) — `REFUGEE_NO_DISTRESS_SLUG`

## Summary
The Slug-nebula, no-distress cut of the refugee encounter, and the **only** member of the
refugee family that carries an `<environment type="nebula"/>` tag — the beacon is inside
the nebula, so you fight (or trade) with sensors down. Hail pool is two entries: barter,
or a pirate ambush.

## Trigger & Where It Appears
- Beacon: **nebula**. The event declares `<environment type="nebula"/>`
  ([[source-newevents]], line 1054); Fandom's location box agrees (`nebula=true`,
  [[source-fandom-refugee-slug]]). Its distress-beacon twin
  [[event-refugee-distress-slug]] has no such tag.
- Sole list membership: `NEBULA_NEUTRAL_SLUG`, marked `<!--DLC - In newEvents-->`
  ([[source-events-slug]], line 90).
- `NEBULA_NEUTRAL_SLUG` serves [[sector-slug-controlled-nebula]] and
  [[sector-slug-home-nebula]] ([[source-sector-data-xml]]).
- Not `unique`.

## Text
> Your sensors have picked up a refugee ship drifting through the system, no doubt one of
> many fleeing the Rebel advance. It doesn't appear to have detected you... or else it is
> trying to avoid notice.

(`event_REFUGEE_NO_DISTRESS_SLUG_text`, per [[source-text-events-xml]])

Note the mild fiction: the intro says your sensors picked the ship up, in a beacon the
same event flags as nebula — where sensors are suppressed.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Hail them. | — | Loads `REFUGEE_HAIL_LIST_SLUG` — two entries, below. | — |
| 2 | Ignore the refugees. | — | `<event/>` — nothing happens. | 100% |

### `REFUGEE_HAIL_LIST_SLUG`
Two members. **Assuming uniform selection across list entries**:

| Outcome | Entries | Share |
|---|---|---|
| `REFUGEE_TRADER` — a resource trade (below) | 1 | 1/2 |
| *"As you hail the refugee ship, a pirate ship jumps into the system... it was using the refugee ship as bait!"* → fight `PIRATE_REFUGEE` | 1 | 1/2 |

([[source-newevents]], [[source-text-events-xml]]) Derived from list contents, not a
stated percentage. The ambusher is a **pirate**, not a Slug ship.

### `REFUGEE_TRADER` — the trade sub-event
*"The vessel is relieved to hear from you! They are running low on supplies. They suggest
a trade."* → **Trade with them** loads `TRADER_LIST` ([[source-events-xml]]); or
**Politely decline** for nothing.

| Trade | You gain | You pay |
|---|---|---|
| 1 | 5–10 fuel | 1–2 drone parts |
| 2 | 4–5 missiles | 1–2 fuel |
| 3 | 2–3 drone parts | 2–3 missiles |
| 4 | 4–10 fuel | 2–4 missiles |

### `PIRATE_REFUGEE`
`auto_blueprint="SHIPS_PIRATE"`; no surrender, no escape ([[source-newevents]]).
`destroyed` → `MED` `standard`; `deadCrew` → `HIGH` `standard`; both then offer a hidden
*"Contact the refugee ship."* choice for a further `LOW` `standard`.

## Blue Options
None.

## Rewards & Risks
- 1/2 barter, 1/2 a committed pirate fight **fought inside a nebula** — no sensors, and
  the enemy cannot flee or surrender.
- The fuel-for-drone-parts trade is worth noting in Slug space, where nebula jumps and
  long routes eat fuel.

## Strategy Notes
- *(Opinion.)* The nebula tag is the whole story here: the same coin flip as
  [[event-refugee-pirate]], but you take the losing side blind.

## Related
- [[event-refugee]] — generic no-distress version, 4/8 trade share
- [[event-refugee-distress-slug]] — same pool, distress framing, **no** nebula tag
- [[entity-pirates]], [[entity-slugs]]
- [[event-refugee-trader]] — the `REFUGEE_TRADER` trade sub-event, which carries its own page

## Open Questions
- [ ] Whether event-list selection is truly uniform.
- [ ] Fandom's `{{Drifting Refugee Ship}}` template was not captured in the raw dump.

## Sources
- [[source-newevents]] (per `raw/gamedata/newEvents.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-events-xml]] (per `raw/gamedata/events.xml`)
- [[source-events-slug]] (per `raw/gamedata/events_slug.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-refugee-slug]] (per `raw/wiki/refugee-slug.md`)
