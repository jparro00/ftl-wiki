---
id: event-trade-resources
type: event
event_name: TRADER_CIV
sectors: [[[sector-civilian-sector]], [[sector-engi-controlled-sector]], [[sector-engi-homeworlds]], [[sector-federation-space]], [[sector-mantis-controlled-sector]], [[sector-mantis-homeworlds]], [[sector-pirate-controlled-sector]], [[sector-rebel-controlled-sector]], [[sector-rebel-stronghold]], [[sector-rock-controlled-sector]], [[sector-rock-homeworlds]], [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]], [[sector-uncharted-nebula]], [[sector-zoltan-controlled-sector]], [[sector-zoltan-homeworlds]]]
beacon_type: any
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 7
tags: [trading, varies-text, no-risk, resource-swap]
---

# Trade resources — `TRADER_CIV`

## Summary
A pure resource-swap beacon: a trader offers one of four fixed exchanges, converting a
surplus resource into a scarce one. There is no scrap involved, no risk, no fight, and no
blue option — the only decision is whether the offered trade is one you want. It appears in
sixteen sector types, making it the single most widely distributed trading event in the
game.

## Trigger & Where It Appears
- Sectors: sixteen of them — see the frontmatter list. It is not `unique`, so it can
  recur.
- Lists it belongs to ([[source-newevents]], [[source-dlceventsoverwrite]],
  [[source-events-zoltan]]):
  - `ITEMS` — the base item pool
  - `OVERRIDE_ITEMS` — the Advanced Edition replacement for `ITEMS`
  - `ITEM_ZOLTAN` — the Zoltan-sector item pool
- Beacon: no `<distressBeacon/>`, no `<store/>`, no environment tag — an ordinary beacon.
  Fandom additionally records it as able to occur on the **exit** beacon
  ([[source-fandom-trade-resources]]).
- > ⚠️ **CONTRADICTION:** [[sector-federation-space]] coverage.
  > The Fandom `{{Locations}}` template lists fifteen sectors and omits Federation Space
  > ([[source-fandom-trade-resources]]), but `STANDARD_SPACE` allocates
  > `<event name="ITEMS" min="1" max="1"/>` ([[source-sector-data-xml]]) and `TRADER_CIV` is
  > a member of `ITEMS` ([[source-newevents]]) — so it can appear there. Trusting the game
  > files (`high` vs `medium`); a gap in the Fandom location list, not a version
  > difference.
- Allocation of the `ITEMS` / `ITEM_ZOLTAN` buckets per sector lives in
  [[source-sector-data-xml]] — see [[concept-sector-event-allocation]].

## Text
The prose **varies** — the event body is a single `<text load="TRADER_CIV"/>` drawing one
of six entries from `textList TRADER_CIV` ([[source-events-xml]]). Three of the six are
gated on the beacon's backdrop (`planet="PLANET_POPULATED"`), two require no planet
(`planet="NONE"`), and one is unconditional. All six, per [[source-text-events-xml]]:

> You arrive at a quiet spaceport and are immediately hailed by another ship at port with a
> "once in a lifetime deal!" *(populated planet)*

> You jump into a sector filled with civilian activity. Your scan the various advertisement
> channels while waiting for your FTL to charge, and are intrigued by a grey-market
> shipwright. *(populated planet)*

> Your ship is flooded with advertisement transmissions from nearby merchants as soon as
> you arrive at this beacon. You arbitrarily pick one to examine in detail. *(populated
> planet)*

> Despite the barren area, a trader has set up shop at this beacon. He presents his offer.
> *(no planet)*

> The beacon at first glance seems home to a junk yard. Upon closer inspection, it reveals
> itself to be a ramshackle market. One trader has a deal that catches your eye.

> A pawn broker has set up shop at this obscure beacon. He might be offering something
> worth looking at. *(no planet)*

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Trade. | — | One of the four `TRADER_LIST` swaps below. | 1/4 each (assumes uniform selection across list entries, [[concept-event-list-weighting]]) |
| 2 | Ignore. | — | Nothing happens. | 100% |

### `TRADER_LIST` — the four offers

| Offer | You give | You get |
|-------|----------|---------|
| 1 | 1–2 drone parts | 5–10 fuel |
| 2 | 1–2 fuel | 4–5 missiles |
| 3 | 2–3 missiles | 2–3 drone parts |
| 4 | 2–4 missiles | 4–10 fuel |

All four are plain `<item_modify>` blocks with no text of their own
([[source-events-xml]]). Fandom records that **the actual offer is shown before you commit
to the choice** ([[source-fandom-trade-resources]]) — so "Trade." is not a blind pick,
even though the game files give no hint of that.

## Blue Options
None. This event has no `req` on either choice.

## Rewards & Risks
- No scrap, no items, no crew, no combat. Only the four swaps above.
- The only way to lose is to accept a trade you did not want, and per Fandom you see the
  terms first.
- Two of the four offers pay out fuel, which makes this the sector pool's most reliable
  answer to a fuel shortage.

## Version differences
`TRADER_CIV` sits in the base `ITEMS` list ([[source-newevents]]) and in the Advanced
Edition replacement `OVERRIDE_ITEMS` ([[source-dlceventsoverwrite]]), so the event itself
is unchanged across editions — but the **pool it competes in is not**. `ITEMS` marks its
last four entries (`TAVERN_HIRE`, `TRADER_UPGRADES`, `TRADER_UPGRADES_EXCHANGE`,
`HELP_MINERS`) as DLC additions, giving 9 vanilla members against 14 in `OVERRIDE_ITEMS`.
Assuming uniform selection across list entries ([[concept-event-list-weighting]]), that is
a **1/9** share of an item-pool slot in vanilla versus **1/14** in Advanced Edition. Its
event body, texts and `TRADER_LIST` carry no DLC markers at all.

## Strategy Notes
- Missiles are the most commonly over-stocked resource on ships without a missile weapon,
  and offers 3 and 4 both convert them. If you are flying beam/laser-only, this event is
  close to free value. *Opinion, derived from the offer table.*
- Drone parts are the worst thing to spend here (offer 1) unless fuel is genuinely
  critical — drone parts have no other renewable source at a beacon.
- "Ignore." always costs nothing, so there is never a reason to accept a bad offer.

## Related
- [[event-trade-resources-in-nebula]] — the nebula-flavoured sibling
- [[concept-event-list-weighting]] — the assumption behind the fractions above
- [[concept-sector-event-allocation]]

## Open Questions
- [ ] Are the six intro texts weighted equally, given three of them are planet-gated?
- [ ] Are the four `TRADER_LIST` offers filtered by what you can actually pay (e.g. is
      offer 1 suppressed at 0 drone parts)? Nothing in the XML says so.
- [ ] Where in the engine is the "offer shown before choosing" behaviour implemented? Only
      Fandom asserts it.

## Sources
- [[source-events-xml]] (per `raw/gamedata/events.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-newevents]] (per `raw/gamedata/newEvents.xml`)
- [[source-dlceventsoverwrite]] (per `raw/gamedata/dlcEventsOverwrite.xml`)
- [[source-events-zoltan]] (per `raw/gamedata/events_zoltan.xml`)
- [[source-sector-data-xml]] (per `raw/gamedata/sector_data.xml`)
- [[source-fandom-trade-resources]] (per `raw/wiki/trade-resources.md`)
</content>
