---
id: event-slug-store-ship
type: event
event_name: NEBULA_SLUG_FAKE_STORE
sectors: [[[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: nebula
hostile: false
blue_options: [slug crew]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unique, nebula, boarding-risk, store-chance, fuel-reward, blue-option, default-rewards]
---

# Slug store ship — `NEBULA_SLUG_FAKE_STORE`

## Summary
A Slug merchant offers to show you his wares, then stalls you through three pages of legal
disclaimers while his crew teleports aboard. Sitting through the whole routine gives a
1-in-3 shot at a real store plus 5 fuel; the other two thirds are ambushes. A Slug crew
member spots the boarder mid-patter and turns the trap into an ordinary fight.

## Trigger & Where It Appears
- Sectors: [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]] — via the
  `NEBULA_NEUTRAL_SLUG` event list (`min 3 / max 5` per sector)
  ([[source-events-slug]], [[source-sector-data-xml]])
- Beacon: nebula (`<environment type="nebula"/>`), `unique="true"`
- A `JELLY` ship is present **non-hostile** from arrival
  (`<ship load="JELLY" hostile="false"/>`)

## Text
> A Slug transport ship is stationed near the beacon with a military escort ship. They
> message you, "We have been waiting for a customer for agesss. Care to see our waresss?"

(`event_NEBULA_SLUG_FAKE_STORE_text`, per [[source-text-events-xml]])

## Choices & Outcomes

The event is a nested chain of choices, not a flat list. (The batch extract flattens it and
loses most of the tree — the structure below is read from [[source-events-slug]] directly.)

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Decline. | — | "Oh well... We ssshall wait here then." Nothing happens. | 100% |
| 2 | Ask to see the goods. | — | "Before we get ahead of ourssselves, I need to explain sssome ground ruless…" → the disclaimer chain below. | 100% |

### The disclaimer chain (choice 2)

1. *"Firssst... We accept no tradesss, couponss or refundss. Purchasess are final.
   Underssstand?"*
   - **Understood.** → *"We hold no liability for productsss damaged post ssale…
     Not a problem?"*
     - **Not a problem.** → rolls `NEBULA_SLUG_FAKE_STORE_LIST` (3 entries, below)
     - **Forget this.** → rolls `NEBULA_SLUG_FAKE_STORE_LEAVING` (2 entries, below)
   - **Forget this.** → *"Fine... Not everyone appreciates good dealss..."* — nothing happens
   - **(Slug crewmember)** *Our Slug senses someone aboard the ship. Investigate it.*
     (`req="slug"`) → *"…You catch him before he could finish and he teleports away."* →
     `<ship load="JELLY" hostile="true"/>`, default rewards, **no boarders**

### `NEBULA_SLUG_FAKE_STORE_LIST` — sitting through the whole pitch

| Entry | Text | Effect |
|---|---|---|
| 1 | "Great. Let me show you our waress… have this complimentary fuel as well." | `<item type="fuel" min="5" max="5"/>` **and** `<store/>` — 5 fuel and a real store |
| 2 | "During our discussion, my man hass taken the liberty of disabling your weaponss…" | `<ship load="JELLY_STATUS_WEAPONS" hostile="true"/>`, `<boarders min="1" max="1" class="slug"/>`, `<status type="limit" target="player" system="weapons" amount="0"/>` — 1 Slug boarder, Weapon Control offline |
| 3 | "Thank you. If you could do me one more courtesssy... please die quietly." | `<ship load="JELLY" hostile="true"/>`, `<boarders min="2" max="2" class="slug"/>` — 2 Slug boarders, default rewards |

> ⚠️ **CONTRADICTION:** what entry 2 actually loads.
> - Game files: `<ship load="JELLY_STATUS_WEAPONS" hostile="true"/>` — which would pay
>   `HIGH standard` and clear the weapons status on a win ([[source-events-ships]]).
> - Fandom: the fight is against a plain Slug ship at **default rewards**, and *"Weapon
>   Control stays offline after the fight, and returns to normal after an FTL jump"* — with
>   an inline note that the `JELLY_STATUS_WEAPONS` load *"for whatever reason"* does not
>   happen, "from at least 2015 till 2022+ game versions"
>   ([[source-fandom-slug-store-ship]]).
>
> This is a claimed **engine bug**, not a data difference — both sides quote the same XML.
> The files say what the designers intended; Fandom reports what the game does. If you are
> planning around the reward, assume default rewards.

### `NEBULA_SLUG_FAKE_STORE_LEAVING` — backing out late

| Entry | Text | Effect |
|---|---|---|
| 1 | "Very well... Impatient alienss..." | Nothing happens |
| 2 | "…the merchant was trying to stall you while they hacked into your systems." | `<ship load="JELLY" hostile="true"/>`, `<boarders min="1" max="1" class="slug"/>` — default rewards |

## Blue Options
- **Slug crew member** (`req="slug"`) — offered at the second disclaimer page. Detects the
  teleporting boarder before he lands, giving a clean fight against a `JELLY` at default
  rewards with **no boarders aboard**. It forfeits any chance at the store and the 5 fuel.

## Rewards & Risks
- Best case: 5 fuel **and** a store opening (1 of 3 entries on the full-patience path).
- Worst case: 2 Slug boarders plus a ship fight, or 1 boarder with your weapons dead.
- Declining at any point is always free; only the final "Not a problem" / "Forget this" pair
  can trigger boarders.
- The `JELLY` ship has a 50% surrender and 50% escape roll at low hull
  ([[source-events-ships]]; Fandom states this as 30–40% hull).

## Strategy Notes
- With a Slug aboard, take the blue option: a fight you control beats a 2-in-3 ambush.
- Without one, the gamble is 5 fuel + a store against boarders. Backing out at the last
  page is *not* safe either — half of `LEAVING` is still an ambush with a boarder. The only
  genuinely free exits are "Decline" at the start and "Forget this" on the **first**
  disclaimer page.
- Boarders are Slugs, so they are immune to mind control and cannot be seen by your sensors
  in a nebula.

## Related
- [[event-store-in-nebula-slug]] — the real Slug store beacon
- [[event-slug-repair-station]], [[event-slug-drink]] — the other Slug bait-and-switch
  events in these sectors
- [[entity-slugs]]

## Open Questions
- [ ] Whether the `JELLY_STATUS_WEAPONS` load failure Fandom describes is present in this
      1.6.x build.
- [ ] Whether the three `_LIST` entries are equally weighted.

## Sources
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-fandom-slug-store-ship]] (per raw/wiki/slug-store-ship.md)
