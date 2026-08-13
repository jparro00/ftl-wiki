---
id: event-destroyed-cargo-ship
type: event
event_name: FLOATING_CARGO
sectors: [[[sector-pirate-controlled-sector]]]
beacon_type: any
hostile: false
blue_options: [sensors lvl 2, long-ranged scanners augment]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 9
tags: [pirate, boarding-risk, blue-option, trap, unique]
---

# Destroyed cargo ship — `FLOATING_CARGO`

## Summary
Free-floating cargo from a wrecked freighter. Taking it aboard is a coin-flip: half the
pool is scrap, half is a pirate ambush that beams 2–4 human boarders onto your ship — and
one of those two also brings a warship. Level-2 Sensors or the Long-Ranged Scanners
augment replaces the whole gamble with a scan that is never worse than neutral and lets
you see the ambush coming.

## Trigger & Where It Appears
- Sector: [[sector-pirate-controlled-sector]]
- Event lists: `BOARDERS_PIRATE` ([[source-events-pirate]]) and `HOSTILE_BOARDING`
  ([[source-newevents]]). Pirate sectors allocate `BOARDERS_PIRATE` at `min=1 max=1` — one
  boarding beacon is guaranteed per Pirate sector, and this is one of five events that can
  fill it ([[source-sector-data-xml]]).
- **`HOSTILE_BOARDING` is effectively dead in `sector_data.xml`**: it is allocated
  `min="0" max="0"` in `STANDARD_SPACE` ([[sector-federation-space]]) and commented out in
  `CIVILIAN_SECTOR` ([[source-sector-data-xml]]). So in practice this event reaches you
  through the Pirate sector's list, which is why
  [[source-fandom-destroyed-cargo-ship]] lists **Pirate Controlled Sector only**.
- `unique="true"` — once per run ([[source-events-pirate]]; Fandom agrees)
- Long-range scanners show no ship ([[source-fandom-destroyed-cargo-ship]],
  `LRSmap=noship`)

## Text
> Not too far from the beacon, you detect a destroyed cargo ship with its cargo scattered
> nearby, intact.

(`event_FLOATING_CARGO_text`, per [[source-text-events-xml]])

## Choices & Outcomes

All four choices are `hidden="true"` — their outcome text is not previewed
([[source-events-pirate]]).

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Bring it aboard. | — | Rolls `FLOATING_CARGO_LIST` — 4 entries, half reward and half ambush (below). | see below |
| 2 | Leave it alone, this looks suspicious. | — | *"You leave the cargo alone and prepare to jump."* → nothing happens. | 100% |
| 3 | **(Advanced Sensors)** Run an advanced scan on the boxes. | `req="sensors" lvl="2"` | Rolls `FLOATING_CARGO_SCAN_LIST` (below). | see below |
| 4 | **(Long-Ranged Scanners)** Run an advanced scan on the boxes. | `req="ADV_SCANNERS"` (augment) | Rolls the **same** `FLOATING_CARGO_SCAN_LIST`. | see below |

### Choice 1 — `FLOATING_CARGO_LIST`
Four distinct entries, so under **uniform selection across list entries** each is **1/4**
— derived from list membership, not stated as a percentage anywhere
([[source-events-pirate]]):

| # | Result | Share |
|---|---|---|
| 1 | *"They appear to be filled with military supplies! You take everything you can use and jettison the rest."* → `autoReward level="MED"` `standard` | 1/4 |
| 2 | *"The cargo was primarily consumer goods and clothing… You manage to collect some scrap."* → `autoReward level="LOW"` `scrap_only` | 1/4 |
| 3 | *"…a pirate bursts out of one of the crates… your ship is filled with the sound of crates breaking open…"* → `<boarders min="2" max="4" class="human"/>` — **2–4 human boarders**, no ship | 1/4 |
| 4 | *"…a pirate ship appears out of hiding and charges. At the same time, the crates fly open."* → **2–4 human boarders** *and* `<ship load="JELLY_PIRATE_WITHBOARDERS" hostile="true"/>` | 1/4 |

So choice 1 is a 50/50 between a payout and being boarded, with a 1/4 chance of being
boarded *and* shot at simultaneously.

### Choices 3 and 4 — `FLOATING_CARGO_SCAN_LIST`
Three distinct entries, **1/3** each under the same assumption ([[source-events-pirate]]):

| # | Result | Share |
|---|---|---|
| 1 | *"The cargo appears to contain nothing of much interest. You salvage some scrap from the destroyed ship."* → `<item type="scrap" min="20" max="35"/>` — **+20–35 scrap** (an explicit value, not an `autoReward` band) | 1/3 |
| 2 | *"Your Advanced Sensors are able to breach the protective barrier… filled with military supplies!"* → `autoReward level="MED"` `standard` | 1/3 |
| 3 | *"Your advanced sensors pick up faint life signatures inside the cargo… This looks like a planned pirate ambush."* → your choice: **Destroy the crates** (hidden) → *"You fire on the crates… A pirate ship appears out of nowhere with a message, 'You will pay for that!'"* → fight `<ship load="PIRATE" hostile="true"/>`; or **Leave it alone and prepare to jump** → nothing | 1/3 |

The scan never boards you. Worst case it shows you the ambush and lets you walk away.

### The ambush ship — `JELLY_PIRATE_WITHBOARDERS`
`<ship name="JELLY_PIRATE_WITHBOARDERS" auto_blueprint="SHIPS_PIRATE">`
([[source-events-ships]]):

| Branch | Trigger in the file | Result |
|---|---|---|
| Surrender | `min="0" max="5"` — **no `chance` attribute at all** → loads `PIRATE_SURRENDER` | Accept: ship non-hostile, `autoReward level="RANDOM"` `stuff`. Refuse: fight continues. |
| Escape | `chance="0.3" min="2" max="4" timer="15"` → loads `PIRATE_ESCAPE` | 15-second FTL countdown at 2–4 hull |
| Got away | — | *"The pirate jumped away in search of weaker targets."* |
| Destroyed | loads `DESTROYED_DEFAULT` | `autoReward level="MED"` `standard` |
| Crew killed | loads `DEAD_CREW_DEFAULT` | The 9-entry default table — see [[event-pirate-fight]] |

Choice-list entry 3 of the scan list loads the ordinary `<ship name="PIRATE">` instead;
its profile is on [[event-pirate-fight]].

> ⚠️ **CONTRADICTION:** [[source-fandom-destroyed-cargo-ship]] describes
> `JELLY_PIRATE_WITHBOARDERS` as *"70% chance for escape attempt at 20-40% hull with 15
> seconds countdown timer and makes a surrender offer at 0-50% hull."* The game file says
> `chance="0.3"` on the escape ([[source-events-ships]]). Fandom is reporting `1 − chance`
> — the same inversion it applies on [[event-pirate-briber]] — which implies the attribute
> is the chance the ship *keeps fighting*. The raw value (`0.3`) is a game-file fact
> (`high`); the semantics are Fandom's reading (`medium`). Both recorded, unresolved. The
> "0-50% hull" surrender figure corresponds to the file's `min="0" max="5"` **hull points**,
> not percentages.

## Blue Options
- **Sensors, level 2** (`req="sensors" lvl="2"`) — the subsystem.
- **[[item-long-ranged-scanners]]** (`req="ADV_SCANNERS"`) — the augment, blueprint title
  *"Long-Ranged Scanners"* ([[source-blueprints]], [[source-text-blueprints]]).

Both load the identical `FLOATING_CARGO_SCAN_LIST`, so having one makes the other
redundant here. Either turns a 50% boarding risk into a 0% boarding risk, and the ambush
entry becomes an *optional* fight you can decline. This is one of the clearest cases in
the game of a blue option removing risk rather than adding reward.

## Rewards & Risks
- **Best case:** `MED` `standard` (choice 1 or 3/4), or a flat 20–35 scrap from the scan.
- **Worst case (choice 1):** 2–4 human boarders inside your ship *and* a hostile warship
  outside it, at a beacon you visited for free loot.
- The scan path has **no downside at all** — its floor is +20–35 scrap and its ambush
  entry can be declined.

## Strategy Notes
- *(Opinion.)* Without Sensors 2 or the augment, this is a genuine gamble: 50% boarders.
  With a crew that fights well (Mantis, Rockmen) and a Medbay, boarders are manageable and
  the 1/4 warship entry pays default rewards on top. With a small or fragile crew, choice
  2 is defensible.
- With the scan available, always scan — there is no scenario where scanning is worse.
- Entry 3 of the scan list is the only place the event lets you *choose* a pirate fight;
  declining costs nothing.

## Related
- [[event-pirate-fight]] — the ship loaded by the scan-list ambush; full default-reward
  tables
- [[event-boarders-humans-near-sun]], [[event-boarders-asteroid]] — the other human-boarder
  events in `BOARDERS_PIRATE` / `HOSTILE_BOARDING`
- [[item-long-ranged-scanners]] — the augment that gates choice 4
- [[entity-pirates]]
- [[sector-pirate-controlled-sector]]
- [[event-pirate-surrender]] — the shared `PIRATE_SURRENDER` aftermath this hull loads
- [[event-pirate-escape]] — the shared `PIRATE_ESCAPE` aftermath this hull loads

## Open Questions
- [ ] What the missing `chance` attribute on `JELLY_PIRATE_WITHBOARDERS`'s `<surrender>`
      means — always offers, or engine default?
- [ ] Exact scrap values behind `LOW`/`MED`/`RANDOM` `autoReward` levels.
- [ ] Whether the boarders' species is always human — `class="human"` is fixed in all
      three boarding entries here.

## Sources
- [[source-events-pirate]] (per raw/gamedata/events_pirate.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-events-xml]] (per raw/gamedata/events.xml — `PIRATE_SURRENDER`,
  `PIRATE_ESCAPE`, `DESTROYED_DEFAULT`, `DEAD_CREW_DEFAULT`)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml — the `HOSTILE_BOARDING` list)
- [[source-blueprints]] / [[source-text-blueprints]] (per raw/gamedata/blueprints.xml,
  raw/gamedata/text_blueprints.xml — the `ADV_SCANNERS` augment title)
- [[source-fandom-destroyed-cargo-ship]] (per raw/wiki/destroyed-cargo-ship.md)
