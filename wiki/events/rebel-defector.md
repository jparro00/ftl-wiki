---
id: event-rebel-defector
type: event
event_name: ALISON_DEFECTOR
sectors: [[[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]]]
beacon_type: hostile
hostile: true
blue_options: []
chain: [[[chain-rebel-defector]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 6
tags: [rebel, unique, crew-reward-chance, crew-loss-risk, boarding-risk, fleet-advance-risk, quest-marker, donor-event]
---

# Rebel defector — `ALISON_DEFECTOR`

## Summary
A Rebel ship engages *and* a lone Rebel soldier teleports aboard begging to defect. The
fight with the [[concept-rebel-fleet-advance]] ship happens regardless; the only thing you decide is
what to do with the defector. Both branches roll on a list where **half the entries hand
you a free Human crew member** and the rest cost you hull, engines, boarders or a
crewmember's life. Rejecting him once opens a second offer that adds a **quest marker** to
the crew-gain outcomes. `unique="true"` — once per run.

## Trigger & Where It Appears
- Sectors: [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]]
- Event list: `NEUTRAL_REBEL` ([[source-events-rebel]]), allocated `min=5 max=6` in both
  `REBEL_SECTOR` and `REBEL_SECTOR_MINIBOSS` ([[source-sector-data-xml]])
- Beacon: an ordinary neutral beacon that turns hostile on arrival —
  `<ship load="REBEL" hostile="true"/>` fires immediately ([[source-events-xml]])
- Long-range scanners show a ship ([[source-fandom-rebel-defector]])
- `unique="true"` — at most once per run ([[source-events-xml]]; Fandom agrees)

## Text
> A Rebel ship is patrolling this beacon, and immediately turns to engage. As your crew
> scramble to battle readiness, sensors detect a short-range teleporter signal. An intruder
> is on board!

Continuing:

> A flushed and panicky rebel soldier has teleported aboard. The rebel, who appears
> unarmed, repeatedly declares his peaceful intentions. It seems the rebel life has lost
> its charm.

(`event_ALISON_DEFECTOR_text`, `event_ALISON_DEFECTOR_c1_text`, per
[[source-text-events-xml]])

## Choices & Outcomes

The event opens with a forced *Continue…*; the real decision is the pair below. **The Rebel
ship fight runs underneath every outcome.**

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Accept his proposal, and prepare to fight the Rebel ship. | — | Rolls `ALISON_DEFECTOR_HELP` — see below. | — |
| 2 | Reject his offer. You can never trust these Rebels. | — | Rolls `ALISON_DEFECTOR_REJECT` — see below. | — |

### Choice 1 → `ALISON_DEFECTOR_HELP` (6 entries)

| Entry | Outcome | Share |
|---|---|---|
| 1 | *"…He damages your engines and steals your flight data…"* → `damage 2` + `damage 1 engines` (AE only) + `modifyPursuit 1` | 1/6 |
| 2 | *"…reveals a small remote trigger…"* → `boarders 2 human` + `damage 3` | 1/6 |
| 3–5 | *"Relieved and light-headed, your new crewmember gets to work…"* → `crewMember 1 human` | **3/6** |
| 6 | *"…suddenly turns and eviscerates the nearest crew-member."* → `boarders 1 human` + `removeCrew` (Clone Bay revives: `<clone>true</clone>`) | 1/6 |

Entry 3 is written out **three times** in the list, so under uniform selection across list
entries the crew gain is **1/2**. This is derived from the duplication in
`ALISON_DEFECTOR_HELP` and assumes each `<event>` entry is equally likely
([[source-events-xml]]).

### Choice 2 → `ALISON_DEFECTOR_REJECT` (3 entries)

| Entry | Outcome | Share |
|---|---|---|
| 1 | *"Your fearless crew easily overcome the intruder…"* → nothing beyond the ship fight | 1/3 |
| 2 | *"Attempting to deal with attacks from inside and out is never easy!"* → `boarders 1 human` | 1/3 |
| 3 | *"He offers to lead you to a secret cache of scrap nearby if you let him join your crew."* → a second three-way choice | 1/3 |

Uniform-selection assumption again ([[source-events-xml]]).

#### The second offer (entry 3)

| # | Choice | Outcome |
|---|--------|---------|
| 3a | Reluctantly accept his proposal and fight the Rebel ship. | Rolls `ALISON_DEFECTOR_HELP_2` — same shape as `HELP`, but the three crew entries also attach `<quest event="ALISON_DEFECTOR_QUEST"/>`, and entry 2 damages **piloting** instead of engines (`damage 2` + `damage 1 pilot`, AE only) |
| 3b | Reject him outright and execute him on the spot. | Nothing — `<event/>` is empty |
| 3c | Reject his offer again. | `boarders 1 human` |

> Fandom flags 3a as **bugged**: the crew-gain tag was not marked hidden, so a crew icon is
> displayed on the choice, telegraphing that you will get a crewmember — which the
> developers normally hide when a choice is meant to be a gamble
> ([[source-fandom-rebel-defector]]).

### The quest marker — `ALISON_DEFECTOR_QUEST`
Only choice 3a can grant it. It is a two-entry list, so **1/2 each** under uniform
selection ([[source-events-xml]]):

- *"Arriving at the specified coordinates you find a sizable stash of useful materials."* →
  `autoReward level="HIGH"` `stuff`
- *"You arrive at the location of the hoard, but discover that it was not quite as large as
  advertised."* → `autoReward level="LOW"` `scrap_only`

### The enemy ship
`<ship name="REBEL" auto_blueprint="SHIPS_REBEL">` with `<surrender chance="0.5" min="2"
max="3" load="PIRATE_SURRENDER"/>` and `<escape chance="0.5" min="3" max="4"
load="PIRATE_ESCAPE"/>`; `destroyed` and `deadCrew` load the shared defaults
([[source-events-ships]]). Per [[concept-surrender-offers]], `chance="0.5"` means a **50%**
surrender offer, not 50% refusal. Rewards are the standard [[event-rebel-fight]] defaults.

## Blue Options
None. No `req` appears anywhere in this event.

## Rewards & Risks
- **Reward:** a free Human crewmember on 3 of 6 entries in either accept path, plus the
  usual Rebel-ship fight rewards. The quest marker (choice 3a only) pays `HIGH` `stuff` or
  `LOW` `scrap_only`.
- **Risks:** 2–3 hull plus an engines or piloting hit and a Rebel fleet advance; 1–2 human
  boarders while you are already in a ship fight; or a dead crewmember (Clone Bay revives
  them — the `removeCrew` block carries `<clone>true</clone>`).
- The `modifyPursuit amount="1"` entry is the only fleet-advance risk here. Fandom renders
  it as *"pursuit is doubled"*; the raw value is a bare `1`. See
  [[concept-rebel-fleet-advance]] for the unresolved units question.

## Version Differences
`ALISON_DEFECTOR` is a base-`events.xml` event, so the encounter exists in both editions,
but three tags inside it are `<!--DLC-->`-marked and therefore **Advanced Edition only**
([[source-events-xml]]):

- `HELP` entry 1 and `HELP_2` entry 1: `<damage amount="1" system="engines"/>`
- `HELP_2` entry 2: `<damage amount="1" system="pilot"/>`
- The `HELP_1` / `HELP_2_1` text ids are marked `<!--DLC2-->`, i.e. the wording was revised
  for AE

In vanilla the deception outcome is therefore **2 hull and no system damage**; in AE it is
3 hull and a disabled engine (or piloting). Clone Bay revival on the eviscerated-crew
outcome is also AE-only, since the Clone Bay itself is.

## Related
- [[chain-rebel-defector]] — the full quest line this belongs to
- [[event-rebel-fight]] — the same `REBEL` ship, without the defector
- [[event-rebel-fight-with-boarders]] — the other Rebel event that mixes a fight with intruders
- [[event-mantis-fugitive]] — the sister "defector aboard, pick a side" event, `ALISON_MANTIS_CREW`
- [[concept-rebel-fleet-advance]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]]
- [[concept-surrender-offers]], [[concept-rebel-fleet-advance]]
- [[event-pirate-surrender]] — the shared `PIRATE_SURRENDER` aftermath this hull loads
- [[event-pirate-escape]] — the shared `PIRATE_ESCAPE` aftermath this hull loads

## Open Questions
- [ ] Are `<eventList>` entries actually selected uniformly? The 1/2 and 1/3 figures above
      depend on it.
- [ ] Numeric values of `HIGH stuff` / `LOW scrap_only` at a given sector depth.
- [ ] Does the quest beacon expire if you jump past it?
- [ ] Is the crew-icon bug still present in 1.6.x, or only in the version Fandom tested?

> ⚠️ **CONTRADICTION:** the deception text on the *accept-immediately* path.
> - Game files: *"He damages your **engines** and steals your **flight data**…"*
>   (`event_ALISON_DEFECTOR_HELP_1_text`, [[source-text-events-xml]])
> - Fandom: *"He damages your **ship** and steals your **flight data**…"*
>   ([[source-fandom-rebel-defector]])
>
> Fandom appears to have transcribed the *reject-path* variant
> (`event_ALISON_DEFECTOR_HELP_2_1_text`: *"damages your ship and steals ship
> information"*) onto both branches, then swapped one noun back. Trusting the game files
> (`high` vs `medium`); the two branches genuinely have different strings, and the text ids
> are `<!--DLC2-->`-marked, so a pre-AE wiki transcription is also plausible.

## Sources
- [[source-events-xml]] (per `raw/gamedata/events.xml`)
- [[source-events-rebel]] (per `raw/gamedata/events_rebel.xml` — `NEUTRAL_REBEL`)
- [[source-events-ships]] (per `raw/gamedata/events_ships.xml` — the `REBEL` ship)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-rebel-defector]] (per `raw/wiki/rebel-defector.md`)
