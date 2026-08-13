---
id: event-asteroid-mining-colony
type: event
event_name: HELP_MINERS
sectors: [[[sector-civilian-sector]], [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-federation-space]], [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]], [[sector-pirate-controlled-sector]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]], [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]], [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]], [[sector-uncharted-nebula]]]
beacon_type: any
hostile: false
blue_options: [missile weapon]
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [trading, unique, missiles, augment-reward, hull-repair, reactor-upgrade, blue-option, cosmetic-blue, ae]
---

# Asteroid mining colony — `HELP_MINERS`

## Summary
A pure trade: hand over missiles, get something back. Five missiles buys one of scrap,
hull repairs, or a reactor upgrade; fifteen buys a strictly better version of the same
table, with a random augment on the top slot. There is no risk anywhere in the event and
no fight in any branch — the only question is whether your missiles are worth more in the
launcher than on the table. Its blue option is famously decorative: it does nothing at all.

## Trigger & Where It Appears
- **Advanced Edition content.** The event lives in the `DLC!!!` block of `newEvents.xml`
  and both list entries that load it are annotated as DLC additions
  ([[source-newevents]]). Its blue-option gate, the `WEAPONS_MISSILES_EVENTS` blueprint
  list, is defined only in `dlcBlueprintsOverwrite.xml`
  ([[source-dlcblueprintsoverwrite]]) — with the DLC off, the gate has no definition.
- Lists: `ITEMS` in `newEvents.xml`, and `OVERRIDE_ITEMS` in `dlcEventsOverwrite.xml`
  which replaces it under the DLC ([[source-newevents]],
  [[source-dlceventsoverwrite]]).
- `sector_data.xml` allocates `ITEMS` in fourteen sector descriptions, from 0–2 up to 2–3
  beacons each ([[source-sector-data-xml]]) — the sectors listed in the frontmatter.
  `ITEMS` is also a member of `EXIT_LIST` and `NON_HOSTILE` in `newEvents.xml`, so the
  event reaches exit beacons as well; Fandom records this as `alsooccur=exit`.
- Beacon: an items/trading beacon; no ship staged, so it is never hostile.
- `unique="true"` — at most once per run.

> ⚠️ **CONTRADICTION:** sector coverage.
> - Game files: `sector_data.xml` allocates `ITEMS` in **fourteen** sector descriptions,
>   including `STANDARD_SPACE` ([[source-sector-data-xml]]).
> - Fandom: lists **thirteen** sectors and omits Federation space
>   ([[source-fandom-asteroid-mining-colony]]).
>
> Trusting the game files — reliability `high` vs `medium`. This looks like an omission in
> the wiki's location template rather than a version difference; `ITEMS` is allocated in
> `STANDARD_SPACE` in the same file that Fandom's other thirteen entries come from.

## Text
> You come across an asteroid mining colony. They message you immediately, saying,
> "Greetings. Our supplies of mining explosives have run out ever since the Rebels
> blockaded this system. Do you have any extra explosives?"

(`event_HELP_MINERS_text`, per [[source-text-events-xml]])

## Choices & Outcomes

All four top-level choices are `hidden="true"` — none of them previews its result.

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | **(Missile Weapon)** Offer to solve their problem by launching a missile. | `req="WEAPONS_MISSILES_EVENTS"` | *"…Launching a military grade weapon into our mines isn't exactly what I would call, 'union-friendly'."* Then **the same three non-blue choices are offered again**. No mechanical effect whatsoever. | 100% nothing |
| 2 | Give them the requested 5 missiles. | — | −5 missiles, then loads `eventList HELP_MINERS_1` (3 entries). | 1/3 each |
| 3 | Give them 15 missiles. | — | −15 missiles, then loads `eventList HELP_MINERS_2` (3 entries). | 1/3 each |
| 4 | Decline. | — | *"I understand. Good luck out there. We'll try to make do with what we have."* Nothing. | 100% |

`HELP_MINERS_1` — the 5-missile table. Every entry deducts 5 missiles:

| # | Prose | Effect |
|---|-------|--------|
| 1 | *"They thank you for your generosity and offer some scrap in exchange."* | **+15 to +25 scrap** |
| 2 | *"They thank you and offer to have their engineers repair some of your ship's hull."* | `damage amount="-10"` — **10 hull repaired** |
| 3 | *"They thank you and offer to have their engineers try to upgrade your reactor."* | `upgrade system="reactor" amount="1"` |

`HELP_MINERS_2` — the 15-missile table. Every entry deducts 15 missiles:

| # | Prose | Effect |
|---|-------|--------|
| 1 | *"…Let me see what I can scrounge up to offer you."* | **+30 to +40 scrap** and `damage amount="-5"` — **5 hull repaired** |
| 2 | *"…They offer to have their engineers fix up your ship and upgrade your reactor."* | `damage amount="-15"` — **15 hull repaired** — and `upgrade system="reactor" amount="1"` |
| 3 | *"…After some time they deliver a ship Augment for installation on your ship."* | `augment name="RANDOM"` — a **random augment** |

**Assuming uniform selection across the three entries in each list**, each outcome is 1/3.
The game files state no percentage; these fractions are derived from list membership only
([[source-newevents]]). [[source-fandom-asteroid-mining-colony]] lists the same three
outcomes per tier without odds, which is consistent.

## Blue Options
- **Any missile weapon** (`req="WEAPONS_MISSILES_EVENTS"`) — **purely cosmetic.** The
  branch prints a joke refusal and re-presents the identical three non-blue choices; it
  grants nothing and costs nothing. Fandom flags it the same way: *"[option has no
  effect]"* ([[source-fandom-asteroid-mining-colony]]).
- The gate is a blueprint list, not a single weapon. Its members are `MISSILES_1`,
  `MISSILES_2`, `MISSILES_2_PLAYER`, `MISSILES_3`, `MISSILES_BURST`, `MISSILES_BREACH`
  and `MISSILE_CHARGEGUN` ([[source-dlcblueprintsoverwrite]]) — i.e. any missile launcher,
  not merely having missile ammunition.
- Worth recording as a case study for [[concept-blue-options]]: a blue option can be
  flavour only, and this event proves the pattern exists.

## Rewards & Risks
- **Cost:** 5 or 15 missiles, deducted on every outcome of the chosen tier. Nothing else
  is ever spent.
- **Rewards, 5 missiles:** 15–25 scrap, *or* 10 hull repair, *or* +1 reactor.
- **Rewards, 15 missiles:** 30–40 scrap and 5 hull, *or* 15 hull and +1 reactor, *or* a
  random augment.
- **Risks: none.** No branch stages a ship, boarders, damage, or a hazard. The only way to
  lose is to overpay in missiles.
- The 15-missile tier is better than three times the 5-missile tier on the scrap slot
  (30–40 vs 15–25) and adds an augment slot that the cheap tier does not have. But it is
  a real commitment: 15 missiles is a substantial fraction of a normal stock.

## Strategy Notes
- If you have no missile-based weapon equipped, missiles are dead weight and both tiers
  are close to free value — take the 15 if you can afford it, for the augment chance.
- If you are running a missile weapon, 15 missiles is a lot of shots. The 5-missile tier
  is the safer trade. (Opinion, reasoned from the outcome table; no source ranks the
  tiers.)
- Both hull-repair outcomes are worth more than they look: repairs bought at a store cost
  scrap, and 10–15 hull is a large chunk of a Kestrel's total.
- The blue option is a trap for attention only — it wastes nothing, but do not go out of
  your way for a missile launcher expecting it to matter here.

> ⚠️ **CONTRADICTION:** minor wording in the blue-option refusal.
> - Game files: *"isn't exactly what I **would call,** 'union-friendly'"*
>   ([[source-text-events-xml]])
> - Fandom: *"isn't exactly what I'**d call** 'union-friendly'"*
>   ([[source-fandom-asteroid-mining-colony]])
>
> Trusting the game files. A transcription slip, not a version difference — the whole
> event is AE content.

## Related
- [[event-refueling-platform]] — the other AE resource-trade filler in the same file
- [[event-abandoned-station]], [[event-confused-mantis]] — same file, same AE additions
- [[concept-blue-options]] — this event's cosmetic blue option
- [[item-reactor]]
- [[event-dock-bomb-salesman]] — the cut event that *sold* missiles, the mirror of this one

## Open Questions
- [ ] Whether `eventList` selection is uniform (the 1/3 figures depend on it).
- [ ] Whether the 15-missile choice is hidden or greyed out when you hold fewer than 15
      missiles — no `req` in the XML controls it.
- [ ] Which augment pool `augment name="RANDOM"` draws from, and whether it can roll a
      duplicate of one you already own.
- [ ] Why Fandom's location list omits Federation space.

## Sources
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-dlcblueprintsoverwrite]] (per raw/gamedata/dlcBlueprintsOverwrite.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-asteroid-mining-colony]] (per raw/wiki/asteroid-mining-colony.md)
