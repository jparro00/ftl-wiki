---
id: event-zoltan-retake-the-ship
type: event
event_name: ZOLTAN_LIFERAFT
sectors: [[[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unique, augment-reward, crew-purchase, boarding-payoff, scrap-cost]
---

# Zoltan retake the ship — `ZOLTAN_LIFERAFT`

## Summary
A rescued Zoltan asks you to clear pirates off his ship **without destroying it**. The
game rewards exactly that: killing the boarding crew and leaving the hull intact pays an
augment plus high scrap, while blowing the ship up pays only medium scrap and a chance
to hire the (now shipless) Zoltan for 40 scrap. One of the clearest boarding-rewards-you
events in Zoltan space.

## Trigger & Where It Appears
- Sectors: [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]
- Beacon: ordinary; a non-hostile ship (`<ship load="ZOLTAN_LIFERAFT" hostile="false"/>`)
  is present on arrival, so the beacon shows a ship on Long-Ranged Scanners
  ([[source-events-zoltan]], [[source-fandom-zoltan-retake-the-ship]]).
- Reached via the `NEUTRAL_ZOLTAN` event list, allocated `min=5 max=6` beacons in both
  Zoltan sectors ([[source-sector-data-xml]]).
- `unique="true"`. The source file annotates it `<!-- ALSO A QUEST!!-->`.

## Text
> You pick up a Zoltan life raft floating in space. Its inhabitant asks you to retake his
> ship from the pirates who recently commandeered it. "I'm certain it is clear," he
> concludes, "that you must not destroy my vessel in the process."

(`event_ZOLTAN_LIFERAFT_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Engage the pirates. | — | `<ship hostile="true"/>` — the already-present `ZOLTAN_LIFERAFT` ship turns hostile. No outcome text; the branches below follow the fight. | 100% |
| 2 | Leave. | — | *"You refuse to get his ship back, but still offer to drop him off at the next station. The Zoltan is displeased, but directs you to a nearby starbase just the same."* Nothing happens. | 100% |

### Post-fight results

From [[source-fandom-zoltan-retake-the-ship]] (these branches live in
`events_ships.xml`, not ingested here):

| Win condition | Text | Reward |
|---------------|------|--------|
| **Killed the crew, hull intact** | *"The last pirate life-signs blink out and the Zoltan returns to his bridge. 'Egalitarianism is a cornerstone of successful cohabitation. Please, enjoy the fruits of your labor.'"* | an **augment** with **high scrap** |
| **Destroyed the ship** | *"You salvage what you can from the ship."* → `medium` scrap with resources, then *"The Zoltan looks deeply dissatisfied with your aiming and demands to be dropped off at your earliest convenience."* | `medium` scrap with resources, plus the hire offer below |

### The hire offer (destroyed branch only)

| # | Sub-choice | Outcome |
|---|-----------|---------|
| a | Let him go. | Nothing happens. |
| b | Offer to hire him for 40 scrap. | Loads `ZOLTAN_LIFERAFT_HIRE` — two entries, see below. |

`ZOLTAN_LIFERAFT_HIRE` ([[source-events-zoltan]], [[source-text-events-xml]]):

| Entry | Text | Effect |
|-------|------|--------|
| 1 | *"He responds haughtily, 'You would presume I would work under your command after such a display of… prowess? No, I must decline.'"* | Nothing. **You are not charged.** |
| 2 | *"He responds defeatedly, 'I suppose I have nowhere else to go without a ship. I accept your offer.'"* | `scrap −40` and `<crewMember amount="1" class="energy"/>` — a Zoltan crew member for 40 scrap. |

The scrap deduction sits inside entry 2 only, so a refusal costs nothing. No percentages
are stated for the two entries.

## Blue Options
None. No `req` attribute on either choice.

## Rewards & Risks
- **Best outcome:** an augment plus **high** scrap, for killing the crew without
  destroying the hull.
- **Second best:** `medium` scrap with resources, plus a coin-flip at a Zoltan crew
  member for 40 scrap.
- **Risk:** an ordinary ship fight. Fandom flags the surrender/escape behaviour of the
  enemy ship as unverified. Fandom also notes the **enemy crew is composed entirely of
  one random race** — which matters, because a Rockman or Mantis crew makes the
  kill-the-crew win much harder than a human one.

## Strategy Notes
- *Opinion:* this is a high-value beacon for any ship with a [[item-teleporter]],
  boarding drones, or anti-personnel weapons — the intended win condition is exactly
  what those builds do anyway, and the augment-plus-high-scrap payout is well above a
  normal fight.
- Without boarding capability, consider ion or hull-preserving damage to disable rather
  than destroy — though no source here confirms that a disabled-but-intact ship counts
  as the crew-kill branch.
- If you do destroy it, the 40-scrap hire is a gamble: only one of the two responses
  actually sells you the crew member, and the other is free.

## Related
- [[entity-zoltan]] — the crew member on offer
- [[item-teleporter]] — the enabling system for the good outcome
- [[event-zoltan-security-checkpoint]], [[event-zoltan-wise-man]] — the other unique
  `NEUTRAL_ZOLTAN` members in this batch

## Open Questions
- [ ] Weighting between the two `ZOLTAN_LIFERAFT_HIRE` entries.
- [ ] Which augment pool the crew-kill branch draws from.
- [ ] `ZOLTAN_LIFERAFT` ship loadout and surrender/escape values (needs
      `events_ships.xml`); Fandom marks these as needing verification.
- [ ] Does an ion-disabled (not destroyed) ship count as the crew-kill win?

## Sources
- [[source-events-zoltan]] (per raw/gamedata/events_zoltan.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-zoltan-retake-the-ship]] (per raw/wiki/zoltan-retake-the-ship.md)
