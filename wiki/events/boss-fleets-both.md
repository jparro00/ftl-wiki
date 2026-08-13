---
id: event-boss-fleets-both
type: event
event_name: BOSS_FLEETS_BOTH
sectors: []
beacon_type: empty
hostile: false
blue_options: []
chain: [[[chain-the-flagship]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [empty, no-choice, endgame, last-stand, fleet, orphan, disputed-reachability]
---

# Two fleets in battle (Last Stand) — `BOSS_FLEETS_BOTH`

## Summary
The peaceful half of the battle-background pair in [[sector-the-last-stand]]: you arrive
beside a raging fleet engagement and nobody shoots at you. Flavour text and a battle skybox,
nothing else. Its reachability is **genuinely disputed by the game files themselves** — no
event list names it, but `events_boss.xml`'s own summary header lists it as a main event that
lists call.

## Trigger & Where It Appears
- Sector: [[sector-the-last-stand]] (`FINAL`) if it fires at all.
- `<fleet>battle</fleet>` — the only mechanical effect, putting both fleets in the background
  art. The XML comment reads *"nodes that have ships fighting - unique background"*.
- **The reachability contradiction:**

> ⚠️ **CONTRADICTION:** whether this event can fire.
> - **Against:** no `<eventList>` contains it. The `FINAL` sector draws on exactly two
>   pools — `BOSS_HOSTILE` (three copies of `BOSS_SCOUT`) and `BOSS_NEUTRAL`
>   (`BOSS_SCOUT_RESCUE`, `BOSS_FLEETS_BOTH_FIGHT`, `BOSS_FLEETS_FED`,
>   `SQUAT_REFUEL_STATION`, `REBEL`) — plus fixed `STORE` and `BOSS_REPAIR_STATION`
>   allocations. `BOSS_FLEETS_BOTH` is in none of them, and no `load=` reference exists
>   anywhere in `raw/gamedata/` ([[source-events-boss]], [[source-sector-data-xml]]).
> - **For:** the summary header at the top of `events_boss.xml` — the developers' own index
>   of *"all main events to be called by lists"* — lists it under **Empty:** alongside
>   `BOSS_FLEETS_FED`, annotated *"(sometimes in !!! events)"*. That is an explicit claim
>   that it appears at the danger-marked beacons ([[source-events-boss]]).
>
> **Not tagged `unreachable`.** Per [[concept-sector-event-allocation]], absence from the
> lists is not by itself proof — the engine calls some events by name, and this file's own
> documentation says this is one of them. Both readings are recorded; neither is settled
> here. `sectors: []` reflects the missing allocation, not a claim that it never fires.

- Beacon: empty. No ship, no `<choice>`, no reward.
- **Version:** `both`. `events_boss.xml` is a base file with no DLC markers.
- Fandom has no page for this id. Its *Rebel fight among Federation and Rebel fleets* page
  covers the sibling `BOSS_FLEETS_BOTH_FIGHT` ([[source-fandom-rebel-fight-among-federation-and-rebel-fleets]]).

## Text
`<text load="BOSS_FLEETS_BOTH"/>` — a 12-entry text list built from **six** distinct strings,
each listed twice, so **1/6 each** assuming uniform selection across list entries
([[concept-event-list-weighting]], [[source-events-boss]], [[source-text-events-xml]]):

> Sensors indicate evidence of a huge battle nearby, but the immediate vicinity seems quiet.
> You try to lay low and keep out of the fighting.

> You arrive to find two fleets crashing against each other. Sensors are tracking the extent
> of the carnage. You quietly wait for the FTL drive to charge, knowing that the only way you
> can help is by completing your mission.

> A battle rages in the distance. Sensors suggest the presence of many vulnerable escape
> pods, but you know you cannot stop to help. The mission is paramount.

> A battle rages on in the distance. As much as you would like to help in the fight, you know
> the importance of your mission.

> You don't need advanced Sensors to tell there is a battle going on. You look out of the
> window quietly, waiting to jump. There's no way you can help in this fight.

> Two fleets are volleying shots at each other. Luckily, no one seems interested in your ship.
> You prepare to make another jump.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none — the event has no `<choice>` elements and no `<ship>`)* | — | Nothing happens. | 100% |

## Blue Options
None.

## Rewards & Risks
Nothing gained, nothing lost. Structurally identical to [[event-empty-beacon-last-stand]]
(`BOSS_FLEETS_FED`) — the two are the "safe draw" pair for the Last Stand, differing only in
whose fleet the background shows.

## Strategy Notes
- If it fires, it is a free beacon: repair crew, vent fires, jump on. The prose repeatedly
  tells you not to intervene, and there is no option to.
- The near-identical `BOSS_FLEETS_BOTH_FIGHT` — same battle skybox, but with a
  `BOSS_FLEETS_REBEL` hull attached — **is** in `BOSS_NEUTRAL`. Do not read a battle
  background as safety: 1 of the 5 `BOSS_NEUTRAL` entries is the fighting version.

## Related
- [[event-empty-beacon-last-stand]] (`BOSS_FLEETS_FED`) — the live empty-beacon twin
- [[event-rebel-fight-among-federation-and-rebel-fleets]] (`BOSS_FLEETS_BOTH_FIGHT`) — the
  hostile version of this beacon, which *is* in `BOSS_NEUTRAL`
- [[event-rebel-fight-among-rebel-fleet]] (`BOSS_FLEETS_REBEL`) — the hull that version stages
- [[sector-the-last-stand]], [[chain-the-flagship]], [[entity-rebels]], [[entity-federation]]
- [[concept-sector-event-allocation]] — why this is not tagged `unreachable`
- [[concept-event-list-weighting]] — basis for the 1/6 figures

## Open Questions
- [ ] Does the engine place `BOSS_FLEETS_BOTH` directly at "!!!" beacons, as the file's
      summary header claims? This is the deciding question for the contradiction above.
- [ ] If it does fire, at what rate relative to `BOSS_FLEETS_BOTH_FIGHT`?
- [ ] What `<fleet>battle</fleet>` changes beyond background art.

## Sources
- [[source-events-boss]] (per raw/gamedata/events_boss.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-rebel-fight-among-federation-and-rebel-fleets]] (per raw/wiki/rebel-fight-among-federation-and-rebel-fleets.md)
