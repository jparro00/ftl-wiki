---
id: event-trade-scrap-for-upgrades
type: event
event_name: TRADER_UPGRADES
sectors: [[[sector-civilian-sector]], [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-federation-space]], [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]], [[sector-pirate-controlled-sector]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]], [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]], [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]], [[sector-uncharted-nebula]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [trading, system-upgrade, reactor, scrap-cost, unique, advanced-edition, items-pool]
---

# Trade scrap for upgrades — `TRADER_UPGRADES`

## Summary
A mobile shipwright who will sell you exactly one (sub)system upgrade for scrap. Which
one is offered is rolled before you see it — Oxygen, Piloting, Doors, Sensors or the
reactor, one fifth each — and the price depends on the current level of the thing being
upgraded. There is no risk at all: nothing here can fight you, cost you fuel, or cost
scrap you did not agree to.

## Trigger & Where It Appears
- Event lists: `ITEMS` and `NEUTRAL_EXIT` in `newEvents.xml`, both tagged
  `<!--DLC - down below-->` ([[source-newevents]]), and their Advanced Edition
  replacements `OVERRIDE_ITEMS` and `OVERRIDE_NEUTRAL_EXIT`
  ([[source-dlceventsoverwrite]]).
- `ITEMS` is allocated by 14 sector definitions ([[source-sector-data-xml]]), which is
  where the sector list above comes from.
- `NEUTRAL_EXIT` has **no `sector_data.xml` allocation of its own** — it is one of the
  lists the engine calls by name to fill exit beacons (`EXIT_LIST` = `NEUTRAL_EXIT` +
  `ITEMS`), so this event can also appear at an exit beacon in any sector. That absence of
  an allocation is *not* evidence of unreachability; see
  [[concept-sector-event-allocation]]. Fandom independently records `alsooccur=exit`
  ([[source-fandom-trade-scrap-for-upgrades]]).
- `unique="true"` — at most once per run.
- Beacon: ordinary, no ship on Long-Ranged Scanners.

### Odds of drawing it
Its two pools are `ITEMS` (13 distinct members in the base file, 14 in `OVERRIDE_ITEMS`)
and `NEUTRAL_EXIT` (17 base / 18 override), none duplicated. **Assuming uniform selection
across list entries** ([[concept-event-list-weighting]]), an `ITEMS` beacon is this event
with probability **1/13** (base) or **1/14** (AE).

## Text
`[varies: textList TRADER_UPGRADES_TEXT]` — four entries, no repeats
([[source-newevents]], [[source-text-events-xml]]):

1. *You are immediately hailed by a mobile docking platform upon arrival, "Welcome to Uncle Joe's Fix-it Shop! Need a tuneup? We got you covered!"*
2. *There are a number of privately owned ship construction platforms in the area. You find one that has a slot open for some immediate work.*
3. *You pick up an automated message from a nearby space station. There appears to be a local shipwright that can perform emergency work on military ships.*
4. *You receive a message from a small refugee convoy, "Hail. We'd like to help you on your mission but don't have much to offer. If you have extra metal perhaps we could work on your ship?"*

> ⚠️ **CONTRADICTION (wording, minor):** Fandom writes *"Need a tune-up?"* with a hyphen;
> the game string is *"Need a tuneup?"* ([[source-fandom-trade-scrap-for-upgrades]] vs
> [[source-text-events-xml]]). Trusting the game files.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Inquire about their specialty. | — (`hidden="true"`) | Loads `TRADER_UPGRADES_LIST` — one of five offers, below. | 100% |
| 2 | Decline. | — | *"You thank them for their offer but prepare to move on."* → nothing. | 100% |

### `TRADER_UPGRADES_LIST` — five entries, no repeats (1/5 each)
**Assuming uniform selection across list entries** ([[concept-event-list-weighting]]):

| Odds | Offer text | What it upgrades |
|---|---|---|
| 1/5 | *They offer to upgrade your Oxygen system in exchange for some scrap.* | Oxygen |
| 1/5 | *They offer to upgrade your Piloting subsystem in exchange for some scrap.* | Piloting |
| 1/5 | *They offer to upgrade your Door subsystem in exchange for some scrap.* | Doors |
| 1/5 | *They offer to upgrade your Sensors subsystem in exchange for some scrap.* | Sensors |
| 1/5 | *They offer to upgrade your reactor in exchange for some scrap.* | Reactor |

Each offer presents the same two choices — "Agree to the exchange." (result text: *"You
let their team on board and after a short time they finish their work."*) and a hidden
"Decline." (*"You thank them but prepare to move on."*).

### Prices — the gate is your current level

The "agree" choices are `req`-gated on the system itself with `max_lvl`, so **only the
one matching your current level is shown**, and none is shown if the system is already
maxed or not installed ([[source-newevents]]):

| Offer | `req` / `max_lvl` | Scrap cost | Result |
|---|---|---|---|
| Oxygen | `oxygen`, `max_lvl="1"` | −15 to −20 | Oxygen → level 2 |
| Oxygen | `oxygen`, `max_lvl="2"` | −25 to −40 | Oxygen → level 3 |
| Piloting | `pilot`, `max_lvl="1"` | −8 to −15 | Piloting → level 2 |
| Piloting | `pilot`, `max_lvl="2"` | −25 to −40 | Piloting → level 3 |
| Doors | `doors`, `max_lvl="1"` | −8 to −15 | Doors → level 2 |
| Doors | `doors`, `max_lvl="2"` | −25 to −40 | Doors → level 3 |
| Sensors | `sensors`, `max_lvl="1"` | −10 to −20 | Sensors → level 2 |
| Sensors | `sensors`, `max_lvl="2"` | −35 to −45 | Sensors → level 3 |
| Reactor | `reactor`, `max_lvl="24"` | −15 to −25 | Reactor +1 bar |

Fandom's figures match the file exactly, and it adds three limits the data implies:
you cannot upgrade past a (sub)system's maximum, cannot upgrade a subsystem you do not
have installed, and cannot take the reactor past 25 power bars
([[source-fandom-trade-scrap-for-upgrades]]).

### A quirk of choice ordering
All four subsystem offers carry `max_group="0"` on their agree-choices; the reactor offer
does not. Fandom explains the visible consequence: choices carrying `max_group` are sorted
**below** choices without it, so on the four subsystem offers "Decline" is listed first
and "Agree" second, while on the reactor offer the order is reversed
([[source-fandom-trade-scrap-for-upgrades]]). The same mechanism is why blue options tend
to sit at the bottom of choice lists. The game files encode the attributes but not the
sorting rule, so this is Fandom's account of engine behaviour, not a file claim.

### Commented-out content
Each of the four subsystem offers contains a **commented-out** third choice —
`req="<system>" lvl="3"` → *"Decline. Your system is fully upgraded."* — that would have
given a distinct message at max level instead of hiding the offer
([[source-newevents]]). Per [[concept-event-list-weighting]], commented-out entries are
excluded before counting; they are recorded here only as cut content.

## Blue Options
None that render blue. The agree-choices carry `req` attributes but every one of them is
explicitly `blue="false"`, so they appear as ordinary options gated on your ship state
rather than as blue options ([[source-newevents]]).

## Rewards & Risks
- **Reward:** one (sub)system or reactor level, priced 8–45 scrap depending on which offer
  rolled and how upgraded you already are.
- **Risk:** none. No fight, no boarders, no fuel, no forced spend. Declining is free.

## Strategy Notes
- *Opinion:* the cheap band is genuinely good value — Piloting or Doors level 2 for 8–15
  scrap undercuts store pricing. The expensive band (25–45 for a level-3 subsystem, or
  35–45 for Sensors 3) is close to store parity and worth skipping unless the sector is
  store-poor.
- The reactor offer at 15–25 scrap is the standout: reactor bars are otherwise only
  buyable at a store and are useful on every build.
- Because the offer is rolled *before* you choose, "Inquire" is never a commitment — you
  can always decline after seeing which of the five you got.

## Related
- [[event-improve-reactor-for-supplies]] — the sibling event that buys a reactor bar with
  missiles/drones/fuel instead of scrap
- [[event-crew-hiring-station]] — the other `ITEMS`-pool purchase event
- [[event-rebel-checkpoint]] — shares the `NEUTRAL_EXIT` / `OVERRIDE_NEUTRAL_EXIT` pool
- [[concept-event-list-weighting]] — basis for the 1/5 and 1/13 figures
- [[concept-sector-event-allocation]] — why `NEUTRAL_EXIT` has no sector allocation

## Open Questions
- [ ] Whether event-list selection is truly uniform.
- [ ] Confirm the reactor `max_lvl="24"` really corresponds to Fandom's "25 power bars"
      ceiling — the off-by-one is unverified here.
- [ ] Is the displayed price the same roll that is charged?

## Sources
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-trade-scrap-for-upgrades]] (per raw/wiki/trade-scrap-for-upgrades.md)
