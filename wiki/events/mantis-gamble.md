---
id: event-mantis-gamble
type: event
event_name: MANTIS_GAMBLE
sectors: []
beacon_type: unknown
hostile: false
blue_options: [[[item-engines]]]
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 2
tags: [orphan, unused-content, gamble, scrap, blue-option, engines, mantis]
---

# Mantis gamble — `MANTIS_GAMBLE`

## Summary
A 50-scrap bet on a Mantis arena fight: pick blue or red, win 100 scrap or owe the house.
The losing branch is the interesting one — you can pay up, or with level-4
[[item-engines]] run out on the debt and eat a Mantis fight instead. **It is not reachable
in normal play** — no event list in the extracted game files loads it.

## Trigger & Where It Appears
- **Orphan.** `MANTIS_GAMBLE` appears in no `<eventList>` anywhere in the extracted game
  data; a grep across every `.xml` in `raw/gamedata/` finds it only in its own definition
  in `events_mantis.xml` and in `text_events.xml`
  ([[source-events-xml]], [[source-text-events-xml]]).
- The file's summary header lists it under `Items:` and tags it **`NEW!!`**, alongside
  `MANTIS_CAPTURE_COMMANDO` — the only two events in `events_mantis.xml` so marked, and
  the only two that are unlisted.
- No Fandom page exists for it, consistent with it never firing in play.
- Sectors, beacon type, and long-range-scanner appearance: **unknown**.
- `unique="true"`. No ship is staged, so the beacon starts non-hostile.

## Text
> This node is currently home to a Mantis leisure ship: a place of brothels and combat
> arenas for warriors to release steam. When they scan your inventory they indicate that
> you're eligible to engage in a grand game of chance.

(`event_MANTIS_GAMBLE_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | You don't gamble with crooks. Prepare to jump. | — | Empty `<event/>` — nothing happens, no text. | 100% |
| 2 | Bet 50 scrap on the warrior with blue paint. | — | −50 scrap, then one of two `MANTIS_GAMBLE_BLUE` entries. | unknown (2 entries) |
| 3 | Bet 50 scrap on the warrior with red paint. | — | −50 scrap, then one of two `MANTIS_GAMBLE_RED` entries. | unknown (2 entries) |

Both betting choices deduct the stake immediately via
`<item_modify><item type="scrap" min="-50" max="-50"/></item_modify>` and share the same
intermediate text:

> You watch over the view-screen as two Mantis juveniles are pitched at one another in
> combat.

The file gives **no weights** on either two-entry list, so the win rate is **unknown** —
it is not stated to be 50/50 ([[source-events-xml]]).

### Choice 2 — `MANTIS_GAMBLE_BLUE`
**(win)**
> The one in blue gets pressed into a corner, but he lashes out at the last moment,
> decapitating his opponent. You claim your winnings!

→ `+100 scrap`. Net **+50** on the round.

**(lose)**
> The blue Mantis seems sure to win, scoring numerous hits on his enemy. However, the one
> in red ends the fight with a single key swipe.

Then two choices:

| Sub-choice | Requirement | Outcome |
|---|---|---|
| Pay what you owe. | — | *"You transfer over the scrap that you bet and quit while you still have a ship to sail off in."* No further scrap change — the 50 already deducted is the loss. Net **−50**. |
| **(Adv. Engines)** Dodge the debt and power up the engines. | `req="engines" lvl="4"` | *"You are able to get out of firing range of the cruiser before they can react. However, a smaller ship breaks off from a patrol and moves in to engage."* → `<ship load="MANTIS_FIGHT" hostile="true"/>`. Net **−50** plus a fight. |

### Choice 3 — `MANTIS_GAMBLE_RED`
Mirror image. The win text is the red warrior's:
> The blue Mantis seems sure to win, scoring numerous hits on his enemy. However, the one
> in red ends the fight with a single key swipe. You claim your winnings!

→ `+100 scrap`, net **+50**.

The loss branch is the same two sub-choices — **except** the Adv. Engines escape here
also carries `<item_modify><item type="scrap" min="50" max="50"/></item_modify>`:

> You recall the scrap you prepared to send and are able to get out of the cruiser's
> firing range before they can react. However, a smaller ship breaks off from a patrol and
> moves in to engage.

→ **+50 scrap back** (recovering the stake) *and* a Mantis fight. Net **0 scrap** plus a
fight.

> ⚠️ **INTERNAL INCONSISTENCY (game files, not a cross-source contradiction):** the two
> mirrored branches are not actually mirrored. `MANTIS_GAMBLE_RED_2_c2` refunds 50 scrap
> on the engine escape; `MANTIS_GAMBLE_BLUE_2_c2` does not, despite otherwise identical
> structure ([[source-events-xml]], per `raw/gamedata/events_mantis.xml` lines 252–286).
> Betting **red** is therefore strictly better than betting blue on the losing branch, for
> a player with level-4 engines. There is no Fandom page to check this against. Most
> likely an authoring oversight in never-shipped content, but it is what the file says.

## Blue Options
- **[[item-engines]] at level 4** (`req="engines" lvl="4"`) — appears only inside the
  losing branch of both bets. It converts "pay the 50" into "keep/recover the scrap and
  fight a Mantis ship." Whether that is an upgrade depends entirely on your combat
  strength; on the red bet it is a strict scrap gain, on the blue bet it saves nothing at
  all (see above).

## Rewards & Risks
- Best case: +50 net scrap for one click.
- Worst case (paying): −50 net scrap.
- Worst case (dodging): a `MANTIS_FIGHT` ship you did not need to fight.
- Choice 1 is free and does nothing.
- The event has an entry cost: you must have 50 scrap on hand to bet.

## Strategy Notes
Moot in practice — the event does not fire. Recorded for completeness.

*(Opinion, hypothetical.)* Were it live and the two-entry lists uniform, both bets would be
break-even in scrap terms (+50 half the time, −50 the other half) — a pure coin flip with
no edge, except that level-4 engines plus a red bet turns the losing half into a free
fight for zero scrap loss.

## Related
- [[event-mantis-capture-commando]] — the other unwired `NEW!!` event in the same file
- [[event-mantis-fight]] — the ship the escape branch drops you into
- [[item-engines]]
- [[entity-mantis]]

## Open Questions
- [ ] Was this event ever reachable in a shipped build?
- [ ] Are the two-entry win/lose lists uniform? No weights in the file.
- [ ] Is the blue-vs-red refund asymmetry deliberate?
- [ ] Does the event gate on having 50 scrap, and what happens if you do not?

## Sources
- [[source-events-xml]] (per raw/gamedata/events_mantis.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
