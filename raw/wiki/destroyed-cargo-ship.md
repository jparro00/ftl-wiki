<!-- Retrieved from the FTL Fandom wiki via api.php on 2026-08-09. Source layer: do not edit. -->
Title: Destroyed cargo ship
URL: https://ftl.fandom.com/wiki/Destroyed_cargo_ship
Categories: Random_Events, Unique_Events
Revision: 74041
Retrieved: 2026-08-09

---
{{Locations|Pirate Controlled Sector|LRSmap=noship|unique=true}}


''Not too far from the beacon, you detect a destroyed cargo ship with its cargo scattered nearby, intact.''
# Bring it aboard.
#*''They appear to be filled with military supplies! You take everything you can use and jettison the rest.''
#** You receive medium [[Rewards#Standard|scrap with resources]].
#* ''The cargo was primarily consumer goods and clothing, nothing particularly useful. You manage to collect some scrap.''
#** You receive low [[Rewards#Scrap only|scrap]].
#* ''Once you bring the cargo onto your ship, a pirate bursts out of one of the crates saying, "Ugh... I was getting cramped in there. Oh, yeah! Prepare to die!" Immediately after this battle-cry your ship is filled with the sound of crates breaking open...''
#** <span style="color:red">2-4 human boarders</span> beam aboard your ship.
#*''You bring the cargo aboard. Before you have a chance to open them a pirate ship appears out of hiding and charges. At the same time, the crates fly open. Intruders aboard the ship!''
#** <span style="color:red">2-4 human boarders</span> beam aboard your ship and you fight a [[Enemy Ships|Pirate ship]] ([[Rewards#Default_rewards|default rewards]]). <ref name="Enemy ship (JELLY_PIRATE_WITHBOARDERS)">{{SurrenderEscape(alt)|escape+surrender*|JELLY_PIRATE_WITHBOARDERS|events_ships.xml|70% chance for escape attempt at {{tooltip|20-40%|actual in-game value may be 2-4 hull + additional hull adjusted by sector progression}} hull with 15 seconds countdown timer ''and'' makes a surrender offer at {{tooltip|0-50%|actual in-game value may be 0-5 hull + additional hull adjusted by sector progression}} hull}}</ref>
# Leave it alone, this looks suspicious.
#* ''You leave the cargo alone and prepare to jump.''
#** Nothing happens.
# {{Blue Option|Advanced Sensors|Run an advanced scan on the boxes.|level=2+|shortreq=Sensors}}
#* [[#Scan the boxes|'''Scan the boxes''']].
# {{Blue Option|Long-Ranged Scanners|Run an advanced scan on the boxes.}}
#* [[#Scan the boxes|'''Scan the boxes''']].

===<h2><span style=font-size:smaller;>Scan the boxes</span></h2>===
* ''The cargo appears to contain nothing of much interest. You salvage some scrap from the destroyed ship.''
** You receive {{Transaction|20-35|add_scrap}}.
* ''Your Advanced Sensors are able to breach the protective barrier and scan the cargo. It appears to be filled with military supplies! You take everything you can use.''
** You receive medium [[Rewards#Standard|scrap with resources]].
* ''Your advanced sensors pick up faint life signatures inside the cargo. The life forms appear to be armed. This looks like a planned pirate ambush.''
*# Destroy the crates to prevent another ship from falling victim.
*#* ''You fire on the crates, breaking them open and scattering the pirates into empty space. A pirate ship appears out of nowhere with a message, "You will pay for that!"''
*#**Fight a [[Enemy Ships|Pirate ship]] ([[Rewards#Default_rewards|default rewards]]). <ref name="Enemy ship (PIRATE)">{{SurrenderEscape(alt)|escape+surrender|PIRATE|events_ships.xml|50|20-40|2-4|50|30-40|3-4}}</ref>
*# Leave it alone and prepare to jump.
*#* Nothing happens.

==Notes==
This event is called "FLOATING_CARGO" in the datafiles.
===Reference notes===
<references/>
[[Category:Fights with Default Rewards]]
[[Category:Boarding risk]]
[[Category:Ship surrender Events]]
[[Category:Pirate ship fights]]
