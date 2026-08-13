---
id: event-lanius-trader-with-translator
type: event
event_name: LANIUS_TRADER_TRANSLATOR
sectors: [[[sector-abandoned-sector]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [lanius, item-event, trading, crew-purchase, unique, no-risk, advanced-edition]
---

# Lanius trader with translator — `LANIUS_TRADER_TRANSLATOR`

## Summary
The near-twin of [[event-lanius-trader]] — same resource-for-scrap tables, same "accept or
decline" shape — with one crucial difference: the third option **sells you a Lanius crew
member for 40 scrap**, named *Translator*. That is the cheapest guaranteed Lanius crew in
the game data read here, and Lanius crew is the key that unlocks blue options across the
whole [[sector-abandoned-sector]]. This event has **no blue option of its own**.

## Trigger & Where It Appears
- Sector: [[sector-abandoned-sector]] (`LANIUS_SECTOR`) only.
- List: `ITEM_LANIUS`, allocated `min="2" max="4"` beacons per sector
  ([[source-sector-data-xml]]). Five members, none duplicated → **1/5** of any item beacon
  *assuming uniform selection across list entries* ([[source-dlcevents-anaerobic]]).
- `unique="true"` — at most once per run.
- Long-range scanners show **no ship**
  ([[source-fandom-lanius-trader-with-translator]]).

> **AE-only.** AE data file, AE sector, `class="anaerobic"` crew — no vanilla form exists.
> `dlcEventsOverwrite.xml` defines no `OVERRIDE_ITEM_LANIUS`
> ([[source-dlceventsoverwrite]]).

## Text
Fixed, not a list — this is what distinguishes it on sight from [[event-lanius-trader]]:

> A Lanius merchant appears to have a significantly improved translator as you clearly
> understand their message. "Metal content more than sufficient. Does your ship care to
> exchange resources for our excess metal?"

(`event_LANIUS_TRADER_TRANSLATOR_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Agree to the exchange. | — | Loads `LANIUS_TRADER_LIST` — the same table [[event-lanius-trader]] uses. | 100% |
| 2 | Decline. | — | "They leave without a word." Nothing happens. | 100% |
| 3 | Decline but ask about their translation device. | — | *"Yes. It is quality. Our ship contains excess. Care to purchase?"* → the crew offer below. | 100% |

### `LANIUS_TRADER_LIST` (choice 1)
Three entries, all sharing the flavour string *"After the exchange is complete they leave
without a word."* → **1/3 each** *assuming uniform selection across list entries*
([[source-dlcevents-anaerobic]]):

| Trade | You lose | You gain |
|---|---|---|
| Fuel | 3–7 fuel | 15–30 scrap |
| Missiles | 3–7 missiles | 20–40 scrap |
| Drone parts | 3–7 drone parts | 20–40 scrap |

Fandom notes the offer is shown before you commit
([[source-fandom-lanius-trader-with-translator]]).

### Choice 3 → the crew offer

| # | Choice | Outcome |
|---|--------|---------|
| 3a | Purchase the translator for 40 scrap. | −40 scrap exactly (`<item type="scrap" min="-40" max="-40"/>`) and **+1 Lanius crew member**, `<crewMember amount="1" class="anaerobic" id="name_Translator"/>` → named **Translator** (`name_Translator`, per [[source-text-events-xml]]). Flavour: *"…the 'device' you purchased was one of the beings that learned your language."* |
| 3b | Decline again. | *"No matter. This one does not mind this ship."* Nothing happens. |

Choice 3 does **not** end the trade — it replaces it. Taking 3 forfeits the resource trade
in choice 1 ([[source-dlcevents-anaerobic]]).

## Blue Options
**None.** This is the deliberate asymmetry with [[event-lanius-trader]], which has a
Lanius-crew reroll but no crew for sale. Fandom states it explicitly: *"…has an option to
get a Lanius named Translator… however, the blue option to get a better trade offer is not
available in this event."* ([[source-fandom-lanius-trader-with-translator]]).

## Rewards & Risks
- **40 scrap for a Lanius crew member** is the headline. Lanius crew gate blue options on
  [[event-lanius-with-federation-science-craft]], [[event-lanius-craftsmen]],
  [[event-lanius-lone-ship]], [[event-lanius-ship-salvager]] and [[event-lanius-trader]] —
  and Lanius crew drain oxygen from any room they stand in, which is a real cost as well as
  a boarding asset ([[entity-lanius]]).
- The resource trades carry the same fuel-drain risk as [[event-lanius-trader]]: 3–7 fuel
  for as little as 15 scrap.
- No fight, no hull risk. Every branch is optional and declining is free.

## Strategy Notes
- *Opinion, derived from the tables:* if you do not already have Lanius crew, buy the
  Translator. 40 scrap is below typical store crew pricing, the crew member itself is
  useful, and it retroactively unlocks blue options on up to four other beacons in the same
  sector — though only on beacons you have not yet visited.
- If you already have Lanius crew, take the resource trade instead and judge it on the
  offer shown.
- Seeing the fixed intro text is the tell: this is the event with the crew, and
  [[event-lanius-trader]] (three rotating intro texts) is the one with the reroll.

## Related
- [[event-lanius-trader]] — the near-identical sibling; same trade table, blue option
  instead of crew
- [[event-lanius-craftsmen]], [[event-lanius-with-federation-science-craft]] — the other
  `ITEM_LANIUS` members
- [[sector-abandoned-sector]], [[entity-lanius]], [[item-lanius-crew]]

## Open Questions
- [ ] Whether "Translator" carries any stat difference from an ordinary Lanius crew member
      — the `crewMember` tag sets only `class` and `id` (name), so presumably not.
- [ ] Whether the crew purchase is blocked when your crew roster is full.

## Sources
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-fandom-lanius-trader-with-translator]] (per raw/wiki/lanius-trader-with-translator.md)
