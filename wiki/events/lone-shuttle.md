---
id: event-lone-shuttle
type: event
event_name: LONE_SHUTTLE
sectors: []
beacon_type: unknown
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 3
tags: [unreachable, orphan, crew-reward, crew-risk, boarding-risk, fuel, rock, unique, ae-difference]
---

# Lone shuttle — `LONE_SHUTTLE`

## Summary
A silent one-man shuttle drifts toward you. Shoot it down for a 1/3 chance at scrap and
fuel from grateful Rebels who mistake you for one of their own; or wait, and take a 1/4
chance each of free fuel, a free Rock crew member, three-to-four Rebel boarders, or a
suicide bombing that kills a crew member. It is **not reachable in normal play** — no
event list in the extracted game data loads it — and it is one of the few events in the
files whose Advanced Edition version is measurably harsher than its vanilla one.

## Trigger & Where It Appears
- **Orphan / unreachable.** `LONE_SHUTTLE` appears in `raw/gamedata/` exactly once — its
  own definition in `nameEvents.xml`. A grep across every `.xml` finds no `<eventList>`
  entry, no `load=`, and no `sector_data.xml` allocation referencing it
  ([[source-nameevents]]).
- Not a stub: two branches, two full sub-lists, seven distinct outcomes with prose,
  rewards, boarders and a crew death. This is shipped content that nothing calls.
- No Fandom page exists for it, consistent with it never firing in play.
- Sectors, beacon type, and long-range-scanner appearance: **unknown**.
- `unique="true"`. No ship is staged at arrival, so the beacon would start non-hostile.
- **Version:** present in both editions, but **not identical**. See the version note under
  Choices & Outcomes.

## Text
> A small, one man shuttle craft is headed straight for you. Repeated hails is yielding no
> response. You've got a strange feeling about this.

(Written inline in `nameEvents.xml` rather than referenced through `text_events.xml`; the
grammatical slip "Repeated hails is yielding" is in the datafile itself.)

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Shoot it down. It's probably just an abandoned vessel, but better safe than sorry. | — | *"The shuttle has no defenses and breaks apart under your heavy weapon fire."* → "continue" → loads `eventList LONE_SHUTTLE_DESTROY` (3 entries). | 1/3 each |
| 2 | Wait it out for a moment. Maybe someone needs help. *(hidden)* | — | Loads `eventList LONE_SHUTTLE_WAIT` (4 entries). | 1/4 each |

`LONE_SHUTTLE_DESTROY` — 3 entries:

| # | Prose | Effect |
|---|-------|--------|
| 1 | *"Scans show no biological remains in the vessel; it was unmanned... very strange."* | Nothing. |
| 2 | *"In the wreckage, you detect multiple human remains. But you also discover an encrypted rebel communication system. That's one less enemy ship to worry about."* | Nothing mechanical — flavour only. |
| 3 | *"A rebel ship arrives at the beacon. 'Ah! It seems you did our dirty work for us. Nothing worse than Engi refugees…'"* | `ship load="REBEL" hostile="false"` — a **non-hostile** Rebel ship — plus **+25 to +50 scrap** and **+1 to +3 fuel**. |

`LONE_SHUTTLE_WAIT` — 4 entries:

| # | Prose | Effect |
|---|-------|--------|
| 1 | *"…It seems to be unmanned. You take what little fuel it has and continue on."* | **+1 fuel**. |
| 2 | *"…'Are you with the Federation? I'm %add1 and it sure is great to find you…'"* | **`crewMember amount="1" type="rock"`** — a free, named Rock crew member. |
| 3 | *"…By the time you realize it's a rebel vessel, it's too late and they've beamed aboard."* | `boarders min="3" max="4" class="human"` — **3–4 Rebel boarders**, no ship. |
| 4 | *"You detect a transporter signal! The shuttle transported multiple explosive devices to the Kestrel before self-destructing…"* | **Lose a crew member** (`crewMember amount="-1"`, named via `%loss1`), 1 hull damage, **and in Advanced Edition an additional `damage amount="1" system="random"`**. |

**Assuming uniform selection across list entries**, choice 1 is 1/3 for the scrap-and-fuel
payout and 2/3 nothing; choice 2 is 1/4 each of fuel, a Rock crew member, a boarding, and
a crew death. The game files state no percentages; these fractions are derived from list
membership only ([[source-nameevents]]).

**Version difference (rule-10 finding).** Entry 4 of `LONE_SHUTTLE_WAIT` reads:
```
<crewMember amount="-1"/>
<damage amount="1"/>
<damage amount="1" system="random"/>  <!--DLC-->
```
The second `damage` tag is wrapped with an inline `<!--DLC-->` marker, meaning it is
Advanced Edition content. So:
- **Vanilla:** lose a crew member and take 1 hull damage.
- **Advanced Edition:** lose a crew member, take 1 hull damage, **and** 1 damage to a
  random system.

This is the only mechanical difference between the two editions anywhere in the event
([[source-nameevents]]).

## Blue Options
None. No choice in the event carries a `req`.

## Rewards & Risks
- **Best outcomes:** a free Rock crew member (choice 2, 1/4), or 25–50 scrap plus 1–3 fuel
  (choice 1, 1/3).
- **Worst outcome:** the suicide bomb — a dead crew member with no clone clause. Unlike
  `removeCrew`, `crewMember amount="-1"` here carries no `<clone>` element, so nothing in
  the event states a Clone Bay revival.
- **Boarding:** 3–4 human boarders with no enemy ship to disable them.
- **Asymmetry:** shooting first is the *safe* branch — its worst case is "nothing happens"
  — while waiting is where all the upside and all the danger live. That inversion of the
  usual "be patient, be rewarded" pattern is the interesting thing about the event.
- Choice 2 is `hidden="true"`, so a player would get no preview of the four-way split.

## Strategy Notes
- Nothing actionable — the event cannot occur. Recorded so the shipped content is visible
  rather than silently dropped, and so it is not mistaken for a playable beacon.
- If it were live, waiting would be a 1/2 chance of something good (fuel or crew) against
  a 1/4 chance of a boarding and a 1/4 chance of a dead crew member — a genuinely tense
  choice, and better designed than most of the unlisted content in these files. That is
  inference from the outcome table, not something any source states.
- The AE edition of the bad outcome is strictly worse than vanilla; no source explains the
  change.

## Related
- [[event-engi-refugees]] — the other complete-but-unlisted event in `nameEvents.xml`
- [[event-free-augment]] — the third, and the smallest
- [[entity-rock-men]], [[entity-rebels]]
- [[concept-ae-vs-vanilla]] — this event is a clean, small example of an inline
  `<!--DLC-->` edition difference

## Open Questions
- [ ] Whether the event was ever live in a shipped list, in any version.
- [ ] Whether a Clone Bay revives the crew member lost to the suicide bomb — the event
      states no `<clone>` clause either way.
- [ ] Whether the non-hostile `REBEL` ship on `LONE_SHUTTLE_DESTROY` entry 3 can be
      attacked, and what happens if you do.
- [ ] What name `%add1` draws for the Rock crew member.

## Sources
- [[source-nameevents]] (per raw/gamedata/nameEvents.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml — for the `REBEL` ship block)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml — checked for allocation;
  none found)
