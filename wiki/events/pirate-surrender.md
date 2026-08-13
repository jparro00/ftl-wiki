---
id: event-pirate-surrender
type: event
event_name: PIRATE_SURRENDER
sectors: []
beacon_type: hostile
hostile: true
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [surrender, aftermath, orphan, pirates, rebels, shared-sub-event]
---

# Pirate surrender — `PIRATE_SURRENDER`

## Summary
The most widely reused surrender offer in the game. Six different enemy hulls — including
the generic `PIRATE` and the generic `REBEL` — hand their low-hull surrender prompt to
this one event. Accepting ends the fight for a single `RANDOM`-level `stuff` payout;
refusing costs nothing and the fight continues.

## Trigger & Where It Appears
- **Not in any sector event list.** It is reached only from `<surrender load=...>` blocks
  in ship definitions, so it inherits the sectors of whatever hull invoked it — which, for
  `PIRATE` and `REBEL`, is effectively the whole game.
- Ships that load it ([[source-events-ships]], [[source-dlcevents]]):

| Ship | `<surrender>` declaration | Surrender chance |
|---|---|---|
| `PIRATE` | `chance="0.5" min="3" max="4"` | 50% |
| `PIRATE_FUEL` | `chance="0.5" min="3" max="4"` | 50% |
| `REBEL` | `chance="0.5" min="2" max="3"` | 50% |
| `ZOLTAN_PIRATE` | `chance="0.5" min="3" max="4"` | 50% |
| `JELLY_PIRATE_WITHBOARDERS` | `min="0" max="5"` — **no `chance` attribute** | unknown |
| `NEWSHIP2` (`dlcEvents.xml`) | `chance="0.5" min="3" max="4"` | dev stub, not live |

- Per [[concept-surrender-offers]], `chance` is the probability the ship **keeps
  fighting**; the surrender chance is `1 − chance`. `min`/`max` are hull points, not
  percentages.
- `JELLY_PIRATE_WITHBOARDERS` omits `chance` entirely. No source here states the engine's
  default, so its surrender probability is `unknown` — see Open Questions.
- No Fandom page joins this event directly; the community wiki folds it into each parent
  fight as a "ship surrenders" template.

## Text
`<text load="PIRATE_SURRENDER_TEXT"/>` — a **23-entry** text list drawing on 14 distinct
strings ([[source-events-xml]], [[source-text-events-xml]]). The list is written as an
11-entry block followed by a 12-entry block explicitly commented *"Duplicates below, just
to make sure"*, so nine of the strings appear twice:

| Weight | Sample |
|---|---|
| 2/23 each — strings 1, 2, 3, 6, 7, 8, 9, 10, 11 | *"Alright, you win! Here's some equipment from our stores, leave us alone!"* · *The ship repeatedly hails you. It looks like they want to surrender.* · *They offer you some of their goods if you don't destroy their ship.* |
| 1/23 each — strings 4, 5, 12, 13, 14 | *They send you a message: "Your ship is surprisingly well equipped! Please take this and let us live."* · *"The day is yours! Show us your honor by allowing us to leave with our lives."* |

Weights assume uniform selection across list entries ([[concept-event-list-weighting]]).
Strings 4/5 and 12/13 are near-identical rewordings of each other, which is presumably why
the second block substituted them.

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Accept their offer. | — | `<ship hostile="false"/>` — the fight ends — plus `<autoReward level="RANDOM">stuff</autoReward>`. | 100% |
| 2 | We will not accept surrender! | — | Empty `<event/>`; the fight continues. | 100% |

`RANDOM` is the game's own reward level here, not `LOW`/`MED`/`HIGH` — the payout tier is
itself rolled ([[source-events-xml]]).

## Blue Options
None. Neither choice carries a `req`.

## Rewards & Risks
- **Accepting:** one `RANDOM`-level `stuff` bundle, and you forgo the ship's `destroyed` /
  `deadCrew` rewards, which for the generic `PIRATE` and `REBEL` hulls are the standard
  default payouts.
- **Refusing:** free. No penalty is attached to choice 2.
- The offer fires once hull is in the declared `min`–`max` band; nothing in the data says
  whether it re-rolls after a refusal.

## Strategy Notes
- *Opinion:* against `PIRATE` and `REBEL` hulls you are usually two or three volleys from
  the kill when the offer arrives, and the kill pays scrap. Refuse unless you are hurt,
  out of ammo, or facing boarders.
- Accept when the fight has already cost more than the wreck is worth — a `RANDOM` `stuff`
  roll can still come in high.

## Related
- [[event-pirate-escape]] — the other aftermath the same `PIRATE` hull can trigger
- [[event-pirate-surrender-civilan]] — a differently-named pirate aftermath (`PIRATE_SURRENDER_CIVILAN`), not this one
- [[event-rock-ship-surrender]], [[event-lanius-surrender]], [[event-zoltan-surrender]] — the species-specific equivalents
- [[entity-pirates]], [[entity-rebels]] — the factions flying the hulls that load it
- [[concept-surrender-offers]] — why `chance="0.5"` is a 50% offer
- [[concept-event-list-weighting]] — basis for the text weights

## Open Questions
- [ ] What surrender probability applies when `<surrender>` omits `chance`
      (`JELLY_PIRATE_WITHBOARDERS`)?
- [ ] What resource spread `RANDOM` `stuff` actually rolls.
- [ ] Does refusing re-offer later in the same fight?

## Sources
- [[source-events-xml]] (per raw/gamedata/events.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-dlcevents]] (per raw/gamedata/dlcEvents.xml)
