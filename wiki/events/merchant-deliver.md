---
id: event-merchant-deliver
type: event
event_name: MERCHANT_DELIVER
sectors: []
beacon_type: quest
hostile: false
blue_options: [[[item-mind-control]], [[item-weapons]], [[item-anti-personnel-drone]]]
chain: [[[chain-merchant-s-request]]]
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 5
tags: [quest-destination, drone-parts, trading, blue-option, ae-vs-vanilla]
---

# Merchant's delivery — `MERCHANT_DELIVER`

## Summary
The delivery destination of [[event-merchant-s-request]]. You arrive carrying the 5 drone
parts the merchant gave you and find either a **silent research station** (a horror
sub-tree that has nothing to do with the delivery) or the **station that ordered the
parts, trying to stiff you on the price**. Three separate blue options exist to force a
better price, and one of them is the single best payout in the quest line.

## Trigger & Where It Appears
- **Not in any sector event list.** It is reached only as a quest marker:
  `<quest event="MERCHANT_DELIVER"/>` fires from the delivery branch of
  `MERCHANT_REQUEST_LIST` ([[source-events-xml]]). That is its sole reference in the game
  files.
- So the sectors it can appear in are whichever sector [[event-merchant-s-request]] placed
  its marker in — the frontmatter `sectors` list is left empty deliberately.
- [[source-fandom-merchant-s-request]] documents it as the "Merchant's Delivery" section of
  that page and marks it `LRSmap=noship`.

## Text
> You arrive at the location given to you by the merchant. You are supposed to deliver
> drone parts to a station here.

(`event_MERCHANT_DELIVER_text`, per [[source-text-events-xml]])

A single unlabelled `continue` choice loads `eventList MERCHANT_DELIVER_LIST`.

## Choices & Outcomes

### `eventList MERCHANT_DELIVER_LIST` (2 entries)
Assuming uniform selection across `eventList` entries ([[concept-event-list-weighting]]),
each scenario is **1/2**.

**Entry 1 — the station doesn't respond**
> You find the small research station and discover that it's putting out a distress signal.
> Strangely, there is no response to your hails.

| # | Choice | Requirement | Outcome |
|---|--------|-------------|---------|
| 1 | Dock with the station and investigate. | — | Loads `eventList STATION_SICK_LIST` — the plague-station tree: `MED droneparts`; or a free crew member that may be followed by 3–4 human boarders; or a traitor who costs you a crew member. Medbay level 2/3 blue options gate the safe outcomes. Documented at [[event-research-station-with-no-response]]. |
| 2 | Leave it alone. | — | Nothing happens. |
| 3 | **(Anti-Personnel Drone)** Use an Anti-Personnel Drone to investigate. | `req="BATTLE"` | Loads `eventList STATION_SICK_DRONE_LIST` — costs 1 drone part per entry. |

This branch **does not deliver the cargo and pays nothing for it** — it is the
[[event-research-station-with-no-response]] encounter reused wholesale ([[source-events-xml]]).
[[source-fandom-merchant-s-request]] notes the standalone version has a slightly different
intro and an extra Lifeform Scanner blue option that this copy lacks.

**Entry 2 — the station responds**
> You find the station and they respond to your hails immediately, saying, "It took you
> long enough! We have practically no use for these now... I refuse to pay full price, take
> this and leave the cargo in our holds."

| # | Choice | Requirement | Outcome | Odds |
|---|--------|-------------|---------|------|
| 1 | Accept the paltry payment. | — | *"You drop the parts off and take your pay."* → **+20 to +30 scrap**, **−5 drone parts**. | 100% |
| 2 | Refuse and keep the drone parts. | — | Loads `eventList MERCHANT_DELIVER_BLUFF_LIST` (**AE only**, see below). | see below |
| 3 | **(Mind Control)** Convince him that he's being 'unfair'. | `req="mind"` | *"I'm being unfair. You did the job and the parts are here safe and sound. Here is the agreed upon amount."* → then **Accept**: **+40 to +55 scrap**, **−5 drone parts**; or **Leave**: nothing. | 100% |
| 4 | **(Weapons)** Remain silent but power up your weapons. | `req="weapons" lvl="6"` | *"You make a good point… we'll even tip you for the inconvenience…"* → **+55 to +70 scrap**, **+2 to +5 fuel**, **−5 drone parts**. | 100% |

Choices 2–4 are `hidden="true"`; choice 1 is not, so its trade is previewed.
[[source-fandom-merchant-s-request]] records the same, and adds that the Weapons option is
the one case where the trade is *not* shown in advance.

### `eventList MERCHANT_DELIVER_BLUFF_LIST` — Advanced Edition only
The list carries a `<!--DLC!-->` marker in `events.xml` ([[source-events-xml]]), so it is
AE content. 2 entries, **1/2** each under uniform selection:

| Entry | Outcome |
|---|---|
| 1 | *"Fine, I was bluffing. I'll pay the full price."* → **Accept**: **+40 to +55 scrap**, **−5 drone parts**; or **Leave**: nothing. |
| 2 | *"The merchant disconnects in a huff."* → nothing; you keep the 5 drone parts. |

**Version note (rule 10).** The choice that loads this list is *not* itself DLC-marked, but
its target is. In vanilla the "Refuse and keep the drone parts" branch therefore has no
defined target — the bluff/huff gamble is AE-only content. Everything else on this page is
common to both editions, which is why `version: both`.

## Blue Options
- **[[item-mind-control]]** (`req="mind"`) — turns the lowball 20–30 into a guaranteed
  40–55 with no gamble. Strictly better than choice 2 even in AE, where choice 2's good
  half pays the same amount only half the time.
- **[[item-weapons]] level 6** (`req="weapons" lvl="6"`) — the best outcome in the quest
  line: 55–70 scrap **and** 2–5 fuel. The gate is the *system level*, not owning weapons.
- **[[item-anti-personnel-drone]]** (`req="BATTLE"`) — only on entry 1, and only routes you
  into a different [[event-research-station-with-no-response]] sub-list; it does not affect the delivery.

## Rewards & Risks
- Best case: 55–70 scrap + 2–5 fuel (Weapons 6).
- Median case: 20–30 scrap for parts the merchant handed you for free.
- Worst case: entry 1 rolls and the delivery never happens at all — you still hold the
  cargo, and the station tree can cost you a crew member or hand you boarders.
- Every payout consumes exactly **5 drone parts**. If you spent them, the paying choices
  cannot be satisfied.

## Strategy Notes
- Take Weapons 6 > Mind Control > (AE) refuse-and-bluff > accept. The bluff is a coin flip
  between 40–55 and nothing, against a guaranteed 20–30, so it is close to break-even and
  only worth it if you value keeping the 5 parts. *(Comparison derived from the tables
  above; no source ranks them.)*
- Entry 1 is the reason not to treat this marker as free money: half the time the beacon
  is the plague station instead.

## Related
- [[chain-merchant-s-request]] — the full quest line this belongs to
- [[event-merchant-s-request]] — the quest start that places this marker
- [[event-research-station-with-no-response]] — the sub-tree entry 1 loads
- [[event-merchant-investigate]] — the other errand from the same quest start
- [[item-mind-control]], [[item-weapons]], [[item-anti-personnel-drone]]

## Open Questions
- [ ] In vanilla, what actually happens when "Refuse and keep the drone parts" loads a
      list that does not exist?
- [ ] Confirm `eventList` selection is uniform — both 1/2 splits depend on it.
- [ ] Does the game block the paying choices if you are short of 5 drone parts, or does it
      let you go negative?

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-newevents]] (per raw/gamedata/newEvents.xml)
- [[source-dlceventsoverwrite]] (per raw/gamedata/dlcEventsOverwrite.xml)
- [[source-fandom-merchant-s-request]] (per raw/wiki/merchant-s-request.md)
