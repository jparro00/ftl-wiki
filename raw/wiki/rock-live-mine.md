<!-- Retrieved from the FTL Fandom wiki via api.php on 2026-08-09. Source layer: do not edit. -->
Title: Rock live mine
URL: https://ftl.fandom.com/wiki/Rock_live_mine
Categories: Random_Events, Unique_Events
Revision: 74671
Retrieved: 2026-08-09

---
{{Locations|Rock Controlled Sector|Rock Homeworlds|LRSmap=noship|unique=true}}


''The burnt out hull of a Rock mine layer drifts by. Behind the wreck drifts a live mine; an automated drone that drills into ships' hulls before exploding. It locks onto your ship's signature and heads your way!''
# Attempt evasive maneuvers.
#*''The ship's turning circle proves too wide and the mine bites down onto the hull. You can hear it now, chewing through the armor.''
#*# Send someone out there to defuse it.
#*#* ''Your crewmember dons a space suit and exits the airlock. They make quick work of the basic device and return inside to relief all round. The mine makes good scrap pickings too.''
#*#** You receive medium [[Rewards#Scrap_only|scrap]].
#*#* ''Your crewmember dons a space suit and exits the airlock. When they open up the mine housing, though, they panic. The red wire or the blue?! 3... 2... 1...''
#*#*# Red!
#*#*#* [[#Cut the wire|'''Cut the wire''']].
#*#*# Blue!
#*#*#* [[#Cut the wire|'''Cut the wire''']].
#*# {{Blue Option|Missile Weapon|Attempt a controlled detonation using a missile.}} &nbsp;[ [[File:Icon missiles (cropped).png]]1 ] -- bugged: Hull Missile doesn't count
#*#*''After drawing straws, a crewmember goes out to fix a modified warhead to the mine. You detonate the missile in a way that dislodges the mine. It blows up shortly after. The ship takes some damage in the blasts, but you're still sailing.''
#*#** Your ship takes <span style="color:red">4 hull</span> damage, 1 damage to a random <span style="color:red">system</span>, and you receive low [[Rewards#Scrap_only|scrap]].
#*# {{Blue Option|Beam Drone|Use a drone to cut away the mine with a precision beam.}} [ {{Transaction|1|subtract_drones}} ] &nbsp;<span style="color:grey">(Anti-Ship Fire Drone doesn't count)</span>
#*#* ''Carefully guided from the bridge, your beam drone removes the mine's grappling arms and sends it drifting off into space, where you shoot at it until it detonates at a safe distance.''
#*#** You receive low [[Rewards#Scrap_only|scrap]].
# {{Blue Option|Improved Engines|Reverse thrusters!|level=5+|shortreq=Engines}}
#* ''It stresses the inertial dampeners, but you reverse course and outrun the mine. You prepare to jump off.''
#** Nothing happens.

==Cut the wire==
* ''You open your eyes and everything is still where it was a moment ago. You did it!''
** You receive medium [[Rewards#Scrap_only|scrap]].
* ''The weapon detonates. Everything goes dark, the bridge illuminated by flames pouring from the hull, your bomb disposal volunteer spinning off toward a nearby sun. You put out the fires and prepare to move on.''
** Your ship takes <span style="color:red">6 hull</span> damage, 1 damage with a <span style="color:red">breach</span> to a random <span style="color:red">room</span>, and you <span style="color:red">lose</span> a <span style="color:red">crewmember</span>.
*** <span style="color:#70b8ff">(Clone Bay)</span> ''Fortunately, your crewmember was close enough to the ship for the Clone Bay to revive them. Sheepish and apologetic, they rejoin the crew.''
**** The lost <span style="color:limegreen">crewmember</span> is <span style="color:limegreen">revived</span>.

==Trivia==
This event is called "ROCK_STARSHIP_MINE" in the datafiles.
* Due to a code error in the line <code><item type="''missile''" min="-1" max="-1"/></code> (instead of <code><item type="'''''missiles'''''" min="-1" max="-1"/></code>) the missile weapon blue option does not waste a missile ammo.
[[Category:Crew loss hazard]]
[[Category:Clone Bay revival]]
[[Category:Hull damage hazard]]
[[Category:System damage hazard]]
[[Category:Hull breach hazard]]
[[Category:Missiles use Events]]<!-- add description for this event in this category if the missile weapon blue option is available and functions at 0 missile ammo -->
[[Category:Drone Parts use Events]]
