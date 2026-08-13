<!-- Retrieved from the FTL Fandom wiki via api.php on 2026-08-09. Source layer: do not edit. -->
Title: Capture the ship
URL: https://ftl.fandom.com/wiki/Capture_the_ship
Categories: Random_Events, Unique_Events
Revision: 74023
Retrieved: 2026-08-09

---
{{Locations|Civilian Sector|Rock Controlled Sector|Rock Homeworlds|Zoltan Controlled Sector|Zoltan Homeworlds|LRSmap=noship|unique=true}}


''You arrive to find a number of ships convening around a station. There is some unencrypted chatter between the ships, you tune in and listen for anything interesting.''
* ''Overhearing their conversation, it seems that they need to take possession of an enemy ship intact.''
*# Offer your services.
*#* ''They briefly scan your ship and inform you that you are not "properly equipped" for this type of mission.''
*#** Nothing happens.
*# Leave them alone.
*#* ''If they wanted your help they would surely ask for it. You prepare to leave.''
*#** Nothing happens.
*# {{Blue Option|Teleporter|Offer to board their ship.}}
*#* [[#Offer a solution|'''Offer a solution''']].
*# {{Blue Option|Fire Bomb|Offer to burn the crew out.}}
*#* [[#Offer a solution|'''Offer a solution''']].
*# {{Blue Option|Bio Beam|Offer to 'remove' their crew.|shortreq=Anti-Bio Beam}} (Requires [[Beam_(Weapon)#Anti-Bio_Beam|Anti-Bio Beam]])
*#* [[#Offer a solution|'''Offer a solution''']].

===<h2><span style=font-size:smaller;>Offer a solution</span></h2>===
''They quickly scan your ship and say, "It appears you could help. A bandit has made off with some very important cargo, though I doubt they have any understanding of what it is they stole. We need you to capture the ship intact."''
# Agree to capture the ship.
#* ''"Great, we'll relay their coordinates. Remember, do NOT destroy that ship! Remember, we'll be right behind you."''
#** A [[#Quest Marker|'''quest marker''']] is added to your map.
# Decline.
#* ''"We understand. Hopefully we can find a solution to this on our own." You prepare to jump.''
#** Nothing happens.

==Quest Marker==
: {{Long-Ranged Scanners info|shipdetected=ship}}

''You find the ship that you were asked to capture intact. You're not sure why, but they stressed that it's of great importance that you kill the crew WITHOUT destroying the ship.''
* Fight a [[Enemy Ships|Pirate ship]]. <ref name="Enemy ship (PIRATE_QUEST_CREWDEAD)">{{SurrenderEscape(alt)|no|PIRATE_QUEST_CREWDEAD|events_ships.xml}}</ref>
** {{Winning|destroyed=true|The explosion rocks the pirate ship and a brilliant light begins to shine from the wreckage. Before you can react the ship is consumed in a massive chain of explosions that send you careening toward a nearby planet. You struggle to put out the fires and your pilot desperately tries to get the controls online before you're dragged down to the surface. Apparently when they said the ship should not be destroyed they had good reason...}}
*** Your ship takes <span style="color:red">15 hull</span> damage, 1 damage to a random <span style="color:red">system</span>, 1 damage with [[File:S_fire2.png|28px|bottom|1-2 fires|alt=fire]] and a <span style="color:red">breach</span> to a random <span style="color:red">room</span>.
** {{Winning|deadCrew=true|You secure the ship and wait for the merchants to arrive. Upon arrival they message you, saying "Good job. We would prefer if you did not speak of this to anyone."}}
*** You receive a <span style="color:limegreen">weapon</span> with high <span style="color:#70b8ff">scrap</span>.

==Notes==
This event is called "QUEST_CREWDEAD_START" in the datafiles.
* This event can deal the most damage to the player ship, at 15.
===Reference notes===
<references/>
__NOTOC__
[[Category:Events with Quest Markers]]
[[Category:Hull damage risk]]
[[Category:System damage risk]]
[[Category:Hull breach risk]]
[[Category:Fire risk]]
[[Category:Weapon reward opportunity]]
[[Category:Pirate ship fights]]
