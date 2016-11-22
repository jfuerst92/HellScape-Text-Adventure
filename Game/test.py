#!/usr/bin/env python

import curses
from curses import wrapper
import os

from player import Player
from reaper import Reaper
from item import Item
from feature import Feature
from feature import DoorFeature
#from feature import getItemList
from room import Room
from room import readFile
from thesaurus import validateWord

########################################CODE FROM PLAY.PY#####################################

rooms = readFile()
rooms.append(Room("Dia De Los Muertos","","",0,0, "muertos"))
rooms.append(Room("Quiet Apartment","","",0,0, "z"))
rooms.append(Room("Loud Banquet Hall","","",0,0, "valhala"))
rooms.append(Room("Room with Other People", "", "", 0, 0, "noexit"))
rooms.append(Room("Dark and Dusty Tomb", "", "", 0, 0, "egypt"))

player = Player()
#items = Item.getItemList()
#Item(type, name, description, room)
doru = Item("weapon", "doru", "A sharp tipped spear sits firmly planted in the sternum of some demonic skeleton. If this spear killed such a monster, I may benefit by holding on to this.", 0)
rooms[0].items.append(doru)
scroll = Item("tele", "scroll", "An old scroll that contains odd pictures and characters. It seems to hum with power. There is a spot with the outline of a hand...", 3)
rooms[3].items.append(scroll)
relic = Item("defense", "relic", "An small pendant with a vial containing the dry blood of a long-passed Saint. Perhaps it may repel what evil lurks here... ", 4)
rooms[4].items.append(relic)
key = Item("key", "key", "An old, bronze, slightly bent key that looks to unlock a door somewhere. I'm not sure this would even fit anymore.", 4)
rooms[4].items.append(key)
torch = Item("util", "torch", "It's a lit torch, how long has this been burning?", 2)
rooms[2].items.append(torch)
hotSauce = Item("weapon", "hotSauce", "bottle o' hot sauce", 10)
rooms[10].items.append(hotSauce)
brains = Item("junk", "brains","brains", 11)
rooms[11].items.append(brains)

items = []
items.append(doru)
items.append(scroll)
items.append(relic)
items.append(key)
items.append(torch)
items.append(hotSauce)
items.append(brains)

#add features
stall = Feature("stall", "", 10)
grave = Feature("grave", "", 10)
zdoor = Feature("zdoor", "", 11)
zmirror = Feature("zmirror", "", 11)
testDoor = DoorFeature("oakdoor", "", 0, 2, True) #True for locked, false for unlocked. The key item will be used on the door to unlock it
testDoor2 = DoorFeature("oakdoor", "", 2, 0, False)
holeInWall = DoorFeature("hole", "", 0, 4, False)
holeInWall2 = DoorFeature("hole", "", 4, 0, False)
features = []
features.append(stall)
features.append(grave)
features.append(zdoor)
features.append(zmirror)
features.append(testDoor)
features.append(testDoor2)
features.append(holeInWall)
features.append(holeInWall2)

reaper = Reaper(9, rooms)
#The current game dictionary. It recognizes these words. 
verbs = ['look', 'touch', 'go', 'help', 'pull', 'use', 'pickup', 'pick', 'drop', 'combine', 'inventory', 'search']

######################################
#Create dictionaries of items and verbs to use with thesaurus api
######################################
verbDic = []
for verb in verbs:
	newArr = []
	newArr.append(verb)
	verbDic.append(newArr)
	
itemDic = []
for item in items:
	newArr = []
	newArr.append(item.name)
	itemDic.append(newArr)

#p1 = Player()  #the player object will be globally accessable to the play functions since they should be able to control and access everything

#

def checkItemInRoom(item):
    
    if item.curRoom == player.curRoom:
        return True
    else:
        return False
        
def checkFeatInRoom(feat):
    
    if feat.room == player.curRoom:
        return True
    else:
        return False
    
def cmdSplit(action): #splits command into seperate words, verb room item etc
    command = []
        
    command = action.split()
    return command
    
def getInput():
    action = raw_input('What do you want to do?>>')
    if (action == 'exit'):
        return None
    #print "This is your action: " + action + "\n"        
    curCmd = action.split()
    
    return curCmd
        
     
def checkVerb(verb): 
    check = 0
    for item in verbs:
        if (verb == item):
            check = 1
            
    return check
 
def checkVerb2(userVerb, verbDic):
	isASyn, index, temp = validateWord(verbDic, userVerb, "verb")
	if isASyn:
			verbs[index] = temp
			return 1, verbs[index][0] 		#return 'base' verb
	else:
			return 0, None
			
 #This function is not done. It will check which verb is being used, and branch of to one of the following functions accordingly.
 ##returns [type, value] where type is "error", "room", "item", or "feature" and value is the name or error message 
def interpret(command, verbDic):
    words = 0
    for word in command:
        words += 1
    if (words == 0):
        return "error", "You must want to do something..."
    check, command[0] = checkVerb2(command[0], verbDic)		#if user entered a synonym, replace command[0] with the 'base' verb
    if (check == 0):
        return  "error", "Not a valid command..."
    else:
        if (command[0] == "look"):  #This will call the appropriate command based on the verb that is used, then the individual functions will process the rest
            return look(command, words)
        elif (command[0] == "pick" or command[0] == "pickup"):
            return pickup(command, words)
        elif (command[0] == "drop"):
            return drop(command, words)
        elif (command[0] == "go"):
            return go(command, words)
        elif (command[0] == "inventory"):
            return inventory()
        elif (command[0] == "help"):
            return help()
        elif (command[0] == "use"):
            return use(command, words)
        elif (command[0] == "search"):
            return search()
        else:
            return "error", "No implementation for this verb"   #This is only here because I keep forgetting to add each new verb here >_>
        
 
#-------------------------------------------------------------------------------------------------------------------------------------------------------
# Function: help
# This function prints a list of the items in user inventory to screen.
# User input: None
#------------------------------------------------------------------------------------------------------------------------------------------------------ 
def help():
	helpString = ("Available commands by verb:\n"
			+"look\n"
            + "look at <item>"
			+"pick up <item> / pickup <item>\n"
			+"drop <item>\n"
			+"go <room> (currently unfinished)\n"
		      	+ "Use <feature> (unfinished. You can type use oakdoor in the first room and it should take you to a connecting room)"
            +"inventory\n")
	
	
	return "message", helpString
 
 
 
#-------------------------------------------------------------------------------------------------------------------------------------------------------
# Function: inventory
# This function prints a list of the items in user inventory to screen.
# User input: None
#------------------------------------------------------------------------------------------------------------------------------------------------------ 
def inventory():
	invString = "Items currently in inventory:\n"
	for item in player.getInventory():
		invString += "      " + item.name + "\n"
	#used for testing to see items in current room	
	#invString += "ROOM INVENTORY:\n"
	#for item in rooms[player.curRoom].items:
	#	invString += "      " + item.name + "\n"
	return "inventory", invString
	
#-------------------------------------------------------------------------------------------------------------------------------------------------------
# Function: look
# This function lets the user look at something.  By itself, it simply looks around the room, and the user gets a long description of the room they're in
# The player can also look at features and items, and permitted that they are in the room or in the players inventory, they can get a long description of 
# the item or feature.
# User input: pickup <item>
#------------------------------------------------------------------------------------------------------------------------------------------------------ 
def look(command, words): 
    lookAt = ""
    if (words == 1):
        
        return "room", rooms[player.curRoom].fname
    
    if (command[1] == "at"):
        lookAt = command[2]
    else:
        lookAt = command[1]
    
    if lookAt == "inventory":
        invString = "Items currently in inventory:\n"
        for item in player.getInventory():
            invString += "      " + item.name + "\n"
        #used for testing to see items in current room	
        #invString += "ROOM INVENTORY:\n"
        #for item in rooms[player.curRoom].items:
        #	invString += "      " + item.name + "\n"
        return "inventory", invString

	#if player is trying to look at feature
    for feature in features:
        if (lookAt == feature.name):
             if feature.room == player.curRoom:
				return "feature", lookAt
    

    #if player is trying to look at an item
    for item in items:
        if (lookAt == item.name):
            if checkItemInRoom(item):
            #roomItems = rooms[player.curRoom].getItems() #get the items (not picked up) of the current room to look at.
            #print "You looked at the " + item.name + ". This is placeholder text for the item description. This will be contained in an item object that will have a get method to obtain the info"
                #item.getDescription()#This function will display the description of the item. 
                return "item", lookAt
	
    #if item is in inventory
    for item in player.inventory:
        if (lookAt == item.name):
            return "item", lookAt
			
    return "error", "You look but you do not see a " + lookAt + " anywhere in the room."

#-------------------------------------------------------------------------------------------------------------------------------------------------------
# Function: search
# This function has the player search the current room for items

# User input: search 
#------------------------------------------------------------------------------------------------------------------------------------------------------ 
def search():     
    message = "you notice something..\n"
    for item in items:
        if (item.curRoom ==player.curRoom):
            message = message + "You see a " + item.name + " in this room.\n"
            
    for feat in features:
        if (feat.room ==player.curRoom):
            message = message + "You see a " + feat.name + " in this room.\n"       
    return "message", message

#-------------------------------------------------------------------------------------------------------------------------------------------------------
# Function: pickup
# This function lets the user pick up an item on the ground and add it to their inventory. It checks that the item is valid and is also presently
# in the same room that the user is in. It will add the item to the player inventory and remove it from the room
# User input: pickup <item>
#------------------------------------------------------------------------------------------------------------------------------------------------------
def pickup(command, words): #the player object should be passed into the constructor, so we can get their current room and it's features
    tItem = ""
    if (words == 1):
        return "error", "You must indicate an item to pick up"
    if (command[1] == "up"):
        tItem = command[2]
    else:
        tItem= command[1]
    #if player is trying to pick up an item
    for item in items:
        if (tItem == item.name):
         
            # = rooms[player.curRoom].getItems() #get the items (not picked up) of the current room to look at.
            #print "You pick up the " + item + ". This is placeholder text an item pick up. This will call the player object to add the item object into their inventory and remove it from the room's 'inventory' \n"
            if checkItemInRoom(item) == True:
                player.addItem(item) #This function adds the item to the players inventory
                rooms[player.curRoom].removeItem(item)
                return "message",  "You pick up the " + item.name + " and put it away in your bag."
    return "error", "You look but you do not see this item anywhere in the room."
    
  
  
#-------------------------------------------------------------------------------------------------------------------------------------------------------
# Function: drop
# This function lets the user drop an item from their inventory onto the ground. It checks that the item is valid and is also presently
# in the user's inventory. It will add the item to the room and remove it from the inventory. THere may be additional functionality, if we want to
#do that. For instance, drop a burning thing on the ground in a carpeted or otherwise flammable room, and you may have an issue.
# User input: drop <item>
#------------------------------------------------------------------------------------------------------------------------------------------------------
def drop(command, words): #the player object should be passed into the constructor, so we can get their current room and it's features
    tItem = ""
    if (words == 1):
        return "error", "You must indicate an item to drop"
    
    tItem = command[1]
    #if player is trying to drop an item
    for item in items:
        if (tItem == item.name):
            playerItems = player.getInventory() #get the items in the players inventory.
            #print "You drop the " + item + ". This is placeholder text an item drop. This will call the player object to drop the item object into their inventory and add it to the room's 'inventory' \n"
           
            for item2 in playerItems:
                if (command[1] == item2.name):
                   player.dropItem(item2) #This function should drop the item from the players inventory
                   item2.curRoom = player.curRoom
                   rooms[player.curRoom].addItem(item2)
                   return "message", "You drop the " + item2.name + " on the floor"
                   #player.curRoom.dropEvent(item) #If dropping the item has some effect on the room, then this function would make that happen.
                  
    return "error", "You you do not have such an item do drop."
    
    
    
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------
# Function: go
# This function ahs the user go to a new room. This isnt final, because the user may not know the names of the connecting rooms, but 
# it works for now.
#------------------------------------------------------------------------------------------------------------------------------------------------------
def go(command, words): #the player object should be passed into the constructor, so we can get their current room and it's features
	room = ""
	if (words == 1):
		return "error", "You must indicate a place to go\n"
    
	goTo = command[1].lower()
    
	i = 0
	for i in range(len(rooms)):
		if (goTo == rooms[i].fname):
			player.changeRooms(i) 
			return "room", rooms[player.curRoom].fname
	
	#added ability to 'go' to feature
	for feature in features:
		if (goTo == feature.name):
			if feature.room == player.curRoom:
				return "feature", goTo
				
	return "error", "That is not a place you can go"
   
   

#-------------------------------------------------------------------------------------------------------------------------------------------------------
# Function: use
# This function lets the player use things in the room. The player can attempt to use certain features of the room such as
# doors, chairs, switches etc. The player can also use items in their inventory. Using an item may have an effect on the room that the player
# is in. The player can also use an item on another item or a feature. For instance, a user could have a lighter item and use it on a candle 
# fixture on the wall or to burn away cobwebs. This will change the feature of the room. THe user may have an unlit torch in their inventory. 
# in this case, they could use the lighter to light the torch.
#may possible add functionality so that the player can use an item on the enemy. For instance, the player could use holy water to make the
#reaper flee the room, or use something else to distract it and escape. 
#
# User input: use <feature>, use <item>, use <item> on <feature>, use <item> on <item>
#------------------------------------------------------------------------------------------------------------------------------------------------------
def use(command, words): #the player object should be passed into the constructor, so we can get their current room and it's features
    #if player is trying to use a feature
    tFeat = ""
    for feat in features:
        if (command[1] == feat.name):
            tFeat = command[1]
            
            if checkFeatInRoom(feat):
                #return "message",  "You can use the " + tFeat
                if (feat.type == "door"):
                    if (feat.locked == True):
                        for item in player.getInventory():
                            if item.name == "key":
                                player.changeRooms(feat.conn) #player has a key
                                return "room", rooms[player.curRoom].fname
                        return "message",  "It's locked.. However you do notice a small keyhole. Surely there must be a key somewhere?"
                    else: #player uses the door. they go to the new room
                        player.changeRooms(feat.conn) 
                        return "room", rooms[player.curRoom].fname
                
    #if player is trying to use an item
    
    for item in items:
         if (command[1] == item.name):
             tItem = command[1]
             for item2 in player.getInventory():
                if (tItem == item2.name):
                    #return "message", "You use the " + item2.name + " in your inventory\n"
                    if (len(command) > 2):
                        if (command[2] == "on"): #player is using an item on something else
                            for feat in features:
                                if (command[3] ==feat.name):
                                    if (feat.room == player.curRoom):
                                        tFeat = command[3]
                                        return useItem(item2, feat)
                    else:
                        return useItem(item2, None)
             return "error", "You do not have such an item.\n"
    return "error", "You cannot find what you are looking for.\n"


def useItem(item, feature):

    if (feature == None):
        if (item.type == "weapon"):
            return "error", "You must indicate something to attack"
        elif (item.type == "defense"):
            return "error", "You cannot use defensive items, their effect is passive"
        else:
            return "message", "You use the " + item.name + " . (not implemented)"
            
    if (item.type == "key" and feature.type == "door"):
        feature.locked = False
        return "message", "you insert the key into the lock and give it a firm twist, and you hear a click as the door opens.\n"
    return "error", "invalid action (or not yet  implemented)"
 
###############################END CODE FROM PLAY.PY#################################

def printFile(fileName, printScreen, startY, startX, color, maxLength):
	yOffset = 0
	with open(fileName, "r") as readFile:
		for line in readFile:
			#display only enough data as can fit on screen
			if yOffset == maxLength - 1:
				printScreen.addstr(startY + yOffset, startX, "-----Press any key to continue-----")
				printScreen.getch()
				printScreen.clear()
				yOffset = 0

			printScreen.addstr(startY + yOffset, startX, line, curses.color_pair(color))
			yOffset += 1

def errorMessage(printScreen, message):
	printScreen.clear()
	printScreen.addstr(1, 1, message, curses.color_pair(5))
	printScreen.refresh()
	
def message(textScreen, picScreen, message):
	textScreen.clear()
	textScreen.border(0)
	textScreen.addstr(3, 1, message, curses.color_pair(4))
	
	picScreen.clear()
	picScreen.border(0)
	
	textScreen.refresh()
	picScreen.refresh()

def printInventory(nameScreen, picScreen, textScreen, invString):
		nameScreen.clear()
		nameScreen.border(0)
		nameScreen.addstr(1,1, "PLAYER INVENTORY", curses.color_pair(1))
		
		picScreen.clear()
		picScreen.border(0)
		
		textScreen.clear()
		textScreen.border(0)
		textScreen.addstr(3,1, invString, curses.color_pair(4))
		
		nameScreen.refresh()
		picScreen.refresh()
		textScreen.refresh()
		
def main(stdscr):	
	#cwd = current working directory.  Used to access .txt files for curses
	cwd = os.getcwd()
	
	stdscr.clear()

	curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
	curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)
	curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_BLACK)

	MAX_LINES = 15

	beginX = curses.COLS / 2 - 20
	beginY = 0
	height = 3
	width = 40
	captionWin = curses.newwin(height, width, beginY, beginX)
	captionWin.border(0)
	captionWin.addstr(1, 15, "---START SCREEN---", curses.color_pair(1))

	beginX = curses.COLS / 2 - 26
	beginY = 3
	height = 15
	width = 60
	picWin = curses.newwin(height, width, beginY, beginX)
	picWin.border(0)
	picWin.addstr(5, 18, "ASCII pic here", curses.color_pair(2))

	beginX = 0
	beginY = 17
	height = 20
	width = curses.COLS - 1
	textWin = curses.newwin(height, width, beginY, beginX)
	textWin.border(0)
	textWin.addstr(10, curses.COLS / 2 - 5, "Enter your name", curses.color_pair(4))

	beginX = 0
	beginY = 37
	height = 3
	width = curses.COLS - 1
	errorWin = curses.newwin(height, width, beginY, beginX)
	
	beginX = 2
	beginY = 40
	height = 3
	width = curses.COLS - 3
	inputWin = curses.newwin(height, width, beginY, beginX)
	inputWin.border(0)
	inputWin.addstr(1, 1, ">", curses.color_pair(3))

	stdscr.refresh()
	picWin.refresh()
	captionWin.refresh()
	textWin.refresh()
	errorWin.refresh()
	inputWin.refresh()
	
	curses.echo()
	pName = inputWin.getstr()
	player.setName(pName)
	curses.noecho()
	#personalize start room description with user name.
	f = open(os.getcwd() + "/roomDescriptions/start.txt", 'w')
	f.write("You wake up with an aching headache and no idea where you are.\n"
			+"Unsure of the disturbing reality that now surrounds you, you stand and rub your eyes.\n"
			+"Suddenly, a voice whispers in your ear : \"Welcome to hell, " + player.name + ". I am coming.\"\n"
			+"You can feel pure terror surrounding you. You must get out.\n"
			+"Type \"help\" to get a list of commands.")
	f.close()
	
	
	value = "start"
	type = "room"
	while value != "exit":
	
		if type == "error":
			errorMessage(errorWin, value)
		
		elif type == "message":
			message(textWin, picWin, value)

		elif type == "inventory":
			printInventory(captionWin, picWin, textWin,value)
			
		else:
			name = str(cwd) + "/" + type + "Names/" + value + ".txt"
			pic = str(cwd) + "/" + type + "Pics/" + value + ".txt"
			text = str(cwd) + "/" + type + "Descriptions/" + value + ".txt"
				
			#clear windows and set up borders
			captionWin.clear()
			picWin.clear()
			textWin.clear()
			inputWin.clear()
			captionWin.border(0)
			picWin.border(0)
			textWin.border(0)
			inputWin.border(0)
		
			#load entity from file
			printFile(name, captionWin, 1, 1, 1, 10)
			printFile(pic, picWin, 1, 1, 2, MAX_LINES) 
			captionWin.refresh()
			picWin.refresh()
			inputWin.refresh()
			printFile(text, textWin, 1, 1, 4, MAX_LINES)	
			textWin.refresh()

		
		
		#get input from user
		inputWin.clear()
		inputWin.border(0)
		inputWin.addstr(1, 1, ">", curses.color_pair(3))
		inputWin.refresh()
		curses.echo()
		userInput = inputWin.getstr()
		if userInput == "exit":
			break
		command = []
		command = userInput.split()
		type, value = interpret(command, verbDic)
		curses.noecho()

		#clear error screen message if any
		errorWin.clear()
		
		#show changed windows
		errorWin.refresh()
		stdscr.refresh()	
		picWin.refresh()
		captionWin.refresh()
		textWin.refresh()
		inputWin.refresh()

	stdscr.getch()	

wrapper(main)
