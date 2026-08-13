---
id: event-crystalline-men-buried
type: event
event_name: CRYSTAL_HELP_DIG
sectors: [[[sector-hidden-crystal-worlds]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unique, crew-risk, weapon-reward, fuel-reward, fleet-advance, clone-bay-fails]
---

# Crystalline men buried — `CRYSTAL_HELP_DIG`

## Summary
The sector's longest branch and its nastiest trade. A Crystalline ship asks you to lend a
crew member to a dig that will "take days, not hours". Every exit costs you something:
your crew member, a fight, or Rebel fleet progress. Waiting through **two** cycles — and
paying two jumps of doubled pursuit — is the only branch that returns the crew member,
and it also pays out the **Heavy Crystal Mark II**.

## Trigger & Where It Appears
- Sector: [[sector-hidden-crystal-worlds]] only
- Pool: one of **10** entries in the `NEUTRAL_CRYSTAL` event list, allocated exactly **12**
  times per sector (`min=12 max=12`) ([[source-events-xml]], [[source-sector-data-xml]])
- `unique="true"` — at most once per run
- Beacon: shows a **ship** on Long-Range Scanners — `<ship load="CRYSTAL_SHIP_NO_SURRENDER"
  hostile="false"/>` sits at the beacon from the start
  ([[source-events-xml]], [[source-fandom-crystalline-men-buried]])

## Text
> A large Crystalline ship is floating in space here. They hail: "Aliens?! How curious. We
> request your aid. We have men buried on a nearby planet and we must dig them out."

(`event_CRYSTAL_HELP_DIG_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Send a crewmember to help. | — | A crew member goes down; the dig will take days. → the first cycle, below. | 100% |
| 2 | Refuse. | — | *"You rely on machines for so much. Yours is a soft and weak species…"* Nothing happens. | 100% |

### Cycle 1 — after sending a crew member

| # | Choice | Outcome(s) |
|---|--------|-----------|
| 1 | Leave your crew member behind. | `autoReward level="MED"` **fuel** (Fandom: 2–4 fuel and scrap) + `removeCrew` with `<clone>false</clone>` → **crew member permanently lost; a Clone Bay does not help.** |
| 2 | Pull your guy out. | The captain takes it as an insult → `ship hostile="true"` — fight the `CRYSTAL_SHIP_NO_SURRENDER` already present, **default rewards**, no surrender, no escape. |
| 3 | Wait. | `modifyPursuit amount="1"` → **Rebel fleet pursuit doubled for 1 jump**. → cycle 2. |

### Cycle 2 — after waiting once
The same three choices, re-rated:

| # | Choice | Outcome(s) |
|---|--------|-----------|
| 1 | Leave your crew member behind. | `autoReward level="HIGH"` **fuel** (Fandom: 3–6 fuel and scrap) + `removeCrew` `<clone>false</clone>` → **crew member permanently lost, no Clone Bay revival.** |
| 2 | Pull your guy out. | Same fight as above. |
| 3 | Wait. | *"…your knowledge of our customs has most impressed us. Your crewmember is on their way back to you now, along with a token of our respect."* → **crew member returns**, `weapon name="CRYSTAL_HEAVY_2"` (**Heavy Crystal Mark II**), `autoReward level="HIGH"` **augment**, and another `modifyPursuit amount="1"` → pursuit doubled for a second jump. |

## Blue Options
- None. No `req` appears anywhere in this event — notably, having Crystal crew does not
  help.

## Rewards & Risks
- **Best outcome:** Heavy Crystal Mark II + your crew member back, for two jumps of
  doubled Rebel pursuit.
- **Fuel outcomes:** MED fuel (cycle 1) or HIGH fuel (cycle 2) in exchange for a crew
  member you cannot clone back.
- **Fight outcome:** `CRYSTAL_SHIP_NO_SURRENDER` — a Crystal warship with no surrender and
  no escape branch ([[source-events-xml]], per raw/gamedata/events_ships.xml).
- **Clone Bay explicitly does not save the crew member**: `<clone>false</clone>` on both
  removeCrew nodes, which Fandom records as *"(Clone Bay): no effect"*
  ([[source-fandom-crystalline-men-buried]]). This is the inverse of
  [[event-crystalline-cache]] and [[event-crystalline-research-facility]], where
  `<clone>true</clone>` does revive.

> **Data-file quirk (not a contradiction):** the wait-twice outcome carries
> `autoReward level="HIGH">augment` *and* a free `<weapon>`. Fandom explains that the
> `<weapon>` tag blocks "weapon", "drone" and "augment" auto-rewards in the same event
> block, so **the augment is never actually awarded** — you get the Heavy Crystal Mark II
> and nothing else from that reward. The same rule is why "standard" and "stuff" rewards
> never include bonuses alongside a free weapon.
> ([[source-fandom-crystalline-men-buried]]; the raw tags are in [[source-events-xml]].)

## Strategy Notes
- Two jumps of doubled pursuit is a heavy price in a sector you cannot exit early. If the
  fleet is already close, the MED-fuel bail-out at cycle 1 is the cheap exit — but it
  costs a crew member outright. *(Opinion.)*
- "Pull your guy out" is the worst node on paper: you get a no-surrender warship fight
  *and* still have to deal with the sector. *(Opinion.)*
- The clean answer is "Refuse" at the top if you cannot afford either the crew member or
  the pursuit. Refusing has no penalty at all.

## Related
- [[sector-hidden-crystal-worlds]]
- [[entity-crystal-men]]
- [[item-heavy-crystal-mark-ii]] — the payoff weapon
- [[event-crystalline-research-facility]] — the sector's other crew-loss branch (Clone Bay
  *does* work there)
- [[event-crystalline-ship-messaging-about-rebels]] — the sector's other pursuit-modifying
  event
- [[concept-rebel-fleet-advance]]

## Open Questions
- [ ] Whether "pursuit doubled for 1 jump" (Fandom's phrasing) and `modifyPursuit
      amount="1"` (the file) describe exactly the same effect.
- [ ] Confirm in play that the augment really is suppressed by the weapon grant.
- [ ] Whether the crew member sent down can be chosen, or is picked by the game.

## Sources
- [[source-events-xml]] (per raw/gamedata/events_crystal.xml, raw/gamedata/events_ships.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-crystalline-men-buried]] (per raw/wiki/crystalline-men-buried.md)
