---
id: event-slug-moons-question
type: event
event_name: SLUG_DISTRESS_QUESTION
sectors: [[[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]]]
beacon_type: distress
hostile: false
blue_options: []
chain: []
version: both
first_seen: 2026-08-09
last_updated: 2026-08-09
sources: 4
tags: [unique, distress, nebula, crew-reward, scrap-loss-risk, fuel-loss-risk, drone-loss-risk]
---

# Slug moons question — `SLUG_DISTRESS_QUESTION`

## Summary
A marooned Slug offers to join your crew if you can say how many moons orbit the planet
you're standing off. The answer is stated in the intro text you just read. Get it right and
you gain a free Slug crew member; get it wrong and he robs you of scrap, fuel and drone
parts.

## Trigger & Where It Appears
- Sectors: [[sector-slug-controlled-nebula]], [[sector-slug-home-nebula]] — via the
  `DISTRESS_BEACON_SLUG` event list (`min 3 / max 4` per sector)
  ([[source-events-slug]], [[source-sector-data-xml]])
- Beacon: **distress** (`<distressBeacon/>`) in a nebula
  (`<environment type="nebula"/>`), `unique="true"` ([[source-events-slug]])

## Text
> You arrive near the distress beacon's signal.

(`event_SLUG_DISTRESS_QUESTION_text`, per [[source-text-events-xml]])

## Choices & Outcomes

| # | Choice | Requirement | Outcome(s) | Odds |
|---|--------|-------------|-----------|------|
| 1 | Continue. | — | Rolls `SLUG_DISTRESS_QUESTION_LIST` — 4 entries, one per moon count. | see below |

### `SLUG_DISTRESS_QUESTION_LIST`

Four entries. Each states a moon count in its text, then offers the identical
*Investigate.* → four-answer quiz. **The correct answer is always the number in that
entry's own intro line.** ([[source-events-slug]])

| Entry | Intro text says… | Correct answer |
|---|---|---|
| 1 | "…one of the **five** moons of a planet hidden in the nebula." | Five. |
| 2 | "…one of the **six** moons…" | Six. |
| 3 | "…one of the **seven** moons…" | Seven. |
| 4 | "…one of the **eleven** moons…" | Eleven. |

> As you drift closer, you are contacted by a Slug marooned on the moon's surface. "I shall
> join your crew, sssay I, if you can answer me this simple quesssstion. How many moons are
> there in orbit here?"

The four offered answers are always **Five / Six / Seven / Eleven**, in that order. One
loads `SLUG_DISTRESS_QUESTION_TRUE`, the other three load
`SLUG_DISTRESS_QUESTION_FALSE`.

### `SLUG_DISTRESS_QUESTION_TRUE`

> "That isss... correct. You sssurprise me. Human, is it? Yesss... we can be partners." The
> Slug beams aboard and joins your crew!

`<crewMember amount="1" class="slug"/>` — a free Slug crew member.

### `SLUG_DISTRESS_QUESTION_FALSE`

> "That issss... incorrect." Further, I have taken advantage of your lack of acuity to beam
> aboard your ship and steal your stuff!

`<item_modify steal="true">` with ([[source-events-slug]]):

| Resource | Loss |
|---|---|
| Scrap | 35 |
| Fuel | 2–4 |
| Drone parts | 1–2 |

(The unclosed quotation mark in the text is in the game files. The event carries the dev
note *"JUSTING - TO DO - Add reduction of scrap"* even though the scrap loss is in fact
present — [[source-events-slug]].)

## Rewards & Risks
- Correct: a free **Slug crew member** — a species with telepathic sensing, immunity to
  mind control, and no oxygen dependency issues in a nebula sector.
- Incorrect: 35 scrap, 2–4 fuel and 1–2 drone parts gone. The fuel loss can strand a ship
  running lean.
- There is no way to decline once you arrive: the only choice at the top level is
  *Continue.*

## Strategy Notes
- **Read the intro line before answering.** The moon count is written in it every time; the
  quiz is only a trap for players clicking through.
- Fandom records that pre-Advanced-Edition the answer could also be inferred from grammar
  cues in the marooned Slug's text, and that AE removed those cues
  ([[source-fandom-slug-moons-question]]). That change is irrelevant now — the intro line
  still gives it away.
- A guess is 25% for a crew member against 75% for a triple resource loss. Do not guess.

## Related
- [[event-slocknog]] — the other Slug distress beacon that recruits a Slug
- [[event-mantis-ship-attacking-slug-ship]], [[event-slug-ship-boarding-rock-ship]],
  [[event-slug-oxygen-malfunction]] — the rest of `DISTRESS_BEACON_SLUG`
- [[entity-slugs]], [[item-slug-crew]]

## Open Questions
- [ ] Whether the four list entries are equally weighted.
- [ ] Whether the recruited Slug has randomised skills.

## Sources
- [[source-events-slug]] (per raw/gamedata/events_slug.xml)
- [[source-text-events-xml]] (per raw/gamedata/text_events.xml)
- [[source-sector-data-xml]] (per raw/gamedata/sector_data.xml)
- [[source-fandom-slug-moons-question]] (per raw/wiki/slug-moons-question.md)
