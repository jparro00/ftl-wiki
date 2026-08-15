---
id: event-plasma-storm-incapacitated-ships
type: event
event_name: STORM_ITEMS
sectors: [[[sector-civilian-sector]], [[sector-federation-space]], [[sector-pirate-controlled-sector]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]], [[sector-uncharted-nebula]], [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: nebula
hostile: false
blue_options: [[[item-piloting]]]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 7
tags: [plasma-storm, salvage, crew-risk, crew-reward, weapon-reward, drone-reward, hull-damage, blue-option, piloting, unique]
---

# Plasma storm incapacitated ships — `STORM_ITEMS`

## Summary
A ship graveyard in a plasma storm, and the richest loot table in `events_nebula.xml`.
Searching by hand is a five-way roll containing a weapon, a drone schematic, a free crew
member, a **crew death**, and a hull-damage-plus-breach branch that pays the file's only
`HIGH`/`stuff` reward. Piloting level 2 removes the two bad branches outright — one of the
strongest cheap blue options in the game.

## Trigger & Where It Appears
- Beacon: **plasma storm** (`<environment type="storm"/>`). No ship present.
- `unique="true"` — once per run.
- Lists: `NEBULA` ([[source-newevents]]), `NEBULA_PIRATE` ([[source-events-pirate]]) and
  `NEBULA_REBEL` ([[source-events-rebel]]). **`NEBULA_PIRATE` lists it twice**, doubling
  its weight in [[sector-pirate-controlled-sector]].
- Long-range scanners show no ship
  ([[source-fandom-plasma-storm-incapacitated-ships]]).

## Text
> You jump into the middle of a plasma storm. Multiple recently incapacitated ships loom in
> the shadows, briefly illuminated by the lightning.

(`event_STORM_ITEMS_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Manually search the wreckage for survivors and equipment. | none (`hidden="true"`) | `STORM_ITEMS_LIST` — five entries, table below. | unknown (5-entry list) |
| 2 | Avoid the risk and wait to jump away unscathed. | — | Empty `<event/>` — nothing happens. | 100% |
| 3 | **(Piloting)** Have your pilot carefully explore the debris. | `req="pilot" lvl="2"`, `hidden="true"` | `STORM_ITEMS_PILOTING` — four entries, table below. | unknown (4-entry list) |

### Choice 1 — `STORM_ITEMS_LIST`

| Entry | Text | Effect |
|---|---|---|
| 1 | *"Despite your caution, the lack of detection equipment allows debris to crash into your ship, damaging the hull…"* | `<damage amount="4"/>` **plus** `<damage amount="0" system="random" effect="breach"/>` (AE), **plus** `autoReward level="HIGH">stuff`. |
| 2 | *"…you find an unconscious passenger, and take them back to the ship. Once awake they offer to join your crew in thanks."* | **+1 crew** and `autoReward level="LOW">standard`. |
| 3 | *"…two hulls crash into each other breaking the crew's tethers. You have no time to react as someone is knocked away…"* | **`<removeCrew>` — you lose a crew member.** Has a `<clone>true</clone>` flag: with a Clone Bay, *"Fortunately, your crewmember was close enough to the ship for the Clone Bay to revive them."* Plus `autoReward level="LOW">standard`. |
| 4 | *"Among the junk and scrap you find a salvageable drone schematic."* | `autoReward level="MED">drone`. |
| 5 | *"Most of the debris is hardly even usable as scrap. However, you eventually find an intact weapon…"* | `autoReward level="MED">weapon`. |

Entry 1's second `<damage>` element is `amount="0"` with `effect="breach"` — it opens a
breach without dealing further hull damage.
[[source-fandom-plasma-storm-incapacitated-ships]] adds the reassurance the XML implies but
does not state: *"The outcome with hull damage and breach does not destroy any system. (it
is safe for crew being cloned)"*. It also expands the `HIGH`/`stuff` payload as
*"fuel: 3-6 ; missiles: 4-8 ; drone parts: 1-2"* — numbers the game files do not contain.

### Choice 3 — `STORM_ITEMS_PILOTING`

| Entry | Text | Effect |
|---|---|---|
| 1 | Same survivor text as list entry 2 (*"…take him back to the ship"*) | **+1 crew** and `autoReward level="LOW">standard`. |
| 2 | Same drone-schematic text | `autoReward level="MED">drone`. |
| 3 | Same intact-weapon text | `autoReward level="LOW">weapon` — **`LOW`, not `MED`**. |
| 4 | *"Your pilot carefully explores the wrecks, but the storm has taken its toll. Any crew are long-since dead and the floating debris has been scorched beyond repair."* | Nothing. |

## Blue Options
- **[[item-piloting]] level 2** (`req="pilot" lvl="2"`) — a cheap system upgrade that
  **removes both bad outcomes**: no hull damage, no breach, and no crew loss. What it costs
  you is the `HIGH`/`stuff` jackpot and a downgrade of the weapon reward from `MED` to
  `LOW`, plus a 1-in-4 chance of nothing at all.

  The trade is explicit in the data: manual searching has a higher ceiling and a real
  floor; piloting has a lower ceiling and no floor below zero. There is no source stating
  which is better.

## Rewards & Risks
- Ceiling: `HIGH`/`stuff` (choice 1, entry 1) — but bundled with 4 hull damage and a
  breach.
- Two free-crew branches, one on each side.
- **Crew-loss risk** on choice 1 only, mitigated by a Clone Bay.
- Choice 2 is a guaranteed zero, always available.
- Fandom tags it `Hull damage risk`, `Hull breach risk`, `Crew loss risk`,
  `Clone Bay revival`, `Crew reward chance`, `Weapon reward chance`,
  `Events with Stuff rewards` ([[source-fandom-plasma-storm-incapacitated-ships]]).

## Strategy Notes
- With Piloting 2 and no Clone Bay, choice 3 is the clear pick — you cannot lose a crew
  member and cannot take hull damage.
- With a **Clone Bay**, the crew-loss branch of choice 1 is neutralised, which materially
  improves manual searching: three of five entries become straightforwardly good, one is
  neutral-after-cloning, and only the hull-damage entry still costs you anything — and it
  pays the biggest reward in the file. *(Opinion, derived from the tables; no source
  recommends a line.)*
- The weapon downgrade on the piloting branch (`LOW` vs `MED`) is easy to miss and is the
  reason a heavily-armed ship might still search by hand.

## Related
- [[event-boarders-humans-in-plasma-storm]] — the other salvage-gone-wrong storm event
- [[event-nebula-lost-ship]] — the nebula file's other crew source
- [[item-piloting]], [[item-clone-bay]], [[concept-crew-loss-risk]],
  [[sector-uncharted-nebula]]

## Open Questions
- [ ] Weights inside `STORM_ITEMS_LIST` (5 entries) and `STORM_ITEMS_PILOTING` (4 entries)
      — none stated.
- [ ] Numeric values behind `HIGH`/`stuff`; Fandom's 3-6 fuel / 4-8 missiles / 1-2 drone
      parts is not in the game files.
- [ ] Whether `req="pilot"` refers to the Piloting system level or a crew member's piloting
      skill (the XML says only `pilot`, `lvl="2"`).

## Sources
- [[source-events-nebula]] (per raw/gamedata/events_nebula.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-plasma-storm-incapacitated-ships]] (per raw/wiki/plasma-storm-incapacitated-ships.md)
