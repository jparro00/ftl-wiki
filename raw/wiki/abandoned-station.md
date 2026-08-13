<!-- Retrieved from the FTL Fandom wiki via api.php on 2026-08-09. Source layer: do not edit. -->
Title: Abandoned station
URL: https://ftl.fandom.com/wiki/Abandoned_station
Categories: Random_Events, Unique_Events, Filler_Events
Revision: 74022
Retrieved: 2026-08-09

---
{{Locations|Slug Controlled Nebula|Slug Home Nebula|alsooccur=exitandfiller|LRSmap=noship|unique=true}}


The intro text for this event varies, and could be any of the following:
*''You arrive to find what appears to be a colonized moon, however scans show it has been abandoned. You also detect an abandoned space station near the Beacon.''
*''You find a small space station that appears to be abandoned.''
*''This area shows signs of a battle some time ago. There are scattered remains of ships but one station appears to be intact.''
----
<onlyinclude>#Move in to examine the station.
#* {{DuplicateEvent|2}} ''You approach cautiously but you detect no danger. It appears to have been a small rest stop that was abandoned a while ago. You take what few supplies you can find.'' &nbsp;'''OR''' &nbsp;''Upon closer inspection it appears to have a large portion of its hull destroyed. You take what few supplies you can find.''
#** You receive low [[Rewards#Scrap only|scrap]].
#* ''You dock with the station to take a look inside. However no sooner do you open the airlock than pirates burst in. Meanwhile scanners pick up a previously undetected pirate ship moving in to attack!''
#** <span style="color:red">2 boarders</span> beam aboard your ship and you fight a [[Enemy Ships|Pirate ship]] ([[Rewards#Default_rewards|default rewards]]). <ref name="Enemy ship (PIRATE)">{{SurrenderEscape(alt)|escape+surrender|PIRATE|events_ships.xml|50|20-40|2-4|50|30-40|3-4}}</ref>
#*''You dock with the station to take a look inside. However no sooner do you open the airlock than pirates burst in. Meanwhile multiple warning signals go off on the bridge. The pirates have activated a remote planetary defense system and it's locking onto your ship!''
#** <span style="color:red">2-4 boarders</span> beam aboard your ship and a planet-side[[File:Danger_pds.png|35px|bottom]]<span style="color:red">Anti-Ship Battery</span> periodically fires at your ship.
#* ''The station is in disarray. You find a cloning bay partially intact but nothing else seems to be functioning.''
#*# {{Blue Option|Clonebay|Search for a surviving DNA bank.|shortreq=Clone Bay}}
#*#* ''While the cloning facilities are no longer functioning, you find someone was in queue to be cloned. You transfer their data to your Clonebay and after a time their body is rebuilt.''
#*#** {{DuplicateEvent|2}} ''The clone is extremely confused but calms down after you try to explain the situation. With no other options the clone offers to work on your ship for a time.'' &nbsp;'''OR''' &nbsp;''The clone is extremely confused but seems to accept their new situation. With no other options the clone offers to work on your ship for a time.''
#*#*** You receive a <span style="color:limegreen">crewmember</span>.
#*#**''The clone emerges in a crazed frenzy and refuses to calm down. You have no choice but to fight.''
#*#*** <span style="color:red">1 boarder</span> beams aboard your ship.
#*# Scrap the machinery.
#*#* ''You take what you can and prepare to move on.''
#*#** You receive low [[Rewards#Scrap only|scrap]].
#* ''As you approach it becomes clear that the station is simply an empty shell. It has been stripped of useful materials long ago.''
#** Nothing happens.
#Stay near the Beacon.
#* ''You decide it's not worth the time to examine.''
#** Nothing happens.</onlyinclude>

==Notes==
This event is called "EMPTY_STATION2" in the datafiles. 
* There are no 'EMPTY_STATION' or 'EMPTY_STATION1' events in the datafiles. "EMPTY_STATION2" is simply a notation to also use this event as a  ([[Space station under construction#Cargo_ship_docked_to_an_empty_space_station|cargo ship is docked to an empty space station]]) subevent of [[Space station under construction]] event.
===Reference notes===
<references/>
[[Category:Filler Events]]
[[Category:Fights with Default Rewards]]
[[Category:Anti-Ship Battery hazard risk]]
[[Category:Boarding risk]]
[[Category:Advanced Edition Content Events]]
[[Category:Pirate ship fights]]
