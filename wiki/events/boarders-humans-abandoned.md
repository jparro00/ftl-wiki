---
id: event-boarders-humans-abandoned
type: event
event_name: LANIUS_PIRATE_BOARDERS
sectors: [[[sector-abandoned-sector]]]
beacon_type: any
hostile: true
blue_options: []
chain: []
version: ae
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [lanius, boarding, human, no-choice, hazard, advanced-edition]
---

# Boarders: Humans (Abandoned) — `LANIUS_PIRATE_BOARDERS`

## Summary
The Abandoned Sector's boarding event, and the whole of its boarding pool. Desperate
humans whose engines the Lanius ate decide to take your ship instead. Three to four human
boarders appear immediately — no ship to shoot, no choice, no negotiation.

## Trigger & Where It Appears
- Sector: [[sector-abandoned-sector]] only.
- List: `BOARDERS_LANIUS`, allocated `min=1 max=2` beacons per sector
  ([[source-sector-data-xml]]). The list has exactly **one live member — this event** —
  plus a commented-out `<!--<event load="LANIUS_BOARDERS"/>-->`. So a boarding beacon in
  this sector is **always** this event ([[source-dlcevents-anaerobic]]).
- `unique="false"` — it can repeat, and the XML carries the dev comment
  `<!-- MATT CHANGED TO STOP CRASHES-->` next to that attribute.
- Long-range scanners show **no** ship ([[source-fandom-boarders-humans-abandoned]]).

> **AE-only** — Advanced Edition file and sector. Fandom does not tag this page as AE
> content, but the file it lives in is AE-only.
>
> **Cut content next door:** the disabled `LANIUS_BOARDERS` event is fully written in the
> file — a Lanius wreck whose occupants launch themselves aboard, `boarders min="3" max="3"
> class="anaerobic"` — but its list entry is commented out, so **Lanius boarders never
> happen in this sector**. Only humans board you here.

## Text
> An image of some weak and hungry humans comes onto your screen. "Those metal bastards
> think they can just absorb half of our engines and leave us here to die? I hope you
> understand the need to take your ship by force."

(`event_LANIUS_PIRATE_BOARDERS_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| — | _(none)_ | — | `<boarders breach="false" min="3" max="4" class="human"/>` — **3-4 human boarders** aboard your ship. No hull breach, no enemy ship. | 100% |

There is no enemy vessel and therefore no combat reward: you fight the boarders, and
whatever you get is whatever the engine gives for repelling boarders. No source read here
states a reward.

## Blue Options
None.

## Rewards & Risks
- Risk: 3–4 human boarders is a serious wave for a small crew, and `breach="false"` means
  they arrive in intact rooms, so venting must be set up rather than exploited.
- No ship to destroy means no scrap for winning the fight, only the damage they do on the
  way out.

> ⚠️ **Community claim, unverifiable from the game files:** Fandom states that *"if this
> event happens after a fight against a Lanius ship, the human boarders will have the
> Emergency Respirators augmentation. If this event repeats sequentially, the human
> boarders will still have the augmentation"*
> ([[source-fandom-boarders-humans-abandoned]]). Nothing in
> `dlcEvents_anaerobic.xml` grants the boarders an augment — this would be engine
> behaviour carrying the previous enemy's augment over. Recorded because it matters
> tactically (respirator-equipped boarders ignore vented rooms), but treated as
> `reliability: medium` and unconfirmed.

## Strategy Notes
- The sector guarantees 1–2 of these beacons and this is the only thing that can be on
  them, so entering the Abandoned Sector means planning for at least one 3–4 human
  boarding party.
- If the respirator claim holds, taking this beacon *immediately after* a Lanius fight is
  the worst case — plan on killing them with crew or drones rather than by venting.

## Related
- [[event-lanius-fight-with-friendly-asb-support]] — the other event in this sector with
  disabled boarder content
- [[item-emergency-respirators]] — the augment in the Fandom claim
- [[sector-abandoned-sector]]
- [[event-lanius-boarders]] — the commented-out `LANIUS_BOARDERS` event this one displaced

## Open Questions
- [ ] Confirm or refute the Emergency Respirators carry-over.
- [ ] What the `MATT CHANGED TO STOP CRASHES` comment fixed — presumably `unique="true"`
      caused a crash when the list ran out of members, given this is the list's only entry.

## Sources
- [[source-dlcevents-anaerobic]] (per raw/gamedata/dlcEvents_anaerobic.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-boarders-humans-abandoned]] (per raw/wiki/boarders-humans-abandoned.md)
