---
id: event-lanius-ship-absorbing-automated-scout
type: event
event_name: LANIUS_AUTO_REBEL
sectors: [[[sector-abandoned-sector]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [lanius, optional-fight, fleet-delay, map-reveal, unique, advanced-edition]
---

# Lanius ship absorbing automated scout — `LANIUS_AUTO_REBEL`

## Summary
A Lanius ship is eating a Rebel automated scout. Scare it off and the half-digested scout
is yours to strip — for either a sector map reveal or a one-turn Rebel fleet delay. The
unusual part is that you get the prize **even if the Lanius escapes**: every terminal
state of the fight, including `gotaway`, routes into the same reward list.

## Trigger & Where It Appears
- Sector: [[sector-abandoned-sector]] only.
- List: `NEUTRAL_LANIUS`, allocated `min=5 max=6` beacons per sector
  ([[source-sector-data-xml]]); thirteen members → **1/13** *assuming uniform selection
  across list entries* ([[source-dlcevents-anaerobic]]).
- `unique="true"` — at most once per sector.
- The Lanius spawns as `<ship load="LANIUS_AUTO_REBEL" hostile="false"/>`.
- Long-range scanners show a ship
  ([[source-fandom-lanius-ship-absorbing-automated-scout]]).

> **AE-only** — Advanced Edition file and sector.
>
> Naming trap: `LANIUS_AUTO_REBEL` names both the event and its enemy ship definition.

## Text
> You come across a Lanius ship in the process of absorbing a Rebel automated scout. If
> you scare off the Lanius you could probably make use of it.

(`event_LANIUS_AUTO_REBEL_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Fight the ship. | — | *"You power up your weapons, which quickly gets the attention of the ship."* → combat with `LANIUS_AUTO_REBEL`. Destroyed → `MED standard`; dead crew → `HIGH standard`; **got away** → no combat reward. All three then run **Inspect the automated ship** below. | 100% |
| 2 | Leave them alone. | — | *"Whatever assistance the disabled scout could provide is not worth the risk of fighting another Lanius. You prepare to move on."* → nothing happens. | 100% |

### Inspect the automated ship (`LANIUS_AUTO_REBEL_LIST`)
Two members, **1/2** each *assuming uniform selection across list entries*
([[source-dlcevents-anaerobic]]):

| Result | Payload |
|---|---|
| Beacon data recovered from the scout | scrap + `<reveal_map/>` — **the current sector map is revealed** |
| False telemetry fed back to the Rebel fleet | scrap + `<modifyPursuit amount="-1"/>` — **Rebel fleet delayed 1 turn** |

> ⚠️ **Reward level in doubt.** Both entries are written
> `<autoReward level="low">scrap_only</autoReward>` — **lowercase `low`**, where every
> other reward tag in the file uses `LOW`/`MED`/`HIGH`
> ([[source-dlcevents-anaerobic]]). Fandom asserts this is a typo the engine mishandles,
> treating the invalid value as `RANDOM`, and describes the payout as "a random amount of
> scrap" ([[source-fandom-lanius-ship-absorbing-automated-scout]]). The lowercase value is
> a verifiable fact in the game files; the engine's response to it is Fandom's inference,
> not something any source here demonstrates. Trusting the game files for *what is
> written* and flagging the *consequence* as unconfirmed.

## Blue Options
None — unusually for a Lanius encounter, there is no `req="anaerobic"` branch here.

## Rewards & Risks
- The `LANIUS_AUTO_REBEL` ship definition is **escape-capable** (`chance="0.2" min="2"
  max="4"` → `LANIUS_ESCAPE`) but has **no surrender** entry
  ([[source-dlcevents-anaerobic]]).
- The `gotaway` branch still offers the "Inspect the automated ship" follow-up — so an
  escaping enemy costs you the combat reward but **not** the map reveal / fleet delay
  ([[source-dlcevents-anaerobic]], confirmed on
  [[source-fandom-lanius-ship-absorbing-automated-scout]]).
- Risk: a Lanius warship fight, freely declinable via choice 2.

## Strategy Notes
- Both prizes are strategic rather than material: a full sector map reveal, or a turn of
  breathing room from the fleet. Which one you get is not yours to choose.
- *Opinion:* the escape-still-pays structure makes this a better fight than it looks —
  you cannot be denied the payoff by a runner, only by losing.

## Related
- [[event-lanius-ship-absorbing-rebel-base]] — the other "Lanius eat Rebel hardware, you
  profit" event, with a Lanius-crew blue option and a fleet delay
- [[event-lanius-fight]] — the `LANIUS_SHIP` tables (a different, surrender-capable
  definition)
- [[entity-lanius]], [[entity-rebels]], [[sector-abandoned-sector]]

## Open Questions
- [ ] What the engine actually pays for `level="low"` (lowercase).
- [ ] Numeric values behind `MED` / `HIGH standard`.

## Sources
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-lanius-ship-absorbing-automated-scout]] (per raw/wiki/lanius-ship-absorbing-automated-scout.md)
