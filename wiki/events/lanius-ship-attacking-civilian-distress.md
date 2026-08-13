---
id: event-lanius-ship-attacking-civilian-distress
type: event
event_name: LANIUS_DISTRESS_FIGHT
sectors: [[[sector-abandoned-sector]]]
beacon_type: distress
hostile: true
blue_options: [lanius crew]
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [lanius, distress, civilian-rescue, blue-option, crew-reward-chance, unique, advanced-edition]
---

# Lanius ship attacking civilian distress — `LANIUS_DISTRESS_FIGHT`

## Summary
A distress beacon where a civilian ship is being shot apart by a rogue Lanius vessel. You
can fight, walk away, or — with a Lanius crew member — have your own Lanius shout down
their captain, which is a coin-flip between defusing the whole thing for free and being
attacked anyway. Winning either way leads to the shared "save the civilian" reward list.

## Trigger & Where It Appears
- Sector: [[sector-abandoned-sector]] only.
- List: `DISTRESS_BEACON_LANIUS`, allocated `min=1 max=2` per sector
  ([[source-sector-data-xml]]); twelve members → **1/12** *assuming uniform selection
  across list entries* ([[source-dlcevents-anaerobic]]).
- Carries `<distressBeacon/>`; `unique="true"`.
- The event spawns `<ship load="LANIUS_CIVILIAN" hostile="false"/>` up front — the enemy
  ship exists but is not yet shooting at you, which is why every fight branch just flips
  it with `<ship hostile="true"/>`.

> **AE-only** — Advanced Edition file, Advanced Edition sector, and the blue option
> requires the AE-exclusive Lanius species (`req="anaerobic"`).

## Text
> You immediately do a short-range scan after arriving at the beacon. It appears to be
> coming from a small civilian vessel under fire from a Lanius ship. Not all Lanius are
> content with simply scavenging the wrecks of previous battles.

(`event_LANIUS_DISTRESS_FIGHT_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Fight the Lanius ship. | — | *"You move in to intercept the ship…"* → combat with `LANIUS_CIVILIAN`. Destroyed → `MED standard`; dead crew → `HIGH standard`; either then offers **Contact the civilian ship** (`SAVE_CIVILIAN_LIST`). | 100% |
| 2 | Avoid the conflict. | — | *"Your crew seems unhappy to leave the civilians to such a fate…"* → nothing happens. | 100% |
| 3 | **(Lanius Crew)** Have your crew admonish their captain. | `req="anaerobic"` | Loads the two-member `LANIUS_DISTRESS_FIGHT_LANIUS` list: (a) the captain stands down, you go straight to **Contact the civilian ship**; (b) the ship is fully rogue and attacks → same fight as choice 1. | **1/2** each *(assuming uniform selection across list entries)* |

### Contact the civilian ship (`SAVE_CIVILIAN_LIST`)
The shared six-member rescue list defined in `events_pirate.xml`
([[source-events-pirate]]) — **1/6** each *assuming uniform selection across list
entries*:

| Result | Payload |
|---|---|
| Survivor asks to join | *"Welcome aboard!"* → **+1 crew member**; or decline → nothing |
| Science vessel thanks you | `autoReward MED standard` |
| Crew did not survive | `autoReward LOW standard` |
| Shipwright offers equipment | `autoReward LOW weapon` |
| Crew patches your hull | `<damage amount="-5"/>` → **5 hull repaired** |
| Civilian already fled | nothing |

## Blue Options
- **Lanius crew member** (`req="anaerobic"`) — turns a guaranteed fight into a 50/50 on
  skipping the fight entirely while keeping the rescue reward. It never makes the outcome
  *worse* than choice 1, since the bad branch is exactly choice 1's fight
  ([[source-dlcevents-anaerobic]], [[source-fandom-lanius-ship-attacking-civilian-distress]]).

## Rewards & Risks
- The enemy `LANIUS_CIVILIAN` ship definition has **no surrender and no escape** entries —
  it fights to the end ([[source-dlcevents-anaerobic]],
  [[source-fandom-lanius-ship-attacking-civilian-distress]]).
- Killing the crew rather than destroying the hull upgrades the payout from `MED` to
  `HIGH`.
- The rescue list can hand you a **free crew member**, a free weapon, or 5 hull — or
  nothing at all.
- Risk: a full warship fight with no bail-out, in a sector where you may already be
  chewed up.

## Strategy Notes
- With a Lanius aboard, always take choice 3 first: half the time you get the rescue
  rewards for free, and the other half you are exactly where choice 1 would have put you.
- Without one, this is a normal "is my hull worth a rescue list roll" decision. The list
  averages modestly, but the crew-member and hull-repair results are meaningful.

## Related
- [[event-lanius-ship-attacking-civilian]] — the non-distress version of the same setup,
  same enemy ship, same rescue list
- [[event-pirate-ship-attacking-civilian-lanius]] — pirate-flavoured twin in this sector
- [[event-lanius-fight-distress]], [[event-lanius-ship-attacking-mantis]] — the other
  Lanius distress beacons
- [[entity-lanius]], [[sector-abandoned-sector]]

## Open Questions
- [ ] Numeric values behind `LOW` / `MED` / `HIGH`.
- [ ] Whether the two `LANIUS_DISTRESS_FIGHT_LANIUS` entries are genuinely equally
      weighted (the list states no weights).

## Sources
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-pirate]] (per raw/gamedata/events_pirate.xml — `SAVE_CIVILIAN_LIST`)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-lanius-ship-attacking-civilian-distress]] (per raw/wiki/lanius-ship-attacking-civilian-distress.md)
