<!-- Retrieved from the FTL Fandom wiki via api.php on 2026-08-09. Source layer: do not edit. -->
Title: Rebel ship attacking civilians in Last Stand
URL: https://ftl.fandom.com/wiki/Rebel_ship_attacking_civilians_in_Last_Stand
Categories: Random_Events
Revision: 73812
Retrieved: 2026-08-09

---
{{Locations|The Last Stand|LRSmap=noship|unique=false}}


The intro text for this event varies, and could be any of the following: 
*''A number of large transports are being pursued by a Rebel bombing squadron. One bomber has managed to slip through the defensive fire, and is poised to wreak among the enormous yet vulnerable transports. There's time for you to advance and take it out!''
*''Shots fly by your port windows followed by a Rebel scout in pursuit of a damaged cruiser. Should we move in to engage?''
*''There seems to be a small Federation colony under attack by a Rebel forward scout. Will you protect them?''
*''A battle rages nearby between small fighters; apparently fighting over a space station. The Federation appears to be losing ships fast. Shall we assist them?''
*''A civilian ship is broadcasting a request for assistance on a secure Federation channel. They are being harassed by Rebel scouts. Will you respond?''
----
#Prepare to fight the Rebel ship!
#* ''You move in to intercept.''
#** Fight a [[Rebel Ships|Rebel ship]]. {{SurrenderEscape|escape|BOSS_SCOUT_RESCUE|events_boss.xml|50|40-80|4-8}}
#*** {{Winning|destroyed=true|With the Rebel ship destroyed you are free to contact their would-be victim.}}
#**** You receive medium [[Rewards#Standard|scrap with resources]].
#***** [[#Contact the survivors|'''Contact the survivors''']].
#*** {{Winning|deadCrew=true|With the Rebel ship defeated you quickly salvage what you can and move to contact their prey.}}
#**** You receive high [[Rewards#Standard|scrap with resources]].
#***** [[#Contact the survivors|'''Contact the survivors''']].
# There's no time, get ready to jump.
#* ''You try to block out the horrors of war and focus on your mission.''
#** Nothing happens.

==Contact the survivors==
* ''You are hailed, "Thank you! It's not much but we can repair a bit of damage before you jump off into the war. Good luck!"''
** Your ship receives <span style="color:limegreen">8 repairs</span>.
* ''The survivors send a message, "Thanks for the support, I don't know how much longer we could have held on. Take some supplies, we probably won't need them at this point."''
** You receive {{Tooltip|medium|fuel: 2-4 ; missiles: 2-4 ; drone parts: 1}} [[Rewards#Stuff|resources with some scrap]].
* ''The people you rescued were primarily refugees fleeing the conflict. They offer you their sincere gratitude.''
** Nothing happens.

==Trivia==
This event is called "BOSS_SCOUT_RESCUE" in the datafiles.
[[Category:Hull Repair chance]]
[[Category:Events with Stuff rewards]]
