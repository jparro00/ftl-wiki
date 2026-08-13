---
id: event-crystalline-research-facility
type: event
event_name: CRYSTAL_HUMAN_TESTS
sectors: [[[sector-hidden-crystal-worlds]]]
beacon_type: any
hostile: false
blue_options: [rock crew, [[item-backup-dna-bank]]]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unique, blue-option, crew-risk, clone-bay-revival, weapon-reward, drone-reward]
---

# Crystalline research facility — `CRYSTAL_HUMAN_TESTS`

## Summary
Crystalline scientists want to study your crew's physiology. Volunteering a crew member is
a 1-in-3 chance of getting them killed (a Clone Bay does bring them back) against two
reward outcomes; refusing is a 1-in-3 chance of a forced fight. Two blue options —
**Rock crew** or the **Backup DNA Bank** — take the payment with no risk at all.

Despite the event id, the Fandom page notes there is **nothing in the code that checks for
a Human crew member** ([[source-fandom-crystalline-research-facility]]) — confirmed by the
raw event, which has no `req="human"` anywhere ([[source-events-xml]]).

## Trigger & Where It Appears
- Sector: [[sector-hidden-crystal-worlds]] only
- Pool: one of **10** entries in the `NEUTRAL_CRYSTAL` event list, allocated exactly **12**
  times per sector (`min=12 max=12`) ([[source-events-xml]], [[source-sector-data-xml]])
- `unique="true"` — at most once per run
- Beacon: shows **no ship** on Long-Range Scanners
  ([[source-fandom-crystalline-research-facility]])

## Text
> You arrive near what appears to be a Crystalline research facility. A scientist quickly
> messages you, "Ah! You're those aliens! Please, I've heard so much about you and I'm
> really curious about your physiology! Would you let us run a few simple tests?"

(`event_CRYSTAL_HUMAN_TESTS_text`, per [[source-text-events-xml]])

> ⚠️ **CONTRADICTION:** intro wording.
> - Game files: *"I've heard so much about you and I'm **really** curious about your
>   physiology"* ([[source-text-events-xml]]).
> - Fandom: *"I've heard so much about you and I'm curious about your physiology"* — no
>   "really" ([[source-fandom-crystalline-research-facility]]).
> Trusting the game files (`high` vs `medium`). Cosmetic, and most likely a transcription
> slip rather than a vanilla/AE difference — nothing else in the page's text differs.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Allow them to run tests on a crewmember. | — | Loads `CRYSTAL_HUMAN_TESTS_ACCEPT` — three entries, below. | — |
| 2 | Refuse. | — | Loads `CRYSTAL_HUMAN_TESTS_REFUSE` — three entries, below. | — |
| 3 | **(Rock crewmember)** Send your Rockman crew. | `req="rock"` | *"Ah! My dear evolutionary cousin!…"* → `autoReward level="MED"` **standard** — medium scrap with resources. | 100% |
| 4 | **(Backup DNA Bank)** Send your crew's data. | `req="BACKUP_DNA"` | *"Full genetic and personal profiles stored digitally?…"* → `autoReward level="MED"` **weapon** — a **weapon** with medium scrap. | 100% |

### Sub-event: `CRYSTAL_HUMAN_TESTS_ACCEPT`
Three entries ([[source-events-xml]], [[source-fandom-crystalline-research-facility]]):

| Entry | Result |
|---|---|
| 1 | *"…your companion is... broken."* → `removeCrew` with `<clone>true</clone>` — **crew member killed, revived by a Clone Bay if you have one** — plus `autoReward level="LOW"` **weapon** (a weapon with low scrap). |
| 2 | Scans go fine → `autoReward level="MED"` **stuff** (Fandom: fuel 2–4, missiles 2–4, drone parts 1, with scrap). |
| 3 | Genome mapped → `autoReward level="LOW"` **drone** — a **drone schematic** with low scrap. |

### Sub-event: `CRYSTAL_HUMAN_TESTS_REFUSE`
Three entries, two of which are the same harmless text ([[source-events-xml]]):

| Entry | Result |
|---|---|
| 1, 2 | *"Perhaps the next aliens we meet will have some respect for the advancement of science."* Nothing happens. |
| 3 | *"…we must not let this opportunity pass us by. Submit and you will be treated reasonably well!"* → `ship load="CRYSTAL_SHIP_NO_SURRENDER" hostile="true"` — a fight with **default rewards**, no surrender, no escape. |

So refusing is a 2-in-3 clean exit and a 1-in-3 forced fight.

## Blue Options
- **Rock crew member** (`req="rock"`) — medium scrap with resources, no risk. Note this is
  a *species* gate, not the Rock Cruiser: any Rockman satisfies it.
- **Backup DNA Bank** (`req="BACKUP_DNA"`) — a weapon with medium scrap, no risk. Marked
  `<!--DLC-->` in the source file, i.e. Advanced Edition content
  ([[source-events-xml]]).

Both blue options bypass the crew-death risk *and* the refusal fight, and both are
strictly better than any non-blue branch.

## Rewards & Risks
- **Rewards:** medium standard (Rock), a weapon with medium scrap (DNA Bank), medium stuff,
  a drone schematic with low scrap, or a weapon with low scrap.
- **Risks:** a dead crew member (1 of 3 accept entries — recoverable with a Clone Bay), or
  a no-surrender Crystal warship fight (1 of 3 refuse entries).
- Note the asymmetry: the "bad" accept outcome still pays you a weapon.

## Strategy Notes
- With either blue option, take it — there is no downside branch behind them.
- Without one, "Allow them" is the better gamble than "Refuse" if you have a Clone Bay,
  since every accept entry pays something and the only loss is reversible; without a Clone
  Bay it is a straight 1-in-3 crew member against a weapon or drone schematic.
  *(Opinion, built on the list weightings above.)*
- Refusing is not the safe option people assume: it carries its own 1-in-3 fight.

## Related
- [[sector-hidden-crystal-worlds]]
- [[item-backup-dna-bank]] — unlocks choice 4
- [[entity-rock-men]] — the species gate on choice 3
- [[entity-crystal-men]]
- [[event-crystalline-men-buried]] — the sector's other crew-loss branch, where a Clone Bay
  explicitly does **not** work
- [[concept-blue-options]]

## Open Questions
- [ ] Which weapon pool the `autoReward MED weapon` and `LOW weapon` grants draw from, and
      whether the sector `rarityList` constrains them.
- [ ] Whether the crew member sent is chosen by the player.

## Sources
- [[source-events-xml]] (per raw/gamedata/events_crystal.xml, raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-crystalline-research-facility]] (per raw/wiki/crystalline-research-facility.md)
