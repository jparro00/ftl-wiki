<!-- Retrieved from the FTL Fandom wiki via api.php on 2026-08-09. Source layer: do not edit. -->
Title: Research station with no response
URL: https://ftl.fandom.com/wiki/Research_station_with_no_response
Categories: Random_Events, Unique_Events
Revision: 74273
Retrieved: 2026-08-09

---
<noinclude>{{Locations|Pirate Controlled Sector|LRSmap=noship|unique=true}}


''You arrive to find a small research station putting out a distress signal. There is no response to your hails.''</noinclude>
<includeonly>''You find the small research station and discover that it's putting out a distress signal. Strangely, there is no response to your hails.''</includeonly>
#Dock with the station and investigate.
#* ''Inside there are signs of a great struggle; scientists lie dead where they fell, brutally dismembered. You grab a few research drone parts lying on a desk near the door and leave quickly.''
#** You receive {{tooltip|medium|1 drone part}} [[Rewards#Drone_parts|drone parts and scrap]].
#* ''You dock with the station and see a frantic person banging on the airlock door. Once inside your ship, he drops to the floor saying, "My... friends... They've gone insane... They're coming!" You hand him a blaster and turn to see a number of people charging toward the ship.''
#**You receive a <span style="color:limegreen">crewmember</span>.
#**# Prepare for a fight!
#**#* <span style="color:red">3-4 human boarders</span> beam aboard your ship.
#**# {{Blue Option|Medbay|Have the advanced medbay analyze their condition.|level=3|shortreq=Medbay}}
#**#* ''You hold them off while retreating into the med-bay. Its advanced systems determine that an alien neurotoxin is the cause of their frenzy. It synthesizes an antidote and releases it into the room. After a time, the scientists recover. One offers their services as thanks for saving them.''
#**#** You receive a <span style="color:limegreen">crewmember</span> with 1 skill in repair and medium [[Rewards#Scrap_only|scrap]].
#* ''As you explore the base, crazed screams are heard. Your team retreats back to your ship with a number of armed scientists in pursuit. One of your team starts to cough and falls in a spasm onto the floor.''
#*# Drag him back to the ship and prepare for a fight.
#*#* ''As you get back on board, your injured friend rises up and starts to attack you, screaming. Caught off-guard, your remaining crew fall back as the other scientists fight their way onto the ship.''
#*#** You <span style="color:red">lose</span> a <span style="color:red">crewmember</span>, who becomes an enemy, and <span style="color:red">3-4 human boarders</span> beam aboard your ship.
#*# {{Blue Option|Teleporter|Use your Teleporter to retrieve your crew.}}
#*#* You beam your away team back to the ship and disengage from the station. Although the ship is safe, the infected crew member quickly becomes frenzied and attacks.
#*#** You <span style="color:red">lose</span> a <span style="color:red">crewmember</span>, who becomes an enemy.
#*# {{Blue Option|Medbay|Drag him back to the Medbay.|level=2|shortreq=Medbay}}
#*#* ''You hold him down and the medbay is able to stop whatever neurotoxin was on the ship from fully infecting your crew. Once he recovers, you prepare to fight off the scientists, who are beyond help.''
#*#** <span style="color:red">3-4 human boarders</span> beam aboard your ship.
#*#{{Blue Option|Medbay|Have the Advanced Medbay analyze their condition.|level=3|shortreq=Medbay}}
#*#* ''You hold them off while retreating into the med-bay. Its advanced systems determine that an alien neurotoxin is driving your crew member insane. It synthesizes an antidote and releases it into the ship. After a time, the frenzied scientists recover and one offers to help out as thanks for saving them.''
#*#** You receive a <span style="color:limegreen">crewmember</span>.
# Leave it alone.
#* Nothing happens.
# {{Blue Option|Anti-Personnel Drone|Send your battle drone in to help.}} &nbsp;[ {{Transaction|1|subtract_drones}} ] <ref name="Drone part bug">Bugged: no drone part is lost if the reward includes drone parts, though you still need at least 1 drone part to choose this blue option.</ref>
#* {{DuplicateEvent|2}} ''You send your Anti-Personnel drone to explore the station. What you find is disconcerting... It appears that something has caused the scientists and guards to tear each other to pieces. You abandon the drone on the station for fear that it is contagious.'' &nbsp;'''OR''' &nbsp;''Once on board the station, your drone is immediately beset by frenzied scientists and guards. It eventually gets torn apart by the mob but it has bought you enough time to disengage from the station and escape into empty space.
#** Nothing happens.
#* ''The cameras mounted to your Anti-Personnel drone show a chaotic scene. No people are to be found but the remnants of a recent battle on-board the ship are obvious. You instruct the drone to retrieve some useful materials before leaving.''
#** You receive medium [[Rewards#Standard|scrap with resources]].
<noinclude># {{Blue Option|Life Scanner|Run advanced life scans.|shortreq=Lifeform Scanner}}
#* ''There are no life signs detected on the ship although there appears to be a number of deceased crew. There does not appear to be any airborn contagions so your crew quickly salvages what they can before moving on. You can only wonder what befell the station.''
#** You receive medium [[Rewards#Standard|scrap with resources]].
#* ''Sensors show scattered signs of life although most of the crew are deceased. However the health signatures of the living indicate they are violent and unstable. You decide it's better to move on than risk engaging the remaining crew.''
#** Nothing happens.

==Notes==
This event is called "STATION_SICK" in the datafiles. 
* This event can occur as [[Merchant's request#The_station_doesn't_respond|the station doesn't respond]] subevent in the [[Merchant's request#Merchant's_Delivery|Merchant's Delivery]] scenario of the [[Merchant's request]] event. However, the <span style="color: #09f">Lifeform Scanner</span> [[Augmentations#Lifeform_Scanner|blue option]] only appears if this event is found alone.
===Reference notes===
<references/></noinclude>
[[Category:Crew loss risk]]
[[Category:Boarding risk]]
[[Category:Crew reward chance]]
[[Category:Drone Parts reward chance]]
[[Category:Drone Parts use Events]]
