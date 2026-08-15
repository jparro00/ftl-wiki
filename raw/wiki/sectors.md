<!-- Retrieved from the FTL Fandom wiki via api.php on 2026-08-15. Source layer: do not edit. -->
Title: Sectors
URL: https://ftl.fandom.com/wiki/Sectors
Categories: Mechanics
Revision: 74796
Retrieved: 2026-08-15

---
[[File:Sector_Map.png|thumb|420px<!--|<center>Sector Map</center>-->]]
'''Sectors''' are zones in FTL: Faster Than Light, each containing between 19 and 24 [[beacon]]s.

On the sector map, there are three groups of sectors: [[Sector#Civilian Sectors|Civilian]], [[Sector#Hostile Sectors|Hostile]], [[Sector#Nebula Sectors|Nebula]]. There are also two "special" sectors: the [[Sector#Hidden Crystal Worlds|Hidden Crystal Worlds]] (never shown on the map) and [[Sector#The Last Stand|The Last Stand]] (final sector with unique mechanics). Sectors are determined randomly, but there is a 48% chance for a sector to be green, 32% to be red, and 20% to be purple.<ref>https://gitlab.com/znixian/xftl/-/blob/master/doc/sector-map?ref_type=heads</ref>

However, the colour-coding of sectors is misleading. It suggests that green sectors are safer, while red sectors have more fights and therefore more scrap; but that [https://www.reddit.com/r/ftlgame/comments/bwk4ot/sector_profit_data_from_200x_sector_4_hard/ is not really true]. For example, while Engi sectors have few fights and are very safe, Zoltan sectors have many fights and are among the most dangerous. It's best to choose your next sector based on an understanding of that specific sector, rather than just looking at its colour. One important difference between sectors is the number of stores they contain.

NOTE 1: the count and type of Beacons in the sector descriptions are taken straight from the game files and can be misleading. You are encouraged to read the [[Sectors#Technical details of sector generation and events|Technical details of sector generation and events]] section first in order to have a better understanding of this. Here are some clues:<div style="margin-top:-15px;">
<div style="margin-bottom:-10px;">
*The beacons listed as "stores" are guaranteed stores. These do not include stores which may appear as a reward or one of the outcomes in some [[:Category:Store Opening Rewards|events]]. Also note that it is possible, while rare, for Uncharted Nebulas to have no guaranteed stores.<ref name="Uncharted Nebula no stores"/></div>
<div style="margin-bottom:-10px;">
*The beacons listed as "various items" may include free scrap/items, refueling/repair station, and trading events depending on the sector event list. Some of these events may require certain equipment/crew/ammo (blue options) to gain the benefits, while others simply grant you an item/scrap/resources.</div>
<div style="margin-bottom:-10px;">
*The beacons listed as "distress" include only the number of events picked from the "DISTRESS"<!-- DISTRESS_BEACON_XYZ eventList, where XYZ is the name suffix of a specific sector --> event list. However, there are other events with a distress tag (the beacon map shows such events as DISTRESS beacons) that belong to different event lists and can appear in a sector. For example, Engi sectors can have 4<!-- or even more? - I haven't looked through all possible events with the distress tag --> distress beacons rather than shown 1-3. It is due to the fact that, for example, 'The Dense asteroid field distress' event (with a distress tag) belongs to NEUTRAL_ENGI eventList, events from which are populating the beacon map before the events from DISTRESS_BEACON_ENGI eventList, and the game can roll for the maximum number of events from the DISTRESS event list, thus, giving 4 distress beacon events in the actual game. There are also other nuances which may come from the fact that some non-unique events (i.e. those that can occur more than once per sector) can belong to several event lists simultaneously; and, on the contrary, some events from DISTRESS event lists may be missing the distress tag by mistake (despite also having the intro flavor text explicitly hinting at the distress nature of the event), so they won't appear as DISTRESS beacons.</div>
<div style="margin-bottom:-10px;">
*The beacons listed as "quest" include only the number of events picked from the "QUESTS" event list, which does not include all the events with possible quests. For example, in the starting sector you can encounter more than 1 "quest" beacon: it means that there is one beacon which selects events from the "QUESTS" event list, but you can actually encounter quests generated from other beacons as well. Also note that one "quest" beacon might not even exist on the map, because all beacons may have been "filled" by other events already. Quests that cannot be spawned in a current sector due to the Rebel Fleet close proximity (and, possibly, other factors) are transferred to a next sector and are not counted towards the quest beacons limit (sector 8 cannot have any quests at all).</div></div>
<!-- @TO-DO: The beacons listing on this page should be updated to reflect the actual evenLists and the order in which the game calls them. These lists - cleaned up, formatted, and supplemented with links to events (additionally supplied with redirects from their datafiles names to the current titles on the wiki) - can be uploaded as templates and linked from this page. And, finally, the grouping and the definition of the events and their types should be clarified to avoid any misunderstanding whatsoever.) -->
NOTE 2:<div style="margin-top:-20px;">
*As of 23/10/2025, the Civilian (Starting) Sector has its beacons placed in proper order (i.e. the sector is populated with the beacons in this exact order).
*To also see the exit beacon events (for non-nebula/not-overtaken-by-the-Rebels exit beacon), see [[Template:EventList EXIT LIST|exit_list]].
*On the template pages, the events datafiles names are alphabetically ordered for convenience - in the game files the events are placed in a different order, however, that doesn't affect the likelihood of them being chosen over the other ones in the same eventList.
*"override_..." eventlists are used when Advanced Edition Content is enabled (usually 1 or 2 events are added to the base game eventlists; added events are in bold on the eventlist template pages and all such events belong to the [[:Category: Advanced Edition Content Events|Category: Advanced Edition Content Events]]).</div>
<!-- @to-do: add link to the aggregate sectordescription page showing sector descriptions (and, possibly, a table with eventlists specifically used for the sector) for all sectors - use Template for individual sector sectordescription pages -->

== <span style="font-size:larger;">'''Civilian Sectors'''</span> ==

=== <h2>Civilian (Starting) Sector</h2> ===
: ''"The data you carry is vital to the remaining Federation fleet. You'll need supplies for the journey, so make sure to explore each sector before moving on to the next. But get to the exit before the pursuing Rebel fleet can catch up!"''

<div style="font-size:larger;">Sector occurrence:</div>
Despite the in-game name, the starting sector is slightly different from the usual Civilian Sector: it has fewer stores, items, quests and nebulas. This sector is always and only Sector 1.

<div style="font-size:larger;">Beacons:</div>
*0-4 [[Template:EventList NEBULA|nebula]] beacons
*1-2 stores
*1 [[Template:EventList ITEMS|items]] / [[Template:EventList OVERRIDE_ITEMS|override_items]] events
*2-4 [[Template:EventList NEUTRAL_CIVILIAN|neutral_civilian]] events
*1-2 empty beacons
*1-2 [[Template:EventList DISTRESS_BEACON|distress_beacon]] events
*4-6 [[Template:EventList HOSTILE_CIVILIAN|hostile_civilian]] events
*1 [[Template:EventList QUESTS|quests]] / [[Template:EventList OVERRIDE_QUESTS|override_quests]] event
*2 [[Template:EventList HOSTILE1|hostile1]] / [[Template:EventList OVERRIDE_HOSTILE1|override_hostile1]] events

<div style="font-size:larger;">Events:</div>
See [[:Category:Civilian Sector Events|Civilian Sector Events]]

<span style="font-size:larger;">Crewmembers:</span>
<div style="margin-top:-25px;">In this sector, crewmembers of the following races can be purchased or received as a crew kill reward. By [[Rarity|rarity]] (only affects the store assortment probability), from common to rare:</div>
*1: Human
*2: Engi, Mantis
*3: Rockmen
*5: Zoltan

<div style="font-size:larger;">Soundtrack:</div>
The following [[Soundtrack|tracks]] can be played in this sector: Civilian, Cosmos, MilkyWay, Lost Ship.

=== <h2>Civilian Sector</h2> ===
:''"Welcome to a new sector! Get to the exit beacon and jump to the next sector before the pursuing Rebels catch you!"''

<div style="font-size:larger;">Sector occurrence:</div>
This sector can occur multiple times per game and is different from the [[#Sectors#Civilian_(Starting)_Sector|starting sector]].

<div style="font-size:larger;">Beacons:</div>
*2-3 stores
*2-3 various items
*2-4 neutral encounters
*1-2 empty beacons
*1-2 distress beacons
*6-8 hostile encounters <!-- 4-6 from "HOSTILE_CIVILIAN" eventList and 2-2 from "HOSTILE1" eventList, which comes after "QUESTS" -->
*0-2 quests
*0-8 nebula spaces

<div style="font-size:larger;">Events:</div>
See [[:Category:Civilian Sector Events|Civilian Sector Events]]

<span style="font-size:larger;">Crewmembers:</span>
<div style="margin-top:-25px;">In this sector, crewmembers of the following races can be purchased or received as a crew kill reward. By [[Rarity|rarity]] (only affects the store assortment probability), from common to rare:</div>
*1: Human
*2: Engi, Mantis
*3: Rockmen
*5: Zoltan

<div style="font-size:larger;">Soundtrack:</div>
The following [[Soundtrack|tracks]] can be played in this sector: Civilian, Cosmos, MilkyWay, Lost Ship.

=== <h2>Engi Controlled Sector</h2> ===
<div class="mw-collapsible mw-collapsed">
: ''"You have arrived in Engi space. The fall of the Federation has brought tough times for these robotic lifeforms, but they're usually willing to help."''

<div class="mw-collapsible-content">
: ''"You have arrived in Engi space. The Mantis have been threatening the Engi core worlds, but you should be able to stock up for your journey."''
</div>
</div>

<div style="font-size:larger;">Sector occurrence:</div>
This sector can occur multiple times per game.

<div style="font-size:larger;">Beacons:</div>
*2-3 stores
*5 various items <!-- 2-2 from "ITEMS" eventList and 3-3 from "ITEMS_ENGI" eventList, which comes after "NOTHING_ENGI" -->
*1-2 empty beacons
*1-3 distress beacons
*1 quest
*4-6 neutral encounters
*5-7 hostile encounters

<div style="font-size:larger;">Events:</div>
See [[:Category:Engi Controlled Sector Events|Engi Controlled Sector Events]]

<span style="font-size:larger;">Crewmembers:</span>
<div style="margin-top:-25px;">In this sector, crewmembers of the following races can be purchased or received as a crew kill reward. By [[Rarity|rarity]] (only affects the store assortment probability), from common to rare:</div>
*1: Engi
*3: Human
*4: Zoltan

<div style="font-size:larger;">Soundtrack:</div>
The following [[Soundtrack|tracks]] can be played in this sector: Engi, Cosmos, Hacking Malfunction.

=== <h2>Engi Homeworlds</h2> ===
<div class="mw-collapsible mw-collapsed">
: ''"You have arrived in Engi space. The Mantis have been threatening the Engi core worlds, but you should be able to stock up for your journey."''

<div class="mw-collapsible-content">
: ''"You have arrived in Engi space. The fall of the Federation has brought tough times for these robotic lifeforms, but they're usually willing to help."''
</div>
</div>

<div style="font-size:larger;">Sector occurrence:</div>
This sector can occur only once per game and only at sector '''3''' or higher.

<div style="font-size:larger;">Beacons:</div>
*1 [[Engi fleet discussion]] event
*2-3 stores
*5 various items <!-- 2-2 from "ITEMS" eventList and 3-3 from "ITEMS_ENGI" eventList, which comes after "NOTHING_ENGI" -->
*1-2 empty beacons
*1-3 distress beacons
*1 quest
*5-7 neutral encounters
*5-7 hostile encounters

<div style="font-size:larger;">Events:</div>
See [[:Category:Engi Homeworlds Events|Engi Homeworlds Events]]

<span style="font-size:larger;">Crewmembers:</span>
<div style="margin-top:-25px;">In this sector, crewmembers of the following races can be purchased or received as a crew kill reward. By [[Rarity|rarity]] (only affects the store assortment probability), from common to rare:</div>
*1: Engi
*3: Human
*4: Zoltan

<div style="font-size:larger;">Soundtrack:</div>
The following [[Soundtrack|tracks]] can be played in this sector: Engi, Cosmos, Hacking Malfunction.

=== <h2>Zoltan Controlled Sector</h2> ===
<div class="mw-collapsible mw-collapsed">
: ''"The Zoltan patrol their borders but let you pass when you ID as Federation. Let's hope they won't be so courteous to the Rebels."''

<div class="mw-collapsible-content">
: ''"You've entered Zoltan territory. This species is not renowned for giving anything for nothing, but you can always be assured a fair hearing."''

: ''"You arrive in Zoltan space. From what you have heard they anticipated the coming war and made preparations to hold their borders."''

: ''"You're far from Federation home space here in Zoltan territory, and it's not clear whether the authorities will have any goodwill remaining. Still, you have to push forward."''
</div>
</div>

<div style="font-size:larger;">Sector occurrence:</div>
This sector can occur multiple times per game.

<div style="font-size:larger;">Beacons:</div>
*1 [[Zoltan research facility]] event
*2 stores
*1-2 empty beacons
*1-2 distress beacons
*2-6 nebula spaces
*6-8 hostile encounters
*1-2 boarders
*1-2 various items
*0-1 quests
*5-6 neutral encounters

<div style="font-size:larger;">Events:</div>
See [[:Category:Zoltan Controlled Sector Events|Zoltan Controlled Sector Events]]

<span style="font-size:larger;">Crewmembers:</span>
<div style="margin-top:-25px;">In this sector, crewmembers of the following races can be purchased or received as a crew kill reward. By [[Rarity|rarity]] (only affects the store assortment probability), from common to rare:</div>
*1: Zoltan
*2: Human
*3: Engi, Mantis, Rockmen, Slug

<div style="font-size:larger;">Soundtrack:</div>
The following [[Soundtrack|tracks]] can be played in this sector: Zoltan, Cosmos.

=== <h2>Zoltan Homeworlds</h2> ===
<div class="mw-collapsible mw-collapsed">
: ''"The Zoltan patrol their borders but let you pass when you ID as Federation. Let's hope they won't be so courteous to the Rebels."''

<div class="mw-collapsible-content">
: ''"You've entered Zoltan territory. This species is not renowned for giving anything for nothing, but you can always be assured a fair hearing."''

: ''"You arrive in Zoltan space. From what you have heard they anticipated the coming war and made preparations to hold their borders."''

: ''"You're far from Federation home space here in Zoltan territory, and it's not clear whether the authorities will have any goodwill remaining. Still, you have to push forward."''
</div>
</div>

<div style="font-size:larger;">Sector occurrence:</div>
This sector can occur only once per game and only occurs at sector '''3 '''or higher.

<div style="font-size:larger;">Beacons:</div>
*1 [[Zoltan research facility]] event
*1 [[Unarmed Zoltan transport]] event
*2 stores
*1-2 empty beacons
*1-2 distress beacons
*2-6 nebula spaces
*6-8 hostile encounters
*1-2 boarders
*1-2 various items
*0-1 quests
*5-6 neutral encounters

<div style="font-size:larger;">Events:</div>
See [[:Category:Zoltan Homeworlds Events|Zoltan Homeworlds Events]]

<span style="font-size:larger;">Crewmembers:</span>
<div style="margin-top:-25px;">In this sector, crewmembers of the following races can be purchased or received as a crew kill reward. By [[Rarity|rarity]] (only affects the store assortment probability), from common to rare:</div>
*1: Zoltan
*2: Human
*3: Engi, Mantis, Rockmen, Slug

<div style="font-size:larger;">Soundtrack:</div>
The following [[Soundtrack|tracks]] can be played in this sector: Zoltan, Cosmos.

== <span style="font-size:larger;">'''Hostile Sectors'''</span> ==

=== <h2>Abandoned Sector</h2> ===
{{Advanced Edition Content|section=yes}}
<div class="mw-collapsible mw-collapsed">
: ''"This sector has been largely abandoned since a series of battles decimated the local population. An unusual alien race is reportedly scavenging in the area. You'd best be on guard."''

<div class="mw-collapsible-content">
: ''"This sector was the site of many major battles between the Federation and Rebel fleets. Strangely, there's very little evidence of those battles remaining..."''

: ''"There have been a number of reports of advanced ships salvaging the wrecks and abandoned mining facilities in this sector. Could it be that the Lanius have resurfaced?"''

: ''"The war tore through this civilian sector, and just recently even the few life signs that remained have begun blinking out. Rumours suggest the Lanius are responsible."''
</div>
</div>

<div style="font-size:larger;">Sector occurrence:</div>
This sector can occur multiple times per game.

<div style="font-size:larger;">Beacons:</div>
*2 stores
*1-2 empty beacons
*1-2 distress beacons
*5-6 hostile encounters
*1-2 hostile environment
*1-2 boarders
*2-4 various items
*0-1 quests
*5-6 neutral encounters

<div style="font-size:larger;">Events:</div>
See [[:Category:Abandoned_Sector_Events|Abandoned Sector Events]]

<span style="font-size:larger;">Crewmembers:</span>
<div style="margin-top:-25px;">In this sector, crewmembers of the following races can be purchased or received as a crew kill reward. By [[Rarity|rarity]] (only affects the store assortment probability), from common to rare:</div>
*2: Lanius, Human
*3: Engi, Mantis, Rockmen
*4: Zoltan, Slug

<div style="font-size:larger;">Soundtrack:</div>
The following [[Soundtrack|tracks]] can be played in this sector: Lanius, Deepspace, Wasteland.

=== <h2>Mantis Controlled Sector</h2> ===
: ''"You've entered a poorly charted area of space that's known to be home to the Mantis. Ensure your hull plating is up to scratch and that you have enough fuel in the tank to make it through."''

<div style="font-size:larger;">Sector occurrence:</div>
This sector can occur multiple times per game.

<div style="font-size:larger;">Beacons:</div>
*1-2 stores
*2-3 empty beacons
*1-3 distress beacons
*6-7 hostile encounters
*1-2 boarders
*1-2 various items
*6-7 neutral encounters

<div style="font-size:larger;">Events:</div>
See [[:Category:Mantis_Controlled_Sector_Events|Mantis Controlled Sector Events]]

<span style="font-size:larger;">Crewmembers:</span>
<div style="margin-top:-25px;">In this sector, crewmembers of the following races can be purchased or received as a crew kill reward. By [[Rarity|rarity]] (only affects the store assortment probability), from common to rare:</div>
*1: Mantis
*2: Human
*3: Engi
*4: Rockmen

<div style="font-size:larger;">Soundtrack:</div>
The following [[Soundtrack|tracks]] can be played in this sector: Mantis, Debris, Void.

=== <h2>Mantis Homeworlds</h2> ===
: ''"You've entered a poorly charted area of space that's known to be home to the Mantis. Ensure your hull plating is up to scratch and that you have enough fuel in the tank to make it through."''

<div style="font-size:larger;">Sector occurrence:</div>
This sector can occur only once per game and only occurs at sector '''3''' or higher.

<div style="font-size:larger;">Beacons:</div>
*1 [[Legendary thief KazaaakplethKilik]] event
*1-2 stores
*2-3 empty beacons
*1-3 distress beacons
*6-7 hostile encounters
*1-2 boarders
*1-2 various items
*6-7 neutral encounters

<div style="font-size:larger;">Events:</div>
See [[:Category:Mantis Homeworlds Events|Mantis Homeworlds Events]]

<span style="font-size:larger;">Crewmembers:</span>
<div style="margin-top:-25px;">In this sector, crewmembers of the following races can be purchased or received as a crew kill reward. By [[Rarity|rarity]] (only affects the store assortment probability), from common to rare:</div>
*1: Mantis
*2: Human
*3: Engi
*4: Rockmen

<div style="font-size:larger;">Soundtrack:</div>
The following [[Soundtrack|tracks]] can be played in this sector: Mantis, Debris, Void.

=== <h2>Pirate Controlled Sector</h2> ===
<div class="mw-collapsible mw-collapsed">
: ''"This somewhat isolated region was thrown into chaos at the start of the rebellion. Even in peacetime it was always beset by pirates but now it houses a center of operations for countless pirate fleets."''

<div class="mw-collapsible-content">
: ''"A few years ago this region was bustling with trade activity. Now it is overrun with bandits and marauders. You should tread lightly here."''

: ''"If the reports are true, this area has been under the control of pirates for quite some time. Some traders still attempt to trade with the few settlements that remain, but they do so at great risk."''

: ''"A few Federation-friendly planets still exist in this sector, but they are constantly under attack by pirate raids. This is a dangerous sector, so be careful."''
</div>
</div>

<div style="font-size:larger;">Sector occurrence:</div>
This sector can occur multiple times per game.

<div style="font-size:larger;">Beacons:</div>
*1-2 stores
*1-2 various items
*6-8 hostile encounters
*1 boarder
*1-2 distress beacons
*0-5 nebula spaces
*1-2 empty beacons
*0-1 quests
*5-6 neutral encounters

<div style="font-size:larger;">Events:</div>
See [[:Category:Pirate_Controlled_Sector_Events|Pirate Controlled Sector Events]]

<span style="font-size:larger;">Crewmembers:</span>
<div style="margin-top:-25px;">In this sector, crewmembers of the following races can be purchased or received as a crew kill reward. By [[Rarity|rarity]] (only affects the store assortment probability), from common to rare:</div>
*1: Human
*2: Engi, Mantis
*3: Rockmen
*5: Zoltan

<div style="font-size:larger;">Soundtrack:</div>
The following [[Soundtrack|tracks]] can be played in this sector: Colonial, Void, Lost Ship, Hacking Malfunction.

=== <h2>Rebel Controlled Sector</h2> ===
<div class="mw-collapsible mw-collapsed">
: ''"You will have to be very cautious in this sector. The Rebels have full control and are no doubt looking for you."''

<div class="mw-collapsible-content">
: ''"This sector was bustling with activity just a few years ago. Now, more than half of the jump beacons have been destroyed, many settlements have been abandoned and the Rebels patrol constantly."''

: ''"This sector was hit hard by the rebellion. The many alien settlements and stations located here are now watched over by almost an equal number of Rebel bases, heavy-handedly 'keeping the peace'."''

: ''"Once the Federation forces were scattered, the Rebels came down hard on the locals here. Between the 'tax collectors' and military bases, the Rebel presence in this sector is high."''

: ''"At one point this was one of the most commonly traveled sectors. Knowing that, the Rebels have stationed a number of fleets here. Be careful."''
</div>
</div>

<div style="font-size:larger;">Sector occurrence:</div>
This sector can occur multiple times per game.

<div style="font-size:larger;">Beacons:</div>
*1-2 stores
*1-2 various items
*6-8 hostile encounters
*1 boarder
*1-2 distress beacons
*0-5 nebula spaces
*1-2 empty beacons
*0-2 quests
*5-6 neutral encounters

<div style="font-size:larger;">Events:</div>
See [[:Category:Rebel Controlled Sector Events|Rebel Controlled Sector Events]]

<span style="font-size:larger;">Crewmembers:</span>
<div style="margin-top:-25px;">In this sector, crewmembers of the following races can be purchased or received as a crew kill reward. By [[Rarity|rarity]] (only affects the store assortment probability), from common to rare:</div>
*1: Human
*2: Engi, Mantis
*3: Rockmen
*5: Zoltan

<div style="font-size:larger;">Soundtrack:</div>
The following [[Soundtrack|tracks]] can be played in this sector: Colonial, Wasteland, Lost Ship, Hacking Malfunction.

=== <h2>Rebel Stronghold</h2> ===
<div class="mw-collapsible mw-collapsed">
: ''"You will have to be very cautious in this sector. The Rebels have full control and are no doubt looking for you."''

<div class="mw-collapsible-content">
: ''"This sector was bustling with activity just a few years ago. Now, more than half of the jump beacons have been destroyed, many settlements have been abandoned and the Rebels patrol constantly."''

: ''"This sector was hit hard by the rebellion. The many alien settlements and stations located here are now watched over by almost an equal number of Rebel bases, heavy-handedly 'keeping the peace'."''

: ''"Once the Federation forces were scattered, the Rebels came down hard on the locals here. Between the 'tax collectors' and military bases, the Rebel presence in this sector is high."''

: ''"At one point this was one of the most commonly traveled sectors. Knowing that, the Rebels have stationed a number of fleets here. Be careful."''
</div>
</div>

<div style="font-size:larger;">Sector occurrence:</div>
This sector can occur only once per game and only at sector '''5''' or higher.

<div style="font-size:larger;">Beacons:</div>
*1 [[Rebel shipyard]] event
*1-2 stores
*1-2 various items
*6-8 hostile encounters
*1 boarder
*1-2 distress beacons
*0-5 nebula spaces
*1-2 empty beacons
*0-2 quests
*5-6 neutral encounters

<div style="font-size:larger;">Events:</div>
See [[:Category:Rebel_Stronghold_Events|Rebel Stronghold Events]]

<span style="font-size:larger;">Crewmembers:</span>
<div style="margin-top:-25px;">In this sector, crewmembers of the following races can be purchased or received as a crew kill reward. By [[Rarity|rarity]] (only affects the store assortment probability), from common to rare:</div>
*1: Human
*2: Engi, Mantis
*3: Rockmen
*5: Zoltan

<div style="font-size:larger;">Soundtrack:</div>
The following [[Soundtrack|tracks]] can be played in this sector: Colonial, Wasteland, Lost Ship, Hacking Malfunction.

=== <h2>Rock Controlled Sector</h2> ===
<div class="mw-collapsible mw-collapsed">
: ''"The Rock people have a particularly aggressive stance toward alien races trespassing in their space. You should tread carefully here."''

<div class="mw-collapsible-content">
: ''"The Rock people are a powerful and proud race. It is not unheard of to have a peaceful journey through their lands, but don't count on it."''
</div>
</div>

<div style="font-size:larger;">Sector occurrence:</div>
This sector can occur multiple times per game.

[[Bomb_(Weapons)#Crystal_Lockdown_Bomb|Crystal Lockdown Bombs]] can be found or bought in this sector, although they have a high rarity (4).

<div style="font-size:larger;">Beacons:</div>
*2 stores
*2-3 empty beacons
*1-2 distress beacons
*6-8 hostile encounters
*1-2 boarders
*1-2 various items
*0-1 quests
*7-8 neutral encounters

<div style="font-size:larger;">Events:</div>
See [[:Category:Rock_Controlled_Sector_Events|Rock Controlled Sector Events]]

<span style="font-size:larger;">Crewmembers:</span>
<div style="margin-top:-25px;">In this sector, crewmembers of the following races can be purchased or received as a crew kill reward. By [[Rarity|rarity]] (only affects the store assortment probability), from common to rare:</div>
*1: Rockmen
*2: Human
*3: Zoltan

<div style="font-size:larger;">Soundtrack:</div>
The following [[Soundtrack|tracks]] can be played in this sector: Rockmen, Wasteland.

=== <h2>Rock Homeworlds</h2> ===
<div class="mw-collapsible mw-collapsed">
: ''"The Rock people have a particularly aggressive stance toward alien races trespassing in their space. You should tread carefully here."''

<div class="mw-collapsible-content">
: ''"The Rock people are a powerful and proud race. It is not unheard of to have a peaceful journey through their lands, but don't count on it."''
</div>
</div>

<div style="font-size:larger;">Sector occurrence:</div>
This sector can occur only once per game and only occurs at sector '''5''' or higher.

[[Bomb_(Weapons)#Crystal_Lockdown_Bomb|Crystal Lockdown Bombs]] can be found or bought in this sector, with an average rarity (2).

<div style="font-size:larger;">Beacons:</div>
*1 [[Ancient device]] event
*1 [[Rock war vessel encounter]] event
*2 stores
*2-3 empty beacons
*1-2 distress beacons
*6-8 hostile encounters
*1-2 boarders
*1-2 various items
*0-1 quests
*7-8 neutral encounters

<div style="font-size:larger;">Events:</div>
See [[:Category:Rock_Homeworlds_Events|Rock Homeworlds Events]]

<span style="font-size:larger;">Crewmembers:</span>
<div style="margin-top:-25px;">In this sector, crewmembers of the following races can be purchased or received as a crew kill reward. By [[Rarity|rarity]] (only affects the store assortment probability), from common to rare:</div>
*1: Rockmen
*2: Human
*3: Zoltan

<div style="font-size:larger;">Soundtrack:</div>
The following [[Soundtrack|tracks]] can be played in this sector: Rockmen, Wasteland.

== <span style="font-size:larger;">'''Nebula Sectors'''</span> ==
In these sectors, visiting a nebula beacon will slow down the [[Rebel Fleet]] by only 20% instead of the regular 50%, since "the Rebel Fleet was prepared for the nebula".

=== <h2>Slug Controlled Nebula</h2> ===
<div class="mw-collapsible mw-collapsed">
: ''"This nebula is home to the telepathic Slugs. They'd sell their own slime for a crate of scrap, but they much prefer to just take it."''

<div class="mw-collapsible-content">
: ''"The only thing that can render a nebula more dangerous is if it's also home to the Slugs. This particular nebula is just that."''

: ''"The Slugs that live in this nebula field are a leisure-centered civilization. Everything in Slug life is done in the pursuit of more currency and more time in which to spend it on extravagant ventures. This, inevitably, leads to much treachery in open space."'

: ''"You're told the Slug home world is somewhere in this nebula. You can't see them, but you know they're watching."''

: ''"The Slugs developed on an ocean planet where the ability to telepathically sense another organism was more important than sight. Today they use this ability to navigate unfettered the depths of the nebulas they inhabit."''
</div>
</div>

<div style="font-size:larger;">Sector occurrence:</div>
This sector can occur multiple times per game and only at sector '''4''' or higher.

<div style="font-size:larger;">Beacons:</div>
*0-1 stores
*2 nebula stores
*0-2 various items
*0-2 empty beacons
*1-2 hostile encounters
*3-4 distress beacons
*2-4 empty nebula beacons
*5-7 nebula hostile encounters
*1-3 storms
*3-5 nebula neutral encounters
*1-2 neutral encounters

<div style="font-size:larger;">Events:</div>
See [[:Category:Slug_Controlled_Nebula_Events|Slug Controlled Nebula Events]]

<span style="font-size:larger;">Crewmembers:</span>
<div style="margin-top:-25px;">In this sector, crewmembers of the following races can be purchased or received as a crew kill reward. By [[Rarity|rarity]] (only affects the store assortment probability), from common to rare:</div>
*2: Slug, Human
*4: Engi, Mantis, Zoltan, Rockmen

<div style="font-size:larger;">Soundtrack:</div>
The following [[Soundtrack|tracks]] can be played in this sector: Slug, Debris, Wasteland, Deepspace.

=== <h2>Slug Home Nebula</h2> ===
<div class="mw-collapsible mw-collapsed">
: ''"You're told the Slug home world is somewhere in this nebula. You can't see them, but you know they're watching."''

<div class="mw-collapsible-content">
: ''"The only thing that can render a nebula more dangerous is if it's also home to the Slugs. This particular nebula is just that."''

: ''"The Slugs that live in this nebula field are a leisure-centered civilization. Everything in Slug life is done in the pursuit of more currency and more time in which to spend it on extravagant ventures. This, inevitably, leads to much treachery in open space."'

: ''"This nebula is home to the telepathic Slugs. They'd sell their own slime for a crate of scrap, but they much prefer to just take it."''

: ''"The Slugs developed on an ocean planet where the ability to telepathically sense another organism was more important than sight. Today they use this ability to navigate unfettered the depths of the nebulas they inhabit."''
</div>
</div>

<div style="font-size:larger;">Sector occurrence:</div>
This sector can occur only once per game and only at sector '''4''' or higher.

<div style="font-size:larger;">Beacons:</div>
*1 [[Slug Home Nebula surrender]] event
*0-1 stores
*2 nebula stores
*0-2 various items
*0-2 empty beacons
*1-2 hostile encounters
*3-4 distress beacons
*2-4 empty nebula beacons
*5-7 nebula hostile encounters
*1-3 storms
*3-5 nebula neutral encounters
*1-2 neutral encounters

<div style="font-size:larger;">Events:</div>
See [[:Category:Slug Home Nebula Events|Slug Home Nebula Events]]

<span style="font-size:larger;">Crewmembers:</span>
<div style="margin-top:-25px;">In this sector, crewmembers of the following races can be purchased or received as a crew kill reward. By [[Rarity|rarity]] (only affects the store assortment probability), from common to rare:</div>
*2: Slug, Human
*4: Engi, Mantis, Zoltan, Rockmen

<div style="font-size:larger;">Soundtrack:</div>
The following [[Soundtrack|tracks]] can be played in this sector: Slug, Debris, Wasteland, Deepspace.

=== <h2>Uncharted Nebula</h2> ===
<div class="mw-collapsible mw-collapsed">
: ''"Nebulas were always dangerous places. Many electronics fail in these clouds. You will have to tread lightly."''

<div class="mw-collapsible-content">
: ''"This nebula must have been an important hub at one point; placing all of these jump beacons would be no easy task. However, now it's hardly navigable."''

: ''"You've entered a sector thick with nebulas. You'll have to navigate on instinct."''

: ''"You've entered a nebula-rich sector. You may put a few light years on the fleet, but that's only useful if you make it out the other side."''

: ''"Thanks to the high nebula density of this sector very little of it has been charted, and rumours of what lurks in the depths abound."''

: ''"The gases that make up the nebulas in this sector threaten to impair your systems; but you have to press on."''
</div>
</div>

<div style="font-size:larger;">Sector occurrence:</div>
This sector can occur multiple times per game.

<div style="font-size:larger;">Sector specifics:</div>
In normal circumstances, this sector will have 1-2 stores. However, issues with map generation mean that about 0.8% will have no stores at all.<ref name="Uncharted Nebula no stores">[https://www.reddit.com/r/ftlgame/comments/vwof4h/uncharted_nebulas_are_even_worse_than_you_think/ Uncharted Nebulas are even worse than you think: ftlgame.]</ref>

<div style="font-size:larger;">Beacons:</div>
*0-1 stores
*1-3 various items
*1 nebula store
*4 empty nebula beacons
*5-6 nebula hostile encounters
*7-8 nebula neutral encounters
*1-3 distress beacons

<div style="font-size:larger;">Events:</div>
See [[:Category:Uncharted_Nebula_Events|Uncharted Nebula Events]]

<span style="font-size:larger;">Crewmembers:</span>
<div style="margin-top:-25px;">In this sector, crewmembers of the following races can be purchased or received as a crew kill reward. By [[Rarity|rarity]] (only affects the store assortment probability), from common to rare:</div>
*1: Human
*3: Slug
*4: Engi, Mantis, Zoltan, Rockmen

<div style="font-size:larger;">Soundtrack:</div>
The following [[Soundtrack|tracks]] can be played in this sector: Void, Deepspace.

== <span style="font-size:larger;">'''Hidden Crystal Worlds'''</span> ==
: ''"You arrive in a sector not listed in any star charts. Strange crystalline ships dot the horizon. Your companion speaks, "Here we are, my home sector. It has been a long time since others have set foot here, I wonder how you will be received."''

<div style="font-size:larger;">Sector occurrence:</div>
This sector can occur only once per game and can only be accessed via the [[Ancient device]] event. The Rebels will continue to follow you through the sector.

<div style="font-size:larger;">Sector specifics:</div>
The Crystal sector is unique in that it is not technically part of the map. Gameplay-wise, it is a standalone sector separate from Rock Homeworlds. Exiting from the Crystal sector will send you to a random sector after the Rock Homeworlds; this sector may not be necessarily connected to the Rock Homeworlds.

In this sector, only [[Crystal (Weapons)|crystal weapons]] (including Lockdown Bomb) can be purchased in [[Stores and resources|stores]] or received as a crew kill reward in [[Random Events|events]].

Bug: restarting the game while staying in the Crystal sector will start the game in a Civilian sector without option to open the Sector Map at the exit beacon when pressing the "Next Sector" button on the Beacon Map, thus preventing the choice of a sector to jump to: the next sector 2 is chosen randomly by the game. (see [https://ftl.fandom.com/wiki/File:Restarting_the_game_from_the_Crystal_Homeworld.png screenshot])

<div style="font-size:larger;">Beacons:</div>
*2-3 stores
*2 various items
*2 empty beacons
*6-10 hostile encounters
*1-2 boarders
*12 neutral encounters

<div style="font-size:larger;">Events:</div>
See [[:Category:Hidden Crystal Worlds Events|Hidden Crystal Worlds Events]]

<div style="font-size:larger;">Crewmembers:</div>
In this sector, only [[Crew_races#Crystal|Crystal crewmembers]] can be purchased or received as a crew kill reward.

<div style="font-size:larger;">Soundtrack:</div>
The following [[Soundtrack|tracks]] can be played in this sector: Debris, Wasteland, Deepspace.

== <span style="font-size:larger;">'''The Last Stand'''</span> ==
: ''"You arrive at an outpost close to the Federation Base. Your access codes get you past initial security and an officer sets up a direct feed to the Federation Base's war room. Admiral Tully speaks first saying, 'What is the meaning of this?! Who are you?'"''

<div style="font-size:larger;">Sector occurrence:</div>
This sector is always sector '''8'''. As the final sector, it can occur only once per game.

<div style="font-size:larger;">Unique Sector behavior:</div>
*At the beginning of this sector, your ship receives <span style="color:limegreen;">10 repairs</span> and you receive {{Transaction|10|add_fuel}}.
*The [[The Rebel Flagship|Rebel Flagship]] appears on the map orbiting a beacon. It spawns on the right side of the sector, and will make a jump every two jumps you make. The next beacon the Flagship will jump to is indicated by a dotted or solid line, depending on if it is jumping this turn. If you end up on the same beacon as the Flagship, you will fight it.
* Rather than gradually moving en-masse from the left of the screen like in every other sector, the [[Rebel Fleet]] overtakes random individual beacons each turn, indicated by flashing red outlines. The Flagship also overtakes any beacon it is on.
*The Federation Base spawns slightly to the right of the centre of the sector. The Flagship will jump towards the base, and if it spends 3 consecutive jumps on the base, you lose the game. The base can never be overtaken by the Rebels, and will return to Federation control if the Flagship is forced off of it. The base itself acts like an empty beacon.
*It is possible to wait at a beacon even if you have fuel. Waiting will cause all map actions to tick forward: the Flagship will jump or prepare to jump, and flashing red beacons will be overtaken. If you end up in a fight after waiting at a beacon, your ship will start the fight with full FTL charge.
*Repair beacons give your ship <span style="color:limegreen;">15 repairs</span> and give you {{Transaction|22-44|add_scrap}} &nbsp;{{Transaction|5|add_fuel}} {{Transaction|4|add_missiles}} {{Transaction|5|add_drones}}. Each beacon can only be used once, and they may be overtaken before you can reach them.

<div style="font-size:larger;">Beacons:</div>
*1 store
*3 repair stations
*6 hostile encounters
*7-10 neutral encounters

<div style="font-size:larger;">Events:</div>
See [[:Category:The_Last_Stand_Events|The Last Stand Sector Events]]

<span style="font-size:larger;">Crewmembers:</span>
<div style="margin-top:-25px;">In this sector, crewmembers of the following races can be purchased or received as a reward. By [[Rarity|rarity]], from common to rare:</div>
*1: Human
*2: Engi, Mantis
*3: Rockmen
*5: Zoltan

<div style="font-size:larger;">Soundtrack:</div>
The [[Soundtrack|track]] ''Last Stand'' is continuously played in this sector.

== <span style="font-size:larger;">'''Technical details of sector generation and events'''</span> ==
Before anything else, beacons are placed on the map. The map is divided into a [https://www.reddit.com/r/ftlgame/comments/fcfdt3/how_the_beacon_map_is_generated/ 6 * 4 grid]. For each grid square, there is an 80% chance to place a beacon at a random position in the square. If too many empty squares already exist, however, the current square cannot be empty. When a beacon is placed, it is connected to all the beacons in adjacent squares that are within 165 pixels. <ref>https://gitlab.com/znixian/xftl/-/blob/master/doc/sector-map?ref_type=heads</ref> 

Beacons are then assigned events based on the order that events are specified in the sector definition (but see nebula generation, below). Each line is either a specific event, or a list of events; and each specifies a minimum and maximum number of occurrences in the sector. The game will randomly choose between the minimum and maximum numbers (inclusive). Note that this wiki page does '''not''' completely reflect the actual order of events in the game files.

When a list of events is used, an event will be picked at random from that list. The same event can be picked multiple times without limit, unless it is specified as a unique event. Unique events can only occur once per sector, but can occur again in a later sector.

After fully populating a line of events, the game will move on to the next line. This is why stores and special events (such as homeworlds events) are listed at the top of the sector event definitions. It ensures those events will always be present in the sector.

Once all beacons on the map have been assigned events, the process stops. No additional beacons will be generated. That means it's possible, with modding, to create "unreachable" events, simply by listing too many in the sector definition. This also explains why some events, such as [[Zoltan wise man]] and the [[Auto-ship carrying shield virus|Shield Virus]], are much less common than others. Not only are they unique events that can only occur once per sector, but also they are called from an event list near the bottom of the sector definition.

=== <h2>Nebula generation</h2> ===
Nebula beacons are the one major exception to this logic.

Any event list that starts with "NEBULA_" will generate nebula beacons on the map. When you arrive at a beacon, however, the existence of a nebula environment is specified by the event itself. This sometimes leads to confusing situations, where you jump to a non-nebula beacon but still land in a nebula environment.

All the event lists starting with "NEBULA_" are processed first, regardless of the order of events in the sector definition. This is because the game has to generate purple cloud graphics on the map. When the game places these graphics, they will sometimes overlap non-nebula beacons. Those beacons will be converted to additional nebula beacons, and will be assigned events from the [[:Category:Nebula Filler Events|default "NEBULA" event list]].

After this process of nebula generation is finished, the sector generation will continue as described above.

=== <h2>Fallback events</h2> ===
Sometimes the game can reach the end of the sector definition, and still have beacons left over that have not been assigned events.

Those beacons will then be assigned events from the "NEUTRAL" event list, which is used as a fallback. In Advanced Edition, the [[:Category:Filler_Events|"OVERRIDE_NEUTRAL" list]] replaces it.

=== <h2>Exit beacon events</h2> ===
These are not specified in the sector definition. Instead, they are chosen from an event list shared between all sectors, called "[[:Category:Exit Beacon Events|EXIT_LIST]]".

Exit beacons can be located in a nebula. This only happens when the exit beacon location is covered by nebula cloud graphics on the sector map. Exits at a nebula beacon will always be an empty event (nothing happens, unless the exit is overtaken by the Rebel Fleet).

== <span style="font-size:larger;">'''References'''</span> ==
{{reflist}}
[[Category:Mechanics]]
