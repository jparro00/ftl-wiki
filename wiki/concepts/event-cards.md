---
id: concept-event-cards
type: concept
version: both
first_seen: 2026-08-09
last_updated: 2026-08-12
sources: 4
related_events: [[[event-rebel-ship-supplying-civilians]], [[event-single-life-form-on-moon]], [[event-deactivated-auto-ship]], [[event-unarmed-zoltan-transport]]]
tags: [tooling, decision-tree, generated, coverage]
---

# Event cards — what they are and what they promise

## Definition & Context

An **event card** is a one-page decision tree for a single event, built to be read in a
couple of seconds while the game is paused. It answers one question — *what does each option
actually do?* — and nothing else.

Cards are **generated from the game files, never written**. An event id resolves to a
machine-readable tree (`ftl-event-tree/1`), which a shared renderer turns into HTML. No card
contains hand-authored content about its event; the same renderer and the same shared
vocabulary produce all of them. The mechanism lives in `tools/EVENT-CARD.md`; the grammar it
walks is [[concept-event-tree-grammar]]. This page is about what a card *means*.

**Coverage: 385 cards, covering 384 of the 395 paged events.** The 11 without cards are
fleet-pursuit internals (`FLEET_EASY*`, `FLEET_HARD`), the two tutorial events, `FUEL_FOR_DRONE`,
and [[event-lanius-boarders]], whose definition is commented out in the shipped data. None can
appear at a beacon, so the reachable event pool is fully carded.

## What a card guarantees

These are the properties that make a card trustworthy mid-run. Each is enforced by the
pipeline rather than by care:

- **Quoted text is the game's own.** Every hail, choice label and outcome string comes from
  `text_events.xml` or `text_misc.xml` through its id. Nothing is paraphrased or shortened.
- **No invented odds.** A percentage appears only where the files state one — a `<surrender>`
  or `<escape>` `chance`. Event lists carry no weights, so their entries carry no fractions;
  the card says so once in its footnote rather than guessing.
- **No recommendations.** A card states what each option does and costs, never which to pick.
  It carries no event ids, citations, version notes or strategy.
- **Nothing unreachable is shown.** Where the data proves a branch cannot happen — a
  `deadCrew` branch on a hull that declares no crew, a ship no option can turn hostile, a
  branch whose text is a developer placeholder — it stays in the underlying tree, marked, and
  off the card.
- **Regenerable and deterministic.** The same inputs produce the same card, byte for byte. A
  card is an artifact, not a document: delete it and rebuild.

## What a card deliberately does not show

- **Which opening you are looking at.** Many events pick their intro from a `<textList>`; the
  card shows the first variant and says how many exist. [[event-rebel-ship-supplying-civilians]]
  has five, so a screenshot often will not match the card's hail — the footnote is what tells
  you that is expected rather than the wrong event.
- **Intermediate narration.** A row shows its choice and its mechanical payload. The prose
  between them is dropped, so a row that continues a fight but has no payload reads
  "nothing happens".
- **Repeated subtrees once.** A fight reachable from three routes renders three times; merging
  happens only between identical siblings.

## How It Shows Up Across Sources

The card layer sits strictly downstream of the game files. It consumes `raw/gamedata/` —
the event files, the string tables, and `blueprints`/`autoBlueprints` for item, gate and ship
names — plus one field from this wiki: the `event_name:` frontmatter on each
`wiki/events/*.md` page, which supplies the human title and the slug. FTL itself never shows
the player an event name, so the wiki is the only source for one.

`raw/wiki/` (the Fandom mirror) is **not** an input. Nothing a card asserts depends on
community sources, with one exception recorded here for honesty: the mapping from
`<unlockShip id="N"/>` to a ship name is not in the game files at all. It is taken from the
wiki pages, which source it to Fandom, so a card naming "the Crystal Cruiser" rests on a
`medium`-reliability claim where everything else rests on `high`.

## Implications For Play

- A card is a **decision aid, not a walkthrough**: it will not tell you the safe option, and
  the absence of odds on a random table is a fact about the game files, not an omission.
- **Blue options are shown even when you cannot take them.** The card lists every gated
  option with its requirement, so it doubles as an answer to "what would a Teleporter have
  bought me here?"
- Where the game offers several gated variants of one choice, it shows you only the best you
  qualify for; the card lists them all, and says so.

## Related

- [[concept-event-tree-grammar]] — the node grammar cards are generated from
- [[concept-event-list-weighting]] — why random tables carry no percentages
- [[concept-blue-options]] — the `req=` gates a card renders in blue
- [[concept-surrender-offers]] — the one place the files publish real odds

## Open Questions

- [ ] `hidden="true"` on a `<choice>` (797 uses) has no established meaning; cards carry it
      through and ignore it.
- [ ] `<damage effect="random">` and `effect="all"` — the hazard wording is inferred from the
      attribute value, not from any source that defines it.
- [ ] Whether AE's `OVERRIDE_SHIPS_*` lists replace the `SHIPS_*` lists at runtime. If they
      do, some ship names on cards are the vanilla variants.

## Sources

- [[source-events-xml]] (per `raw/gamedata/events.xml`)
- [[source-text-events-xml]] (per `raw/gamedata/text_events.xml`)
- [[source-autoblueprints]] (per `raw/gamedata/autoBlueprints.xml`)
- [[source-blueprints]] (per `raw/gamedata/blueprints.xml`)
