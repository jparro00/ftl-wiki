---
id: source-fandom-ship
type: source
source_kind: wiki
raw: raw/wiki/ship.md
game_version: ae
date: 2026-06-21
ingested: 2026-08-14
reliability: medium
tags: [ship, power, reactor, zoltan, battery, hull, mechanics]
---

# Fandom — "Ship"

## Summary
The community wiki's top-level ship page, retrieved at revision 74911 (edited 2026-06-21) —
the most recently edited source in this repo. Four sections: playable ships, enemy ships, hull,
and **power**. The power section is why it was fetched: it is the only source we hold that
states the reactor's cost curve, its ceiling, or how Zoltan and Backup Battery power differ from
reactor power.

Reached by redirect — `wiki/Reactor` is a `#REDIRECT [[Ship#Reactor]]` and has been since 2014,
so there is no standalone Reactor page to capture.

## Key Takeaways

- **The reactor caps at 25 bars.** Absolute maximum ship power is **37** = 25 reactor + 8 Zoltan
  (one per crew member, at the 8-crew cap) + 4 Backup Battery.
- **Reactor upgrade costs are banded**, in the template captured as
  [[source-fandom-template-reactor-power-cost]]. The prose here supplies the cross-check that
  makes the table unambiguous — see Contradictions.
- **"Reactor upgrades become more expensive to upgrade"** — which is *false as stated*: bars
  6–10 cost 20, cheaper than bars 1–5 at 30. The curve dips before it climbs.
- Player ships average **about 8** starting reactor power; upgrading such a ship to 25 costs
  **490 scrap**.
- **Enemy ships always have exactly enough reactor power to fully power their ship** — they are
  not modelled with a scrap economy. **In ion storms that power is halved.**
- **Zoltan power: exactly one bar per Zoltan**, to the room they occupy. It is **not halved by
  ion storms** and **cannot be removed by ion weapons** — the basis of "ion shielding". It can
  power a Medbay or Clone Bay through complete ionisation.
- **Backup Battery: 2 bars (4 upgraded) for 30 seconds, then 20 seconds of cooldown.** Not
  halved in ion storms. If *hacked*, it immediately enters cooldown **and drains 2 real reactor
  bars** for the duration of the hack.
- **Hull: every playable ship starts at exactly 30**, the maximum. Enemy hull varies by ship
  type, sector and difficulty.
- **Rock Plating's 15%** *"cannot prevent damage from fires and sabotage, solar flares, or
  events"* — an exclusion list absent from the augment's own game-file description.
- Hull Beam, Hull Laser I/II and Hull Missiles deal **double damage to systemless rooms**;
  bombs cannot damage hull at all, only rooms and systems.
- The upgrade menu is unavailable while **IN DANGER**, but nebulas and ion storms alone do not
  block it — only an actual hostile ship or intruders do.

## Events Covered
None directly — a mechanics page. It references the ship-unlock quest category, already mapped
across [[chain-rock-cruiser-unlock]] and siblings.

## Other Pages Touched
- [[concept-power-and-reactor]] — the page this source primarily created
- [[item-reactor]], [[item-backup-battery]], [[item-rock-plating]]
- [[entity-zoltan]], [[item-zoltan-shield]]
- [[concept-nebula-mechanics]] — the ion-storm power rules

## Reliability Notes
`medium`. Recent (2026-06-21) and internally consistent — its 490-scrap figure arithmetically
reproduces the transcluded cost table exactly, which is a strong self-check.

`game_version: ae` — it documents Lanius and Crystal cruisers, Backup Battery, Hacking and
Clone Bay throughout, all AE content.

Its weakest content is the prose generalisation about costs rising monotonically, which its own
table contradicts.

## Contradictions Flagged

> ⚠️ **Internal, and the page's own table wins.** The prose says *"Reactor upgrades become more
> expensive to upgrade."* The transcluded table
> ([[source-fandom-template-reactor-power-cost]]) gives 30 / 20 / 25 / 30 / 35 across the five
> bands — bars 6–10 are the **cheapest in the game**, below the opening 30. The curve is
> non-monotonic. Trust the table; the prose is a loose summary.

**Ambiguity resolved rather than flagged:** the cost table's band labels ("11–15") could denote
either the bar being bought or the level already held. This page's *"fully upgrade a ship with 8
power, it costs 490"* settles it — only the bar-being-bought reading sums to 490 (the other
gives 475). Worked through on [[concept-power-and-reactor]].

**Apparent conflict with the game files, which resolves cleanly:** `newEvents.xml` gates reactor
rewards with `req="reactor" max_lvl="24"` ([[source-newevents]]), while this page states a
25-bar ceiling. Not a contradiction — `max_lvl="24"` is an *inverse* gate hiding the "take a
reactor bar" choice from ships at 24 or more, which is exactly what a 25 cap requires. Recorded
on [[item-reactor]], whose open question this closes.

## Links
- Source URL: https://ftl.fandom.com/wiki/Ship (revision 74911)
- Redirect origin: https://ftl.fandom.com/wiki/Reactor → `Ship#Reactor`
- [[source-fandom-template-reactor-power-cost]] — the transcluded cost table
- [[source-blueprints]], [[source-dlcblueprints]], [[source-newevents]]
