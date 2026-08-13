---
id: event-malfunctioning-defense-system
type: event
event_name: DISTRESS_SATELLITE_DEFENSE
sectors: [[[sector-abandoned-sector]], [[sector-civilian-sector]], [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-federation-space]], [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]], [[sector-pirate-controlled-sector]], [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]], [[sector-uncharted-nebula]], [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: distress
hostile: false
blue_options: [[[item-cloaking]], [[item-ion-weapons]], engi crew]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 11
tags: [distress, unique, blue-option, cloaking-tiered, hull-damage-risk, breach-risk, cut-content, engi-crew]
---

# Malfunctioning defense system — `DISTRESS_SATELLITE_DEFENSE`

## Summary
A station's automated gun has gone rogue. The unaided answer — shoot it — is a coin flip
between a small payout and a hull breach. Five blue options replace that gamble, and one of
them is the game's clearest **tiered** blue option: Cloaking pays out `LOW`, `MED` or `HIGH`
depending on the *level* of the system, and the two upper tiers are Advanced Edition only.
The widest sector spread of any event in this batch. `unique="true"`.

## Trigger & Where It Appears
- Sectors: [[sector-federation-space]], [[sector-civilian-sector]],
  [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]],
  [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]],
  [[sector-pirate-controlled-sector]], [[sector-rock-controlled-sector]],
  [[sector-rock-homeworlds]], [[sector-zoltan-controlled-sector]],
  [[sector-zoltan-homeworlds]], [[sector-uncharted-nebula]], [[sector-abandoned-sector]]
- Event lists: `DISTRESS_BEACON` ([[source-newevents]]), `DISTRESS_BEACON_ENGI`
  ([[source-events-engi]]), `DISTRESS_BEACON_MANTIS` ([[source-events-mantis]]),
  `DISTRESS_BEACON_ROCK` ([[source-events-rock]]), `DISTRESS_BEACON_ZOLTAN`
  ([[source-events-zoltan]]), `DISTRESS_BEACON_LANIUS` ([[source-dlcevents-anaerobic]])
- Allocation: 1–2 or 1–3 depending on sector; `DISTRESS_BEACON_LANIUS` 1–2 in
  `LANIUS_SECTOR` ([[source-sector-data-xml]])
- Beacon: `<distressBeacon/>`
- Long-range scanners show **no ship** ([[source-fandom-malfunctioning-defense-system]])
- `unique="true"` — once per run

## Text
> The distress signal is coming from a small space station orbiting an uninhabited planet.
> Their satellite defense system has gone haywire and their repair crew can't approach
> without being fired on. They're looking for help to fix or disable it.

(`event_DISTRESS_SATELLITE_DEFENSE_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Promise to help. | — | *"You consider your options."* → a second screen with the five options below | — |
| 2 | Leave them alone. | — | *"You can't help them so you prepare to move on."* → nothing | 100% |

### After "Promise to help"

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1a | Simply fire on the defense system from a distance. | — | Rolls `SATELLITE_DEFENSE_BORING` (2 entries) — see below | 1/2 each |
| 1b | **(Ion Weapon)** Disable the defense system. | `req="WEAPONS_ION"` | `autoReward level="HIGH"` `standard` | 100% |
| 1c | **(Cloaking)** Use your Cloaking to disable the system. | `req="cloaking" lvl="1"` | *"…your cloaking gives out and you are forced to destroy the satellite…they don't seem happy…"* → `autoReward level="LOW"` `standard` | 100% |
| 1d | **(Improved Cloaking)** Use your Cloaking to disable the system. | `req="cloaking" lvl="2"` | *"It was a sloppy job but they appreciate it…"* → `autoReward level="MED"` `standard` | 100% |
| 1e | **(Advanced Cloaking)** Use your Cloaking to disable the system. | `req="cloaking" lvl="3"` | *"…you are able to safely disable the system."* → `autoReward level="HIGH"` `standard` | 100% |
| 1f | **(Engi Crew)** Remotely repair its targeting system. | `req="engi"` | *"Your crew-member is able to remotely fix the glitch in the defense AI…"* → `autoReward level="HIGH"` `standard` | 100% |

Options 1c–1e all carry `max_group="0"`, which is how the game shows only the **best** tier
your Cloaking qualifies for rather than all three at once ([[source-events-xml]]).

### Choice 1a → `SATELLITE_DEFENSE_BORING`

| Entry | Outcome | Share |
|---|---|---|
| 1 | *"…the defense system is no match for your weapons. However, the station does not seem happy with your 'solution'."* → `autoReward level="LOW"` `standard` | 1/2 |
| 2 | *"…you take minor damage before escaping. The station will need to find help elsewhere."* → `damage 3` + `damage 1 random system` (AE only) + `damage 1 room effect="breach"` | 1/2 |

Two entries → **1/2 each**, assuming uniform selection across list entries
([[source-events-xml]]).

## Blue Options
- **[[item-ion-weapons]]** (`req="WEAPONS_ION"`) — the blueprint list resolves to
  `ION_1`, `ION_2`, `ION_4`, `BOMB_ION`, `ION_STUN`, `BOMB_STUN`, `ION_CHARGEGUN`,
  `ION_CHAINGUN` ([[source-autoblueprints]]). Fandom confirms the two bombs count and notes
  that **no missile ammo is consumed** ([[source-fandom-malfunctioning-defense-system]]).
  Pays `HIGH` `standard` — the joint-best outcome.
- **[[item-cloaking]]** (`req="cloaking"`, `lvl` 1 / 2 / 3) — a genuine three-tier gate:
  level 1 pays `LOW`, level 2 `MED`, level 3 `HIGH`. Owning Cloaking at level 1 is *worse*
  than owning an ion weapon.
- **Engi crew** (`req="engi"`) — `HIGH` `standard`, free, no equipment needed. The easiest
  route to the best outcome.

### Cut content: the Lanius option
A sixth blue option exists in the file but is **commented out**:

```
<!-- <choice hidden="true" req="anaerobic"> … (Lanius Crew) Your crew offers to help.
     … autoReward level="HIGH" scrap_only … -->
```

Its prose is finished — the Lanius walks out of the airlock because it gives off no heat
signature and melts the satellite down for scrap. It is inert; the commented block also
contains a broken nested comment (`<!-DLC!-`) which is likely why it was disabled.
Fandom records the same finding ([[source-events-xml]],
[[source-fandom-malfunctioning-defense-system]]).

## Rewards & Risks
- **Rewards:** `HIGH` `standard` via ion weapons, Engi crew, or Cloaking 3; `MED` via
  Cloaking 2; `LOW` via Cloaking 1 or a lucky unaided shot.
- **Risk:** the unaided branch only — 4 hull (vanilla) / 5 hull, a random system and a hull
  **breach** (AE), half the time.
- Choice 2 is a completely free skip. No cost, no fleet advance.

## Version Differences
Base-`events.xml` event, present in both editions, with three `<!--DLC!-->` / `<!--DLC-->`
markers ([[source-events-xml]]):

- **Cloaking level 2 and level 3 branches are AE-only.** In vanilla, Cloaking pays `LOW`
  `standard` no matter how upgraded it is — the tiering is an Advanced Edition addition.
- `SATELLITE_DEFENSE_BORING` entry 2: `<damage amount="1" system="random"/>` is AE-only, so
  vanilla takes 4 hull and a breach rather than 5 hull, a breach and a dead system.

The commented-out Lanius option would have been AE content (Lanius are an AE species) but is
disabled in both.

## Strategy Notes
- *(Opinion.)* With an Engi crewmember or any ion weapon, this is a free `HIGH standard` —
  one of the better distress beacons in the game.
- With Cloaking at level 1 only, prefer an ion weapon if you have one; `LOW` is barely better
  than the coin flip.
- Without any gate, the unaided shot is a 50/50 for `LOW standard` against 4–5 hull *and a
  breach*. On a damaged hull, choice 2 is the better play — it costs nothing.

## Related
- [[event-giant-alien-spiders]], [[event-fire-on-research-station]],
  [[event-unknown-disease-on-mining-colony]], [[event-crushed-pirate]],
  [[event-asteroid-belt-distress]] — the rest of the shared `DISTRESS_BEACON` pool
- [[item-cloaking]], [[item-ion-weapons]]
- [[entity-engi]], [[entity-lanius]]

## Open Questions
- [ ] Are `<eventList>` entries selected uniformly? The 1/2 assumes it.
- [ ] Exactly how `max_group="0"` picks between the three Cloaking tiers — the behaviour is
      inferred from the attribute, not documented in the files.
- [ ] Numeric values behind `LOW`/`MED`/`HIGH` `standard`.
- [ ] Was the Lanius option cut for balance, or simply broken by the malformed nested
      comment?

## Sources
- [[source-events-xml]] (per `raw/gamedata/events.xml`)
- [[source-newevents]] (per `raw/gamedata/newEvents.xml` — `DISTRESS_BEACON`)
- [[source-events-engi]] (per `raw/gamedata/events_engi.xml`)
- [[source-events-mantis]] (per `raw/gamedata/events_mantis.xml`)
- [[source-events-rock]] (per `raw/gamedata/events_rock.xml`)
- [[source-events-zoltan]] (per `raw/gamedata/events_zoltan.xml`)
- [[source-dlcevents-anaerobic]] (per `raw/gamedata/dlcEvents_anaerobic.xml` — `DISTRESS_BEACON_LANIUS`)
- [[source-autoblueprints]] (per `raw/gamedata/autoBlueprints.xml` — `WEAPONS_ION`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-malfunctioning-defense-system]] (per `raw/wiki/malfunctioning-defense-system.md`)
