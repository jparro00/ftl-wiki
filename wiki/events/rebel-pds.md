---
id: event-rebel-pds
type: event
event_name: REBEL_PDS
sectors: []
beacon_type: hostile
hostile: true
blue_options: [hacking]
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 7
tags: [rebel, combat, asb, pds, hazard, blue-option, hacking, unique, no-fandom-page, advanced-edition]
---

# Rebel fight with hostile ASB — `REBEL_PDS`

## Summary
A Rebel forward base opens up on you with an Anti-Ship Battery while a patrol ship closes
in. Unlike the pulsar events, this hazard **can be turned**: the Hacking system lets you
confuse the battery into firing on both ships, or — at Hacking 3 — redirect it onto the
Rebel ship entirely, converting the sector's worst hazard into artillery support. Each
Hacking option costs 1 drone part.

## Trigger & Where It Appears
- Sectors: **not determinable from the files alone.** `REBEL_PDS` belongs to exactly one
  list, `OVERRIDE_HOSTILE2` in `dlcEventsOverwrite.xml` ([[source-dlceventsoverwrite]]),
  which replaces the vanilla `HOSTILE2` list when the DLC is on. `HOSTILE2` is **not
  allocated by any `sectorDescription`** in `sector_data.xml`; its only allocations are the
  depth-based `<eventCounts sector="0">` … `sector="3"` blocks in `newEvents.xml`, at
  `min="3" max="4"`, `2–4`, `4–6` and `4–6` respectively ([[source-newevents]],
  [[source-sector-data-xml]]). That would place it in the first four sectors of a run
  regardless of sector type, but how `eventCounts` composes with per-sector-type allocation
  is not documented in the files. Left `[]` rather than guessed.
- Share: `OVERRIDE_HOSTILE2` has **15** members, none duplicated → **1/15** of any such
  beacon *assuming uniform selection across list entries* ([[source-dlceventsoverwrite]]).
  It is the **first** entry in that list.
- `unique="true"` — at most once per run ([[source-dlcevents]]).
- **No Fandom page** covers this event; everything here is from the game files.

> **AE-only.** Defined in `dlcEvents.xml` and reachable only through an `OVERRIDE_` list
> that takes effect with the DLC on. **Vanilla behaviour is this event not existing** — the
> vanilla `HOSTILE_CIVILIAN`/`HOSTILE1` lists in `newEvents.xml` contain no PDS entry, and
> the ASB hazard and the Hacking system are both Advanced Edition features
> ([[source-dlcevents]], [[source-dlceventsoverwrite]], [[source-newevents]]).

## Text
`[varies: textList REBEL_PDS_TEXT]` — nominally a list, but all **four** entries point at
the same string `text_REBEL_PDS_TEXT_1`, with a `<!-- NEEDS MORE-->` comment marking the
padding. In practice the text never varies ([[source-dlcevents]]):

> You're shocked to discover a Rebel forward base on this planet. A patrol ship moves in to
> intercept and sensors indicate an Anti-Ship Battery is about to fire. We've got to get out
> of here!

(`text_REBEL_PDS_TEXT_1`, per [[source-text-events-xml]])

## Choices & Outcomes

The event body applies `<environment type="PDS" target="player"/>` and loads
`<ship load="REBEL" hostile="true"/>` **before** the choice screen — the battery is already
aimed at you when you pick ([[source-dlcevents]]).

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-------------|------|
| 1 | Prepare to fight. | — | Empty `<event/>` — nothing changes. Fight the `REBEL` ship with the ASB firing **on you**. | 100% |
| 2 | **(Simple Hacking)** Confuse the Anti-Ship Battery's targets. | `req="hacking" lvl="1"` | −1 drone part; `<environment type="PDS" target="all"/>` — the ASB now fires on **both** ships. | 100% |
| 3 | **(Advanced Hacking)** Overwrite the Anti-Ship Battery's target. | `req="hacking" lvl="3"` | −1 drone part; `<environment type="PDS" target="enemy"/>` — the ASB fires on the **Rebel ship only**. | 100% |

Choice 2: *"You spot a weakness in the targeting satellites. Your crew is able to launch a
hacking drone to confuse the Anti-Ship Battery's targeting matrix. It should also fire on
the Rebel ship now."*

Choice 3: *"…launch an improved hacking drone to overwrite the Anti-Ship Battery's targeting
matrix. It will fire on the Rebel ship instead!"* ([[source-text-events-xml]])

### The `REBEL` enemy
`auto_blueprint="SHIPS_REBEL"` ([[source-events-ships]]):

| Outcome | Definition | Payout |
|---|---|---|
| Surrender | `chance="0.5" min="2" max="3"` → `PIRATE_SURRENDER` | standard surrender offer |
| Escape | `chance="0.5" min="3" max="4"` → `PIRATE_ESCAPE` | they jump out; nothing |
| Destroyed | `DESTROYED_DEFAULT` | `MED standard`, always |
| Dead crew | `DEAD_CREW_DEFAULT` (9 entries) | **3/9** `MED standard`; **2/9** `HIGH standard`; **2/9** `HIGH fuel`; **1/9** free crew member + `LOW scrap_only`; **1/9** `LOW weapon` |

Fractions assume uniform selection across list entries ([[source-events-xml]]).

## Blue Options
- **Hacking, level 1** (`req="hacking" lvl="1"`) — costs 1 drone part. Moves the ASB from
  `target="player"` to `target="all"`. This does **not** stop it hitting you; it adds the
  Rebel ship as a target.
- **Hacking, level 3** (`req="hacking" lvl="3"`) — costs 1 drone part. Moves the ASB to
  `target="enemy"`. You stop being shot at entirely and the battery works for you.

Both require the Hacking **system** installed and powered to the stated level; neither
consumes a hacking-drone charge in the files, only one generic drone part
([[source-dlcevents]]).

## Rewards & Risks
- No bonus reward for using either Hacking option — the payoff is purely defensive, plus
  the extra damage the ASB does to the Rebel at Hacking 3.
- Cost: 1 drone part for either option.
- Risk without Hacking: a crewed Rebel warship *and* sustained ASB fire on your hull. The
  ASB ignores shields in the sense that it is an unavoidable periodic hull hit; there is no
  choice to disengage.

## Strategy Notes
- *Opinion, derived from the option table:* Hacking 3 is a huge swing — it removes the
  hazard from you and adds it to the enemy in one move for 1 drone part. Hacking 1 is much
  weaker (`target="all"` still shoots you) and is worth taking mainly if the extra pressure
  on the Rebel will end the fight faster than the incoming hull damage costs you.
- If you carry Hacking but are sitting at level 1–2, powering it to 3 before choosing is
  worth considering — the gate is on system level, not on any augment.
- This is one of only two events in the batch where a blue option changes an *environment*
  rather than granting an item; the other is [[event-rebel-auto-pds]].

## Related
- [[event-rebel-auto-pds]] — the near-identical auto-ship version, which is unreachable in
  the shipped data
- [[event-rebel-fight-near-pulsar]], [[event-pirate-fight-near-pulsar]] — the pulsar-hazard
  fights from the same file, which offer no hazard manipulation
- [[event-fuel-escape-pds]] — the out-of-fuel escape from an ASB beacon
- [[event-lanius-fight-with-friendly-asb-support]] — an ASB already pointed at the enemy
- [[item-hacking]], [[entity-rebels]], [[concept-hazards]], [[concept-blue-options]]
- [[event-pirate-surrender]] — the shared `PIRATE_SURRENDER` aftermath this hull loads
- [[event-pirate-escape]] — the shared `PIRATE_ESCAPE` aftermath this hull loads

## Open Questions
- [ ] Which sectors actually roll `HOSTILE2` beacons — the single most important unknown on
      this page.
- [ ] Whether the `target="all"` mode splits ASB fire evenly or randomly per volley.
- [ ] Whether the Hacking options require an unused hacking drone in inventory beyond the
      1 drone part the file deducts.
- [ ] Why this event has no Fandom page despite being in a live list.

## Sources
- [[source-dlcevents]] (per raw/gamedata/dlcEvents.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml — `DESTROYED_DEFAULT`, `DEAD_CREW_DEFAULT`)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
