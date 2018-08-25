import os
import keyboard
import random
import time
from datetime import datetime
clear = lambda: os.system('cls')

def main():
	#         X  Y  Icon
	#         0  1   2
	player = [6, 7, "@"]
	map = []
	name = input("What's your name? : ")

	worlds = [
		[	"................................................................M ",
			"......                                                           ",
			"......                                                           ",
			"......                                                           ",
			"......                                                           ",
			"......                                                           ",
			"......                                                           ",
			"......                                                           ",#World 0
			"......                                                           ",
			"......                                                           ",
			" !!!                                                             ",
			"                                                                 "
		],[
			"    #@@@#                                                        ",
			"#####...##########################                               ",
			">................................#                               ",
			">..................######........#                               ",
			">.......................##########                               ",
			"~~~~~~>......................$                                   ",
			"~~~~~~>......................$                                   ",
			">............#################                                   ", #World 1
			">......#.....#                                                   ",
			">......#.....#                                                   ",
			"##############                                                   ",
			"                                                                 "
		],[
			"W#########################################                       ",
			".........................................#                       ",
			"....                                ....#                        ",
			"....                                ....###########****##########",
			"......###############...........................................#",
			"~~~~..###.......................................................#",
			"!.....###############...........................................#", #World 2
			"!...............................................................#",
			"~~~~                                    ~~~~~~~                 #",
			"                                                                 ",
			"                                                                 ",
			"                                                                 "
		],[
			"##############                                                   ",
			".............0                                                  ",
			".............#                                                   ",
			"......####.                                                      ",
			"......####.                                                      ",
			"..........                                                       ", #World 3
			"......                                                           ",
			"......                                                           ",
			"......                                                           ",
			"...                                                              ",
			".                                                                ",
			"$                                                                " 
		],[
			"       ###################################                       ",
			"       ..................................#                       ",
			"W........                               *                        ",
			"###......                                                        ",
			"###   ...#########.........   ..................                 ",
			"      .........................................                  ",
			"      ###############..............................              ",
			"   ...........................................                   ", #World 4
			"                         ......                                  ",
			"                         ......                                  ",
			"                           ..                                    ",
			"                           ##                                    "
		],[
			"                            ##############         MMMM#         ",
			"###0                         .............#        ....#         ",
			"....                        .       .... ###       ....#         ",
			"....                        .       .....######    ....##########",
			".                    ...........................................#",
			".     ###.......................................................#", #World 5
			"......###            ...........................................#",
			"    ..         ....  ..            .........................     ",
			"    ....       . ..  ..            .........................     ",
			"       ......... ..  ..                            ....          ",
			"                 ..  ..                            ....          ",
			"                 ......                            $$$$          "
		],[
			"@.......                                             .....       ",
			"      ..     .......            ............         .   .       ",
			"      ..   ...  .  .            .          .         .   .       ",
			"      ........     .      ....  .          .  ........   .       ",
			"      ..           .      .  .  .          .  .          .       ",
			"      ..      ......      .  ....          .  .   ........       ",
			"      ..      .           .                .  .   .              ", #World 6
			"      ..      .           .       ..........  .   .............. ",
			"      ..      .............       .           .                . ",
			"###   ..                          .           .                . ",
			"##[.....                          .           .             .... ",
			"###                               .............             **** "
		]
	]

	triggersRaisin = [
	#   From To ΔX   ΔY
	#    0   1  2    3
		[1,  2, -29,  1],
		[1,  0,  -4, 10],
		[2, 5,  0 , 8],
		[2, 3, 0, 11], 
		[0, 6,  -64,  0],
		[6, 5,   -9,-11],
		[5, 4,  37 , 1], 
		[3, 4, -13, 1] 
	] 

	getOutofHere = ["@","!","$","W","0","*","M"]

	whereYouAt = False #boolean that defines if the player has just changed maps
	wuhtChuWant = False #boolean that tells us if you don't want to pick up an item

	item_high = 35
	item_low = 0

	max_y = 11
	max_x = 65

	maxHP = 10
	currentHP = 10
	attack = 10
	defense = 0
	level = 0 
	XP = 0
	
	
	items = [
		#name  #HP increase  #attack increase  #defense increase  #level increase #XP increase #rarity #quantity 
		["a pouch of Capri Sun", 2, 0, 0, 0, 0, 0, 20, 0],
		["a half eaten chocolate bar", 2, 1, 0, 0, 0, 0, 10, 0],
		["something you really shouldn't be putting in your mouth", -1, 0, 0, 0, 0, 12, 20,0],
		["a pack of Fruit Gushers", 2, 0, 0, 0, 0, 0, 20, 0]
	]

	shieldid = 0  #current shielf
	shields = [
		#name        #def increase
		["no shield", 0],
		["a paper plate", 1],
		["a paper bag", 2],
		["last week's newpaper",2],
		["a clipboard", 2],
		["an umbrella", 1],
		["a trash can lid", 2],
		["a white board",1],
		["a captain America shield", 2]

	]

	swordid = 0 #current sword
	swords = [
		# name       #attack increase
		["no weapon", 0],
		["an unopened toothpick", 2],
		["a spork from Wendy's", 2],
		["a butterknife from Denny's", 2],
		["a pack of pencils bound with a rubberband", 2],
		["a heavy switchblade that you don't know how to open",1],
		["a large bag of expired candy",1],
		["A baseball bat", 3]
	]
	
	status = "\nStatus: ready to mingle" 

	logThatStuff("has started playing the game ")
	
	for world in range(len(worlds)):
		numitems = random.randint(item_low,item_high) 
		mapNum = world
		map = worlds[mapNum][:]
		for _ in range(numitems):
			while True:
				itemx = random.randint(0, max_x-1)
				itemy = random.randint(0, max_y-1)
				if getTileAt(itemx, itemy) == ".":
					worlds[world] = placeCharacter("+", itemx, itemy, worlds[world])
					break
					
					
			
	mapNum = 1
	map = worlds[mapNum][:]
	drawMap() #draws map original instance

	while True:

		currentx = player[0]
		currenty = player[1]
	
		if keyboard.is_pressed('d') and not defineWalls(getTileAt(player[0] + 1, player[1])) : #allows movement to the right if d is pressed and there is no barrier 
			player[0] += 1
		
		if keyboard.is_pressed('a') and not defineWalls(getTileAt(player[0] - 1, player[1])): #allows movement to the left if a is pressed and there is no barrier 
			player[0] -= 1
		
		if keyboard.is_pressed('w') and not defineWalls(getTileAt(player[0], player[1] - 1)): #allows movement up if w is pressed and there is no barrier 
			player[1] -= 1
		
		if keyboard.is_pressed('s') and not defineWalls(getTileAt(player[0], player[1] + 1)): #allows movement down if s is pressed and there is no barrier 
			player[1] += 1
		
		if player[0] != currentx or player[1] != currenty:
			if newRoom(getTileAt(player[0], player[1])) == -1:
				whereYouAt = False
			wuhtChuWant = False
			drawMap()
		
		if wuhtChuWant == False and getTileAt(player[0], player[1]) == "+":
			status = "You found an item! (press space)"
			print(status)
			while True:
				if keyboard.is_pressed(' '):
					break
			status = "Would you like to pick it up? (Y or N)"
			print(status)
			while True:
				if keyboard.is_pressed('y'):
					thing = generateItem()
					if thing >=0:
						print("You found " + items[thing][0] + ". You can put this in your mouth!") 
						items[thing][8] = (items[thing][8]+1)
						logThatStuff("has picked up a consumeable item ")
					elif thing == -1:
						if swordid < len(swords)-1:
							swordid +=1
							print("You found " + swords[swordid][0] + "! You can swing this like a sword!")
							print("You increased your attack by " + str(swords[swordid][1]) + ".")
							attack += swords[swordid][1]
							logThatStuff("has picked up a sword ")
						else: 
							thing = -89
					elif thing != -89: #this is a shield 
						if shieldid < len(shields)-1:
							shieldid +=1
							print("You found " + shields[shieldid][0] + "! You can use this as a shield!")
							print("You increased your defense by " + str(shields[shieldid][1]) + ".")
							defense += shields[shieldid][1]
							logThatStuff("has picked up a shield ")
						else: 
							thing = -89
					if thing == -89:
						a = random.randint(0,11)
						print("Oh... It's just " + ["a used napkin. It's got a mustard stain","an empty video game case. Wish there was something to play","a broken bottle. Looks sort of like dad's", "a plastic cup. There's still coffee in it","a battery. Something is oozing out of it", "an entire tire. I can't carry this","a burnt cigarette. My teacher said not to touch this","a match box. It is empty though..","a used bottle rocket. Who shot this off..","a 10 piece mcNugget! It's empty..","a plastic spoon. It's melted on the bottom", "a crumpled up piece of paper. It reads Ev__t_on N_t_ce. You can't quite make it out"][a] + ". Better put it back.")
					placeCharacter(".", player[0], player[1], worlds[mapNum])
					placeCharacter(".", player[0], player[1], map)
					logThatStuff("has picked up trash ... and put back down ")
					break
				if keyboard.is_pressed('n'):
					wuhtChuWant = True
					drawMap()
					break

	
		loadMap(newRoom(getTileAt(player[0], player[1])))



def couldBeAWallFam():
	return	

def logThatStuff(whatHappened):
	global name
	file = open("Log.txt", "a+")
	file.write("\n" + name + " "+  whatHappened + " at " + str(datetime.now()))
	

def replaceNth(row, index, replacement):
	return row[:(index-1)] + replacement + row[(index):]

def getTileAt(x, y):
	global max_x, max_y
	if x < 0 or y < 0 or x > max_x or y > max_y:
		return "#"
	return map[y][x-1] #returns character that is one tile next to the player's current location. Direction determined by arguments.

def loadMap(newWorld):
	global map, mapNum, whereYouAt
	if newWorld == -1 or whereYouAt == True:
		return
	else:
		whereWeWereAMomentAgo = mapNum
		mapNum = newWorld
		map = worlds[newWorld][:]
		for grape in range(len(triggersRaisin)):
			if triggersRaisin[grape][0] == whereWeWereAMomentAgo and triggersRaisin[grape][1] == newWorld:
				player[0] += triggersRaisin[grape][2]
				player[1] += triggersRaisin[grape][3]
				break
			if triggersRaisin[grape][1] == whereWeWereAMomentAgo and triggersRaisin[grape][0] == newWorld:
				player[0] -= triggersRaisin[grape][2]
				player[1] -= triggersRaisin[grape][3]
				break
		logThatStuff("entered into world " + str(worlds[newWorld]))
		drawMap()
		whereYouAt = True
		
def drawUI():
	global status, maxHP, currentHP
	if currentHP > maxHP/2:
		status = "\nStatus: Let's go on an adventure!"
	if currentHP == maxHP/2:
		status = "\nStatus: Just a little longer. You're doing great!"
	if currentHP < maxHP/2:
		status = "\nStatus: You don't feel so good."
	if currentHP == 1:
		status = "\nStatus: !!!!!!!!!!!!"
	global attack, defense, level, XP, swordid, swords, shieldid, shields
	print( "Level: " + str(level) + " -- Current HP: " + str(maxHP) + " -- Current Attack: " + str(attack) + " -- Current Defense: " + str(defense) + " -- Current XP: " + str(XP) )
	print(status)
	print("\nWeapon: " + swords[swordid][0])
	print("Shield: " + shields[shieldid][0] + "\n")
	
		#do this before and after inventory block but only when items exist -- print("******************************************************************************************************************** \n")
	for _ in range(len(items)):
		if items[_][8] > 0:
			print(str(items[_][0]) + ": " + str(items[_][8]) + "\n")
	
def placeCharacter(character, xCoor, yCoor, display):
	display[yCoor] = replaceNth(display[yCoor], xCoor, character) #places character on map
	return display #returns map with character placed on it
	
def drawMap():
	clear() #clears map
	display = map[:] #copies map to display
	
	for trigger in range(len(getOutofHere)):
		for row in range(len(display)):  #feeds rows to display to read
			display[row] =display[row].replace(getOutofHere[trigger], ".") #does the thing
	display = placeCharacter("@", player[0], player[1], display) 			
	for row in range(len(display)): 
		print(display[row]) #prints display
		
	drawUI()
	
	time.sleep(.085)#delays input receptor so that character moves naturally
	
def defineWalls(tile):
	notQuiteMap = ["#","~",">"," "]
	return tile in notQuiteMap #returns true if it's a wall
	
def newRoom(tile):
	if tile in getOutofHere:
		return getOutofHere.index(tile) #returns true if this tile exists
	else:
		return -1
		
def generateItem(): #sword is -1, shield -2, item -3, piece of trash -89
	whatKindofStuff = random.randint(0,5)
	if whatKindofStuff == 1:
		return -1
	elif whatKindofStuff == 2:
		return -89
	elif whatKindofStuff == 3:
		return -2
	else:
		quoteunquoteTREASURE = []
		for target in range(len(items)):
			for _ in range(items[target][7]):
				quoteunquoteTREASURE.append(target)
		trashroulette = random.randint(0, len(quoteunquoteTREASURE)-1)
		return quoteunquoteTREASURE[trashroulette]

	
	#TODO -- add logging when item is used
	#TODO -- add logging when enemy is defeated
	#TODO -- add logging when you 
	#Battle Sequences
	#Store score 
	#key to pizza place
	#toggle map/inventory
		#consume items/ discard
		
# cd Desktop/Python Files/Final 2