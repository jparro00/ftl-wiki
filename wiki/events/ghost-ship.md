---
id: event-ghost-ship
type: event
event_name: GHOST_SHIP
sectors: [[[sector-federation-space]]]
beacon_type: unknown
hostile: false
blue_options: [[[item-sensors]]]
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [unreachable, cut-content, unique, blue-option, crew-risk, boarders, weapon-reward]
---

# Ghost ship — `GHOST_SHIP`

## Summary
A fully authored multi-branch salvage encounter — a derelict with no life signs, a deep
tree of boarding outcomes, a Sensors blue option, a unique `ghost` boarder class, and a
high-tier weapon reward — that **cannot occur in the extracted 1.6.x build**. Its only
list membership is `HOSTILE_BOARDING`, and `sector_data.xml` allocates that list zero
beacons everywhere it is mentioned. Documented here as shipped-but-unreachable content,
not as something you will meet in a run.

## Trigger & Where It Appears
- Defined in `events.xml` as `<event name="GHOST_SHIP" unique="true">`
  ([[source-events-xml]]).
- **Only reference:** `<event load="GHOST_SHIP"/>` inside `<eventList name="HOSTILE_BOARDING">`
  ([[source-newevents]]).
- `HOSTILE_BOARDING` appears exactly twice in `sector_data.xml` ([[source-sector-data-xml]]):
  - `STANDARD_SPACE` ([[sector-federation-space]]) — `<event name="HOSTILE_BOARDING" min="0" max="0"/>`
  - `CIVILIAN_SECTOR` ([[sector-civilian-sector]]) — the line is **commented out**:
    `<!-- <event name="HOSTILE_BOARDING" min="0" max="1"/> -->`
- No other file references `HOSTILE_BOARDING`, and `dlcEventsOverwrite.xml` does not
  redefine it or add it to any `OVERRIDE_*` list ([[source-dlceventsoverwrite]]).
- **Therefore: unreachable.** A zero/zero allocation places no beacons, and the one sector
  that would have placed 0–1 has the line disabled. The commented-out line is a dev note
  that the content was pulled rather than never wired up.
- Arrives **non-hostile**: `<ship load="GHOST_SHIP" hostile="FALSE"/>`. The ship uses
  `auto_blueprint="JELLY_TRUFFLE"` and is crewed entirely by the `ghost` class
  (`<crewMember class="ghost" prop="2"/>`) ([[source-events-ships]]). Its `deadCrew` text
  is the placeholder *"Should not be seen"* — ghosts cannot be killed conventionally.

## Text
The intro prose **varies**: `<text load="GHOST_SHIP_TEXT"/>` draws from a 4-entry
`textList` ([[source-events-xml]], [[source-text-events-xml]]). All four describe a
heavily damaged, ancient or abandoned vessel with no life-signs — e.g.

> This beacon lies in an empty section of space. You almost move on before spotting a
> heavily damaged ship drifting nearby. The ship's markings are unfamiliar.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | This is a great opportunity. Let's dock and see if we can find valuable supplies. | — | Loads `eventList GHOST_DOCK` — 2 entries, see below. | see below |
| 2 | We're in a hurry, let's just quickly pull some scrap off the ship. | — | `GHOST_SCRAP`: *"You recover what you can before making preparations to jump away."* → `autoReward level="LOW"` `scrap_only`, then continue into `GHOST_SPACE`. | 100% |
| 3 | Something seems wrong here. Let's just leave. | — | Nothing happens. | 100% |

All three choices are `hidden="true"` — outcomes are not previewed ([[source-events-xml]]).

### Choice 1 — `eventList GHOST_DOCK` (2 entries)
Assuming uniform selection across `eventList` entries ([[concept-event-list-weighting]]),
each entry is **1/2**:

| Entry | What happens |
|---|---|
| 1 | *"Your crew complains of hearing strange voices as they work. One requests that they end the salvage operation early."* → a three-way choice, below. |
| 2 | Goes straight to `GHOST_BOARDING`. |

Entry 1's choices:

| # | Choice | Requirement | Outcome |
|---|--------|-------------|---------|
| 1a | They're being ridiculous. Finish the job. | — | → `GHOST_BOARDING` |
| 1b | They've gathered enough supplies. Let's get going. | — | → `GHOST_SCRAP` (LOW `scrap_only`, then `GHOST_SPACE`) |
| 1c | **(Sensors)** Wait, sensors are picking up something strange… | `req="sensors" lvl="3"` | *"…it's as if the ship is slowly activating. You pull everyone back to your ship with what they have gathered."* → `autoReward level="MED"` `scrap_only`, then `GHOST_SPACE`. |

### `eventList GHOST_BOARDING` (2 entries — 1/2 each under uniform selection)

| Entry | What happens |
|---|---|
| 1 | *"The salvage operation ends without a hitch."* → `autoReward level="HIGH"` **`weapon`** |
| 2 | Ghosts attack the boarding party. Choice: **retreat** → `autoReward level="MED"` `scrap_only` then `GHOST_SPACE`; or **stand their ground** → `GHOST_STAND`. |

### `eventList GHOST_STAND` (3 entries — 1/3 each under uniform selection)

| Entry | What happens |
|---|---|
| 1 | *"The fight doesn't go well… your crew is forced to abandon the supplies and retreat."* → `GHOST_BOARDED` |
| 2 | *"The ghosts prove to be even weaker than you'd expected."* → `autoReward level="HIGH"` `standard`, then `GHOST_SPACE` |
| 3 | *"Your crew is losing the fight…"* → choice: **full retreat** → `GHOST_BOARDED`; or **protect the ship first** → `<removeCrew><clone>true</clone></removeCrew>` — you lose a crew member, and the clone text (*"You get back to find your crew-member cloned…"*) fires if a [[item-clone-bay]] can recover them. |

### `GHOST_BOARDED`
> The ghosts follow your crew-members back on board the ship!

`<boarders min="2" max="4" class="ghost"/>` — 2–4 ghost boarders on **your** ship
([[source-events-xml]]).

### `eventList GHOST_SPACE` (2 entries — 1/2 each under uniform selection)
The exit path from most branches:

| Entry | What happens |
|---|---|
| 1 | *"Suddenly the wreckage powers up… it has clearly become hostile."* → `<ship hostile="true"/>` — the `GHOST_SHIP` turns on you. |
| 2 | *"You got what you came for. Now leave us!"* → choice: leave (nothing), or *"This ship could be dangerous to future travelers. We should destroy it."* → fight. |

Destroying the ship: *"The haunted ship is destroyed. It won't be able to trouble future
travelers."* → `autoReward level="HIGH"` `standard` ([[source-events-ships]]).

## Blue Options
- **Sensors, level 3** (`req="sensors" lvl="3"`) — only on the `GHOST_DOCK` entry-1 branch.
  It converts the ambiguous "keep going or bail" decision into a clean exit with
  `MED scrap_only`, skipping `GHOST_BOARDING` and its crew-loss tree entirely. Note the
  gate is the **system level**, not merely owning Sensors ([[source-events-xml]]).

## Rewards & Risks
- Best case: `HIGH weapon` from `GHOST_BOARDING` entry 1, or `HIGH standard` from
  `GHOST_STAND` entry 2 / destroying the ship.
- Worst case: lose a crew member (`GHOST_STAND` entry 3), and/or 2–4 `ghost` boarders on
  your ship from `GHOST_BOARDED`, and/or a fight with a `JELLY_TRUFFLE`-hulled ship whose
  crew cannot be killed off (`deadCrew` is a placeholder string).
- The bail-out choices (2 and 3) cost nothing but `LOW scrap_only` or nothing at all.

## Strategy Notes
None applicable — the event cannot be reached in this build. If a mod re-enables
`HOSTILE_BOARDING`, the shape of the tree is: choice 2 is a small guaranteed payout,
choice 1 is a gamble whose good half is a free weapon and whose bad half is ghost boarders.
*(Opinion, read off the outcome table above; no source states it.)*

## Related
- [[event-research-station-with-no-response]], [[event-boarders-humans-pirate]], [[event-boarders-asteroid]], [[event-boarders-humans-jammed-sensors]] — the other `HOSTILE_BOARDING` members, equally affected by the zero allocation
- [[item-sensors]] — the gating system
- [[sector-federation-space]] — the sector whose description mentions the list
- [[item-clone-bay]] — determines whether the crew loss is permanent

## Open Questions
- [ ] Was `HOSTILE_BOARDING` live in pre-AE 1.0? Only the AE build was extracted here, so
      the vanilla `sector_data.xml` allocation is unverified.
- [ ] Does the `ghost` crew class have a blueprint entry, and what are its stats?
- [ ] Confirm `eventList` selection is uniform — every fraction above depends on it.

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
