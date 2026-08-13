---
id: event-donor-mantis-chase2
type: event
event_name: DONOR_MANTIS_CHASE2
sectors: [[[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]]]
beacon_type: quest
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [mantis, donor-event, quest-marker, combat, ship-escape, surrender, weapon-reward, unique]
---

# Mantis ship-collectors, rematch — `DONOR_MANTIS_CHASE2`

## Summary
The quest-marker half of the [[event-mantis-ship-collectors]] chase. The Mantis captain who
ran from you has bought a bigger ship and wants a rematch. This is the branch with the money
in it: **every** resolution — destroyed, dead crew, surrender, even letting them escape a
second time — pays better than finishing the first fight ever could, and three of the four
hand you a free weapon.

## Trigger & Where It Appears
- **Not in any sector event list.** It is a **quest-marker beacon**, placed by
  `<quest event="DONOR_MANTIS_CHASE2"/>` inside `DONOR_MANTIS_CHASE1`'s `<gotaway>` block
  ([[source-events-xml]]).
- The only route in: fight [[event-mantis-ship-collectors]], let the `DONOR_MANTIS_CHASE1`
  fighter complete its escape (it always attempts one — `escape timer="5" min="5" max="5"`,
  no `chance` attribute), then take the *"After them!"* choice. Choosing *"Forget it."*
  destroys the chain.
- Sectors are inherited from the parent: [[sector-mantis-controlled-sector]] and
  [[sector-mantis-homeworlds]]. The parent is `unique="true"`, so this can happen at most
  once per run.
- Long-Range Scanners show a ship at the beacon
  ([[source-fandom-mantis-ship-collectors]]).
- **Version:** `both`. The parent is pooled in the base `HOSTILE_MANTIS` list *and* in
  `OVERRIDE_HOSTILE_MANTIS`, so the chase exists in both editions.

## Text
> You catch up with the Mantis ship that escaped before, only to see them transferring their
> crew into an even bigger ship!

(`event_DONOR_MANTIS_CHASE2_text`, per [[source-text-events-xml]])

Combat starts immediately — the `<ship load="DONOR_MANTIS_CHASE2" hostile="true"/>` is in
the event body, before the single hidden continue choice:

> "Not YOU again! Do you know how much these repairs are going to cost me? Time to take out
> the big guns."

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none before combat — one hidden "continue" that only prints the taunt)* | — | Fight `DONOR_MANTIS_CHASE2`, a **Mantis Bomber** (`auto_blueprint="MANTIS_BOMBER"`) crewed entirely by Mantis. | 100% |

### The `DONOR_MANTIS_CHASE2` hull ([[source-events-xml]])

| Resolution | Declaration | Outcome |
|---|---|---|
| **Escape** | `<escape timer="12" min="6" max="6">` — no `chance` attribute | *"They appear to be trying to get away again."* |
| **Got away** | — | *"Looks like they got away. At least you're able to scrap their abandoned fighter."* → `HIGH standard` |
| **Surrender** | `<surrender min="2" max="2">` — no `chance` attribute | *"Look, you proved your point. We don't want to die… Take this and let us go. Please?"* → see below |
| **Destroyed** | — | `<weapon name="RANDOM"/>` + `MED standard` |
| **Dead crew** | — | `<weapon name="RANDOM"/>` + `HIGH standard` |

### The surrender offer

| # | Choice | Outcome |
|---|--------|---------|
| 1 | Let them live. | *"Thank you. But do you have any idea how much repairing TWO ships will set us back?…"* → `<autoReward level="HIGH">weapon</autoReward>` and `<ship hostile="false"/>`. |
| 2 | Finish them off. | *"No! Hurry up, get us out of here! They're crazy!"* → the fight continues. |

Fandom notes the weapon and scrap amounts are shown **before** you accept
([[source-fandom-mantis-ship-collectors]]).

> ⚠️ **CONTRADICTION:** the escape and surrender thresholds.
> - Game files: `escape … min="6" max="6"` and `surrender min="2" max="2"`, with **no
>   `chance` attribute on either** ([[source-events-xml]]).
> - Fandom: *"attempts to escape at 60% hull (12 seconds timer) and makes a surrender offer
>   at 20% hull"*, hedged in its own tooltip as *"actual in-game value may be 6 hull +
>   additional hull adjusted by sector progression"*
>   ([[source-fandom-mantis-ship-collectors]]).
>
> Trusting the game files: per [[concept-surrender-offers]], `min`/`max` on these blocks are
> **hull points, not percentages**. Fandom's own tooltip concedes as much. The 60%/20%
> figures are a gloss that only holds for a 10-hull ship.
>
> The missing `chance` attribute is a second, unresolved gap: with no `chance` declared, the
> data does not state how likely either the escape attempt or the surrender offer is.

## Blue Options
None. No `req` appears anywhere in the event or the ship block.

## Rewards & Risks
- **Best outcome: dead crew** — a random weapon *and* `HIGH standard`.
- **Surrender** — `HIGH weapon` (a weapon bundled with high scrap), and you take no further
  damage.
- **Destroyed** — a random weapon and `MED standard`.
- **They escape again** — `HIGH standard`, no weapon. Still better than the parent fight's
  best result.
- **Risk:** a Mantis Bomber with an all-Mantis crew. Boarders and missile fire; the bomber
  blueprint is a step up from the fighter you already struggled with.
- There is no way to skip the fight once you arrive — the beacon starts hostile.

## Strategy Notes
- *Opinion:* this is one of the few chains where **losing the first fight is correct**.
  Destroying `DONOR_MANTIS_CHASE1` pays `MED standard` and ends it; letting it run pays a
  guaranteed weapon here. If you can afford to stop shooting at low hull, do.
- Do not accept the surrender reflexively — killing the crew pays a weapon *and* `HIGH
  standard`, strictly better than `HIGH weapon` alone if you have a boarding party.
- Watch the 12-second escape timer. Once it starts you have a hard clock before the payout
  drops to `HIGH standard` with no weapon.

## Related
- [[event-mantis-ship-collectors]] — the parent fight and the only route here
- [[entity-mantis]] — the faction
- [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]] — where the parent
  appears
- [[concept-surrender-offers]] — why `min`/`max` are hull points, not percentages

## Open Questions
- [ ] What escape and surrender probabilities apply when `chance` is omitted entirely.
- [ ] Whether the `RANDOM` weapon on destroyed/deadCrew draws from the same pool as the
      `HIGH weapon` surrender payout.
- [ ] Whether the parent's escape is truly guaranteed (no `chance` there either).

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-mantis]] (per raw/gamedata/events_mantis.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-fandom-mantis-ship-collectors]] (per raw/wiki/mantis-ship-collectors.md)
