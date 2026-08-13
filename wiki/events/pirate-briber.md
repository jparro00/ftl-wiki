---
id: event-pirate-briber
type: event
event_name: PIRATE_BRIBER
sectors: [[[sector-abandoned-sector]], [[sector-civilian-sector]], [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-federation-space]], [[sector-pirate-controlled-sector]], [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]], [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 9
tags: [pirate, moral-choice, optional-fight, store-chance, hull-repair-chance, fleet-delay-chance, unique]
---

# Pirate briber — `PIRATE_BRIBER`

## Summary
A pirate is running down another ship and offers you scrap to look the other way. Take the
bribe for a small guaranteed payout, or intervene — an entirely optional fight against an
elite-flavoured pirate that, if you win it, opens a second roll on `PIRATE_BRIBER_WIN`:
the rescued ship might open a **store**, repair **15 hull**, delay the **rebel fleet**, or
turn out to be a Rebel scout. It is the richest neutral beacon in the pirate pool and also
the only one that can hand you a store out of nowhere.

## Trigger & Where It Appears
- Sectors: [[sector-abandoned-sector]], [[sector-civilian-sector]],
  [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]],
  [[sector-federation-space]], [[sector-pirate-controlled-sector]],
  [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]],
  [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]
- Event lists: `NEUTRAL_PIRATE` ([[source-events-pirate]]); `NEUTRAL`,
  `NEUTRAL_CIVILIAN`, `NEUTRAL_EXIT` ([[source-newevents]]); `NEUTRAL_ENGI`
  ([[source-events-engi]]); `NEUTRAL_LANIUS` ([[source-dlcevents-anaerobic]]); plus the Advanced
  Edition replacements `OVERRIDE_NEUTRAL` and `OVERRIDE_NEUTRAL_EXIT`
  ([[source-dlceventsoverwrite]]) — both of which are described in the file as
  *"hardcoded to fill out a sector if it ran out of all other calls"*, i.e. this is a
  filler event as well as a pool event
- `unique="true"` — once per run ([[source-events-pirate]];
  [[source-fandom-pirate-briber]] agrees, and also lists Uncharted Nebula among its
  locations)
- The ship is loaded `hostile="false"`, so nothing happens until you choose
- Long-range scanners show a ship ([[source-fandom-pirate-briber]], `LRSmap=ship`)

## Text
Varies — `<text load="PIRATE_BRIBER"/>` over a three-entry `textList`
([[source-events-pirate]]). All three, per [[source-text-events-xml]]:

> You come across a pirate in hot pursuit of an unidentified ship. You quickly receive a
> transmission from the pirate: "Stay out of this fight and we'll make it worth your
> while."

> An unidentified ship is badly damaged and still being assaulted by a space pirate. The
> victim begins a distress message until the pirate cuts in and offers to split the bounty
> if you sit tight.

> A missile shoots across your bow when the jump completes. Your scans quickly reveal a
> ship with pirate markings pursuing an unknown vessel. The pirate hails you: "Damn it, we
> weren't expecting company. Stay out of this and you could profit."

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Accept their bribe. | — | *"Good choice, son. We've both come out of this richer."* → `autoReward level="LOW"` `standard`. No fight. | 100% |
| 2 | Try to be a hero. Attack the pirate. | — | *"The pirate ship stops its pursuit and locks weapons onto your ship."* → `<ship hostile="true"/>`, fight `PIRATE_BRIBER` (below). | 100% |

### The `PIRATE_BRIBER` ship
`<ship name="PIRATE_BRIBER" auto_blueprint="SHIPS_PIRATE">`, tagged `<!-- NEEDS ELITE TAG -->`
in the file ([[source-events-ships]]):

| Branch | Trigger in the file | Result |
|---|---|---|
| Surrender | `chance="0.3" min="3" max="4"` | *"Fine! Our previous offer was not generous enough, let's improve it."* → **Accept**: ship goes non-hostile, `autoReward level="HIGH"` `stuff`. **Reject**: fight continues. Accepting ends the event here — it does **not** load `PIRATE_BRIBER_WIN`. |
| Escape | `chance="0.4" min="3" max="4"` | *"You've proved a sufficient match for the pirates; they are powering up their FTL and trying to get away."* |
| Got away | — | *"The pirate has abandoned pursuit of both you and its former prey. You attempt to hail the damaged ship."* → loads `PIRATE_BRIBER_WIN` |
| Destroyed | — | *"The pirate explodes, leaving behind a substantial collection of useful scrap material. You go to examine the ship you just saved."* → `autoReward level="RANDOM"` `scrap_only`, then `PIRATE_BRIBER_WIN` |
| Crew killed | — | *"The pirates are all dead, leaving the ship dead in space. You scrounge what you can from their ship before contacting its former prey."* → `autoReward level="MED"` `standard`, then `PIRATE_BRIBER_WIN` |

Note the escape branch still pays out: the `gotaway` text hands you `PIRATE_BRIBER_WIN`
anyway, so driving the pirate off is not a wasted fight.

### `PIRATE_BRIBER_WIN` — hailing the ship you saved
Five entries in the list. Every entry is distinct, so under **uniform selection across
list entries** each is **1/5** ([[source-events-pirate]]):

| # | Result | Share |
|---|---|---|
| 1 | *"…the ship under attack was a Rebel scout! It's too damaged to put up much of a fight."* → two choices: **Destroy the ship and salvage it** → `autoReward level="LOW"` `standard`; or **use the leverage to convince them to delay the pursuing fleet** → `<modifyPursuit amount="-1"/>`, the rebel fleet is set back **1 turn** | 1/5 |
| 2 | *"You were too late. A hull breach deprived the crew of oxygen during your fight…"* → `autoReward level="MED"` `scrap_only` | 1/5 |
| 3 | *"The pirate's victim quickly jumps away before you have a chance to speak to them."* → nothing | 1/5 |
| 4 | *"Thank you for the aid! I'm an arms dealer that usually only works with Rebels…"* → a **store opens** (`<store/>`) | 1/5 |
| 5 | *"…our engineer should be proficient enough to patch your ship up a bit."* → `<damage amount="-15"/>`, i.e. **15 hull repaired** | 1/5 |

[[source-fandom-pirate-briber]] lists the same five outcomes and adds that the fleet delay
has no effect in [[sector-the-last-stand]].

## Blue Options
None. No `req=` gate anywhere in this event or its sub-lists — which is notable given how
large the payoff is.

## Rewards & Risks
- **Choice 1 (bribe):** a guaranteed but small `LOW` `standard` payout, zero risk.
- **Choice 2 (fight):** `RANDOM` `scrap_only` / `MED` `standard` for the win, *plus* a 1/5
  shot at a free store, a 1/5 shot at 15 hull, and a 1/5 shot at a fleet delay. Or `HIGH`
  `stuff` if you accept the surrender — the biggest single payout in the event, but it
  skips `PIRATE_BRIBER_WIN` entirely.
- **Risk:** an elite-flavoured pirate you had no obligation to fight, and a 1/5 chance the
  ship you "saved" is a Rebel scout that pays you least of all.

## Strategy Notes
- *(Opinion.)* Fighting is the better line on any ship that can take a pirate cleanly:
  four of the five `PIRATE_BRIBER_WIN` entries are worth more than the `LOW` bribe, and
  two of them (store, 15 hull) are worth far more than any scrap payout in the pool.
- The surrender offer is a trap for value: `HIGH` `stuff` is a lot of resources, but
  refusing it and finishing the ship keeps your `PIRATE_BRIBER_WIN` roll alive. Take the
  surrender only if the fight has already cost you hull you cannot spare.
- The fleet-delay outcome is the only rebel-pursuit lever in the entire pirate pool.

## Related
- [[event-pirate-toll]] — the mirror image: you pay the pirate instead
- [[event-pirate-ship-attacking-civilian]] — the other "intervene or don't" pirate beacon,
  with a different reward tree
- [[event-store-pirate]] — the ordinary store beacon
- [[concept-rebel-fleet-advance]] — what `modifyPursuit` moves
- [[entity-pirates]], [[entity-rebels]]
- [[sector-pirate-controlled-sector]], [[sector-abandoned-sector]],
  [[sector-civilian-sector]], [[sector-zoltan-controlled-sector]]

## Open Questions
- [ ] `raw/gamedata/events_pirate.xml` has a stray `-` character immediately after the
      `</event>` closing entry 4 of `PIRATE_BRIBER_WIN`. Harmless-looking typo, but it is
      inside the list — does the parser tolerate it? ([[source-events-pirate]])
- [ ] Exact values behind `LOW`/`MED`/`HIGH`/`RANDOM` `autoReward` levels, and what
      `stuff` rolls. Fandom reads `HIGH` `stuff` as fuel 3–6, missiles 4–8, drone parts
      1–2 ([[source-fandom-pirate-briber]]) — a community reading, not a file value.
- [ ] Whether `chance="0.3"` / `chance="0.4"` are the probabilities of surrendering and
      escaping, or of *not* doing so — see the contradiction on [[event-pirate-fight]].

## Sources
- [[source-events-pirate]] (per raw/gamedata/events_pirate.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml — `NEUTRAL`, `NEUTRAL_CIVILIAN`,
  `NEUTRAL_EXIT`)
- [[source-events-engi]] (per raw/gamedata/events_engi.xml — `NEUTRAL_ENGI`)
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml — `NEUTRAL_LANIUS`)
- [[source-fandom-pirate-briber]] (per raw/wiki/pirate-briber.md)
