---
id: event-escape-pod
type: event
event_name: MANTIS_CREW
sectors: [[[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [mantis, unique, crew-reward-chance, crew-loss-risk, boarding-risk, clone-bay, gamble]
---

# Escape pod — `MANTIS_CREW`

## Summary
A pure gamble with no cost to decline. Jettison the pod and nothing happens; pry it open
and you draw one of three outcomes — a free Mantis crew member, a free Human crew member,
or a Mantis boarder that **kills one of your crew on the spot**. Two of the three
outcomes are good, but the bad one is one of the harshest single-click penalties in the
game. A [[item-clone-bay]] converts the bad outcome from permanent to survivable.

## Trigger & Where It Appears
- Sectors: [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]]
- Drawn from the `NEUTRAL_MANTIS` event list, allocated `min=6 max=7` per Mantis sector
  ([[source-events-xml]], [[source-sector-data-xml]])
- `unique="true"` — once per sector
- No ship at the beacon; long-range scanners show none
  ([[source-fandom-escape-pod]])

## Text
> You detect and retrieve an escape pod floating nearby. You consider returning it to
> space when you learn it's Mantis.

(`event_MANTIS_CREW_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Jettison the pod. | — | *"You send the pod back out the airlock. You're not stupid."* Nothing happens. | 100% |
| 2 | Pry it open. | — | One of three entries from `MANTIS_CREW_LIST` — see below. | unknown |

### Choice 2 — `MANTIS_CREW_LIST`
Three entries, no weights stated in the file, so the split is **unknown**
([[source-events-xml]]):

**(a) The boarder.**
> The Mantis inside is FURIOUS. He cuts the closest person in half with a single swipe.
> Kill it before anyone else is hurt.

Payload: `<boarders min="1" max="1" class="mantis"/>` **and** `<removeCrew>` — you
immediately lose one crew member and then have to fight the Mantis that killed them. The
`removeCrew` element carries `<clone>true</clone>`, so a Clone Bay recovers the lost
crew member:
> The Mantis is shocked to see the crewmember it just slaughtered step out of the Clone Bay.

**(b) The Mantis recruit.**
> The Mantis inside considers you a messenger from the god of mercy and demands to join
> your crew.

Payload: `<crewMember amount="1" class="mantis"/>` — **+1 crew member**. See the
contradiction below on which species you actually get.

**(c) The Human survivor.**
> A man bursts out of the life-pod screaming and claws his way into a corner. A rare
> survivor of Mantis captivity. Once calm, the survivor offers to join your crew for a
> time.

Payload: `<crewMember amount="1" class="human"/>` — **+1 Human crew member**.

> ⚠️ **CONTRADICTION:** does outcome (b) actually give a Mantis?
> - Fandom: *"You receive a Mantis crewmember."* ([[source-fandom-escape-pod]])
> - Game files: the element is `class="mantis"`, but it carries an inline developer
>   comment reading **`NOTE - Doesnt work yet -gives human`**
>   ([[source-events-xml]], per `raw/gamedata/events_mantis.xml` line 453).
>
> These are not straightforwardly rankable: the game file is the higher-reliability
> source for the *declared* class, but the comment is a dev note about a bug and gives no
> date — it may well have been fixed by 1.6.x AE, in which case Fandom is right about
> observed behaviour. The comment survives verbatim in the shipped AE data, which proves
> nothing either way about whether the underlying code still misbehaves. **Unresolved.**
> Confirming this needs an observed run, not another file.

## Blue Options
None as such. The Clone Bay revival is not a blue option — it is a `<clone>` flag on the
`removeCrew` effect and it applies automatically if you have the system, with no extra
choice presented.

## Rewards & Risks
- **Best case:** a free crew member (Mantis or Human) — worth roughly a store crew
  purchase, for free.
- **Worst case:** one crew member dead *and* a Mantis boarder loose on your ship. The crew
  death is scripted; it is not a fight you can win to prevent it.
- With a [[item-clone-bay]], the worst case degrades to "one crew member spends a while
  in the cloning queue plus a boarder fight" — a materially different event.

## Strategy Notes
- *(Opinion.)* Two of three listed outcomes are a free crew member and the file gives no
  weights, so the naive read is favourable — but the losing outcome is asymmetrically
  bad on a 3-crew starting ship, where losing one body can cascade.
- *(Opinion.)* With a Clone Bay online this is close to a free roll and worth taking. With
  a Medbay only, and low crew, jettisoning is defensible.
- Note this event is `unique="true"` per sector — it will not repeat, so there is no way
  to grind it.

## Related
- [[concept-event-tree-grammar]] — the node grammar every event is built from
- [[event-boarders-mantis]] — the other Mantis-sector boarding hazard
- [[event-mantis-capture-commando]] — the other Mantis prisoner-disposal event
- [[item-clone-bay]] — changes the risk profile of choice 2
- [[entity-mantis]]
- [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]]

## Open Questions
- [ ] Weights of the three `MANTIS_CREW_LIST` entries — not stated anywhere in the files.
- [ ] Does outcome (b) give a Mantis or a Human in 1.6.x AE? (see contradiction)
- [ ] Does the Human survivor in (c) actually leave later? The prose says "for a time" but
      no source describes any departure mechanic.

## Sources
- [[source-events-xml]] (per raw/gamedata/events_mantis.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-escape-pod]] (per raw/wiki/escape-pod.md)
