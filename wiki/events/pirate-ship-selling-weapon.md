---
id: event-pirate-ship-selling-weapon
type: event
event_name: NEBULA_WEAPONS_TRADER
sectors: [[[sector-civilian-sector]], [[sector-federation-space]], [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]], [[sector-uncharted-nebula]]]
beacon_type: nebula
hostile: false
blue_options: [[[item-mind-control]]]
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [nebula, pirate, trading, blue-option, mind-control, scrap-risk, weapon-reward, unique]
---

# Pirate ship selling weapon — `NEBULA_WEAPONS_TRADER`

## Summary
A black-market weapon for 45 scrap, sight unseen — and a coin-flip chance the seller simply
takes your scrap and laughs. The Mind Control blue option looks like a fix but isn't: it
still leaves a 50/50, only now the bad half is an ambush instead of a robbery, and the
"better deal" it promises is retracted in the same paragraph.

## Trigger & Where It Appears
- Beacon: nebula (`<environment type="nebula"/>`).
- `unique="true"` — once per run.
- Lists: `NEBULA` ([[source-newevents]]), `NEBULA_NEUTRAL` ([[source-events-nebula]]) and
  `NEBULA_NEUTRAL_SLUG` ([[source-events-slug]]) — Federation Space and Civilian via
  `NEBULA`, [[sector-uncharted-nebula]] via `NEBULA_NEUTRAL` (7–8 beacons), the Slug
  sectors via `NEBULA_NEUTRAL_SLUG` (3–5 beacons) ([[source-sector-data-xml]]).
- Arrives non-hostile: `<ship load="PIRATE" hostile="false"/>`. Long-range scanners show a
  ship ([[source-fandom-pirate-ship-selling-weapon]]).
- Flagged `NEW` in the file's header comment — a later addition.

## Text
> A black market weapons trader spins you a tale of the dangers of the nebula before
> pushing his wares.

(`event_NEBULA_WEAPONS_TRADER_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Ignore the ship. | — | Empty `<event/>` — nothing happens. | 100% |
| 2 | Attack the ship. | — | `<ship hostile="true"/>` — fight the `PIRATE` ship, default rewards. | 100% |
| 3 | Purchase an unknown weapon for 45 scrap. | none (`hidden="true"`) | `NEBULA_WEAPONS_TRADER_LIST`, two entries — see below. | unknown (2-entry list) |
| 4 | **(Mind Control)** Convince him to make it a better deal. | `req="mind"`, `hidden="true"` | `NEBULA_WEAPONS_TRADER_LIST2`, two entries — see below. | unknown (2-entry list) |

### Choice 3 — `NEBULA_WEAPONS_TRADER_LIST`

| Entry | Text | Effect |
|---|---|---|
| 1 | *"You transfer the scrap and receive a weapon in return. Lets hope it was worth it."* | **−45 scrap**, `<weapon name="RANDOM"/>` — a random weapon. |
| 2 | *"You transfer over the scrap, but he reneges on the agreement. 'I told you this was a dangerous place!'"* | **−45 scrap, no weapon.** Then: *Attack the ship!* → fight; or *Learn a valuable lesson and move on* → nothing. |

**The scrap is deducted in both entries**, because `item_modify` sits inside each branch of
the sub-list. [[source-fandom-pirate-ship-selling-weapon]] makes the consequence explicit:
*"If the trader cheated you, the lost 45 scrap won't be refunded even if you then attack
and win the fight against him."*

### Choice 4 — `NEBULA_WEAPONS_TRADER_LIST2` (AE only, `<!--DLC-->`)

| Entry | Text | Effect |
|---|---|---|
| 1 | *"Once 'convinced' to help he lowers the price and describes the weapon. However, he eventually comes to his senses and confusedly takes back his discount."* | **Buy the weapon** → −45 scrap, `<weapon name="RANDOM"/>`; or **Decline** → nothing, no cost. |
| 2 | *"Once 'convinced' to help, he casually states that his offer was actually a lie and that they planned to attack your ship."* | `<ship hostile="true"/>` — fight, no scrap lost. |

## Blue Options
- **[[item-mind-control]]** (`req="mind"`, no level) — AE-only. What it actually changes:
  - It **removes the robbery outcome**. You never lose 45 scrap for nothing.
  - It **does not reduce the price**. The discount is narratively offered and withdrawn
    inside the same string; the purchase is still 45 scrap.
  - It replaces the robbery with an **ambush** — a fight you didn't pick, though at least a
    free one.
  - Entry 1 also lets you see the weapon before buying
    ([[source-fandom-pirate-ship-selling-weapon]]) and decline at no cost.

  So it converts "50% chance of losing 45 scrap" into "50% chance of a fight, 50% chance of
  an informed purchase". That is a clear upgrade, but not the discount the choice label
  advertises.

## Rewards & Risks
- Best case: a random weapon for 45 scrap — potentially far above or far below that price.
- Worst case (choice 3): **−45 scrap and nothing**, unrecoverable.
- The `PIRATE` ship, if it comes to a fight:
  `<surrender chance="0.5" min="3" max="4" load="PIRATE_SURRENDER"/>` (accept →
  `autoReward level="RANDOM">stuff`), `<escape chance="0.5" min="2" max="4"
  load="PIRATE_ESCAPE"/>`, `<destroyed load="DESTROYED_DEFAULT"/>` → `MED` / `standard`
  ([[source-events-ships]], [[source-events-xml]]).
- `<weapon name="RANDOM"/>` places no floor on quality — the source states no rarity
  filter.

## Strategy Notes
- Without Mind Control, choice 3 is a genuine 50/50 on 45 scrap. Early in a run that is a
  meaningful fraction of your economy; late it is trivial. The event's difficulty therefore
  scales inversely with when you meet it. *(Opinion; no source frames it this way.)*
- With Mind Control, take choice 4 over choice 3 always — it strictly dominates.
- Choice 2 (attack immediately) is the option nobody takes and is arguably fine: default
  pirate rewards with a 50% surrender chance, and no scrap at risk.
- Fandom tags the event `Scrap loss risk` and `Weapon reward chance`
  ([[source-fandom-pirate-ship-selling-weapon]]).

## Related
- [[event-trade-resources-in-nebula]] — the nebula's risk-free trade
- [[event-pirate-smuggler]] — the other optional pirate encounter in the nebula pool
- [[event-pirate-fight-in-nebula]] — the shadowed forced pirate fight
- [[item-mind-control]], [[sector-uncharted-nebula]], [[sector-slug-home-nebula]]
- [[event-pirate-surrender]] — the shared `PIRATE_SURRENDER` aftermath this hull loads
- [[event-pirate-escape]] — the shared `PIRATE_ESCAPE` aftermath this hull loads

## Open Questions
- [ ] Weights inside both two-entry sub-lists (assumed 50/50, not stated).
- [ ] Whether `<weapon name="RANDOM"/>` draws from the full weapon pool or a rarity-limited
      subset.
- [ ] What happens if you have fewer than 45 scrap — no source addresses it.

## Notes on sector coverage
> ⚠️ **CONTRADICTION:** [[source-fandom-pirate-ship-selling-weapon]] lists four sectors
> (Civilian, Slug Controlled Nebula, Slug Home Nebula, Uncharted Nebula); the game files
> add [[sector-federation-space]] via the `NEBULA` allocation to `STANDARD_SPACE`
> ([[source-sector-data-xml]], [[source-newevents]]). Trusting the game files
> (`high` vs `medium`).

## Sources
- [[source-events-nebula]] (per raw/gamedata/events_nebula.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-pirate-ship-selling-weapon]] (per raw/wiki/pirate-ship-selling-weapon.md)
