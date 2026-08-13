<!-- Retrieved from the FTL Fandom wiki via api.php on 2026-08-09. Source layer: do not edit. -->
Title: Engi ship attacked by Mantis ship
URL: https://ftl.fandom.com/wiki/Engi_ship_attacked_by_Mantis_ship
Categories: Random_Events
Revision: 74854
Retrieved: 2026-08-09

---
{{Locations|Engi Controlled Sector|Engi Homeworlds|LRSmap=noship|unique=false}}

''You receive a distress call from a nearby Engi ship. "Assistance requested. Danger present. Imminent destruction."''
# Respond to the call and move in to assist.
#* ''You approach to find a Mantis ship assaulting a small Engi space station. You prepare for a fight!''
#** You fight a normal [[Mantis Ships|Mantis ship]]. <ref name="Enemy ship (MANTIS_ENGI_STATION)">{{SurrenderEscape(alt)|no|MANTIS_ENGI_STATION|events_ships.xml}}</ref>
#*** {{Winning|destroyed=true|The Mantis ship breaks apart.}}
#**** You receive medium [[Rewards#Standard|scrap with resources]].
#***** [[#Contact the Engi|'''Attempt to contact the Engi''']].
#*** {{Winning|deadCrew=true|No more life signs detected on the Mantis ship. You hasten to contact the Engi.}}
#**** You receive high [[Rewards#Standard|scrap with resources]].
#***** [[#Contact the Engi|'''Attempt to contact the Engi''']].
#*''You receive another message from the ship, this time with a Mantis at the comm-log. "Foolish meatsacks," he yells. Sensors indicate the ship is moving in to attack and boarders teleport from the station.''
#** <span style="color:red">1-2 mantis boarders</span> beam aboard your ship and you fight a mantis-controlled [[Engi Ships|Engi ship]] ([[Rewards#Default_rewards|default rewards]]). <ref name="Enemy ship (ENGI_MANTIS_CONTROLLED)">{{SurrenderEscape(alt)|no|ENGI_MANTIS_CONTROLLED|events_ships.xml}}</ref>
# Keep your distance.
#* Nothing happens.

===<h2><span style=font-size:smaller;>Contact the Engi</span></h2>===
* ''They thank you for the assistance and when you tell them of your mission, one of the Engi asks if he can assist your crew. You welcome him aboard.''
** You receive an <span style="color:limegreen">Engi crewmember</span> and low [[Rewards#Standard|scrap with resources]].
* ''The station was in the process of being evacuated. A number of civilian Engi offer their gratitude as they finalize their preparations to leave. They offer some fuel as a reward.''
** You receive {{tooltip|medium|2-4}} [[Rewards#Fuel_only|fuel]].
* ''The Engi station is stripped bare and there are signs of a fierce battle. The Mantis must have left the distress call active to lure other ships into a trap.''
** Nothing happens.
* ''The station hails you, "Gratitude. Expected probability of defeat without assistance... 86.2 percent. Request suitable reward."''
*# Request fuel.
*#* ''"Request granted. Fuel transferring."''
*#** You receive {{tooltip|high|3-6 fuel}} [[Rewards#Fuel|fuel and scrap]].
*# Request weapon.
*#* ''"Request granted. Weapon transferring."''
*#** You receive a <span style="color:limegreen">weapon</span> with low <span style="color:#70b8ff">scrap</span>.
*# Request drone.
*#* ''"Request granted. Drone schematic transferring."''
*#** You receive a <span style="color:limegreen">drone schematic</span> with low <span style="color:#70b8ff">scrap</span>.
*# {{Blue Option|Engi Crew|Threat unresolved. Current Mission imperative: Protocol 52.34.}}
*#* ''They respond, "Understood. Re-establishment of Federation highest import. Transmitting hidden base coordinates. Repairing hull and attaching ship to ship ordnance."''
*#** You receive a <span style="color:limegreen">weapon</span> with low <span style="color:#70b8ff">scrap</span>, your ship receives <span style="color:limegreen">10 repairs</span> and a [[#Hidden Federation Base|'''Hidden Federation Base''']] quest marker is added to your map.


{{Hidden federation base}}
==Notes==
This event is called "ENGI_STATION_DISTRESS" in the datafiles.
* This event is meant to occur at a [[distress beacon]] but won't because the <code><distressBeacon/></code> tag is missing in its definition.
__NOTOC__
[[Category:Fights with Default Rewards]]
[[Category:Boarding risk]]
[[Category:Crew reward chance]]
[[Category:Fuel reward chance]]
[[Category:Drone Schematics reward chance]]
[[Category:Hull Repair chance]]
[[Category:Weapon reward chance]]
[[Category:Events with Quest Markers]]
