<!-- Retrieved from the FTL Fandom wiki via api.php on 2026-08-09. Source layer: do not edit. -->
Title: Mantis ship-collectors
URL: https://ftl.fandom.com/wiki/Mantis_ship-collectors
Categories: Random_Events, Unique_Events
Revision: 74723
Retrieved: 2026-08-09

---
{{Locations|Mantis Controlled Sector|Mantis Homeworlds|LRSmap=ship|unique=true}}


''You are immediately hailed by an impressive-looking Mantis ship, "Your ship would make a mighty fine prize. Prepare for battle!"''
* Fight a [[Mantis_Ships#Mantis_Fighter_/_Pirate_Fighter|Mantis Fighter]] with crew entirely composed of Mantis. <ref name="Enemy ship (DONOR_MANTIS_CHASE1)">{{SurrenderEscape(alt)|escapechance100timer|DONOR_MANTIS_CHASE1|events_ships.xml|50|5|5}}</ref>
** {{Winning|escape=true|You pick up more chatter from the enemy ship, "You know what... Forget this. Prepare for retreat!" Looks like they're preparing to make a hasty get away!}}
*** {{Winning|gotaway=true|The ship made an emergency FTL jump, but it looks like they didn't mask their signatures. You could easily follow them if you want.}}
***# After them!
***#* ''You input their coordinates into your map and prepare to follow.''
***#** A [[#Quest Marker|'''quest marker''']] is added to your map.
***# Forget it.
***#* ''They're not worth the trouble. You prepare to leave.''
***#** Nothing happens.
** {{Winning|destroyed=true|Their ship breaks apart and you move in to scrap the remains.}}
*** You receive medium [[Rewards#Standard|scrap with resources]].
** {{Winning|deadCrew=true|With no more crew on board you are free to salvage what you can from the remains.}}
*** You receive high [[Rewards#Standard|scrap with resources]].

==Quest Marker==
:{{Long-Ranged Scanners info|shipdetected=ship}}
''You catch up with the Mantis ship that escaped before, only to see them transferring their crew into an even bigger ship!''
* ''"Not YOU again! Do you know how much these repairs are going to cost me? Time to take out the big guns."''
** Fight a [[Mantis_Ships#Mantis_Bomber_/_Pirate_Bomber|Mantis Bomber]] with crew entirely composed of Mantis. <ref name="Enemy ship (DONOR_MANTIS_CHASE2)">{{SurrenderEscape(alt)|escape+surrender*|DONOR_MANTIS_CHASE2|events_ships.xml|attempts to escape at {{tooltip|60%|actual in-game value may be 6 hull + additional hull adjusted by sector progression}} hull (12 seconds timer) and makes a surrender offer at {{tooltip|20%|actual in-game value may be 2 hull + additional hull adjusted by sector progression}} hull}}</ref>
*** {{Winning|escape=true|They appear to be trying to get away again. You doubt they'll forget to mask their jump signature this time.}}
**** {{Winning|gotaway=true|Looks like they got away. At least you're able to scrap their abandoned fighter.}}
***** You receive high [[Rewards#Standard|scrap with resources]].
*** {{Winning|surrender=true|"Look, you proved your point. We don't want to die... Take this and let us go. Please?"}}
***# Let them live. &nbsp;<span style="color:grey;">[ the weapon and the amount of scrap are shown before you accept or reject the offer ]</span>
***#* ''"Thank you. But do you have any idea how much repairing TWO ships will set us back?..." What an odd Mantis. You prepare to leave.''
***#** You receive a <span style="color:limegreen">weapon</span> with high <span style="color:#70b8ff">scrap</span>.
***# Finish them off.
***#* ''"No! Hurry up, get us out of here! They're crazy!" You cut transmissions.''
***#** The fight continues.
*** {{Winning|destroyed=true|Their ship breaks apart and you salvage the two ships.}}
**** You receive a <span style="color:limegreen">weapon</span> and medium [[Rewards#Standard|scrap with resources]].<ref name=":0">The "scrap with resources" component will never give a bonus weapon, drone schematic or augmentation, due to its interaction with a guaranteed weapon/drone schematic reward.</ref>
*** {{Winning|deadCrew=true|You find an intact weapon on their now empty ship. You take as much scrap from the ships as possible.}}
**** You receive a <span style="color:limegreen">weapon</span> and high [[Rewards#Standard|scrap with resources]].<ref name=":0" />

==Notes==
This is a donor event called "DONOR_MANTIS_CHASE" in the datafiles.
===Reference notes===
<references/>
[[Category:Donor Events]]
[[Category:Ship escape Events]]
[[Category:Events with Quest Markers]]
[[Category:Ship surrender Events]]
[[Category:Weapon reward opportunity]]
