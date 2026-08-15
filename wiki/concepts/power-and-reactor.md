---
id: concept-power-and-reactor
type: concept
version: ae
first_seen: 2026-08-14
last_updated: 2026-08-14
sources: 5
related_events: [[[event-improve-reactor-for-supplies]], [[event-trade-scrap-for-upgrades]], [[event-asteroid-mining-colony]], [[event-the-engi-virus]]]
tags: [mechanics, power, reactor, scrap-economy, zoltan, battery, ion]
---

# Power — the reactor, and the two things that aren't it

## Definition & Context

Power is the resource every system competes for, and the reactor is **the only system in the
game with no `<systemBlueprint>` entry at all** ([[item-reactor]]). It exists in
`raw/gamedata/` purely as a target — `<upgrade system="reactor">` in event rewards and
`req="reactor"` in gates. Its cost, its curve and its ceiling appear in no game file, by
construction rather than by oversight.

Everything on this page therefore comes from [[source-fandom-ship]] and
[[source-fandom-template-reactor-power-cost]], at `medium` reliability — the same footing as
[[concept-oxygen-and-suffocation]], and for the same reason.

**Absolute maximum ship power is 37**: 25 reactor + 8 Zoltan + 4 Backup Battery.

## The cost curve

Banded by **the bar you are buying**, not the level you currently hold:

| Bar bought | Cost each | Running total from 0 |
|---|---|---|
| 1–5 | 30 | 150 |
| 6–10 | **20** ← cheapest in the game | 250 |
| 11–15 | 25 | 375 |
| 16–20 | 30 | 525 |
| 21–25 | 35 | 700 |

**The curve is not monotonic.** [[source-fandom-ship]]'s prose claims *"reactor upgrades become
more expensive to upgrade"*; its own transcluded table says bars 6–10 cost **less** than bars
1–5. Since almost every ship starts around 8 bars, most runs never see the expensive opening
band at all — they begin partway through the cheap one.

### Why the bands mean what they mean

The labels are ambiguous in isolation. [[source-fandom-ship]] independently states that a ship
starting with 8 power costs **490 scrap** to max, which discriminates the two readings:

| Reading | Arithmetic | Total |
|---|---|---|
| **Bar being bought** ✓ | 20×2 + 25×5 + 30×5 + 35×5 | **490** |
| Level currently held ✗ | 20×3 + 25×5 + 30×5 + 35×4 | 475 |

Only the first matches. Two Fandom pages last edited three years apart agreeing to the scrap is
better corroboration than either carries alone.

**So: the 12th bar costs 25 scrap.** The 10th costs 20; the 11th is where the price turns.

## The two power sources that aren't the reactor

Both matter mainly because **ion storms halve reactor power and neither of these**
([[source-fandom-ship]]):

| Source | Amount | Ion storm | Ion weapons | Notes |
|---|---|---|---|---|
| Reactor | up to 25 | **halved** | n/a | The scrap sink |
| [[entity-zoltan]] | 1 bar each, to their room | immune | **immune** | Caps at 8 (the crew limit) |
| [[item-backup-battery]] | 2, or 4 upgraded | immune | — | 30s on, 20s cooldown |

- **Zoltan power cannot be stripped by ion weapons**, so a Zoltan in a fully ionised room keeps
  it running — "ion shielding". It works on Medbay and Clone Bay too, which is the difference
  between a crew that heals through an ion lock and one that doesn't.
- **Backup Battery is the one that gets punished by [[item-hacking]]**: a hack forces it
  straight into cooldown *and* drains **2 real reactor bars** for the hack's duration. It is the
  only system whose hack takes power away from elsewhere.

## Implications For Play

- **Bars 6–10 are the bargain of the game**, and most ships start inside that band. Buying up to
  10 costs 20 apiece; the next five cost 25. If scrap is tight, the cheap bars are already
  behind you — which is the opposite of how the game's own description reads.
- **Maxing the reactor is a 490-scrap commitment** from a typical start, comparable to several
  system upgrades or a good weapon. It is rarely the right buy outright, which is why the
  seven events that grant reactor bars ([[item-reactor]]) are worth more than their apparent
  scrap value.
- **Enemies don't play by this economy at all.** They *always* have exactly enough power to run
  their ship ([[source-fandom-ship]]) — there is no under-powered enemy to exploit, except in
  ion storms, where their reactor is halved along with yours. Against a Zoltan ship, that
  asymmetry cuts the other way.
- **Ion storms are a reactor tax, so the counters are the non-reactor sources.** A Zoltan crew
  and a Backup Battery both keep their full value in a storm — see [[concept-nebula-mechanics]].
- **The upgrade menu needs safety, not calm.** It is blocked by **IN DANGER** — a hostile ship
  or intruders — but nebulas and ion storms alone do not block it.

## Where It Applies

- [[item-reactor]] — the system these numbers belong to
- [[item-backup-battery]], [[entity-zoltan]], [[item-zoltan-shield]] — the alternatives
- [[item-hacking]] — the Backup Battery interaction
- [[concept-scrap-economy]] — what 490 scrap competes with
- [[concept-nebula-mechanics]] — ion storms, where reactor power is halved
- [[event-improve-reactor-for-supplies]], [[event-trade-scrap-for-upgrades]],
  [[event-asteroid-mining-colony]], [[event-the-engi-virus]] — reactor bars as event rewards

## Related
- [[concept-oxygen-and-suffocation]] — the other mechanic whose numbers exist only outside the
  game files
- [[item-weapons]], [[item-shields]], [[item-engines]], [[item-drone-control]] — what eats bars

## Open Questions
- [ ] Whether reactor cost varies by **difficulty**. Nothing in either source says so, and both
      describe a single table — but neither states that it is difficulty-independent either.
- [ ] Whether ion-storm halving **rounds up or down**, and how it interacts with a reactor
      already partly allocated.
- [ ] Whether the 8-Zoltan figure in the "37 maximum" is achievable in practice, or a
      theoretical cap assuming an all-Zoltan crew of 8 each in a distinct powered room.
- [ ] The Battery Charger augment (`BATTERY_BOOSTER`, *"Backup Battery's lock time is halved"*,
      [[source-text-blueprints]]) has no page and is unmentioned by [[source-fandom-ship]].
- [ ] Whether starting reactor power per playable ship is recorded anywhere — "about 8" is an
      average, and the per-ship values would come from the ship blueprints.

## Sources
- [[source-fandom-ship]] (per raw/wiki/ship.md)
- [[source-fandom-template-reactor-power-cost]] (per raw/wiki/template-reactor-power-cost.md)
- [[source-dlcblueprints]] (per raw/gamedata/dlcBlueprints.xml) — the Backup Battery blueprint
- [[source-text-blueprints]] (per raw/gamedata/text_blueprints.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml) — the `max_lvl="24"` gates
