---
id: event-store-lanius
type: event
event_name: STORE_LANIUS
sectors: [[[sector-abandoned-sector]]]
beacon_type: store
hostile: false
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [store, lanius, guaranteed, no-choice, advanced-edition]
---

# Store (Lanius) — `STORE_LANIUS`

## Summary
The Abandoned Sector's store beacon. It opens a store and nothing else; the six flavour
variants exist to explain why anyone is still trading in a sector the Lanius are eating.
Exactly **2** are allocated per sector ([[source-sector-data-xml]]) — the same guarantee as
most faction sectors, and the main thing keeping an Abandoned Sector survivable given its
5–6 hostile beacons.

## Trigger & Where It Appears
- Sector: [[sector-abandoned-sector]] (`LANIUS_SECTOR`) only.
- Allocation: `<event name="STORE_LANIUS" min="2" max="2"/>` — a fixed 2, not a range, and
  allocated directly by the sector definition rather than drawn from a list
  ([[source-sector-data-xml]], per `raw/gamedata/sector_data.xml`).
- Beacon: **store** ([[source-fandom-store-lanius]] marks `store=true`, `LRSmap=noship`).
- No `unique` attribute — it appears twice per sector by design
  ([[source-dlcevents-anaerobic]]).

> **AE-only.** AE data file, AE sector. `dlcEventsOverwrite.xml` defines no
> `OVERRIDE_STORE_LANIUS` ([[source-dlceventsoverwrite]]); Fandom files it under
> *Advanced Edition Content Events*.

## Text
`[varies: textList STORE_LANIUS]` — six entries, none duplicated → **1/6 each** *assuming
uniform selection across list entries* ([[source-dlcevents-anaerobic]]). The six framings,
per [[source-text-events-xml]]: a transport waiting on a Coolant Shaft repair and offloading
stock; Lanius merchants who emigrated with the scavengers and greet you in your own
language; a heavily guarded trading depot advertising on a wide band; an abandoned station
whose ship depot is running an "Everything Must Go!" sale; merchants capitalising on refugee
traffic; and a doomsday-preacher advertisement for a space dock. All six are transcribed on
[[source-fandom-store-lanius]].

Representative:

> You arrive to discover a number of Lanius ships docked at what appears to be a station.
> You hasten to leave but are relieved when they message you in your language. "Buy? Sell?
> Traders." Apparently some merchants emigrated with the scavengers.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(no choices; continue)_ | — | A store opens. | 100% |

The event body is `<text load="STORE_LANIUS"/>` plus a bare `<store/>` tag
([[source-dlcevents-anaerobic]]). The store's inventory is not constrained by the event.

## Rewards & Risks
- No scrap, fuel or items are granted by the event itself.
- No risk — the beacon is never hostile and there is nothing to decide.

## Strategy Notes
- Two guaranteed stores is the reason an Abandoned Sector is enterable at all. Budget
  around them: the sector's item beacons ([[event-lanius-craftsmen]],
  [[event-lanius-trader]]) sell blind or at fixed prices, so the stores are your only
  chance to see what you are buying.
- The sector rolls `anaerobic` crew at rarity 2 in its `rarityList`
  ([[source-sector-data-xml]]) — Lanius crew can therefore appear in these stores, which
  matters because Lanius crew gate blue options on five other beacons in the sector. The
  cheaper alternative is buying "Translator" for 40 scrap at
  [[event-lanius-trader-with-translator]].
- Nothing in the event biases inventory toward Lanius equipment, despite the flavour.

> ⚠️ **CONTRADICTION (minor, wording):** Fandom's third variant reads *"A trading **beacon**
> is set up near the beacon"* ([[source-fandom-store-lanius]]); the game files read
> *"A trading **depot** is set up near the beacon."* ([[source-text-events-xml]], per
> `raw/gamedata/text_events.xml`). Trusting the game files — reliability `high` vs `medium`.
> Reads as a transcription slip, not a version difference.

## Related
- [[event-empty-beacon-lanius]], [[event-start-beacon-lanius]] — the sector's other no-op
  beacons
- [[event-lanius-lone-ship]] — the one Lanius beacon whose blue option opens an *extra*
  store
- [[event-store-rock]], [[event-store-engi]], [[event-store-mantis]] — the same slot in
  other sectors
- [[sector-abandoned-sector]], [[entity-lanius]], [[concept-stores]]

## Open Questions
- [ ] Whether `STORE_LANIUS` biases its inventory toward Lanius or AE-only blueprints — the
      event says nothing, so presumably it is the generic store roll.
- [ ] How often Lanius crew actually appear for sale given the sector's `anaerobic` rarity
      of 2.

## Sources
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-fandom-store-lanius]] (per raw/wiki/store-lanius.md)
