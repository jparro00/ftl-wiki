---
id: concept-surrender-offers
type: concept
version: both
first_seen: 2026-08-09
last_updated: 2026-08-16
sources: 6
related_events: []
tags: [mechanics, rewards, resolves-contradictions]
---

# Surrender offers and the `chance` attribute

## Definition & Context
Enemy ships in `events_ships.xml` can offer to surrender. The offer is declared as:

```xml
<surrender chance="0.3" min="3" max="4">
```

The `chance` attribute is the single most misread value in the game data, and it
generated the same flagged contradiction on a dozen event pages before it was resolved
here.

## The finding

> **`chance` is the probability the ship KEEPS FIGHTING, not the probability it
> surrenders.** The surrender chance is `1 − chance`.

The attribute sits on a `<surrender>` element and is named `chance`, so the natural
reading is "chance of surrendering". That reading is wrong.

## Evidence

Every ship where both the game file and a Fandom percentage exist agrees with `1 − chance`
and disagrees with `chance`:

| Ship | `chance=` | `1 − chance` | Fandom states |
|---|---|---|---|
| `ROCK_SHIP` | 0.7 | **30%** | 30 |
| `CRYSTAL_SHIP` | 0.6 | **40%** | 40 |
| `CRYSTAL_HUNTER` | 0.5 | **50%** | 50 |
| `PIRATE` | 0.5 | **50%** | 50 |
| `REBEL` | 0.5 | **50%** | 50 |

5 of 5 match, 0 counterexamples. The 0.5 rows are uninformative on their own — they match
under either reading — but `ROCK_SHIP` (0.7 → 30) and `CRYSTAL_SHIP` (0.6 → 40) are decisive.
([[source-events-ships]], and the Fandom pages listed under Sources)

**The `chance="0"` cases confirm it independently.** Exactly four ships carry `chance="0"`:

- `CRYSTAL_CONVOY` — [[event-crystal-fight-with-surrender-offer-hull-repairs]]
- `JELLY_UNLOCK1` — [[event-slug-home-nebula-surrender]]
- `QUEST_SLUG_PIRATE_TRAP1` — [[event-slug-comm-tapping]]
- `DONOR_BLACK_RAVEN` — [[event-the-black-raven]] (declared in `events.xml`, not
  `events_ships.xml`, which is why an earlier revision of this page missed it)

Read literally as "0% chance of surrendering", all four are contradictions: each event is
built around its surrender offer, and Fandom marks them as a **100%** offer. Under
`1 − chance`, `chance="0"` means the ship never keeps fighting — it **always** offers
surrender. Every one resolves cleanly, and the wiki's "100%" is correct.

**A ship that truly never surrenders omits the element entirely.** This is the strongest
single argument, because it is what the developers actually did:

| Ship | How "never surrenders" is expressed |
|---|---|
| `CRYSTAL_SHIP_NO_SURRENDER` | **no `<surrender>` element at all** |
| `CRYSTAL_FED` | no `<surrender>` element |
| `STORM_PIRATE_SUPPLY_FUEL` | no `<surrender>` element |

If `chance="0"` meant "never surrenders", `CRYSTAL_SHIP_NO_SURRENDER` — a ship named for
that exact behaviour — is precisely where it would have been used. It isn't. Absence of the
element is the game's way of saying "no offer"; `chance="0"` therefore has to mean
something else, and `1 − chance` is the only reading that fits.

Across all game files: **20 ships declare a surrender chance** — 4 at `0`, 3 at `0.2`,
1 at `0.3`, 10 at `0.5`, 1 at `0.6`, 1 at `0.7`. ([[source-events-ships]], [[source-events-xml]])

## What this resolves
This was independently flagged as an unresolved contradiction by four separate ingest
passes before being settled:

- the Crystal batch, on `CRYSTAL_CONVOY` (`chance="0"` vs a documented offer)
- the Slug batch, on `JELLY_UNLOCK1` and `QUEST_SLUG_PIRATE_TRAP1`
- the Pirate batch, which first spotted the systematic `1 − chance` pattern across
  `PIRATE_BRIBER` (0.3 → 70%, 0.4 → 60%)
- the Lanius batch, on `LANIUS_SHIP` (`chance="0.2"` vs Fandom's 80)

The contradiction is resolved in favour of *both* sources being right about different
quantities.

**Cleared (lint, 2026-08-13).** The four event pages still carrying the old flag were
annotated: [[event-crystal-fight]] (`0.6`) and [[event-rock-fight]] (`0.7`) had additionally
**stated the wrong percentage** — 60% and 70% — by trusting the raw attribute at face value;
both now read 40% and 30%, matching Fandom. [[event-crystal-fight-with-surrender-offer-hull-repairs]]
and [[event-slug-home-nebula-surrender]] (`chance="0"`) had guessed correctly but recorded it
as unresolved, and are now closed at 100%. [[event-donor-mantis-chase2]]'s flag concerns
`min`/`max` units, which remain genuinely open.

## What a surrender pays

The offer's *size* is a separate mechanism from its *probability*, and it is the `stuff` tier
of [[concept-autoreward-tiers]] — "less scrap, mostly resources (intended for surrenders)" in
the developers' own schema comment. From [[source-fandom-rewards]]:

- **Ships in the default-reward categories offer random tier.** `LANIUS_SHIP`, `PIRATE`,
  `REBEL`, `ROCK_SHIP` and their siblings roll the level as well as the outcome, so the same
  ship's offer varies run to run.
- **~6% of `stuff` rewards carry a bonus item** — a weapon, augment or drone schematic on top.
  When that roll lands, the scrap half is **upgraded** from low to match the resources tier, so
  a bonus item and a bigger scrap payout arrive together rather than trading off.
- Resource amounts are flat (`LOW` 1–3 fuel / 1–2 missiles / 1 drone part, up to `HIGH` 3–6 /
  4–8 / 1–2); the scrap half scales with sector.

> **Slug ships hide the offer.** Every other surrender shows its exact reward before you decide,
> and can be rejected once seen. Most Slug ships show the reward **only after acceptance**, and
> it cannot then be refused. Accepting a Slug surrender is a blind trade
> ([[source-fandom-rewards]]). The table of possible Slug rewards is transcluded on the Fandom
> page and was **not captured** into `raw/`, so this wiki knows the rule and not the range.

## A related trap: `min` / `max`

The same `<surrender>` element carries `min` and `max`. These are **hull points**, not
percentages. Fandom renders them as percentages on several pages
(`ENGI_UNLOCK_2REAL`: files `min="5" max="5"`, Fandom "50% hull"). Treat the raw values as
hull points and the wiki's percentages as an unconfirmed interpretation.

## Confidence & limits
Strong but not proven. Three independent lines of evidence agree: the `1 − chance` match
across five ships, the four `chance="0"` reconciliations, and the fact that "never
surrenders" is expressed by omitting the element. None of it is engine code. The naming
remains genuinely odd, which is the only reason for residual doubt.

> **Method note.** An earlier revision of this page said there were three `chance="0"`
> ships. That count came from a scan that read a fixed byte window after each `<ship>` tag,
> so short blocks bled into their neighbours — it both missed `DONOR_BLACK_RAVEN` (declared
> outside `events_ships.xml`) and invented several false positives, including
> `CRYSTAL_SHIP_NO_SURRENDER`, which would have *falsified* the hypothesis had it been
> real. Re-scanned with exact `<ship>…</ship>` boundaries. Counts here are from that
> corrected scan.

**What would settle it:** an in-game observation of a `chance="0.7"` ship (e.g. any
`ROCK_SHIP` fight) surrendering at roughly 30%, not 70%, of low-hull encounters.

## Where It Applies
Every enemy-ship encounter with a `<surrender>` block — the majority of hostile events in
the wiki.

## Related
- [[event-stalemate-surrender]] — `STALEMATE_SURRENDER`, the *other* way a fight ends in a
  stand-down: engine-invoked rather than rolled from a `<surrender>` block, in no event list,
  and reached when a battle cannot be finished at all
- [[concept-event-tree-grammar]] — the node grammar every event is built from
- [[concept-rebel-fleet-advance]] — the `modifyPursuit` attribute has a similar
  raw-value-vs-Fandom-gloss problem, still unresolved
- [[source-events-ships]] — where every `<surrender>` block lives

## Open Questions
- [ ] In-game confirmation per the test above.
- [ ] Does `<escape chance="X">` follow the same inverted convention? Untested here.
- [ ] Are `min`/`max` hull points or percentages?
- [ ] What the Slug hidden-surrender reward table actually contains — the Fandom template
      holding it was not captured into `raw/`.

## Sources
- [[source-fandom-rewards]] (per raw/wiki/rewards.md)
- [[source-events-ships]] (per raw/gamedata/events_ships.xml)
- [[source-fandom-rock-fight]] (per raw/wiki/rock-fight.md)
- [[source-fandom-crystal-fight]] (per raw/wiki/crystal-fight.md)
- [[source-fandom-pirate-briber]] (per raw/wiki/pirate-briber.md)
