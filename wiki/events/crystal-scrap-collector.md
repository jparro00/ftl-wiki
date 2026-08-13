---
id: event-crystal-scrap-collector
type: event
event_name: CRYSTAL_SCRAP_EXCITED
sectors: [[[sector-hidden-crystal-worlds]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unique, crew-purchase, weapon-reward, scrap-cost]
---

# Crystal scrap collector — `CRYSTAL_SCRAP_EXCITED`

## Summary
A collector of alien junk offers to trade. Pay **35 scrap** and you choose your payment:
either a **Crystal crew member** or one of two Crystal-flavoured weapons. It is the
cheapest guaranteed crew member in [[sector-hidden-crystal-worlds]] and one of the few
events in the game where you effectively *buy* a specific outcome.

## Trigger & Where It Appears
- Sector: [[sector-hidden-crystal-worlds]] only
- Pool: one of **6** entries in the `ITEMS_CRYSTAL` event list, allocated exactly twice
  per sector (`min=2 max=2`) ([[source-events-xml]], [[source-sector-data-xml]])
- `unique="true"` — at most once per run
- Beacon: shows **no ship** on Long-Range Scanners
  ([[source-fandom-crystal-scrap-collector]])

## Text
> You receive a signal from a private relay on a nearby inhabited planet. "Are you the
> alien ship they've been talking about?! You are! Please, I am a collector of alien
> artifacts, I'm sure what is scrap to you is priceless to me."

(`event_CRYSTAL_SCRAP_EXCITED_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Offer 35 scrap. | — | `item_modify` `scrap −35` (fixed, `min=max=-35`). He proposes joining you instead of paying → second choice, below. | 100% |
| 2 | Turn him down. | — | *"Scrap is priceless no matter where you are in the galaxy."* Nothing happens. | 100% |

### After paying 35 scrap
> "My word! Is this... a 25th century Rockman thrust stabilizer?! What do you want for it?
> Wait, I have a better proposal. I long to see the galaxy. I propose I come with you. What
> do you say?"

| # | Choice | Outcome(s) | Odds |
|---|--------|-----------|------|
| 1 | Accept. | `crewMember amount="1" class="crystal"` → a **Crystal crew member** joins. | 100% |
| 2 | Request another payment. | Loads `CRYSTAL_SCRAP_EXCITED_LIST` — two equally listed entries: `BOMB_LOCK` (**Crystal Lockdown Bomb**) or `CRYSTAL_BURST_2` (**Crystal Burst Mark II**). | 1 of 2 each |

([[source-events-xml]], [[source-fandom-crystal-scrap-collector]])

## Blue Options
- None. Nothing here is gated on crew, system or augment.

## Rewards & Risks
- **Cost:** a flat 35 scrap, paid before you see which weapon you'd get.
- **Rewards:** a Crystal crew member (guaranteed if you accept), or a random pick between
  the Crystal Lockdown Bomb and the Crystal Burst Mark II.
- **Risk:** none mechanical — no fight branch, no crew loss. The only risk is the 35 scrap
  itself and the fact that the weapon branch is a coin flip you cannot steer.

## Strategy Notes
- The crew branch is the only *deterministic* Crystal crew member in the sector — the
  [[event-crystal-fight]] surrender is 1-in-7 and [[event-store-crystal]] depends on stock
  rolls. If you are here without Crystal crew and want the `req="crystal"` blue options at
  [[event-crystalline-cache]] and [[event-crystal-chat]], this is the reliable buy.
  *(Opinion, built on the sourced odds above.)*
- Note `CRYSTAL_BURST_2` and `BOMB_LOCK` both also appear in this sector's store rarity
  list (rarity 4 and 3 respectively, [[source-sector-data-xml]]) — so the weapon branch is
  buying you a store roll you could otherwise get at a [[event-store-crystal]].

## Related
- [[sector-hidden-crystal-worlds]]
- [[entity-crystal-men]]
- [[event-store-crystal]] — the other place to buy Crystal crew
- [[event-crystal-fight]] — free Crystal crew via surrender
- [[event-crystalline-cache]] — the other `ITEMS_CRYSTAL` Crystal-specific entry
- [[item-crystal-lockdown-bomb]], [[item-crystal-burst-mark-ii]]

## Open Questions
- [ ] Whether the Crystal crew member gained here is a full Crystal crew (lockdown +
      double health) or a reskin — no ingested source addresses it.
- [ ] Stats for the two weapons (blueprints.xml not yet ingested).

## Sources
- [[source-events-xml]] (per raw/gamedata/events_crystal.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-crystal-scrap-collector]] (per raw/wiki/crystal-scrap-collector.md)
