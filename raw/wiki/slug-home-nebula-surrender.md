<!-- Retrieved from the FTL Fandom wiki via api.php on 2026-08-09. Source layer: do not edit. -->
Title: Slug Home Nebula surrender
URL: https://ftl.fandom.com/wiki/Slug_Home_Nebula_surrender
Categories: Random_Events, Unique_Events, Ship_Unlocking_Events
Revision: 74817
Retrieved: 2026-08-09

---
{{Locations|Slug Home Nebula|nebula=true|LRSmap=ship+nebula|unique=true}}


This is the [[The_Slug_Cruiser#Layout_A|Slug Cruiser]] ship unlocking event. <span style="color:grey">(the ship can also be unlocked by winning the game with the Mantis Cruiser)</span>

:This event is impossible to distinguish from [[Slug fight in nebula]] event, as it has the same intro and surrender text. Unfortunately, the only way to find out is to accept the surrender.
----


The intro text for this event varies, and could be any of the following: 
* ''Your sensors are no match for the Slug's telepathic abilities - a ship you never even saw opens fire from astern!''
* ''The Slug vessel you encounter here has obviously made a big score and is looking to test its new armaments. They picked the wrong ship to attack.''
* ''A Slug passenger ship hails: "Please, your worthy alien highnessesss, we are unarmed and sseeking asssylum." You approach cautiously, and weapons immediately spring from their hull!''
* ''A Slug ship - a rogue, you suspect - approaches, but when he sees you're Federation he thinks better of the sneak attack and fires everything he has.''
* ''Direct attacks are not preferred by the Slugs, but of the three you see at this beacon, one has the brass to make a move on your position!''
** Fight a [[Slug Ships|Slug ship]] ([[Rewards#Default_rewards|default rewards]]). &nbsp;<span style="color:grey">(<!--ship: JELLY_UNLOCK1; datafile: events_ships.xml-->surrender [[#When the Slug ship surrenders|offer]]: 100% chance at {{tooltip|30-40%|actual in-game value may be 3-4 hull + additional hull adjusted by sector progression}} hull; &nbsp;escape attempt: 50% chance at {{tooltip|30-40%|actual in-game value may be 3-4 hull + additional hull adjusted by sector progression}} hull)</span>

==When the Slug ship surrenders==
''"You have besssted us! Will you accept what is in our storeesss in exchange for our livess?"''
# Let them live.
#*''"Take thisss newly developed weapon we're transporting... They're not going to be happy we gave it up, that isss for ssure..."''
#*# Accept the prototype weapon.
#*#* ''This odd beam weapon does no damage to ships but instead greatly hurts the crew! Diabolical!''
#*#** You receive [[Beam_(Weapons)#Anti-Bio_Beam|<span style="color:limegreen">Anti-Bio Beam</span>]].
#*# We don't want the weapon, we want information.
#*#* ''You ask where they were delivering the weapon. "By telling you we will probably die jussst as like as not... Oh well." They give you the coordinates of the a prototype cruiser's mobile construction platform.''
#*#** A [[#Quest Marker|'''quest marker''']] is added to your map.
# We will not accept surrender!
#* Continue the fight.


==Quest Marker==
: Note: this event occurs at a regular quest marker beacon, but when you arrive there will be a nebula environment.
: {{Long-Ranged Scanners info|shipdetected=noship}}

''You arrive to discover an impressive cruiser being worked on by a few smaller ships and guarded by an assault ship. The mobile construction platform is slowly slipping into the clouds. You have not yet been noticed.''
# Charge them before they escape.
#* [[#Fight the ship defending the platform|'''Fight the ship defending the platform''']]. (this ship is always a [[Slug_Ships#Slug_Assault_/_Pirate_Assault|Slug Assault]] class)
#** {{Winning|destroyed/deadCrew=true|With the assault ship taken care of, you turn your attention to the construction platform. However, you find that it has long since disappeared into the clouds. You scrap what you can and prepare to move on.}}
#*** You receive high [[Rewards#Standard|scrap with resources]].
# Try to tail them without being noticed.
#* ''You slip into the nebula undetected but at this rate you are likely to get lost and lose track of them.''
#*# Fly slowly toward their last known position.
#*#* ''You are advancing slowly when suddenly the assault ship bursts through the clouds. They must have been able to detect you with their telepathy!''
#*#** [[#Fight the ship defending the platform|'''Fight the ship defending the platform''']]. (this ship is always a Slug Assault class)
#*#*** {{Winning|destroyed/deadCrew=true|With the assault ship taken care of, you turn your attention to the construction platform. However, you find that it has long since disappeared into the clouds. You scrap what you can and prepare to move on.}}
#*#**** You receive high [[Rewards#Standard|scrap with resources]].
#*# Wait and hope the escort leaves.
#*#* ''You wait for a time before attempting to advance toward the platform. However, after some frantic searching you can't tell if they left or you simply miscalculated your trajectory... You give up the search and prepare to leave.''
#*#**Nothing happens.
#*# {{Blue Option|Slug Crew|Have your crewmember monitor their life signatures.}}
#*#* ''You try to stay just far enough away that they won't detect your life signatures without actively searching for you. After a time, your Slug tells you the ship with a larger crew has jumped away. He guides the helm toward the platform...''
#*#**''The only ship left near the cruiser is an interceptor. This should be easy!''
#*#*** [[#Fight the interceptor|'''Fight the interceptor''']].
#*# {{Blue Option|Improved Sensors|Try to maintain a lock on their ships from a distance.|level=2+|shortreq=Sensors}}
#*#* ''You overclock your sensors, trying to get them to function in the clouds. They work just enough to let you keep tabs on their general position. After a time, the assault ship and most of the escort jumps away from the platform. You take the opportunity and move in to attack.''
#*#**''The only ship left near the cruiser is an interceptor. This should be easy!''
#*#*** [[#Fight the interceptor|'''Fight the interceptor''']].

==Fight the interceptor==
This ship starts to escape with 35 seconds countdown timer. It is always a [[Slug_Ships#Slug_Interceptor_/_Pirate_Interceptor|Slug Interceptor]] class.
* {{Winning|escape=true|The interceptor powers up its FTL drive in preparation to escape. At the same time, the cruiser's FTL drive does the same. They must be linked! Don't let them get away!}}
** {{Winning|gotaway=true|The interceptor jumps away with the cruiser linked to its FTL signatures. You were so close...}}
*** Nothing happens.
* {{Winning|destroyed/deadCrew=true|With the escort destroyed you take a look at your impressive prize. Your mission is too pressing to take a test flight. Before you rig the ship's computer to guide the it back to the main Federation hangar you discover a unique augment that duplicates the Slug's ability to heal breaches!}}
** You unlock the [[The Slug Cruiser|Slug Cruiser]]; receive high [[Rewards#Standard|scrap with resources]] and <span style="color:limegreen">Slug Repair Gel</span> [[Augmentations#Slug Repair Gel|augmentation]].<ref>Bugged: if the "scrap with resources" component gives an augmentation, it will overwrite the guaranteed augmentation.</ref>

==Trivia==
This event is called "NEBULA_SLUG_FIGHT_UNLOCK" in the datafiles.
* If a Slug ship doesn't offer a surrender at low hull integrity, then it is the [[Slug fight in nebula]] event.
* The Slug ship has 50% chance to initiate its escape at low hull integrity. The hull integrity threshold for the surrender offer and escape attempt is within the same margins, hence, if the Slugs try to escape first, some more damage needs to be dealt to the ship to trigger the surrender offer.

=== Reference notes ===<!--==Code Trivia==
This event is called <code><span style="color:#CEF8B0">NEBULA_SLUG_FIGHT_UNLOCK</span></code> in the <code>data.dat</code> file:
 <span style="color:#F8C97D"><event name="</span><span style="color:#CEF8B0">'''NEBULA_SLUG_FIGHT_UNLOCK'''</span><span style="color:#F8C97D">" unique="true"> COMMENT THIS OUT-> this is the special fight that looks like the normal ones but actually gives you the unlock <-COMMENT THIS OUT
     <text load="</span><span style="color:#CEF8B0">'''NEBULA_SLUG_FIGHT'''</span><span style="color:#F8C97D">"/>
     <ship load="</span><span style="color:#CEF8B0">'''JELLY_UNLOCK1'''</span><span style="color:#F8C97D">" hostile="true"/>
     <environment type="nebula"/>
 </event></span>
It loads the normal introduction text, <code><span style="color:#CEF8B0">NEBULA_SLUG_FIGHT</span></code>, and loads a ship that has the blueprint as the other ships, but it loads a special event when it surrenders:
 <span style="color:#F8C97D"><ship name="JELLY_UNLOCK1" auto_blueprint="SHIPS_JELLY">
     <surrender  chance="0" min="3" max="4" load="</span><span style="color:#CEF8B0">'''SLUG_UNLOCK_SURRENDER'''</span><span style="color:#F8C97D">"/>
     <escape  chance="0.5" min="3" max="4" load="PIRATE_ESCAPE"/>
     <destroyed load="DESTROYED_DEFAULT"/>
     <deadCrew load="DEAD_CREW_DEFAULT"/>
 </ship></span>
It is only listed once in the sector specifications:
 <span style="color:#F8C97D"><sectorDescription name="SLUG_HOME" minSector="3" unique="true"> 
     <nameList>
         <name>Slug Home Nebula</name>
     </nameList></span>
     ''[...]''
     <span style="color:#CEF8B0"><event name="NEBULA_SLUG_FIGHT_UNLOCK" min="1" max="1"/></span>
     ''[...]''
 <span style="color:#F8C97D"></sectorDescrption></span> ''[sic]''<noinclude>-->
__NOTOC__
[[Category:Ship Unlocking Events]]
[[Category:Ship surrender Events]]
[[Category:Events with Quest Markers]]
[[Category:Ship escape Events]]
[[Category:Augmentation reward opportunity]]
[[Category:Weapon reward opportunity]]
