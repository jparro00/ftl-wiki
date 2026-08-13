---
id: source-text-sectorname-xml
type: source
source_kind: gamedata
raw: raw/gamedata/text_sectorname.xml
game_version: ae
ingested: 2026-08-09
reliability: high
tags: [strings]
---

# text_sectorname.xml

## Summary
The English display names for sectors, keyed by id. `sector_data.xml` carries only the
ids; this file turns them into the names shown on the map.

## Key Takeaways
- Two strings per sector: `sectorname_<ID>` (full) and `sectorname_short_<ID>` (map label).
- 19 sectors have names. The two stub entries in
  [[sector-vestigial-definitions]] have none — good evidence they are dead code.
- The mapping is not always intuitive:

| In-game id | Display name |
|---|---|
| `STANDARD_SPACE` | Federation Space |
| `LANIUS_SECTOR` | Abandoned Sector |
| `NEBULA_SECTOR` | Uncharted Nebula |
| `REBEL_SECTOR_MINIBOSS` | Rebel Stronghold |
| `CRYSTAL_HOME` | Hidden Crystal Worlds |
| `FINAL` | The Last Stand |

- Short names differ from full ones for most sectors ("Engi Controlled" vs "Engi
  Controlled Sector"), so matching a wiki page title against either form needs care.

## Pages Created From This Source
Contributed the title of every sector page — see [[source-sector-data-xml]] for the list.

## Contradictions Flagged
None.

## Links
- [[source-sector-data-xml]]
