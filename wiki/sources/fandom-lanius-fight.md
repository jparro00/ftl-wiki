---
id: source-fandom-lanius-fight
type: source
source_kind: wiki
raw: raw/wiki/lanius-fight.md
game_version: unknown
date: 2026-08-09
ingested: 2026-08-09
reliability: medium
tags: [lanius, combat, default-rewards, advanced-edition]
---

# Fandom — "Lanius fight"

## Summary
The community wiki page for `LANIUS_FIGHT`, the baseline hostile Lanius encounter in the
Abandoned Sector. Retrieved via the MediaWiki API at revision 74222. Almost entirely a
transcription of the intro text list plus an enemy-ship annotation.

## Key Takeaways
- **Names the in-game id:** *"This event is called 'LANIUS_FIGHT' in the datafiles."*
- Locations: Abandoned Sector; `LRSmap=ship`, `unique=false`.
- Transcribes eleven intro strings — matching the eleven `<text>` entries of the
  `LANIUS_FIGHT_TEXT` list, including the repeat of `text_LANIUS_FIGHT_TEXT_8`.
- Outcome: *"Fight a Lanius ship (default Lanius rewards)"*, annotating `LANIUS_SHIP` as
  escape + surrender capable, citing `dlcEvents_anaerobic.xml`.
- Categorised `Advanced Edition Content Events`, `Fights with Default Rewards (Lanius)`.

## Events Covered
- [[event-lanius-fight]]

## Other Pages Touched
- [[entity-lanius]], [[sector-abandoned-sector]]

## Reliability Notes
`medium`. Version unstated in the body, but the AE category and the AE-only source file
make this Advanced Edition content. Its `SurrenderEscape` template renders numbers
(`80`, `20-40`, `2-4`) whose mapping to the XML attributes (`chance="0.2"`, `min`/`max`)
the page never explains — see the note on [[event-lanius-fight]].

## Contradictions Flagged
None on mechanics. Minor transcription drift: Fandom writes "many tiny Lanius crafts"
where `text_LANIUS_FIGHT_TEXT_5` reads "many tiny Lanius craft".

## Links
- Source URL: https://ftl.fandom.com/wiki/Lanius_fight
- [[source-dlcevents-anaerobic]], [[source-text-events-xml]], [[source-sector-data-xml]]
