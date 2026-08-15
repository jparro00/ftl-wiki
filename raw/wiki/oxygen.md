<!-- Retrieved from the FTL Fandom wiki via api.php on 2026-08-14. Source layer: do not edit. -->
Title: Oxygen
URL: https://ftl.fandom.com/wiki/Oxygen
Categories: Systems
Revision: 74853
Retrieved: 2026-08-14

---
[[File:OxygenCircle.png]] Oxygen is a key element on most ships. All crew members require oxygen to prevent suffocation, except [[Drone_Control#Drone_Schematics|crew and boarding drones]] and [[Races/Crew#Lanius|Lanius]].

==Overview==
<onlyinclude>
* Functioning Oxygen system replenishes the ship's oxygen (O<sub>2</sub>) supply.
* The color of the room indicates the current O<sub>2</sub> level: white - maximum, pink/red - lower, red lines across the room - 5% or less O<sub>2</sub>.
** The "''O2 LOW!''" warning appears when the total O<sub>2</sub> percentage on the ship drops below 25%.
** A room's O<sub>2</sub> level decreases when: the room has fires (0.96% O<sub>2</sub> every second per fire in the room); there is a breach or a Lanius in the room (both have the same O<sub>2</sub> draining rate)<!-- @to-do: what is the oxygen drains speed? -->; a door to another room with lower O<sub>2</sub> level is open; the Oxygen system is unpowered or hacked; there is an open airlock in a connected room with opened door (an airlock instantly drains the O<sub>2</sub> in the room it is opened in, and quickly drains the O<sub>2</sub> from the connected rooms with opened doors; more airlocks drain the O<sub>2</sub> from farther rooms quicker; the drain speed surpasses that of several Lanius and breaches); the Oxygen system is unpowered.
** If the Oxygen system is unpowered, the ship's O<sub>2</sub> level drops by 1.2% every second in every room.
** A functioning level 1 Oxygen system replenishes the O<sub>2</sub> at 1.2% rate every second in every room.
* Crew suffocation occurs at 5% or less O<sub>2</sub> in the room. Suffocating crewmembers take 6.4 HP damage per second.
** A functioning level 1 Medbay negates the suffocation damage in an airless Medbay. Level 2 Medbay will slowly heal the crew.
** Boarders and your mind-controlled crew will attempt to move out of O<sub>2</sub>-deprived rooms to reach rooms with 10% or more O<sub>2</sub>.
** [[Augmentations#Emergency Respirators|Emergency Respirators]] (Advanced Edition content) augmentation halves the suffocation damage of your crew<!-- @to-do: test if enemy mind-controlled crew benefits from the augmentation while being MC-ed or even afterwards -->; also works when boarding the enemy ships.
** The Crystal race takes half of the suffocation damage. With Emergency Respirators they take only 25% of the suffocation damage.
** The Lanius race doesn't need O<sub>2</sub>, nor suffers from suffocation - they drain the O<sub>2</sub> instead (at the rate of a breach).
* Fires begin to die out when a room has less than 10% O<sub>2</sub>. (see [https://pastebin.com/iP6EnKm4 details])
* If a room is totally vented, opening a nearby room with some oxygen will speed up the O<sub>2</sub> recovery; more opened rooms with higher O<sub>2</sub> levels connected to the vented room will speed up the O<sub>2</sub> recovery even more<!-- @to-do: test if higher O2 levels in the connected rooms have more impact compared to if they had just barely some; what is the cut-off O2 value when the oxygen stabilization between rooms doesn't occur - e.g. does a 3% O2 room equalize O2 if it is adjacent to an opened 0% O2 room? -->; a long pathway of rooms with O<sub>2</sub> connected to the vented room has the biggest impact on the O<sub>2</sub> recovery (the longer the pathway of consecutively connected opened-doors rooms with O<sub>2</sub>, the bigger the impact).
* When a room has a breach (or a Lanius), the O<sub>2</sub> level drop in the room can be slowed down by opening doors of adjacent rooms with O<sub>2</sub>. Opening multiple rooms with O<sub>2</sub> slows down the O<sub>2</sub> level drop in the breached room more, at the expense of lowering their O<sub>2</sub> levels. A long pathway of consecutively connected opened-doors rooms with O<sub>2</sub> slows down the O<sub>2</sub> level drop in the breached room the most (the longer, the better).
* During FTL Jump:
** The ship's oxygen level is not affected by the Oxygen system status (i.e. whether it is on or off) and the rooms' O<sub>2</sub> levels are not being equalized.
** Opened airlocks, breaches/Lanius, and fires drain O<sub>2</sub>; though the ship's O<sub>2</sub> level will be updated only after the Jump, the crew will be taking suffocation damage as usual.
** Fires can die out due to low O<sub>2</sub> level in a room (and can also spread naturally).
* Upgrading the system increases the O<sub>2</sub> refill rate.
** The refill multipliers for level-2 and level-3 Oxygen system in the ship upgrade menu are incorrect: Oxygen-2 refills O<sub>2</sub> 4x faster than Oxygen-1, and Oxygen-3 refills 7x faster.
** Oxygen-2 can counter the O<sub>2</sub> loss due to a breach (or one Lanius) if enough adjacent rooms with O<sub>2</sub> are opened or if there is a long enough pathway of consecutively connected opened-doors rooms with O<sub>2</sub>.
** Oxygen-2 refills the O<sub>2</sub> level fast enough to counter the O<sub>2</sub> drain even from Hacking-3 disruption pulse.
** Oxygen-2 prevents fires from dying out. (the O<sub>2</sub> refill rate surpasses the O<sub>2</sub> loss caused even by 4 fires)
** Oxygen-3 refill rate exceeds the O<sub>2</sub> loss from a breach (or one Lanius) without requiring the room's doors being opened (although it might take a while to refill a fully-vented room).
* Upgraded Oxygen system can be used as a blue option in some [[Blue_Options#Oxygen|events]].
* Can be upgraded in [[Federation terraforming team C12]] and [[Specialty work on your ship]] events.</onlyinclude>

==System Upgrades==
{| class="article-table" style="text-align:center;" border="0" cellpadding="1" cellspacing="1"
|-
! scope="col" style="text-align:center;" |Level
! scope="col" style="text-align:center;" |Cost
! scope="col" style="text-align:center;" |Oxygen refill rate
|-
|1
| -
|1.2%/sec
|-
|2
|25 [[File:Ftlgame-scrap.png]]
|4.8%/sec
|-
|3
|50 [[File:Ftlgame-scrap.png]]
|8.4%/sec
|}

==See also==
* Reverse-engineered [https://gitlab.com/znixian/xftl/-/blob/master/doc/oxygen Oxygen data]
* Wiki articles: [[Fires]], [[Venting]]
[[Category:Systems]]
