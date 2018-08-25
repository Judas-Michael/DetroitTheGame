import os
import keyboard
import random
import time
import urllib.request
from datetime import datetime
clear = lambda: os.system('cls')
color = lambda: os.system('color 4F')
exit = False

#         X  Y  Icon
#         0  1   2
player = [6, 7, "@"]

							# X		Y	Type	CurrentHP 	World
enemies_currently_generated = []
map = []
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
item_low = 1

max_y = 11
max_x = 65

maxHP = 10
currentHP = 10
attack = 2
defense = 0
level = 0 
XP = 0

enemies = [ #description of enemy                               #HP #Attack #defense #XP worth #rarity #character
	["a medium sized raccoon. It stares at you with its eyes", 10,    3,      2,      20,     15,  "D", "%"],
	["a swarm of angry squirrel. They're making buzzing noises",10,     2,    3 ,      15,     20, "O", "%"],
	["a passed out homeless person",                            10,    0,     1,       5,      25, "L", "&"],
	["a young child who's lost their mother. They're shouting at you" ,8, 4,  1,      15,       15,"G", "&"],
	["a cow. Why is there a cow???",                            15,  1 ,     3,      15,        15,"F", "%"],
	["a tourist asking for directions. You have no idea how to help", 10, 2,  4,   15,          15,"H", "&"],
	["a teenager that just got off their shift at Taco Bell. Where's your crunch wrap?", 8, 5, 2, 20, 15,"J", "&"] #Note character is not what is displayed
]

items = [
	#name  #HP increase  #attack increase  #defense increase  #level increase #XP increase #rarity #quantity 
	["a pouch of Capri Sun", 2, 0, 0, 0, 0, 20, 0],
	["a half eaten chocolate bar", 2, 1, 0, 0, 0, 10, 0],
	["something you really shouldn't be putting in your mouth", -2, 0, 0, 0, 12,20, 0],
	["a pack of Fruit Gushers", 2, 0, 0, 0, 0, 20, 0]
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
	["a pack of unsharpened pencils bound with a rubberband", 2],
	["a heavy switchblade that you don't know how to open",1],
	["a large bag of expired candy",1],
	["a baseball bat", 3]
]

name = ""

mapNum = 1

password = False

Trash_Counter = 0

enemies_in_worlds = [0,0,0,0,0,0,0] 

def main():
	global mapNum, name, clear, player, map, worlds, triggersRaisin, getOutofHere, whereYouAt, wuhtChuWant, item_high, item_low, max_y, max_x, maxHP, currentHP, attack, defense, level, XP, items, shieldid, shields, swordid, swords
	highScoresHere()
	name = input("What's your name? : ")
	logThatStuff("has started playing the game ")

	trashGenerator()
	
	
	mapNum = 1
	
	map = worlds[mapNum][:]
	weShouldAddSomeEnemies()
	drawMap() #draws map original instance

	while not exit:
		readKeyStrokes()
		
def readKeyStrokes():
	global player, wuhtChuWant, whereYouAt, password

	currentx = player[0]
	currenty = player[1]
	
	if keyboard.is_pressed('d') and not defineWalls(getTileAt(player[0] + 1, player[1])): #allows movement to the right if d is pressed and there is no barrier 
		player[0] += 1
		
	if keyboard.is_pressed('a') and not defineWalls(getTileAt(player[0] - 1, player[1])): #allows movement to the left if a is pressed and there is no barrier 
		player[0] -= 1
		
	if keyboard.is_pressed('w') and not defineWalls(getTileAt(player[0], player[1] - 1)): #allows movement up if w is pressed and there is no barrier 
		player[1] -= 1
		
	if keyboard.is_pressed('s') and not defineWalls(getTileAt(player[0], player[1] + 1)): #allows movement down if s is pressed and there is no barrier 
		player[1] += 1
	
	if not keyboard.is_pressed('d') and not keyboard.is_pressed('a') and not keyboard.is_pressed('w') and not keyboard.is_pressed('a'):
		omNomTheNomNoms()
	
	if player[0] != currentx or player[1] != currenty:
		thetypeofbadguywearefacing = isThereABADGUYhere(player[0],player[1])
		if thetypeofbadguywearefacing >= 0:
			player[0] = currentx
			player[1] = currenty
			timeToFight(thetypeofbadguywearefacing)
			time.sleep(1/2)
		else:
			if newRoom(getTileAt(player[0], player[1])) == -1:
				whereYouAt = False
			wuhtChuWant = False
		hesGonnaGetChu()
		drawMap()
	
	if wuhtChuWant == False and getTileAt(player[0], player[1]) == "+": #allows player to pick up an item or leave it. If picked up it is removed from the board
		status = "You found an item! (press space)" #I did it for aesthetics
		print(status)
		while True:
			if keyboard.is_pressed(' '):
				break
		status = "Would you like to pick it up? (Y or N)"
		print(status)
		
		giveRandomItem()
		
	
	if wuhtChuWant == False and getTileAt(player[0], player[1]) == "x":  #This mimicks picking up an item, but it's a key item -- the password
		status = "You found an item! (press space)" #I did it for aesthetics
		print(status)
		while True:
			if keyboard.is_pressed(' '):
				break
		status = "Would you like to pick it up? (Y or N)"
		print(status)
		password = thePasswordIsInWorld4()
		
	
		
	checkForPizzaPlace()

	loadMap(newRoom(getTileAt(player[0], player[1])))

def trashGenerator():
	global worlds, mapNum, item_low, item_high, map 
	for world in range(len(worlds)):
		numitems = random.randint(item_low,item_high) 
		mapNum = world
		map = worlds[mapNum][:]
		for _ in range(numitems): #this bit of code decides how much trash will be on each level and then it puts it on the map at a random x/y coordinate that is also not a wall ect
			while True:
				itemx = random.randint(0, max_x-1)
				itemy = random.randint(0, max_y-1)
				if getTileAt(itemx, itemy) == ".":
					worlds[world] = placeCharacter("+", itemx, itemy, worlds[world])
					break
		if mapNum == 4:
			while True:
				itemx = random.randint(0, max_x-1) #This does the same thing, but only in world 4 after a certain x/y coordinate. This randomly generates the location of the password
				itemy = random.randint(0, max_y-1)
				if itemx>20 and itemy>4:
					if getTileAt(itemx, itemy) == ".":
						worlds[world] = placeCharacter("x", itemx, itemy, worlds[world])
						break
					
def giveRandomItem():
	global items, swords, shields, swordid, shieldid, attack, defense, wuhtChuWant, Trash_Counter
	while True:
		if keyboard.is_pressed('y'):
			thing = generateItem()
			if thing >= 0: #this is a consumeable item
				print("You found " + items[thing][0] + ". You can put this in your mouth!") 
				items[thing][7] = (items[thing][7]+1) #adds to inventory
				logThatStuff("has picked up a consumeable item ")
			elif thing == -1:
				if swordid < len(swords)-1: #this is a sword
					swordid += 1 #upgrades your sword
					print("You found " + swords[swordid][0] + "! You can swing this like a sword!")
					print("You increased your attack by " + str(swords[swordid][1]) + ".")
					attack += swords[swordid][1] #upgrades your attack
					logThatStuff("has picked up a sword ")
				else: 
					thing = -89
			elif thing != -89: #this is a shield 
				if shieldid < len(shields)-1:
					shieldid += 1 #upgrades shield
					print("You found " + shields[shieldid][0] + "! You can use this as a shield!")
					print("You increased your defense by " + str(shields[shieldid][1]) + ".")
					defense += shields[shieldid][1] #upgrades defense
					logThatStuff("has picked up a shield ")
				else:
					thing = -89
			if thing == -89:
				a = random.randint(0,11)
				Trash_Counter +=1 #this counts how much garbage you've encountered 
				print("Oh... It's just " + ["a used napkin. It's got a mustard stain","an empty video game case. Wish there was something to play","a broken bottle. Looks sort of like dad's", "a plastic cup. There's still coffee in it","a battery. Something is oozing out of it", "an entire tire. I can't carry this","a burnt cigarette. My teacher said not to touch this","a match box. It is empty though..","a used bottle rocket. Who shot this off..","a 10 piece mcNugget! It's empty..","a plastic spoon. It's melted on the bottom", "a crumpled up piece of paper. It reads Ev__t_on N_t_ce. You can't quite make it out"][a] + ". Better put it back.")
			placeCharacter(".", player[0], player[1], worlds[mapNum])
			placeCharacter(".", player[0], player[1], map)
			logThatStuff("has picked up trash ... and put back down ") 
			break
		if keyboard.is_pressed('n'):
			wuhtChuWant = True
			drawMap()
			break
					
def couldBeAWallFam():
	return	

def logThatStuff(whatHappened): #creates a log of when characters do things
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
	else: #this puts you on a new map
		whereWeWereAMomentAgo = mapNum 
		mapNum = newWorld
		map = worlds[newWorld][:]
		for grape in range(len(triggersRaisin)): #This is a joke. It's an array within an array. I decided those are called raisins 
			if triggersRaisin[grape][0] == whereWeWereAMomentAgo and triggersRaisin[grape][1] == newWorld: 
				player[0] += triggersRaisin[grape][2]
				player[1] += triggersRaisin[grape][3]
				break
			if triggersRaisin[grape][1] == whereWeWereAMomentAgo and triggersRaisin[grape][0] == newWorld:
				player[0] -= triggersRaisin[grape][2]
				player[1] -= triggersRaisin[grape][3]
				break
		logThatStuff("entered into world " + str(worlds[newWorld]))
		weShouldAddSomeEnemies()
		drawMap()
		whereYouAt = True
		
def drawUI(): #this is the stuff the player sees under the map and is interactable 
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
	print( "Level: " + str(level) + " -- Current HP: " + str(currentHP) +"/" + str(maxHP)+ " -- Current Attack: " + str(attack) + " -- Current Defense: " + str(defense) + " -- Current XP: " + str(XP) )
	print(status)
	print("\nWeapon: " + swords[swordid][0])
	print("Shield: " + shields[shieldid][0] + "\n")
	
		#do this before and after inventory block but only when items exist -- print("******************************************************************************************************************** \n")
	individualtypesofitem = 0
	for _ in range(len(items)): #this adds items and sees how many types of items you have
		if items[_][7] > 0:
			individualtypesofitem += 1
			print("[" + str(individualtypesofitem) + "] " + str(items[_][0]) + " (" + str(items[_][7]) + "x)")
			
	if password is True:
		print("A scrap of paper")
	
def placeCharacter(character, xCoor, yCoor, display): 
	display[yCoor] = replaceNth(display[yCoor], xCoor, character) #places character on map
	return display #returns map with character placed on it
	
def drawMap():
	global player, mapNum
	clear() #clears map
	display = map[:] #copies map to display
	
	for trigger in range(len(getOutofHere)):
		for row in range(len(display)):  #feeds rows to display to read
			display[row] = display[row].replace(getOutofHere[trigger], ".") #makes loading zones look like floor!!
			display[row] = display[row].replace("x", "+") #replaces password with trash symbol
			
	for monster in range(len(enemies_currently_generated)):
		if enemies_currently_generated[monster][4] == mapNum and enemies_currently_generated[monster][1] >= 0:
			display = placeCharacter(enemies_currently_generated[monster][2], enemies_currently_generated[monster][0], enemies_currently_generated[monster][1], display)
	
	display = placeCharacter("@", player[0], player[1], display) 			
	for row in range(len(display)): 
		print(display[row]) #prints display
	drawUI()
	
	time.sleep(.085)#delays input receptor so that character moves naturally
	
def defineWalls(tile):
	notQuiteMap = ["#","~",">"," ","["]
	return tile in notQuiteMap #returns true if it's a wall

def isThereABADGUYhere(checkx, checky):
	for BAADGUY in range(len(enemies_currently_generated)):
		if enemies_currently_generated[BAADGUY][0] == checkx and enemies_currently_generated[BAADGUY][1] == checky and enemies_currently_generated[BAADGUY][4] == mapNum:\
			return BAADGUY-0
	return -1

def hesGonnaGetChu():
	global enemies_currently_generated, player
	for he in range(len(enemies_currently_generated)):
		if enemies_currently_generated[he][4] == mapNum and enemies_currently_generated[he][2] != "L" and enemies_currently_generated[he][1] >= 0:
			if (enemies_currently_generated[he][0] == player[0] and abs(enemies_currently_generated[he][1] - player[1]) <= 1) or (enemies_currently_generated[he][1] == player[1] and abs(enemies_currently_generated[he][0] - player[0]) <= 1):
				ouchThatHurt(he)
				time.sleep(1/3)
			else:
				tries = 100
				while tries > 0:
					notOk = False
					directionHeWantToGo = random.randint(1,4)
					tileHeWantToGoToX = enemies_currently_generated[he][0]
					tileHeWantToGoToY = enemies_currently_generated[he][1]
					if directionHeWantToGo == 1:
						tileHeWantToGoToX -= 1
					if directionHeWantToGo == 2:
						tileHeWantToGoToX += 1
					if directionHeWantToGo == 3:
						tileHeWantToGoToY -= 1
					if directionHeWantToGo == 4:
						tileHeWantToGoToY += 1
					for otherHe in range(len(enemies_currently_generated)):
						if enemies_currently_generated[otherHe][0] == tileHeWantToGoToX and enemies_currently_generated[otherHe][1] == tileHeWantToGoToY and enemies_currently_generated[otherHe][4] == mapNum:
							notOk = True
					if not notOk and getTileAt(tileHeWantToGoToX,tileHeWantToGoToY) == "." or getTileAt(tileHeWantToGoToX,tileHeWantToGoToY) == "+" and tileHeWantToGoToX != player[0] and tileHeWantToGoToY != player[1]:
						enemies_currently_generated[he][0] = tileHeWantToGoToX
						enemies_currently_generated[he][1] = tileHeWantToGoToY
						tries = 0
						break
					else:
						tries -= 1
	
def newRoom(tile):
	if tile in getOutofHere:
		return getOutofHere.index(tile) #returns true if this tile exists
	else:
		return -1
		
def checkForPizzaPlace(): #this function should see if the next tile is [
	global exit, player, level
	if getTileAt(player[0]-1, player[1]) == "[" and password is True:
		clear()
		print("Do you have the password? ..... You do! \n Welcome to Paulie's Pizza. Your cousin's party started 30 minutes ago! Where have you been! \nAt least you had a good time along the way." )
		if level > 1:
			print("You're already level " + str(level) + ". Wow!")
		else:
			print("...You're only level " + str(level) + ". How did you even get here??")
		print("\n \n \n \n")
		print("Y O U  W O N")
		print("(You can leave now (Press Z))")
		logThatStuff("won the game ")
		submitScore()
		highScoresHere()
		while not keyboard.is_pressed('z'): #This makes the map stop being interactable
			continue
		exit = True
		
	
	elif getTileAt(player[0]-1,player[1]) == "[" and password is False: #if you don't have the password, it tells you to leave
		clear()
		print("Do you have the password? ..... Nah. Doesn't look like it. Beat it, kid.(.... Press 'd' to beat it I guess)")

		
		
def highScoresHere(): #this prints out the scores in the database using PHP script
	print(urllib.request.urlopen("http://localhost/").read().decode())

def submitScore(): #this adds your score to the database
	global name, level, Trash_Counter
	print(urllib.request.urlopen("http://localhost/?name=" + name.replace(" ","_").replace("&","_") + "&level=" + str(level) + "&trash=" + str(Trash_Counter)).read().decode())

#def whatsThePassword(): #this function should see if the password paper is in your inventory

def thePasswordIsInWorld4(): #this is what plays if you find the password and it reads it in your inventory once found
	global password, wuhtChuWant
	while True:
		if keyboard.is_pressed('y'):
			logThatStuff("has found the password ")
			a = random.randint(0,9)
			print("You found a scrap piece of paper! It has the word " +["Herby fully loaded", "toothbrush", "swanky", "swiggity swizza gotta get that pizza", "something you can't pronounce", "OHHHH YEAHHHHHHH", "jeepers creepers who's got the pizzers", "Are you done yet?", "Open sesame", "Honey I'm home"][a]	+ " scribbled on it.")
			password = True 
			placeCharacter(".", player[0], player[1], worlds[mapNum])
			placeCharacter(".", player[0], player[1], map)
			break
		if keyboard.is_pressed('n'):
			logThatStuff("didn't pick up the password?? ")
			wuhtChuWant = True
			drawMap()
			break
	
	return password
	
def didYouDie(HPNow): #this checks your HP. We call this after consuming items and during battle so it kills you if you die
	global exit
	if HPNow <= 0:
		clear()
		color()
		print("G A M E  O V E R")
		submitScore()
		logThatStuff("died... ")
		while not keyboard.is_pressed('z'):
			continue
		exit = True
		
		
def generateItem(): #sword is -1, shield -2, item -3, piece of trash -89
	whatKindofStuff = random.randint(0,5) #we use this extra function in conjunction with the one that reads the trash because it allows us to manipulate the probability and looks cleaner
	if whatKindofStuff == 1:
		return -1
	elif whatKindofStuff == 2:
		return -89
	elif whatKindofStuff == 3:
		return -2
	else:
		quoteunquoteTREASURE = []
		for target in range(len(items)):
			for _ in range(items[target][6]):
				quoteunquoteTREASURE.append(target)
		trashroulette = random.randint(0, len(quoteunquoteTREASURE)-1)
		return quoteunquoteTREASURE[trashroulette]
			#name  #HP increase  #attack increase  #defense increase  #level increase #XP increase #rarity #quantity
			
def levelUp():
	global level, XP, attack, defense, maxHP, currentHP
	if XP >= 100:
		XP = XP -100 #this reads how much XP you have and levels you up if it's over 100 
		increase_amount = random.randint(0,3) #this decides how many of your stats will increase
		if increase_amount > 0:
			for x in range(increase_amount): #this decides which stat will increase
				which_stat =random.randint(0,2)
				if which_stat == 0: #this increases HP
					maxHP = maxHP + random.randint(2,12)
					print("You improved your HP!")
				elif which_stat == 1: #this increases attack
					attack = attack + random.randint(1,3)
					print("You improved your attack!")
				else:
					defense = defense + random.randint(1,3) #this increases defense
					print("You improved your defense!")
		currentHP = maxHP #when you level up you're revived to max health
		level +=1
		drawMap()
		logThatStuff("leveled up ")
		
def weShouldAddSomeEnemies(): #adds enemies to the world
	global enemies, enemies_in_worlds, mapNum, max_x, max_y
	if enemies_in_worlds[mapNum] == 0:
		howMany = random.randint(1,5)
		for x in range(howMany):
			while True:
				badguyx = random.randint(0, max_x-1)
				badguyy = random.randint(0, max_y-1)
				if getTileAt(badguyx, badguyy) == "." or getTileAt(badguyx, badguyy) == "+":
					monsterrarity = []
					for target in range(len(enemies)):
						for _ in range(enemies[target][5]):
							monsterrarity.append(enemies[target][6])
					badguyroulette = monsterrarity[random.randint(0, len(monsterrarity)-1)]
					#print(badguyroulette)
					#time.sleep(1)
					thisguysHP = 0
					thisguysSymbol = "*"
					for enemytype in range(len(enemies)):
						if enemies[enemytype][6] == badguyroulette:
							thisguysHP = enemies[enemytype][1]
							thisguysSymbol = enemies[enemytype][7]
							thisguysType = enemies[enemytype][6]
							break
					enemies_currently_generated.append([badguyx,badguyy,thisguysType,thisguysHP,mapNum,thisguysSymbol])
					enemies_in_worlds[mapNum] += 1
					break

def isItDead(guy): #checks if enemy is dead
	global enemies_currently_generated, enemies, XP, mapNum
	type = -1
	for x in range(len(enemies)):
		if enemies[x][6] == enemies_currently_generated[guy][2]:
			type = x
			break
	if enemies_currently_generated[guy][3] <= 0:
		enemies_in_worlds[mapNum] -= 1
		del enemies_currently_generated[guy]
		XP += enemies[type][4]
		levelUp()
		logThatStuff(" has killed an enemy ")
		
def timeToFight(guy):
	global currentHP, attack, enemies_currently_generated, enemies
	type = -1
	for x in range(len(enemies)):
		if enemies[x][6] == enemies_currently_generated[guy][2]:
			type = x
			break
	print("A " + str(enemies[type][0]) + " is in your way. Beat them up!")
	enemies_currently_generated[guy][3] -= attack -enemies[type][3]
	isItDead(guy)
	time.sleep(1.5)
	drawMap()
	
	
def ouchThatHurt(guy):
	global currentHP, attack, enemies_currently_generated, enemies
	type = -1
	for x in range(len(enemies)):
		if enemies[x][6] == enemies_currently_generated[guy][2]:
			type = x
			break
	print("A " + enemies[type][0] + " attacked you!")
	currentHP -= max(enemies[type][2] - random.randint(0,defense), 0)
	print("You lost HP!")
	didYouDie(currentHP)
	time.sleep(1)
	drawMap()

	
def omNomTheNomNoms():
	global items, currentHP, maxHP, attack, defense, level, XP
	thenumberoftypesofitemsthatwehaveavailableatthemoment = 0
	for f in range(len(items)): #this figures out how many items we have
		if items[f][7] > 0: #if you have more than one in your inventory
			thenumberoftypesofitemsthatwehaveavailableatthemoment += 1 #add it to how many types of items we have
			if keyboard.is_pressed(str(thenumberoftypesofitemsthatwehaveavailableatthemoment)): #this checks the number associated with the item. An "ID" if you will 
				currentHP += items[f][1] #affects HP
				hesGonnaGetChu()
				if currentHP > maxHP:
					currentHP = maxHP #makes sure you can't go over max HP
				attack += items[f][2] #affects attack
				defense += items[f][3] #affects defense
				level += items[f][4] #affects level
				XP += items[f][5] #affects XP
				items[f][7] -= 1 #decreases one from your inventory
				drawMap()
				print("You ate it! Check out your stats!") #generic print message
				levelUp() #checks to see if you leveled up 
				didYouDie(currentHP) #checks if you died
				time.sleep(.2)
				logThatStuff("ate an item ")

main()

# cd Desktop/Python Files/Final 2