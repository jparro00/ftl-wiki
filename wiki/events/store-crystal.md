---
id: event-store-crystal
type: event
event_name: STORE_CRYSTAL
sectors: [[[sector-hidden-crystal-worlds]]]
beacon_type: store
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [store, crystal-route, crew-purchase]
---

# Store (Crystal) — `STORE_CRYSTAL`

## Summary
The [[sector-hidden-crystal-worlds]] store beacon. Mechanically an ordinary store, but
strategically the most distinctive one in the game: the Fandom page states these are the
**only stores where you can normally buy Crystal crew**
([[source-fandom-store-crystal]]).

## Trigger & Where It Appears
- Sector: [[sector-hidden-crystal-worlds]] only
- Allocation: `STORE_CRYSTAL` is placed 2–3 times per sector (`min=2 max=3`)
  ([[source-sector-data-xml]])
- Beacon: store marker; shows **no ship** on Long-Range Scanners
  ([[source-fandom-store-crystal]])

## Text
The greeting **varies** — `<text load="STORE_CRYSTAL"/>` draws from an 8-slot list built
from 6 distinct strings; `text_STORE_CRYSTAL_1` and `_2` each appear twice, and `_5`/`_6`
are near-duplicates of `_3`/`_4` ([[source-events-xml]]). Distinct variants
([[source-text-events-xml]]):

> You arrive in an area bustling with crystalline ships and stations. A merchant quickly
> messages you, "You're from the outside, no? This is a great opportunity for both of us!
> Do you have anything you wish to sell or trade?"

> "Ah! Hello aliens", says a rotund crystalline being on the vid screen. "I hoped I would
> run into one of you. I am a collector of alien artifacts and hoped you would have some
> equipment to barter!"

> You arrive at a trade depot and find a store that is willing to open communications with
> you. "I can't say I've traded with your kind before, but perhaps we could work out some
> sort of exchange."

> You receive an incoming transmission, but it seems badly garbled. Eventually you realize
> it's advertising an equipment store. "Apologies," says the vendor, when you finally get
> him on the vid screen, "Long time since use universal translator no necessary. Please,
> buy, buy!"

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _none — the event body is `<store/>`_ | — | A store opens | 100% |

## Blue Options
- None.

## Rewards & Risks
- No event reward. What is on the shelves is governed by the sector's `rarityList`, which
  is unusual: **every** standard laser, missile, beam, bomb and ion blueprint is set to
  `rarity="0"` (excluded), and the only stocked weapons are the Crystal line —
  `CRYSTAL_BURST_1` (1), `CRYSTAL_HEAVY_1` (2), `BOMB_LOCK` (3), `CRYSTAL_BURST_2` (4),
  `CRYSTAL_HEAVY_2` (5). Crew rarity is likewise zeroed for engi/mantis/energy/slug/rock/
  human, with `crystal` at rarity 1. ([[source-sector-data-xml]])
- That rarity table is the mechanical reason behind the Fandom claim that these are the
  only stores selling Crystal crew ([[source-fandom-store-crystal]]).

## Strategy Notes
- If you want a Crystal crew member and did not get one from
  [[event-crystal-scrap-collector]] or a [[event-crystal-fight]] surrender, this is the
  reliable route — 2–3 of these exist per sector.
- Conversely, do not come here expecting to shop for a missing standard weapon: the sector
  rarity table excludes essentially the whole normal weapon pool.
  *(Inference from [[source-sector-data-xml]]; no source states the shopping implication
  directly.)*

## Related
- [[sector-hidden-crystal-worlds]]
- [[entity-crystal-men]]
- [[event-crystal-scrap-collector]] — the other way to buy Crystal crew here
- [[event-crystal-fight]] — a Crystal crew member as a surrender outcome

## Open Questions
- [ ] Whether the sector `rarityList` governs store stock only, or also event-granted
      weapons (`WEAPONS_CRYSTAL` rewards appear in several events here).
- [ ] Whether drones/augments in these stores are also restricted (the rarity list names
      no drones or augments).

## Sources
- [[source-events-xml]] (per raw/gamedata/events_crystal.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-store-crystal]] (per raw/wiki/store-crystal.md)
