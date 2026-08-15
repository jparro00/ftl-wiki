---
id: source-fandom-oxygen
type: source
source_kind: wiki
raw: raw/wiki/oxygen.md
game_version: ae
date: 2025-12-09
ingested: 2026-08-14
reliability: medium
tags: [oxygen, suffocation, venting, breach, lanius, crystal, mechanics]
---

# Fandom — "Oxygen"

## Summary
The community wiki's system page for Oxygen, retrieved at revision 74853 (edited 2025-12-09) —
the first source in this repo to carry **numbers for oxygen and suffocation**. It is the only
source we hold that states the crew suffocation damage rate. Unlike the event pages in
`raw/wiki/`, this one reads as current AE-era content: it discusses Emergency Respirators,
Lanius and Hacking-3.

## Key Takeaways

- **Crew suffocation: 6.4 HP per second**, beginning at **≤5% O₂ in the room**. This is the
  headline number and the reason the page was fetched.
- **O₂ drain with the system unpowered: 1.2%/sec in every room.** A functioning level-1 Oxygen
  system refills at the same 1.2%/sec — the two exactly cancel, which is why level 1 holds a
  sealed ship steady and nothing more.
- **Refill table: 1.2 / 4.8 / 8.4 %/sec** for levels 1/2/3, with upgrade costs 25 and 50 scrap.
  Those costs match `blueprints.xml` exactly ([[source-blueprints]]) — independent corroboration
  that this page describes the same build we hold.
- **The in-game UI is wrong about its own multipliers.** The page states Oxygen-2 refills **4×**
  and Oxygen-3 **7×**, "the refill multipliers … in the ship upgrade menu are incorrect".
  [[source-xftl-oxygen-mechanics]] independently names the UI's figures as 1/3/6 and confirms the
  true values are 1/4/7.
- **Fires consume 0.96%/sec each**, in their own room only. Fires begin to die below **10% O₂**.
- **A breach and a Lanius drain at the same rate** — stated here without a figure, quantified as
  8%/sec by [[source-xftl-oxygen-mechanics]].
- **Suffocation modifiers**: [[item-emergency-respirators]] halves it (and works while boarding
  an enemy ship); Crystal crew take half; the two stack to **25%**; Lanius are exempt entirely.
- **A powered level-1 [[item-medbay]] fully negates suffocation damage** in an airless Medbay;
  level 2 slowly heals through it. This makes the Medbay room the one place venting cannot kill.
- **AI pathing**: boarders and mind-controlled crew retreat from low-O₂ rooms toward rooms with
  **≥10% O₂** — the mechanic that makes vent-the-boarders work, and that they can escape.
- **During an FTL jump** the Oxygen system's status is ignored and rooms do not equalise, but
  airlocks, breaches and fires still drain — **and crew still take suffocation damage as usual**.
- The **"O2 LOW!"** warning fires when *ship-total* O₂ drops below 25%, which is not the same
  threshold as the per-room 5% at which crew actually start dying.

## Events Covered
None — this is a systems page, not an event page. It names
[[event-terraforming-scan]] and [[event-trade-scrap-for-upgrades]] as the two events that
upgrade Oxygen, both already mapped.

## Other Pages Touched
- [[concept-oxygen-and-suffocation]] — the page this source primarily created
- [[item-oxygen-system]], [[item-emergency-respirators]], [[item-lanius-crew]],
  [[item-medbay]], [[item-doors]], [[item-hacking]]
- [[entity-crystal-men]], [[entity-lanius]]

## Reliability Notes
`medium` per the repo convention, but this page is **better evidenced than a typical Fandom
page**: it cites a reverse-engineering project for its mechanics, its upgrade costs check out
against the game files, and its multiplier claims are independently confirmed. The one figure
that carries no corroboration is, unfortunately, the headline one — see below.

The page carries its own visible `@to-do` HTML comments (unquantified drain speed, untested
mind-control interaction, untested O₂-equalisation cut-off), which is a mark of honesty rather
than sloppiness: the authors flag what they have not measured.

## Contradictions Flagged

> ⚠️ **CONTRADICTION:** airlock drain speed. Fandom: an open airlock *"instantly drains the O₂
> in the room it is opened in"*. [[source-xftl-oxygen-mechanics]], reading the engine: **16%/sec
> per open airlock door**, with adjacent rooms scaled by `0.75^distance`. 16%/sec is fast but
> emphatically not instant — a full room takes over six seconds. Trust xftl; Fandom's "instantly"
> is loose prose describing a felt experience, and the same page's own tactical advice (open
> *all* the airlocks to vent faster) only makes sense if venting has a rate.

**Not a contradiction — a documented engine/UI mismatch:** the 1/3/6 multipliers shown in the
ship upgrade menu versus the real 1/4/7. Both sources agree the *game itself* displays the wrong
number. Recorded on [[item-oxygen-system]].

**Unconfirmed, and flagged as such:** the 6.4 HP/sec suffocation rate appears **only here**.
[[source-xftl-oxygen-mechanics]] documents oxygen drain, refill and redistribution but never
touches crew damage, so it cannot corroborate the one figure this ingest was run to obtain.

## Links
- Source URL: https://ftl.fandom.com/wiki/Oxygen (revision 74853)
- The page's own See-also cites the xftl doc now held as [[source-xftl-oxygen-mechanics]]
  and a Pastebin on fire mechanics (https://pastebin.com/iP6EnKm4) — **not** retrieved
- [[source-blueprints]], [[source-text-blueprints]], [[source-text-tooltips]]
