<!-- Retrieved from the FTL Fandom wiki via api.php on 2026-08-09. Source layer: do not edit. -->
Title: Pirate ship attacking civilian distress
URL: https://ftl.fandom.com/wiki/Pirate_ship_attacking_civilian_distress
Categories: Random_Events
Revision: 74784
Retrieved: 2026-08-09

---
{{Locations|Civilian Sector|Pirate Controlled Sector|Rock Controlled Sector|Rock Homeworlds|Slug Controlled Nebula|Slug Home Nebula|Uncharted Nebula|LRSmap=noship|unique=false}}


''The distress beacon is coming from a civilian ship. It appears it is being chased by a pirate.''
# Aid the civilian ship
#* ''You power up your weapons and engage the pirate ship.'' {{SurrenderEscape|surrenderno+escapeno|PIRATE_CIVILIAN|events_ships.xml}}
#** Fight the [[Enemy Ships|Pirate ship]].
#*** {{Winning|destroyed=true|The pirate ship breaks apart. You hasten to contact the civilian ship.}}
#**** You receive medium [[Rewards#Standard|scrap with resources]].
#***** [[#Contact the civilian ship|'''Contact the civilian ship''']].
#***{{Winning|deadCrew=true|No more life signs detected on the pirate ship. You hasten to contact the civilian ship.}}
#**** You receive high [[Rewards#Standard|scrap with resources]].
#***** [[#Contact the civilian ship|'''Contact the civilian ship''']].
# Stay out of it.
#* ''The fight brings them out of your immediate scanning range; however, after a time the distress calls stop.''
#** Nothing happens.
# {{Blue Option|Improved Weapons|Fire a warning shot from your strongest weapon.|level=6+|shortreq=Weapon Control}}
#* ''Detecting the greater threat (and potential reward), they turn and engage your ship.''
#** Fight the [[Enemy Ships|Pirate ship]].
#*** {{Winning|destroyed=true|The pirate ship breaks apart. You hasten to contact the civilian ship.}}
#**** You receive medium [[Rewards#Standard|scrap with resources]].
#***** [[#Contact the civilian ship|'''Contact the civilian ship''']].
#***{{Winning|deadCrew=true|No more life signs detected on the pirate ship. You hasten to contact the civilian ship.}}
#**** You receive high [[Rewards#Standard|scrap with resources]].
#***** [[#Contact the civilian ship|'''Contact the civilian ship''']].
#* ''It seems the pirate wasn't looking for a fight with someone who could fight back. They leave and you move to contact the civilian ship.''
#** [[#Contact the civilian ship|'''Contact the civilian ship''']].

==Contact the civilian ship==
{{Save the Civilian Ship}}

==Trivia==
This event is called "PIRATE_CIVILIAN_BEACON" in the datafiles.
* This event is meant to occur at a [[distress beacon]] but won't because the <code><distressBeacon/></code> tag is missing in its definition.
* This event is very similar to the [[Civilian ship chased by Pirate]] event, but the blue option appears only in this one.
* If you successfully scare off the pirate with the blue option, you will get a preview of the reward if it is scrap with resources. This doesn't happen with other routes to "Contact the civilian ship".
[[Category:Pirate ship fights]]
