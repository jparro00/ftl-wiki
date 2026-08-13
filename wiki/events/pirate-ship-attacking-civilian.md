---
id: event-pirate-ship-attacking-civilian
type: event
event_name: PIRATE_CIVILIAN
sectors: [[[sector-civilian-sector]], [[sector-federation-space]], [[sector-pirate-controlled-sector]], [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]], [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 8
tags: [pirate, moral-choice, optional-fight, crew-reward-chance, save-civilian-list]
---

# Pirate ship attacking civilian — `PIRATE_CIVILIAN`

## Summary
A pirate is running down a civilian ship. Intervene and you fight a pirate that **cannot
surrender and cannot escape** — then roll the shared `SAVE_CIVILIAN_LIST` reward table on
top of the kill reward. Walk away and nothing happens. This is the canonical home of
`SAVE_CIVILIAN_LIST`, which several other events across the game reuse.

## Trigger & Where It Appears
- Sectors: [[sector-civilian-sector]], [[sector-federation-space]],
  [[sector-pirate-controlled-sector]], [[sector-rock-controlled-sector]],
  [[sector-rock-homeworlds]], [[sector-slug-controlled-nebula]],
  [[sector-slug-home-nebula]]
- Event lists: `NEUTRAL_PIRATE` ([[source-events-pirate]]); `NEUTRAL`,
  `NEUTRAL_CIVILIAN`, `NEUTRAL_EXIT` ([[source-newevents]]); `NEUTRAL_ROCK`
  ([[source-events-rock]]); plus the Advanced Edition replacements
  `OVERRIDE_NEUTRAL` and `OVERRIDE_NEUTRAL_EXIT` ([[source-dlceventsoverwrite]]), where it
  is the **first** entry in both filler lists
- `unique="false"` — explicitly, so it can repeat within a sector
  ([[source-events-pirate]]; [[source-fandom-pirate-ship-attacking-civilian]] agrees)
- Drawn with `<img back="BACKGROUND" planet="PLANET_POPULATED"/>`
  ([[source-events-pirate]])
- Long-range scanners show **no** ship
  ([[source-fandom-pirate-ship-attacking-civilian]], `LRSmap=noship`) — the pirate is not
  loaded until you choose to intervene

## Text
Varies — `<text load="PIRATE_CIVILIAN"/>` over a six-entry `textList`
([[source-events-pirate]]). All six, per [[source-text-events-xml]]:

> You arrive in the system to see a pirate ship pursuing a civilian ship. You detect
> messages from the civilian ship on a distress frequency.

> Scanners indicate that a battle is taking place nearby. It seems that someone is under
> attack by space pirates.

> You detect two ships, one chasing the other... Scanners show the pursuer is a pirate!

> There are only two ships within range and they seem to be engaged in battle. One of them
> has the markings of a space pirate.

> You arrive at the next beacon only to be immediately hailed by a small shuttle. "Help
> us! We are being attacked by pirates!"

> You come out of the jump to see laser blasts coming from the other side of the beacon.
> It looks like someone is under attack from pirates.

The first entry is tagged `planet="PLANET_POPULATED_SMALL"` and swaps the background
planet ([[source-events-pirate]]).

> ⚠️ **CONTRADICTION (trivial):** Fandom renders variant 5 as *"only to immediately be
> hailed"*; the game file says *"only to be immediately hailed"*
> ([[source-fandom-pirate-ship-attacking-civilian]] vs [[source-text-events-xml]]).
> Trusting the game files.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Aid the civilian ship. | — | *"You power up your weapons and engage the pirate ship."* → `<ship load="PIRATE_CIVILIAN" hostile="true"/>`. On winning: kill reward **plus** a hidden follow-up choice, "Contact the civilian ship", which rolls `SAVE_CIVILIAN_LIST`. | 100% |
| 2 | Stay out of it. | — | *"The fight brings them out of your immediate scanning range. After a time the distress calls stop."* → nothing happens. | 100% |

### The `PIRATE_CIVILIAN` ship
`<ship name="PIRATE_CIVILIAN" auto_blueprint="SHIPS_PIRATE">` — it has **no `<surrender>`,
no `<escape>` and no `<gotaway>` branch**. Only two endings ([[source-events-ships]]):

| Branch | Result |
|---|---|
| Destroyed | *"The pirate ship breaks apart. You hasten to contact the civilian ship."* → `autoReward level="MED"` `standard`, then the hidden "Contact the civilian ship" choice → `SAVE_CIVILIAN_LIST` |
| Crew killed | *"No more life signs detected on the pirate ship. You hasten to contact the civilian ship."* → `autoReward level="HIGH"` `standard`, then the same follow-up |

Boarding is worth a full reward tier here (`HIGH` vs `MED`) and costs you nothing else,
since the ship cannot flee mid-fight.

### `SAVE_CIVILIAN_LIST` — contacting the civilian
Defined in `raw/gamedata/events_pirate.xml` and **shared with other events across the game**
(e.g. [[event-mantis-ship-attacking-civilian]], and `PIRATE_SURRENDER_CIVILAN` in
`events.xml`). Six entries, all distinct, so under **uniform selection across list
entries** each is **1/6** ([[source-events-pirate]]):

| # | Result | Share |
|---|---|---|
| 1 | *"The ship you saved was badly damaged… One offers to join your crew."* → accept ("Welcome aboard!") → **+1 crew member**; decline → nothing | 1/6 |
| 2 | *"Apparently the ship that was being assaulted was a science vessel…"* → `autoReward level="MED"` `standard` | 1/6 |
| 3 | *"It seems the crew did not survive the assault. You take what you can from the remains."* → `autoReward level="LOW"` `standard` | 1/6 |
| 4 | *"I'm a shipwright and I'd like to help you like you helped me."* → the captain installs equipment → `autoReward level="LOW"` **`weapon`** | 1/6 |
| 5 | *"I think my crew can patch up some of your hull damage as thanks."* → `<damage amount="-5"/>`, i.e. **5 hull repaired** | 1/6 |
| 6 | *"The civilian ship wisely made a fast retreat while you distracted the hostile ship."* → nothing | 1/6 |

Entry 4's only choice is not `hidden`, so the reward is behind an explicit "the captain
offers to install a piece of equipment on your ship" click; entries 2, 3, 5 and 6 resolve
immediately ([[source-events-pirate]]).

## Blue Options
None. Neither choice carries a `req=` attribute.
[[source-fandom-pirate-ship-attacking-civilian]] notes this event is nearly identical to
the distress-beacon version (`PIRATE_CIVILIAN_BEACON`) **but lacks its Improved Weapons
blue option** — confirmed in the files, where `event_PIRATE_CIVILIAN_BEACON_c3_choice`
exists and has no counterpart here ([[source-text-events-xml]]).

## Rewards & Risks
- **Choice 1:** `MED` (destroyed) or `HIGH` (boarded) `standard`, then a 1/6 shot at a
  free crew member, a 1/6 shot at a weapon, a 1/6 shot at 5 hull — and a 2/6 chance of
  nothing extra at all.
- **Choice 2:** free, gains nothing.
- **Risk:** a fully optional fight with **no surrender offer and no escape**. Once you
  commit, one of the two ships is being destroyed. There is no bail-out.

## Strategy Notes
- *(Opinion.)* Good expected value, but not free money — two of the six follow-up entries
  pay nothing. Take it when your weapons are ahead of the sector curve; skip it on a thin
  hull, because there is no surrender branch to end the fight early.
- Kill the crew rather than the hull where you can: it is a whole reward tier better
  (`HIGH` vs `MED`) and there is no escape branch to punish the slower approach.

## Related
- [[event-mantis-ship-attacking-civilian]] — the Mantis version, sharing
  `SAVE_CIVILIAN_LIST`
- [[event-pirate-ship-attacking-civilian-distress]] — the distress-beacon variant, which
  adds an Improved Weapons blue option
- [[event-pirate-briber]] — the other "intervene or don't" pirate beacon
- [[entity-pirates]]
- [[sector-pirate-controlled-sector]], [[sector-civilian-sector]],
  [[sector-rock-controlled-sector]], [[sector-slug-controlled-nebula]]

## Open Questions
- [ ] Weights inside `SAVE_CIVILIAN_LIST` — the file lists six entries with no `prop`, so
      1/6 is derived, not stated.
- [ ] Which species the `SAVE_CIVILIAN_LIST` entry-1 crew member is
      (`<crewMember amount="1"/>` with no `class`).
- [ ] Exact scrap values behind `LOW`/`MED`/`HIGH` `standard`.

## Sources
- [[source-events-pirate]] (per raw/gamedata/events_pirate.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml — `PIRATE_SURRENDER_CIVILAN` also
  loads `SAVE_CIVILIAN_LIST`)
- [[source-newevents]] (per raw/gamedata/newEvents.xml — `NEUTRAL`, `NEUTRAL_CIVILIAN`,
  `NEUTRAL_EXIT`)
- [[source-events-rock]] (per raw/gamedata/events_rock.xml — `NEUTRAL_ROCK`)
- [[source-fandom-pirate-ship-attacking-civilian]] (per raw/wiki/pirate-ship-attacking-civilian.md)
