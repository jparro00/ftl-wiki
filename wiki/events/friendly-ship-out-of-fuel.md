---
id: event-friendly-ship-out-of-fuel
type: event
event_name: FRIENDLY_BEACON
sectors: [[[sector-abandoned-sector]], [[sector-civilian-sector]], [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-federation-space]], [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]], [[sector-pirate-controlled-sector]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]], [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]], [[sector-uncharted-nebula]], [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: distress
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [distress, trading, fuel, weapon-reward-chance, map-reveal, reactor-upgrade, repeatable, no-risk]
---

# Friendly ship out of fuel — `FRIENDLY_BEACON`

## Summary
A stranded civilian ship asks for fuel. Give 2–4 fuel and you get a gift from a
four-outcome pool: high scrap (twice as likely as the rest), a free weapon, a full sector
map reveal, or — in Advanced Edition only — a reactor upgrade. There is no risk anywhere
in the event; the only question is whether you can spare the fuel.

## Trigger & Where It Appears
- Sectors: fifteen — see frontmatter for the full list.
- Beacon: **distress**. The event carries `<distressBeacon/>` and is pooled in
  `DISTRESS_BEACON` and its Engi, Lanius, Mantis, Pirate, Rebel, Rock and Zoltan variants
  ([[source-events-xml]], [[source-newevents]], [[source-dlcevents-anaerobic]]).
- A non-hostile `CIVILIAN_SHIP` sits at the beacon, so Long-Range Scanners show a ship
  ([[source-events-ships]], [[source-fandom-friendly-ship-out-of-fuel]]).
- **Not `unique`** — it can recur in a run.

## Text
Drawn from the `FRIENDLY_BEACON` textList — `[varies: textList FRIENDLY_BEACON]`. Five
strings, none DLC-marked, so the pool is the same in both editions
([[source-text-events-xml]]):

1. *"Greetings! It is so good to see you! We've been out of fuel and floating out here for weeks. We were terrified a pirate or those damn Rebels would find us first. Could you spare some fuel?"*
2. *"You arrive to find a ship floating among some debris. 'Hello. Our impulse drives are shot and we can't jump. Could you give us some fuel?'"*
3. *"A small civilian ship flies over as soon as you arrive. You're prepared to fight but they just inform you that they're out of FTL fuel and can't jump."*
4. *"Hello. We used our last FTL fuel to jump to this station."* … *"As you can see the war must have spread to this sector. We've been stranded ever since."*
5. *"The ship emitting the distress beacon messages you, 'Sorry to bother you, but we're out of fuel and can't get out of this barren sector. Could you help us out?"*

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Give them the fuel. | — | *"You give them the fuel."* → `<item type="fuel" min="-4" max="-2"/>` — **you pay 2–4 fuel** — then a continue screen loading the `RANDOM_GIFT` list. | 100% |
| 2 | Apologize, wish them luck, and continue on. | — | *"We understand... Please send help our way if you meet anyone trustworthy."* → nothing. | 100% |

The exact fuel cost is shown before you commit — *"the requested amount of fuel is shown
before you make the choice"* ([[source-fandom-friendly-ship-out-of-fuel]]).

### `RANDOM_GIFT` — the payment

This list is **not visible in the parsed event structure**; it is reached through a hidden
continue choice inside outcome 1 (`<choice hidden="true"><event load="RANDOM_GIFT"/>`).
Five entries in Advanced Edition, four in vanilla, with **one entry duplicated**
([[source-events-xml]]):

| Odds (AE / vanilla) | Outcome |
|---|---|
| **2/5 · 2/4** | *"Thank you. Here, have this extra scrap as payment."* → `autoReward level="HIGH"` type `scrap_only`. **This entry appears twice in the list.** |
| 1/5 · 1/4 | *"Thank you so much! We don't have much to offer, but have a look at the sector scans we took." Your map is updated.* → `<reveal_map/>` — the sector map is revealed. |
| 1/5 · 1/4 | *"Thank the Gods. We can finally get out of here! We're jumping straight home so take this extra weapon. We won't need it, hopefully."* → `<weapon name="RANDOM"/>`. |
| 1/5 · — | **AE only.** *"Thank you. Perhaps as payment our engineer can try to optimize your ship's reactor output?"* → `<upgrade amount="1" system="reactor"/>`. |

**These fractions assume uniform selection across list entries.** The duplication is the
derivation: `event_RANDOM_GIFT_2_text` with `autoReward level="HIGH">scrap_only` is written
twice in a row, so it is twice as likely as any other single entry. Fandom independently
marks that outcome `{{DuplicateEvent|2}}`, which corroborates the reading
([[source-fandom-friendly-ship-out-of-fuel]]).

> **Version difference.** The reactor-upgrade entry carries a `<!--DLC!-->` marker inside
> `events.xml`, so the vanilla gift pool is four entries and the Advanced Edition pool is
> five ([[source-events-xml]]). This shifts the high-scrap outcome from 1/2 in vanilla to
> 2/5 in AE.

Fandom adds a failure case the files do not state: if your reactor is already maxed you get
*"Could not upgrade the Reactor, it's maxed"* and **nothing happens**
([[source-fandom-friendly-ship-out-of-fuel]]).

## Blue Options
None. No `req=` gate anywhere in the event.

## Rewards & Risks
- **Cost:** 2–4 fuel, shown before you commit.
- **Return:** ~2/5 high scrap, ~1/5 a random weapon, ~1/5 a full sector map reveal, ~1/5
  (AE) a reactor upgrade. Every branch is a gain.
- **Risk:** none. No combat, no crew exposure, no hull damage — the ship is loaded
  `hostile="false"` and there is no path to it turning on you.
- The real risk is indirect: handing over up to 4 fuel when you are low can strand you,
  which is its own event family.

## Strategy Notes
- Take it unless your fuel is genuinely tight. There is no bad outcome, and the map reveal
  alone is worth the trade in an unexplored sector. *Opinion*, from the outcome table; no
  source rates it.
- Fuel is cheap to replace at stores and from `ITEMS`-pool events; a random weapon or a
  reactor bar is not.
- Note the asymmetry with [[event-trade-fuel-for-drone-parts]], which charges the same 2–4
  fuel for a fixed 1–3 drone parts. This event's expected value is much higher, but it is
  a distress beacon rather than an item beacon, so you do not choose between them.

## Related
- [[event-trade-fuel-for-drone-parts]] — the other fuel-for-goods trade, fixed payout
- [[item-reactor]] — what the AE-only gift upgrades
- [[concept-fuel]], [[concept-scrap-economy]]

## Open Questions
- [ ] The actual distribution across `RANDOM_GIFT` — the 2/5 and 1/5 figures assume uniform
      selection across list entries.
- [ ] Whether the fuel cost is rolled before or after the gift, and whether the two are
      correlated.
- [ ] What `autoReward level="HIGH"` of type `scrap_only` pays.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml — the `DISTRESS_BEACON` pool)
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml — the `DISTRESS_BEACON_LANIUS` pool)
- [[source-fandom-friendly-ship-out-of-fuel]] (per raw/wiki/friendly-ship-out-of-fuel.md)
