---
id: event-terraforming-scan
type: event
event_name: TERRAFORMING_SCAN
sectors: [[[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: any
hostile: false
blue_options: [sensors lvl 2, zoltan crew]
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [blue-option, system-upgrade, scrap-gain, scrap-cost, pirate-fight, unique, advanced-edition, filler]
---

# Terraforming scan — `TERRAFORMING_SCAN`

## Summary
A Federation terraforming crew needs a planetary life-scan they can't power themselves.
Helping is free and cannot hurt you at the top level; the whole event is about *how good
your scan is*. A plain scan succeeds half the time; Advanced Sensors or a Zoltan crew
member skip straight to the good branch. The payoff branch is a 1/3 split between an
Oxygen upgrade, a pirate ambush, and a small moral dilemma worth 15–25 scrap.

## Trigger & Where It Appears
- Event lists: `NEUTRAL` in `newEvents.xml`, tagged `<!--DLC matt - down below-->`
  ([[source-newevents]]), and `OVERRIDE_NEUTRAL` in the Advanced Edition replacement
  ([[source-dlceventsoverwrite]]). The event's own inline comment reads
  *"in neutral only"*.
- `NEUTRAL` is allocated directly by two sectors —
  [[sector-slug-controlled-nebula]] and [[sector-slug-home-nebula]], both at
  `min=1 max=2` ([[source-sector-data-xml]]) — **and** is the engine's hardcoded fallback
  list used to fill out any sector that has run out of its own allocations
  ([[source-newevents]], list comment). Fandom records the same shape: Slug sectors, plus
  `alsooccur=filler` ([[source-fandom-terraforming-scan]]).
- `unique="true"` — at most once per run.
- Beacon: ordinary. No distress flag, no environment, no ship on arrival.

## Text
> You receive a hail from a station orbiting a nearby planet. "Captain, we are Federation
> Terraforming Team C12 and are in need of assistance. Do you have some time?"

(`event_TERRAFORMING_SCAN_text`, per [[source-text-events-xml]])

> ⚠️ **CONTRADICTION (wording, minor):** Fandom transcribes the follow-up line as *"any
> chance you **could** help?"*; the game string reads *"any chance you **can** help?"*
> ([[source-fandom-terraforming-scan]] vs [[source-text-events-xml]]). Trusting the game
> files — reliability `high` vs `medium`. Not a version difference: there is only one
> `event_TERRAFORMING_SCAN_c1_text` string in the 1.6.x data.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | You offer your assistance. | — | *"Thank you! We need to scan this planet for life before we can begin terraforming, but our sensors can't get the necessary power to scan through this atmosphere. We've got a schedule to keep, any chance you can help?"* → opens the scan sub-menu below. | 100% |
| 2 | You do not have time. | — | *"We understand. Best of luck on your mission, sir!"* → a single "Prepare to jump away." continue → nothing happens. | 100% |

### The scan sub-menu (after choice 1)

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1a | Attempt to scan the planet. | — | Loads `NORMAL_SCAN_TERRAFORMING` — see below. | — |
| 1b | **(Advanced Sensors)** Set sensors to maximum and scan. | `req="sensors" lvl="2"` | Loads `HIGH_SCAN_TERRAFORMING` directly. | 100% |
| 1c | **(Zoltan)** Send your crewman to overcharge their systems. | `req="energy"` | Loads `HIGH_SCAN_TERRAFORMING` directly. | 100% |

### `NORMAL_SCAN_TERRAFORMING` — two entries, no repeats
**Assuming uniform selection across list entries** ([[concept-event-list-weighting]]),
each is **1/2**:

| Odds | Text | Effect |
|---|---|---|
| 1/2 | *It seems your sensors are no more powerful than the terraformer's. You apologize and continue on your way.* | Nothing. |
| 1/2 | *You find if you modulate the feedback signal of your sensors to just the right frequency, you're able to get through the atmosphere and perform a complete scan!* | A hidden continue then loads `HIGH_SCAN_TERRAFORMING`. |

So the unaided scan reaches the payoff table **half** the time; either blue option reaches
it **always**.

### `HIGH_SCAN_TERRAFORMING` — three entries, no repeats (1/3 each)

| Odds | Text | Effect |
|---|---|---|
| 1/3 | *After a complete scan of the planet, you find no life. The team is grateful and ready to get to work. The station scientists have a unique talent for life support units and offer to upgrade your oxygen system as thanks.* | `<upgrade amount="1" system="oxygen"/>` — free Oxygen level. |
| 1/3 | *A complete scan of the planet reveals no life signs other than a single ship on the surface. The terraformers thank you for your help, and attempt to contact the ship. Just as you're about to jump away, the ship takes off and attacks, it's a pirate!* | `<ship load="PIRATE" hostile="true"/>` — pirate fight, default rewards. |
| 1/3 | *A complete scan of the planet reveals a simple mold as the only life present. The terraformers claim their terraforming plans are only hindered by intelligent life; they can begin their work.* | Opens the mold dilemma below. |

([[source-newevents]], [[source-text-events-xml]])

### The mold dilemma (third `HIGH_SCAN` entry)

| # | Choice | Outcome(s) |
|---|---|---|
| 1 | Tell them to stop. Any life is valuable. | *"But our livelihood depends on this job! Who cares about some silly mold? We'll pay you to look the other way!"* → three sub-choices below. |
| 2 | Leave them to their work. | `<event/>` — nothing happens. |

| # | Sub-choice | Outcome(s) |
|---|---|---|
| 1 | Accept the bribe and leave. | **+15 to +25 scrap.** No result text at all — the event body is a bare `item_modify`. |
| 2 | Offer to pay them to at least delay until the mold can be studied. | *"They see reason and accept the offer. The station scientists have a unique talent for life support units and offer to upgrade your oxygen system as an apology for their behaviour."* → `<upgrade amount="1" system="oxygen"/>` **and −15 to −25 scrap.** |
| 3 | Power your weapons and demand they leave at once. | *"They shut off communications, but you can tell they have begun an evacuation procedure."* → nothing. |

Fandom notes that the actual scrap figure is shown before you commit, for both the +
and − branches ([[source-fandom-terraforming-scan]]).

### The `PIRATE` ship
`auto_blueprint="SHIPS_PIRATE"`; **50% surrender chance** at `min=3 max=4`
(`chance="0.5"`, and per [[concept-surrender-offers]] the surrender probability is
`1 − chance`) loading `PIRATE_SURRENDER`; 50% escape chance at `min=2 max=4` loading
`PIRATE_ESCAPE`; `DESTROYED_DEFAULT` / `DEAD_CREW_DEFAULT` — default rewards
([[source-events-ships]]).

## Blue Options
- **Advanced Sensors** (`req="sensors" lvl="2"`) — converts the 1/2 scan gamble into a
  guaranteed entry to `HIGH_SCAN_TERRAFORMING`. Note the label says "Advanced Sensors"
  but the gate is Sensors **level 2**, which the game calls *Improved* Sensors; Fandom
  renders the requirement as "level 2+" ([[source-fandom-terraforming-scan]]).
- **Zoltan crew member** (`req="energy"`) — identical effect, no system requirement. Any
  Zoltan aboard satisfies it.

Both options bypass the failure branch entirely; neither changes the odds *within*
`HIGH_SCAN_TERRAFORMING`.

## Rewards & Risks
- Best case: free Oxygen upgrade, or +15–25 scrap for looking the other way.
- Worst case: a pirate fight you did not have to take, at 1/3 of every successful scan.
- Declining at the top level (choice 2) is completely safe and costs nothing.
- There is **no** scrap or fuel cost to helping; the only outlay is the optional
  −15–25 scrap bribe-back.

## Strategy Notes
- *Opinion:* with either blue option this is a good event — 2/3 of the payoff table is
  positive and the fight is a standard pirate. Without them the expected value is halved
  by the coin-flip failure, but failing costs nothing, so helping is still free upside.
- On a damaged ship the 1/3 pirate branch is the only reason to decline. Choice 2 is a
  clean exit.
- In the mold dilemma, the bribe (+15–25) and the delay (−15–25 plus an Oxygen level) are
  a straight scrap-versus-system trade. Oxygen is a cheap system to upgrade at a store,
  so *(opinion)* taking the scrap is usually the stronger line unless you are already
  fighting Oxygen fires.

## Related
- [[event-rebel-checkpoint]], [[event-battlefield-wreckage]] — the other AE additions to
  the same `NEUTRAL` / `OVERRIDE_NEUTRAL` filler pool
- [[event-pirate-fight]] — the fight this can hand you
- [[concept-surrender-offers]] — how the `PIRATE` surrender number is read
- [[concept-event-list-weighting]] — basis for the 1/2 and 1/3 figures
- [[event-pirate-surrender]] — the shared `PIRATE_SURRENDER` aftermath this hull loads
- [[event-pirate-escape]] — the shared `PIRATE_ESCAPE` aftermath this hull loads

## Open Questions
- [ ] Whether event-list selection is truly uniform.
- [ ] Does the Zoltan option also require the Zoltan to be alive and aboard at the time,
      or merely present in the crew roster?
- [ ] Exact scrap value shown for the bribe before committing — the files give a range,
      the engine picks one.

## Sources
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-fandom-terraforming-scan]] (per raw/wiki/terraforming-scan.md)
