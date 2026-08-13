<!-- Retrieved from the FTL Fandom wiki via api.php on 2026-08-09. Source layer: do not edit. -->
Title: Lanius ship absorbing automated scout
URL: https://ftl.fandom.com/wiki/Lanius_ship_absorbing_automated_scout
Categories: Random_Events, Unique_Events
Revision: 74231
Retrieved: 2026-08-09

---
{{Locations|Abandoned Sector|LRSmap=ship|unique=true}}


''You come across a Lanius ship in the process of absorbing a Rebel automated scout. If you scare off the Lanius you could probably make use of it.''
#Fight the ship.
#*''You power up your weapons, which quickly gets the attention of the ship.''
#**Fight a [[Lanius Ships|Lanius ship]]. <ref name="Enemy ship (LANIUS_AUTO_REBEL)">{{SurrenderEscape(alt)|escapechance|LANIUS_AUTO_REBEL|dlcEvents_anaerobic.xml|80|20-40|2-4}}</ref>
#***{{Winning|escape=true|Scanners indicate the Lanius ship is preparing to jump. Don't let them escape!<!--Escape flavor text2: The Lanius ship begins to prepare their FTL drive for a jump. They appear to no longer wish to fight.-->}}
#****{{Winning|gotaway=true|The Lanius ship has escaped. You move to inspect the automated Rebel ship that it was absorbing.}}
#*****[[#Inspect the automated ship|'''Inspect the automated ship''']].
#***{{Winning|destroyed=true|The Lanius craft breaks apart. You move to inspect the automated Rebel ship that it was absorbing.}}
#****You receive medium [[Rewards#Standard|scrap with resources]].
#*****[[#Inspect the automated ship|'''Inspect the automated ship''']].
#***{{Winning|deadCrew=true|No more life signs detected on the Lanius ship. You move to inspect the automated Rebel ship that it was absorbing.}}
#****You receive high [[Rewards#Standard|scrap with resources]].
#*****[[#Inspect the automated ship|'''Inspect the automated ship''']].
#Leave them alone.
#*''Whatever assistance the disabled scout could provide is not worth the risk of fighting another Lanius. You prepare to move on.''
#**Nothing happens.

===<h2><span style=font-size:smaller;>Inspect the automated ship</span></h2>===
*''You are able to retrieve a significant amount of data about the surrounding beacons from the scout before you scrap it.''
**You receive a random amount of [[Rewards#Scrap only|scrap]] and the current sector <span style="color:limegreen">map</span> is <span style="color:limegreen">revealed</span>. <!-- GAME CODE has <autoReward level=> line with "low" value, while it should have been "LOW" - and the game treats this as "RANDOM" value -->
*''You find the ship has a built-in method of warning the Rebel fleet of contact with your ship. You feed it some false data about your ship's whereabouts that should keep the fleet off your tail for a time.''
**You receive a random amount of [[Rewards#Scrap only|scrap]] and the Rebel Fleet is <span style="color:limegreen">delayed</span> for <span style="color:limegreen">1</span> turn. <!-- GAME CODE has <autoReward level=> line with "low" value, while it should have been "LOW" - and the game treats this as "RANDOM" value -->

==Notes==
This event is called "LANIUS_AUTO_REBEL" in the datafiles.
===Reference notes===
<references/>
[[Category:Advanced Edition Content Events]]
[[Category:Rebel Fleet delay chance]]
[[Category:Beacon Map reveal chance]]
