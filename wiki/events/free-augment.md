---
id: event-free-augment
type: event
event_name: FREE_AUGMENT
sectors: []
beacon_type: unknown
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 2
tags: [unreachable, orphan, augment-reward, no-choice]
---

# Free augment — `FREE_AUGMENT`

## Summary
One line of text and a free random augment, with no choices and no risk. It is **not
reachable in normal play** — no event list in the extracted game data loads it — and it is
the smallest piece of complete-but-unlisted content in `nameEvents.xml`. Not to be
confused with [[event-zoltan-free-augment]] (`ZOLTAN_FREE_AUGMENT`), which is a different
event that does fire.

## Trigger & Where It Appears
- **Orphan / unreachable.** `FREE_AUGMENT` appears in `raw/gamedata/` exactly once — its
  own definition in `nameEvents.xml`. A grep across every `.xml` finds no `<eventList>`
  entry, no `load=`, and no `sector_data.xml` allocation referencing it
  ([[source-nameevents]]).
- It is not a test stub: the prose is finished, in-character, and uses the `%crew`
  name-substitution machinery the rest of the file exists to exercise. It is simply a
  complete event that nothing calls.
- No `unique` attribute, no ship, no environment, no choices.
- No Fandom page exists for it. The Fandom page titled *Zoltan free augment* documents
  `ZOLTAN_FREE_AUGMENT`, a different id — do not join the two.
- Sectors, beacon type, and long-range-scanner appearance: **unknown**.
- **Version:** `nameEvents.xml` is a base-game file that Advanced Edition patched in place
  — other events in it carry inline `<!--DLC-->` markers on individual tags. This event
  carries none, so its definition is the same in both editions as far as the extracted
  files show, and it is equally unreachable in both.

## Text
> Wow! A ship enhancement is just floating in space. %crew seems especially excited about
> this one.

`%crew` is a runtime substitution that inserts one of your crew members' names, so the
line **varies** per run. The prose is written inline in `nameEvents.xml` rather than
referenced through `text_events.xml` ([[source-nameevents]]).

## Choices & Outcomes

The event has **no `<choice>` elements at all** — it resolves immediately.

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | *(none — the event has no choices)* | — | `augment name="RANDOM"` — you receive a random augment. | 100% |

## Blue Options
None.

## Rewards & Risks
- **Reward:** one random augment, free, unconditional. Which pool `RANDOM` draws from is
  not stated in the event.
- **Risks:** none. No damage, no fight, no boarders, no cost.
- What happens when your augment slots are already full is not stated here; the game has a
  separate `AUGMENT_FULL` system message for that case, which is UI text rather than an
  encounter.

## Strategy Notes
- Nothing actionable — the event cannot occur. Recorded so the shipped content is visible
  rather than silently dropped, and so it is not mistaken for a playable beacon or joined
  to the wrong Fandom page.
- Its shape — pure reward, no choice — is what the live "free item" events in
  `newEvents.xml`'s `ITEMS` list look like, so it reads as an early draft of that family
  rather than as debug scaffolding. That is inference from the file's structure, not
  something any source states.

## Related
- [[event-zoltan-free-augment]] — `ZOLTAN_FREE_AUGMENT`, the reachable event with a
  confusingly similar name; **different id, different event**
- [[event-engi-refugees]], [[event-lone-shuttle]] — the other complete-but-unlisted events
  in `nameEvents.xml`
- [[event-asteroid-mining-colony]] — a live event that also hands out `augment
  name="RANDOM"`

## Open Questions
- [ ] Whether the event was ever live in a shipped list, in any version.
- [ ] Which blueprint list `augment name="RANDOM"` draws from, and whether it can roll a
      duplicate of one you already own.
- [ ] What the game does with the award if every augment slot is full.

## Sources
- [[source-nameevents]] (per raw/gamedata/nameEvents.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml — checked for allocation;
  none found)
