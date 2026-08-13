---
id: event-engi-distress-rebel-fight
type: event
event_name: DISTRESS_ENGI_REBEL
sectors: [[[sector-engi-controlled-sector]], [[sector-engi-homeworlds]]]
beacon_type: distress
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unique, forced-fight, trading, augment-reward, weapon-chance, drone-chance]
---

# Engi distress Rebel fight — `DISTRESS_ENGI_REBEL`

## Summary
A distress beacon that is really an ambush: there is no choice, you simply fight a Rebel
fighter. Winning hands you scrap and then rolls straight into
[[event-distress-engi-rebel-result]], a trading event where the rescued Engi will sell you
an augmentation for 40 scrap, 2 missiles and 2 fuel.

## Trigger & Where It Appears
- Sectors: [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]]
- Beacon: **distress** — carries `<distressBeacon/>` ([[source-events-xml]], per
  `raw/gamedata/events_engi.xml`)
- Event list: `DISTRESS_BEACON_ENGI`, allocated `min=1 max=3` per Engi sector
  ([[source-sector-data-xml]])
- `unique="true"` — at most once per run

## Text
> The distress signal originates from a small Engi ship under attack by a rebel fighter -
> but when the Rebels see Federation markings they turn to attack!

(`event_DISTRESS_ENGI_REBEL_text`, per [[source-text-events-xml]])

## Choices & Outcomes

The event has **no choices**. It loads `<ship load="DISTRESS_ENGI_REBEL" hostile="true"/>`
immediately.

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none — forced fight)* | — | Fight a Rebel ship (`auto_blueprint="SHIPS_REBEL"`). **Destroyed** → `LOW` `standard`. **Dead crew** → `MED` `standard`. Either way, continue → [[event-distress-engi-rebel-result]]. | 100% |

The ship definition has no `<surrender>` and no `<escape>` block — it fights to the end.
([[source-events-xml]], per `raw/gamedata/events_ships.xml`;
[[source-fandom-engi-distress-rebel-fight]])

## Blue Options
None.

## Rewards & Risks
- `LOW` scrap-with-resources for destroying the ship; `MED` for killing the crew instead
  (boarding or an anti-personnel approach is worth one reward tier here).
- The real payload is the follow-up event, not the fight — see
  [[event-distress-engi-rebel-result]] for the Engi Med-bot Dispersal augment, the Healing
  Burst chance and the drone chance.
- Risk: an unavoidable fight at a beacon that advertised itself as a rescue. Nothing
  identifies it as a trap before you jump.

> ⚠️ **CONTRADICTION:** the intro text differs between sources.
> - Game files: *"The distress signal originates **from** a small Engi ship under attack by
>   a rebel fighter - but when **the Rebels** see Federation markings they turn to
>   attack!"* ([[source-text-events-xml]], per `raw/gamedata/text_events.xml`)
> - Fandom: *"The distress signal originates **at** a small Engi ship under attack by a
>   rebel fighter - but when **they** see Federation markings they turn to attack!"*
>   ([[source-fandom-engi-distress-rebel-fight]])
>
> Trusting the game files — `high` reliability against `medium`, and they are the exact
> build being played. Most likely the wiki preserves pre-AE wording; not confirmed as a
> version difference.

## Strategy Notes
- Killing the crew rather than destroying the hull upgrades the payout from `LOW` to `MED`.
  *(Opinion: worth doing only if you already have boarders or a Beam/anti-bio setup.)*
- Budget for the follow-up before you take the fight — the best outcome downstream costs
  40 scrap, 2 missiles and 2 fuel, and the fight itself only pays `LOW`/`MED`.

## Related
- [[event-distress-engi-rebel-result]] — the trading event this always leads to
- [[event-engi-research-station]] — the other unique distress event in `DISTRESS_BEACON_ENGI`
- [[concept-rebel-fleet-advance]]

## Open Questions
- [ ] Scrap values of `LOW` and `MED` `standard` at a given sector depth.
- [ ] Is the intro-text difference a vanilla/AE change or a wiki transcription error?

## Sources
- [[source-events-xml]] (per `raw/gamedata/events_engi.xml`, `raw/gamedata/events_ships.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-engi-distress-rebel-fight]] (per `raw/wiki/engi-distress-rebel-fight.md`)
