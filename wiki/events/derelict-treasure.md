---
id: event-derelict-treasure
type: event
event_name: DERELICT_TREASURE
sectors: []
beacon_type: unknown
hostile: false
blue_options: [engi crew]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [unreachable, orphan, blue-option, weapon-reward, scrap-reward, hull-damage-risk, fleet-advance-risk, unique, ae-difference]
---

# Derelict treasure — `DERELICT_TREASURE`

## Summary
A three-variant salvage beacon with a real risk/reward split and a strong Engi blue option:
salvage blind for a 1/3 shot at 50–60 scrap and a free weapon (with a 1/3 chance of hull
damage and a 1/3 chance of advancing the Rebel fleet), or let an Engi scan first and take the
same jackpot at 2/3 with **no risk at all**. It is **not reachable in normal play** — no
event list in the extracted game data loads it — and it is the largest complete-but-unlisted
event in `nameEvents.xml`.

## Trigger & Where It Appears
- **Orphan / unreachable.** `DERELICT_TREASURE` appears in `raw/gamedata/` only inside
  `nameEvents.xml`: its own `<event>`, the `<textList>` of the same name that it loads, and
  the two sub-lists it references. A search of every `.xml` finds **no `<eventList>` entry,
  no `load=`, and no `sector_data.xml` allocation** ([[source-nameevents]]).
- It shares this fate with the rest of the file's finished content —
  [[event-free-augment]], [[event-lone-shuttle]] and [[event-engi-refugees]] are all
  unreferenced in the same way. `nameEvents.xml` reads as a scratch file for exercising the
  `%crew` name-substitution machinery that was never wired into the sector pools.
- This is the positive evidence [[concept-sector-event-allocation]] requires: no reference of
  any kind, not merely a missing sector allocation.
- Not a stub: three flavour variants, three choices, two three-entry outcome lists, a blue
  option, and both a weapon and a scrap payout.
- `unique="true"`. No ship is staged, so the beacon would start non-hostile.
- Sectors, beacon type and long-range-scanner appearance: **unknown**.
- No Fandom page exists for it, consistent with it never firing in play.
- **Version:** `both`, with an AE difference — see below.

## Text
`<text load="DERELICT_TREASURE"/>` — three distinct strings, no repeats, so **1/3 each**
assuming uniform selection across list entries ([[concept-event-list-weighting]],
[[source-nameevents]]). Unusually for this file, the strings are written inline rather than
as `text_events.xml` ids:

> You stumble upon the remnents of a recent battle. One ship nearby looks like it could still
> have some valuable resources.

> A derelict Selz class freighter is floating near this beacon. It could contain something
> valuable.

> A massive space station is orbitting a nearby moon. Initial scans show it to be empty and
> abandoned.

(The typos — *remnents*, *orbitting* — are in the game data.)

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Attempt to salvage what you can from the debris. | — (`hidden="true"`) | Loads `DERELICT_TREASURE_REWARD` — three entries, 1/3 each. | — |
| 2 | **(Engi)** *"%req isn't convinced that it's safe. %req_He asks you to give %req_him some time to run some more scans."* | `req="engi" lvl="1"`, `hidden="true"` | Loads `DERELICT_ENGI` — three entries, 1/3 each. | — |
| 3 | Who knows what dangers that wreckage could hold? You don't need the supplies anyway. Continue on your way. | — | Empty `<event/>` — nothing happens. | 100% |

### `DERELICT_TREASURE_REWARD` — the blind salvage (1/3 each)

| Odds | Text | Effect |
|---|---|---|
| 1/3 | *"An explosion rocks your ship, it seems the wreckage was rigged to explode. You don't know why anyone would do something so malicious..."* | **5 hull damage**, plus — AE only — `<damage amount="1" system="room" effect="breach"/>`, a hull breach in a random room |
| 1/3 | *"When you get close enough to start scrapping the wreckage, your systems detect a transmission going out. It seems the Rebels rigged it to warn them of your arrival."* | `<modifyPursuit amount="1"/>` — the Rebel fleet gains a step |
| 1/3 | *"You discover the wreckage has tons use-able scrap and even some weaponry!"* | **+50 to 60 scrap** and `<weapon name="RANDOM"/>` |

### `DERELICT_ENGI` — the blue-option scan (1/3 each)

| Odds | Text | Effect |
|---|---|---|
| 1/3 | *"%req discovers that the ship is rigged to explode if you get too near. Better that you avoid the wreckage and continue on your way."* | Nothing — the trap is avoided, not triggered |
| 1/3 | *"%req finds a hidden rebel transmitter on the wreckage! %req_He's able to disable it remotely and leaves you to scrap the ship for valuable supplies."* | **+50 to 60 scrap** and `<weapon name="RANDOM"/>` |
| 1/3 | *"%req discovers nothing extraordinary about this specific wreckage. You go about salvaging what you can."* | **+50 to 60 scrap** and `<weapon name="RANDOM"/>` |

The two lists are the same three scenarios with the Engi neutralising both hazards: the bomb
becomes "walk away", the transmitter becomes "disabled, and here's the loot". Blind salvage
pays the jackpot **1/3** of the time; the Engi path pays it **2/3** of the time and never
costs anything.

## Blue Options
- **Engi crew member** (`req="engi" lvl="1"`) — converts a genuine gamble into a strictly
  dominant option. It doubles the jackpot rate, removes 5 hull damage (and, in AE, a breach)
  from the outcome space, and removes the Rebel-fleet advance entirely. One of the cleanest
  blue options in the extracted data.

## Rewards & Risks
- **Best case:** 50–60 scrap plus a random weapon — a large payout for a no-combat beacon.
- **Risks (blind path only):** 5 hull damage plus an AE hull breach, or `modifyPursuit +1`.
- **Engi path:** no downside case exists. The worst outcome is nothing.

> **Version difference.** The breach on the explosion outcome is `<!--DLC-->`-marked, so in
> **vanilla** that branch does 5 hull damage only; in **Advanced Edition** it also opens a
> breach in a random room ([[source-nameevents]]). Everything else is identical between
> editions — and the event is equally unreachable in both.

## Strategy Notes
None — the event cannot occur. Had it shipped in a list, the correct play would be trivial:
Engi if you have one, otherwise weigh 50–60 scrap and a weapon against a 2/3 chance of hull
damage or a fleet step.

## Related
- [[event-free-augment]], [[event-lone-shuttle]], [[event-engi-refugees]] — the other
  complete-but-unlisted events in the same file
- [[entity-engi]] — the species gating the blue option
- [[concept-sector-event-allocation]] — the evidence bar for calling something unreachable
- [[concept-event-list-weighting]] — basis for the 1/3 and 2/3 figures

## Open Questions
- [ ] Was `nameEvents.xml` ever loaded by a shipped build, or is the whole file dead?
- [ ] Which weapon pool `<weapon name="RANDOM"/>` draws from here.
- [ ] Whether the three flavour texts were meant to gate different sub-lists — the freighter,
      the station and the battle debris all resolve identically.

## Sources
- [[source-nameevents]] (per raw/gamedata/nameEvents.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
