---
id: event-lanius-with-federation-science-craft
type: event
event_name: LANIUS_RESEARCHER_CONTACT
sectors: [[[sector-abandoned-sector]]]
beacon_type: any
hostile: false
blue_options: [lanius crew]
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [lanius, item-event, blue-option, unique, no-risk, advanced-edition]
---

# Lanius with Federation science craft — `LANIUS_RESEARCHER_CONTACT`

## Summary
A pure-upside item beacon in the [[sector-abandoned-sector]]: Federation xenolinguists
studying the Lanius will hand you something for nothing. There is no fight, no cost and no
way to lose anything. With a Lanius crew member you can trade your translator's accumulated
data for a **guaranteed** piece of equipment instead of rolling on the ordinary
give-you-something table — the blue option is strictly better than the free-hand-out one.

## Trigger & Where It Appears
- Sector: [[sector-abandoned-sector]] (`LANIUS_SECTOR`) only.
- List: `ITEM_LANIUS`, allocated `min="2" max="4"` beacons per sector
  ([[source-sector-data-xml]], per `raw/gamedata/sector_data.xml`).
- `ITEM_LANIUS` has five members — `LANIUS_FREE_STUFF`, `LANIUS_TRADER_TRANSLATOR`,
  `LANIUS_TRADER`, `LANIUS_RESEARCHER_CRAFT`, `LANIUS_RESEARCHER_CONTACT` — none
  duplicated, so each is **1/5** of any item beacon *assuming uniform selection across list
  entries* ([[source-dlcevents-anaerobic]]).
- `unique="true"` — at most once per run ([[source-dlcevents-anaerobic]];
  [[source-fandom-lanius-with-federation-science-craft]] renders `unique=true`).
- Long-range scanners show **no ship** ([[source-fandom-lanius-with-federation-science-craft]]).

> **AE-only.** `dlcEvents_anaerobic.xml` is an Advanced Edition data file and
> `LANIUS_SECTOR` is an AE sector. `dlcEventsOverwrite.xml` defines no `OVERRIDE_`
> replacement for `ITEM_LANIUS`, so there is no vanilla pool to compare against
> ([[source-dlceventsoverwrite]]). Fandom files it under *Advanced Edition Content Events*.

## Text
> A Federation science craft is docked with a few Lanius ships. You hail them and ask what
> is going on. "Greetings! We have been attempting to understand our region's newest
> visitors, the Lanius, although we have been making little headway in deciphering their
> language."

(`event_LANIUS_RESEARCHER_CONTACT_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Ask if they have anything that could help your mission. | — | Loads `LANIUS_RESEARCHER_CONTACT_LIST` — see below. | 100% |
| 2 | **(Lanius Crew)** Offer to copy your translator's data suite. | `req="anaerobic"` | Flavour, then a hidden *continue* choice loading `LANIUS_RESEARCHER_CONTACT_LIST2` — an item, guaranteed. | 100% |
| 3 | Leave. | — | "You wish them well and prepare to jump." Nothing happens. | 100% |

### `LANIUS_RESEARCHER_CONTACT_LIST` (choice 1)
Four entries, none duplicated → **1/4 each** *assuming uniform selection across list
entries* ([[source-dlcevents-anaerobic]]):

| Outcome | Payload |
|---|---|
| "There should be some extra junk metal in some cargo bay…" | `autoReward level="MED">scrap_only` |
| "We use drones frequently in our work and have extra parts lying around." | `autoReward level="MED">droneparts` |
| "We were doing research on some Lanius weaponry before." | `<weapon name="RANDOM"/>` — a random weapon |
| "Sorry we don't really carry much equipment that would be of use to a military vessel." | nothing |

### `LANIUS_RESEARCHER_CONTACT_LIST2` (choice 2, the blue option)
Three entries, all sharing the same flavour string
(`event_LANIUS_RESEARCHER_CONTACT_LIST2_1_text`, *"They are grateful for your contribution
and offer you some Lanius equipment that they were previously studying."*) and differing
only in payload → **1/3 each** *assuming uniform selection across list entries*
([[source-dlcevents-anaerobic]]):

| Outcome | Payload |
|---|---|
| Augment | `<augment name="RANDOM"/>` |
| Weapon | `<weapon name="RANDOM"/>` |
| Drone schematic | `<drone name="RANDOM"/>` |

Because all three share one text string, the prose gives no hint which you got until you
look at the ship.

## Blue Options
- **Lanius crew member** (`req="anaerobic"`) — replaces a 1/4-chance-of-nothing roll with a
  guaranteed weapon, drone schematic or augment. Any Lanius crew member satisfies it,
  including the one bought from [[event-lanius-trader-with-translator]]
  ([[source-dlcevents-anaerobic]]).

## Rewards & Risks
- **No risk at all** — no `<ship>` tag anywhere in the event, no resource cost on any
  branch ([[source-dlcevents-anaerobic]]).
- Without the blue option: 3/4 chance of something (`MED` scrap, `MED` drone parts, or a
  random weapon), 1/4 chance of nothing.
- With it: a random augment, weapon or drone schematic, guaranteed.
- `MED` / `RANDOM` are the game's own `autoReward` levels; no source read here converts them
  to scrap numbers.

## Strategy Notes
- Always take a choice — there is no downside to asking, and "Leave" exists only for
  completeness.
- *Opinion, derived from the tables above, not stated by any source:* if you have Lanius
  crew, choice 2 dominates choice 1 — the item pool is better and the miss chance is gone.
- The random weapon from choice 1 draws from the unrestricted `RANDOM` pool, unlike
  [[event-lanius-craftsmen]], whose items come from the Advanced-Edition-only blueprint
  lists ([[source-dlcblueprints]]).

> ⚠️ **CONTRADICTION (minor, wording):** the "nothing happens" line reads *"Sorry we don't
> **really** carry much equipment…"* in the game files
> ([[source-text-events-xml]], per `raw/gamedata/text_events.xml`) and *"Sorry we don't
> carry much equipment…"* on Fandom
> ([[source-fandom-lanius-with-federation-science-craft]]). Trusting the game files —
> reliability `high` vs `medium`. Not a version difference: this event has no vanilla form.

> ⚠️ **CONTRADICTION (numeric claim):** Fandom annotates the drone-parts outcome as
> *"medium (1 drone part) drone parts and scrap"*
> ([[source-fandom-lanius-with-federation-science-craft]]). The game files state only
> `autoReward level="MED">droneparts` — the "1 drone part" figure appears nowhere in
> `raw/gamedata/` ([[source-dlcevents-anaerobic]]). Recorded, not adopted; the exact
> quantity behind `MED droneparts` remains unknown here.

## Related
- [[event-lanius-craftsmen]] — the other Lanius-scientist item beacon, and the one that
  charges you
- [[event-lanius-trader]], [[event-lanius-trader-with-translator]] — the other
  `ITEM_LANIUS` members with Lanius blue options
- [[sector-abandoned-sector]], [[entity-lanius]]
- [[concept-blue-options]]

## Open Questions
- [ ] Scrap / drone-part quantities behind `MED scrap_only` and `MED droneparts`.
- [ ] Which blueprint list `<weapon name="RANDOM"/>` and the `LIST2` items draw from —
      the tag names no list, unlike [[event-lanius-craftsmen]]'s `DLC_WEAPONS`.

## Sources
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-fandom-lanius-with-federation-science-craft]] (per raw/wiki/lanius-with-federation-science-craft.md)
