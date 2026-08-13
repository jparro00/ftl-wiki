---
id: event-refugee-distress
type: event
event_name: REFUGEE_DISTRESS
sectors: [[[sector-civilian-sector]], [[sector-federation-space]], [[sector-pirate-controlled-sector]], [[sector-uncharted-nebula]]]
beacon_type: distress
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 7
tags: [distress, trading, ambush-risk, refugee, advanced-edition]
---

# Refugee distress — `REFUGEE_DISTRESS`

## Summary
A stranded refugee ship broadcasting a distress beacon. Hailing it is a coin flip: half
the time it is an ordinary resource trade, half the time it is bait for one of four
different ambushes. This is the **generic-sector** member of a family of five nearly
identical refugee events — see *Related* for the sector-specific twins, which have much
smaller (and therefore much more dangerous) outcome pools.

## Trigger & Where It Appears
- Beacon: **distress signal** — the event carries `<distressBeacon/>`
  ([[source-newevents]]).
- Reached through the `DISTRESS_BEACON` event list, where it is one of 14 entries:

  ```xml
  <event load="REFUGEE_GHOST"/><!--DLC CHRIS - down below-->
  <event load="REFUGEE_DISTRESS"/> <!--DLC - down below-->
  ```

  ([[source-newevents]], lines 217–218). Both refugee entries are marked as DLC additions.
- `DISTRESS_BEACON` is allocated by `sector_data.xml` in `STANDARD_SPACE`
  ([[sector-federation-space]], `min=1 max=2`), `CIVILIAN_SECTOR` (`min=1 max=2`) and
  `NEBULA_SECTOR` ([[sector-uncharted-nebula]], `min=1 max=3`)
  ([[source-sector-data-xml]]). It is additionally an entry in `NEUTRAL_CIVILIAN`
  ([[source-newevents]]) and in `NEUTRAL_PIRATE` ([[source-events-pirate]]), which is how
  it reaches [[sector-pirate-controlled-sector]].
- Not `unique` — it can recur.

> ⚠️ **CONTRADICTION:** sector scope.
> - Fandom lists Civilian Sector, Pirate Controlled Sector and Uncharted Nebula
>   ([[source-fandom-refugee-distress]]).
> - `sector_data.xml` also allocates `DISTRESS_BEACON` in `STANDARD_SPACE`
>   ([[source-sector-data-xml]]), which is [[sector-federation-space]].
>
> Trusting the game files (`high` vs `medium`). Fandom's location boxes are hand-curated
> and routinely omit the generic starting sector.

## Text
> You have encountered a refugee ship drifting in space. It looks as if it was fleeing the
> Rebel advance and ran out of fuel. Its distress beacon is active, but you're not sure
> anyone is on board.

(`event_REFUGEE_DISTRESS_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Hail them. | — | Loads `REFUGEE_HAIL_LIST` — see the pool below. | — |
| 2 | Ignore the refugees. | — | `<event/>` — nothing happens. | 100% |

### `REFUGEE_HAIL_LIST` — the hail pool

Eight entries, four of which are the same event. **Assuming uniform selection across list
entries** (the game files state no weights), that gives:

| Outcome | Entries | Share |
|---|---|---|
| `REFUGEE_TRADER` — a resource trade (below) | 4 | 4/8 |
| *"As you hail the freighter, it advances, weapons bristling from its hull! It's a pirate ambush!"* → fight `PIRATE` | 1 | 1/8 |
| *"…a Zoltan ship suddenly jumps into the system… it claims the refugees are criminals, and accuses you of escorting fugitives!"* → fight `ZOLTAN_REFUGEE` | 1 | 1/8 |
| *"…a pirate ship jumps into the system… it was using the refugee ship as bait!"* → fight `PIRATE_REFUGEE` | 1 | 1/8 |
| *"…a Slug ship jumps into the system… it was hunting the refugee ship for sport and now they've found you instead!"* → fight `SLUG_REFUGEE` | 1 | 1/8 |

([[source-newevents]], [[source-text-events-xml]]) This is a derivation from the list
contents, not a stated percentage.

### `REFUGEE_TRADER` — the trade sub-event
*"The vessel is relieved to hear from you! They are running low on supplies. They suggest
a trade."* Two choices: **Trade with them** (loads `TRADER_LIST`) or **Politely decline**
(nothing). `TRADER_LIST` lives in `raw/gamedata/events.xml` and has four equally weighted
members ([[source-events-xml]]):

| Trade | You gain | You pay |
|---|---|---|
| 1 | 5–10 fuel | 1–2 drone parts |
| 2 | 4–5 missiles | 1–2 fuel |
| 3 | 2–3 drone parts | 2–3 missiles |
| 4 | 4–10 fuel | 2–4 missiles |

The offer is a barter, not a purchase — no scrap changes hands. `REFUGEE_TRADER` is a
shared sub-event: the same node is reached from all nine refugee beacons in this family.

### The ambush ships
- **`PIRATE`** — `auto_blueprint="SHIPS_PIRATE"`, 50% surrender chance, 50% escape chance,
  `DESTROYED_DEFAULT` / `DEAD_CREW_DEFAULT` (default rewards) ([[source-events-ships]]).
- **`ZOLTAN_REFUGEE`** (`SHIPS_ZOLTAN`), **`PIRATE_REFUGEE`** (`SHIPS_PIRATE`) and
  **`SLUG_REFUGEE`** (`SHIPS_JELLY`) are defined in `newEvents.xml` and share one shape
  ([[source-newevents]]): no surrender, no escape;
  `destroyed` → `autoReward level="MED"` `standard`, `deadCrew` → `autoReward level="HIGH"`
  `standard`. Each then offers a hidden follow-up choice, *"Contact the refugee ship."*,
  in which the rescued refugees hand over `autoReward level="LOW"` `standard` on top.

## Blue Options
None — this event has no `req`-gated choices.

## Rewards & Risks
- **Best case:** a favourable barter, or a won fight paying `MED`/`HIGH` `standard` plus a
  `LOW` `standard` thank-you.
- **Worst case:** a real fight you did not choose, in a sector where you may already be
  damaged. There is no way to back out once you hail.
- Ignoring costs nothing but forgoes the beacon entirely.

## Strategy Notes
- *(Opinion, from the list structure rather than any source's advice.)* The 4/8 trader
  share makes this the safest member of the refugee family; the sector-specific variants
  (`_PIRATE`, `_SLUG`, `_ZOLTAN`) run 1/2 fights instead of 1/8-per-ship.
- The trades all cost consumables you may want. Declining after hailing is free — hailing
  commits you to the ambush roll, not to the trade.

## Related
- [[event-refugee]] — the same hail pool at a non-distress beacon
- [[event-refugee-comms-down]] — the other refugee entry in `DISTRESS_BEACON`
- [[event-refugee-distress-pirate]], [[event-refugee-distress-slug]],
  [[event-refugee-distress-zoltan]] — sector-specific twins
- [[entity-pirates]], [[entity-zoltan]], [[entity-slugs]]
- [[event-refugee-trader]] — the `REFUGEE_TRADER` trade sub-event, which carries its own page

## Open Questions
- [ ] Whether FTL's event-list selection is genuinely uniform (the odds above assume it).
- [ ] Exact scrap/resource values behind `LOW` / `MED` / `HIGH` `standard`.
- [ ] The Fandom `{{Drifting Refugee Ship}}` template was not captured in the raw dump, so
      Fandom's own outcome numbers for this event are unavailable here.

## Sources
- [[source-newevents]] (per `raw/gamedata/newEvents.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-events-xml]] (per `raw/gamedata/events.xml`)
- [[source-events-ships]] (per `raw/gamedata/events_ships.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-events-pirate]] (per `raw/gamedata/events_pirate.xml`)
- [[source-fandom-refugee-distress]] (per `raw/wiki/refugee-distress.md`)
