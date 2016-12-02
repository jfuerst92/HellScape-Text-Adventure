#!/usr/bin/env python

import curses
from curses import wrapper
import os

from player import Player
from reaper import Reaper
from item import Item
from feature import Feature
from feature import DoorFeature
from feature import PuzzFeature
from feature import HandFeature
from feature import LookFeature
from feature import LeverFeature
from feature import ChestFeature
#from feature import getItemList
from room import Room
from room import readFile
from thesaurus import validateWord
import time
import sys

########################################CODE FROM PLAY.PY#####################################

rooms = readFile()
rooms.append(Room("Dia De Los Muertos","","",0,0, "muertos"))
rooms.append(Room("Quiet Apartment","","",0,0, "z"))
rooms.append(Room("Loud Banquet Hall","","",0,0, "valhala"))
rooms.append(Room("Room with Other People", "", "", 0, 0, "noexit"))
rooms.append(Room("Dark and Dusty Tomb", "", "", 0, 0, "egypt"))
rooms.append(Room("Muertos Ending", "", "", 0, 0, "pinkending"))
rooms.append(Room("Z Ending", "", "", 0, 0, "greenending"))
rooms.append(Room("Valhala Ending", "", "", 0, 0, "goldending"))
rooms.append(Room("No Exit Ending", "", "", 0, 0, "purpleending"))
rooms.append(Room("Egypt Ending", "", "", 0, 0, "yellowending"))
rooms.append(Room("Good Ending", "", "", 0, 0, "goodending"))

player = Player()



#items = Item.getItemList()
#Item(type, name, description, room)
doru = Item("weapon", "doru", "A sharp tipped spear sits firmly planted in the sternum of some demonic skeleton. If this spear killed such a monster, I may benefit by holding on to this.", 0)
rooms[0].items.append(doru)
scroll = Item("heal", "scroll", "An old scroll that contains odd pictures and characters. It seems to hum with power. There is a spot with the outline of a hand...", 3)
rooms[3].items.append(scroll)
relic = Item("defense", "relic", "An small pendant with a vial containing the dry blood of a long-passed Saint. Perhaps it may repel what evil lurks here... ", 4)
rooms[4].items.append(relic)
key = Item("key", "key", "An old, bronze, slightly bent key that looks to unlock a door somewhere. I'm not sure this would even fit anymore.", 4)
rooms[4].items.append(key)
torch = Item("gem", "torch", "It's a lit torch, how long has this been burning?", 5)

rooms[5].items.append(torch)
hotSauce = Item("weapon", "hotSauce", "bottle o' hot sauce", 10)
rooms[10].items.append(hotSauce)
brains = Item("junk", "brains","brains", 11)
rooms[11].items.append(brains)
goldcoin = Item("junk", "goldcoin", "a gold coin", 14)
rooms[14].items.append(goldcoin)
heart = Item("junk", "heart", "a beating human heart", 14)
rooms[14].items.append(heart)
workingbrain = Item("junk", "workingbrain", "a pulsing human brain", 12)
#rooms[12].items.append(workingbrain)
knife = Item("junk", "knife", "a large steak knife", 13)
rooms[13].items.append(knife)
heirloom = Item("junk", "heirloom", "a family heirloom", 12)
rooms[12].items.append(heirloom)
spirit = Item("junk", "spirit", "a ghostly apparition resembling yourself", 10)
rooms[10].items.append(spirit)

gem1 = Item("gem", "ruby", "A large gem sits on the floor, covered in dust. Yet it still shines vibrantly, malevolently.", 5)
rooms[5].items.append(gem1)
gem2 = Item("gem", "sapphire", "A long forgotton sapphire jewel that is chipped on one end. It is blue, but it is of the darkest blues you've ever seen. ", 6)
rooms[6].items.append(gem2)
gem3 = Item("gem", "obsidian", "A black piece of obsidian hastily cut into a gemstone shape. It seems to suck the very light out of the air around it. .", 7)
rooms[7].items.append(gem3)
rooms[10].items.append(hotSauce)

armor = Item("defense", "armor", "An old suit of armor that is bursting forth with light. It exudes purity. It looks heavy but is as light as a feather.", -1)

sword = Item("weapon", "sword", "It's a silver sword. Its old, but still quite sharp.", -1)

items = []
items.append(doru)
items.append(scroll)
items.append(relic)
items.append(key)
items.append(torch)
#items.append(hotSauce)
#items.append(brains)
items.append(gem1)
items.append(gem2)
items.append(gem3)
items.append(armor)
items.append(sword)

#add features
stall = Feature("stall", "", 10)
stall.type = "other"
grave = Feature("grave", "", 10)
grave.type = "other"
zdoor = Feature("bedroomdoor", "", 11)
zdoor.type = "other"
zmirror = Feature("mirror", "", 11)
zmirror.type = "other"
jar1 = Feature("jar1", "", 14)
jar1.type = "other"
jar2 = Feature("jar2", "", 14)
jar2.type = "other"
man1 = Feature("man1", "", 13)
man1.type = "other"
man2 = Feature("man2", "", 13)
man2.type = "other"
woman = Feature("woman", "", 13)
woman.type = "other"
odin = Feature("oneeye", "", 12)
odin.type = "other"
table = Feature("table", "", 12)
table.type = "other"
testDoor = DoorFeature("oakdoor", "", 0, 2, True) #True for locked, false for unlocked. The key item will be used on the door to unlock it
testDoor2 = DoorFeature("oakdoor", "", 2, 0, False)
holeInWall = DoorFeature("jetty", "", 0, 4, False)
holeInWall2 = DoorFeature("jetty", "", 4, 0, False)
#doors from center to 'special' rooms
pinkdoor1 = DoorFeature('pinkdoor', '', 9, 10, False)
pinkdoor2 = DoorFeature('pinkdoor', '', 10, 9, False)
greendoor1 = DoorFeature('greendoor', '', 9, 11, False)
greendoor2 = DoorFeature('greendoor', '', 11, 9, False)
golddoor1 = DoorFeature('golddoor', '', 9, 12, False)
golddoor2 = DoorFeature('golddoor', '', 12, 9, False)
purpledoor1 = DoorFeature('purpledoor', '', 9, 13, False)
purpledoor2 = DoorFeature('purpledoor', '', 13, 9, False)
yellowdoor1 = DoorFeature('yellowdoor', '', 9, 14, False)
yellowdoor2 = DoorFeature('yellowdoor', '', 14, 9, False)

#PLACEHOLDER DOORS TO FACILITATE MOVEMENT AROUND THE MAP#
phDoor = DoorFeature("gate", "", 2, 3, False)
phDoor2 = DoorFeature("gate", "", 3, 2, False)

phDoor3 = DoorFeature("woodendoor", "", 2, 1, False)
phDoor4 = DoorFeature("woodendoor", "", 1, 2, False)

phDoor5 = DoorFeature("tdoor", "", 1, 5, False)
phDoor6 = DoorFeature("tdoor", "", 5, 1, False)

phDoor7 = DoorFeature("diamonddoor", "", 1, 6, False)
phDoor8 = DoorFeature("diamonddoor", "", 6, 1, False)

phDoor9 = DoorFeature("xdoor", "", 1, 7, False)
phDoor10 = DoorFeature("xdoor", "", 7, 1, False)

statue = PuzzFeature("statue", "", 3, 8)
ladder = DoorFeature("ladder", "", 8, 3, False)

gargoyle = HandFeature("gargoyle", "", 6, armor)

lever1 = LeverFeature("lever", "", 5)
lever2 = LeverFeature("lever", "", 6)
lever3 = LeverFeature("lever", "", 7)
			
			
chest = ChestFeature("chest", "", 1, sword)

message = LookFeature("message", "", 2)

features = []
features.append(stall)
features.append(grave)
features.append(zdoor)
features.append(zmirror)
features.append(testDoor)
features.append(testDoor2)
features.append(holeInWall)
features.append(holeInWall2)
features.append(pinkdoor1)
features.append(pinkdoor2)
features.append(greendoor1)
features.append(greendoor2)
features.append(purpledoor1)
features.append(purpledoor2)
features.append(golddoor1)
features.append(golddoor2)
features.append(yellowdoor1)
features.append(yellowdoor2)
features.append(jar1)
features.append(jar2)
features.append(man1)
features.append(man2)
features.append(woman)
features.append(odin)
features.append(table)

features.append(phDoor)
features.append(phDoor2)
features.append(phDoor3)
features.append(phDoor4)
features.append(phDoor5)
features.append(phDoor6)
features.append(phDoor7)
features.append(phDoor8)
features.append(phDoor9)
features.append(phDoor10)
features.append(statue)
features.append(ladder)
features.append(gargoyle)
features.append(lever1)
features.append(lever2)
features.append(lever3)
features.append(chest)
features.append(message)

###################STATIC VARIABLES FOR ANIMATIONS################
#PIC_FILES and COLOR_ARRAY should be the same length
WORKING_BRAIN_MESSAGE = "Your brain starts to steam and then begins to pulse"
REAPER_MESSAGE = "You are startled by a sound behind you. A dark hooded skeletal figure materializes in the room. It is the Grim Reaper, come to finish what he has started. It approaches you, you must act quickly!"

WORKING_BRAIN_PIC_FILES = ["itemPics/brains.txt", "itemPics/workingbrain.txt"]
REAPER_PIC_FILES = ["itemPics/grimreaper1.txt", "itemPics/grimreaper2.txt", "itemPics/grimreaper3.txt"]

WORKING_BRAIN_COLOR_ARRAY = [2, 3]
REAPER_COLOR_ARRAY = [3, 4, 2]
##################################################################

#################List to check rooms visited#######################
roomsVisited = {}
for room in rooms:
	i = room.fname.find('F')
	if i < 0:
		roomsVisited[room.fname] = False	#all rooms start as unvisited
	else:
		roomsVisited[room.fname[:i]] = False
			
###################################################################

reaper = Reaper(2)
#The current game dictionary. It recognizes these words. 
verbs = ['look', 'touch', 'go', 'help', 'pull', 'use', 'pickup', 'pick', 'drop', 'combine', 'inventory', 'search', 'whatroom', 'rTurn', 'open']

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
def whatRoom():
	return "message", "You are in room " + str(player.curRoom) + ".\n"
	
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
			verbDic[index] = temp
			return 1, verbDic[index][0] 		#return 'base' verb
	else:
			return 0, None
			
def checkNount(userNoun, nounDic):
	isASyn, index, temp = validateWord(nounDic, userNoun, "noun")
	if isAsyn:
		nounDic[index] = temp
		return 1, nounDic[index][0]
	else:
		return 0, None
			
 #This function is not done. It will check which verb is being used, and branch of to one of the following functions accordingly.
 ##returns [type, value] where type is "error", "room", "item", or "feature" and value is the name or error message 
def interpret(command, verbDic):
	if (reaper.curRoom == player.curRoom):
		if (player.inFight == False):
			return initiateFight()
		else:
			return fightInterpret(command, verbDic)
	else:
		reaper.reaperAction(player)
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
		elif (command[0] == "pull"):
			return pull(command, words)
		elif (command[0] == "open"):
			return openChest(command, words)
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
		elif (command[0] == "whatroom"):
			return whatRoom()
		else:
			return "error", "No implementation for this verb"   #This is only here because I keep forgetting to add each new verb here >_>
		
def fightInterpret(command, verbDic):
	words = 0
	for word in command:
		words += 1
	if (words == 0):
		return "error", "You must want to do something..."
	check, command[0] = checkVerb2(command[0], verbDic)		#if user entered a synonym, replace command[0] with the 'base' verb
	if (check == 0):
		return  "error", "Not a valid command..."
	else:
		if (command[0] == "rTurn"): #it is the reapers turn to act
			switchTurn()
			return reaperBattle()
		elif (command[0] == "look"):  #Should look in this case look specifically at the reaper??
			return look(command, words)
		elif (command[0] == "pick" or command[0] == "pickup"):
			switchTurn()
			return pickup(command, words)
		elif (command[0] == "drop"):
			switchTurn()
			return drop(command, words)
		elif (command[0] == "go"):
			return go(command, words)
		elif (command[0] == "inventory"):
			return inventory()
		elif (command[0] == "help"):
			return help()
		elif (command[0] == "use"):
			switchTurn()
			return use(command, words)
		elif (command[0] == "pull"):
			switchTurn()
			return pull(command, words)
		elif (command[0] == "open"):
			switchTurn()
			return openChest(command, words)
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
			+"   look\n"
			+"   look at <item>\n"
			+"   look <feature>\n"
			+"   look inventory\n"
			+"   pick up <item> / pickup <item>\n"
			+"   drop <item>\n"
			+"   go <room> (currently unfinished)\n"
			+"   go <feature>\n"
			+"   use <feature>\n"
			+"   use  <item> on <feature>\n"
			+"   inventory\n"
			+"   search")
	
	
	return "message", helpString
 
#-------------------------------------------------------------------------------------------------------------------------------------------------------
# Function: checkPlayerHealth
# Checks the status of player health
# User input: None
#------------------------------------------------------------------------------------------------------------------------------------------------------ 
def checkPlayerHealth():
	if (player.health > 0):
		return True
	else:
		return False
 
 #-------------------------------------------------------------------------------------------------------------------------------------------------------
# Function: checkPlayerHealth
# Checks the status of player health
# User input: None
#------------------------------------------------------------------------------------------------------------------------------------------------------ 
def getHealth():
	if (player.health > 0):
		return True
	else:
		return False
 
#-------------------------------------------------------------------------------------------------------------------------------------------------------
# Function: inventory
# This function prints a list of the items in user inventory to screen.
# User input: None
#------------------------------------------------------------------------------------------------------------------------------------------------------ 
def inventory():
	invString = "Items currently in inventory:\n"
	for item in player.getInventory():
		invString += "	  " + item.name + "\n"
	#used for testing to see items in current room	
	#invString += "ROOM INVENTORY:\n"
	#for item in rooms[player.curRoom].items:
	#	invString += "	  " + item.name + "\n"
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
			invString += "	  " + item.name + "\n"
		#used for testing to see items in current room	
		#invString += "ROOM INVENTORY:\n"
		#for item in rooms[player.curRoom].items:
		#	invString += "	  " + item.name + "\n"
		return "inventory", invString

	#if player is trying to look at feature
	for feature in features:
		if (lookAt == feature.name):
			if feature.room == player.curRoom:
			#conditional cases#####
				if (lookAt == 'bedroomdoor'):
					items.append(brains)
				if (lookAt == 'jar1'):
					items.append(heart)
				if (lookAt == 'jar2'):
					items.append(goldcoin)
				if (lookAt == 'woman'):
					items.append(knife)
				#######################

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
		
	if (not player.invHasSpace()):
		return "message", "You cannot pick that up. You may only carry two things at a time. You must drop something before you can pick another item up."
	#if player is trying to pick up an item
	for item in items:
		if (tItem == item.name):
		 
			# = rooms[player.curRoom].getItems() #get the items (not picked up) of the current room to look at.
			#print "You pick up the " + item + ". This is placeholder text an item pick up. This will call the player object to add the item object into their inventory and remove it from the room's 'inventory' \n"
			if checkItemInRoom(item) == True:
				player.addItem(item) #This function adds the item to the players inventory
				rooms[player.curRoom].removeItem(item)
				
				###check for good ending####
				if tItem == "heart" or tItem == "workingbrain" or tItem == "spirit":
					if (heart in player.getInventory()) and (spirit in player.getInventory()) and (workingbrain in player.getInventory()):
						return "room", "goodending"
						
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
					
					####conditional action######
					if (command[1] == 'knife' and player.curRoom == 12):	#if current room is valhala
						items.append(heirloom)
						return "message", "you drop the " + command[1] + " on the table and an old watch appears on your plate"
					############################
					
					return "message", "You drop the " + item2.name + " on the floor"
					#player.curRoom.dropEvent(item) #If dropping the item has some effect on the room, then this function would make that happen.
				  
	return "error", "You you do not have such an item do drop."
	
#-------------------------------------------------------------------------------------------------------------------------------------------------------
# Function: pull
# used to pull levers
# User input: pull <feature>
#------------------------------------------------------------------------------------------------------------------------------------------------------

def pull(command, words):	
	if (words == 1):
		return "error", "You must indicate an item to drop"
	
	tFeat = ""
	for feat in features:
		if (command[1] == feat.name and checkFeatInRoom(feat)):
			tFeat = command[1]
			if (feat.type == "lever"):
				feat.switch()
				if (feat.getSwitched() == True):
					return "message", "you pulled the lever up. Gears can be heard moving someplace else."
				else:
					return "message", "you pulled the lever down. Gears can be heard moving someplace esle."
			else:
				return "message", "try as you might, you cannot pull it down."
	return "message", "You cannot find what you are seeking."
	
	
#-------------------------------------------------------------------------------------------------------------------------------------------------------
# Function: open
# used to open chests
# User input: open <feature>
#------------------------------------------------------------------------------------------------------------------------------------------------------

def openChest(command, words):	
	if (words == 1):
		return "error", "You must indicate an item to drop"
	tFeat = ""
	for feat in features:
		if ((command[1] == feat.name) and (checkFeatInRoom(feat))):
			tFeat = command[1]
			if (feat.type == "chest"):
				if (checkLevers()):
					feat.dropItem(rooms)
					rooms[1].items.append(sword)
					return "message", "The  correct combination of switches caused the chest to click open Inside you see sword, buried under musty rags and wrappings."
				else:
					return "message", "The chest won't open. You notice the locking mechanism connects to a gear going into the wall."
			else:
				return "message", "try as you might, you cannot pull it down."
	
	return "message", "You cannot find what you are seeking."

	
def checkLevers():
	if ((lever1.switched == False) and (lever2.switched == True) and (lever3.switched == True)):
		return True
	else:
		return False

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
			player.inFight = False
			player.pTurn = True
			return "room", rooms[player.curRoom].fname
	
	#added ability to 'go' to feature
	for feature in features:
		if (goTo == feature.name):
			if feature.room == player.curRoom:
				#conditional actions#######		
					if (goTo == 'bedroomdoor'):
						items.append(brains)
					if (goTo == 'jar1'):
						items.append(heart)
					if (goTo == 'jar2'):
						items.append(goldcoin)
					if (goTo == 'woman'):
						items.append(knife)
					##########################
					return "feature", goTo
	
	#if players are in center they can go to an ending
	if player.curRoom == 9:			#if player is in center
		if goTo == "pink":
			return "room", "pinkending"
		elif goTo == "green":
			return "room", "greenending"
		elif goTo == "gold":
			return "room", "goldending"
		elif goTo == "purple":
			return "room", "purpleending"
		elif goTo == "yellow":
			return "room", "yellowending"
			
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
def use(command, words): 
	if (words == 1):
		return "error", "You must indicate something to use\n"
	#if player is trying to use a feature
	tFeat = ""
	for feat in features:
		if (command[1] == feat.name):
			tFeat = command[1]
			
			if checkFeatInRoom(feat):
				#return "message",  "You can use the " + tFeat
				if (feat.type == "door"):
					if (feat.locked == True):
						#for item in player.getInventory():
							#if item.name == "key":
								#player.changeRooms(feat.conn) #player has a key
								#return "room", rooms[player.curRoom].fname
						return "message",  "It's locked.. However you do notice a small keyhole. Surely there must be a key somewhere?"
					else: #player uses the door. they go to the new room
						player.changeRooms(feat.conn) 
						player.pTurn = True
						player.inFight = False
						return "room", rooms[player.curRoom].fname
				elif (feat.type == "puzz"):
					if (feat.slots > 0):
						return "message", "there are " + str(feat.slots) + " empty slots left."
					else:
						player.changeRooms(feat.conn)
						player.pTurn = True
						player.inFight = False
						return "message", "With the three gems inserted into the slots, the ground begins to shake and the statue moves, revealing a hidden passage underneath, which you enter.\n"
				else:
					return "message", "you can't use that feature"
	#if player is trying to use an item
	
	for item in items:
		 if (command[1] == item.name):
			 tItem = command[1]
			 for item2 in player.getInventory():
				if (tItem == item2.name):
					#return "message", "You use the " + item2.name + " in your inventory\n"
					if (len(command) > 2):
						if (command[2] == "on" and len(command) > 3): #player is using an item on something else
							for feat in features:
								if (command[3] == feat.name):
									if (feat.room == player.curRoom):
										tFeat = command[3]
										return useItem(item2, feat)
										
							for secItem in items:
								if (command[3] == secItem.name):
									if secItem in player.getInventory():
										if (item2.name == "hotSauce" and secItem.name == "brains") or (item2.name == "brains" and secItem == "hotSauce"):
											player.dropItem(hotSauce)
											player.dropItem(brains)
											rooms[player.curRoom].items.append(workingbrain)
											player.addItem(workingbrain)
											##check for good ending condition##
											if (spirit in player.getInventory()) and (heart in player.getInventory()):
												return "room", "goodending";
											else:
												return "specialmessage", "workingbrain"
					else:
						return useItem(item2, None)
			 return "error", "You do not have such an item.\n"
	return "error", "You cannot find what you are looking for.\n"


def useItem(item, feature):

	if (feature == None):
		if (item.type == "weapon"):
			if (reaper.curRoom == player.curRoom): #attack the reaper with your weapon if it is present
				item.decUses()
				if (item.broken()):
					player.dropItem(item)
					return "message", "as you go to attack, the weapon brakes! It is no longer useable!"
				return "message", reaper.getAttacked()
			else:
				return "error", "There is nothing to attack"
		elif (item.type == "defense"):
			return "error", "You cannot use defensive items, their effect is passive"
		elif (item.type == "heal"):
			if (player.health >= 10):
				return "message", "you place your hand on the outline, but nothing happens..."
			else:
				player.health = 10
				player.dropItem(item)
				return "message", "The scroll bursts into flames and it's magic flows into your body. You feel rejuvinated."
		else:
			return "message", "You use the " + item.name + " . (not implemented)"
			
	if (item.type == "key" and feature.type == "door"):
		feature.locked = False
		return "message", "you insert the key into the lock and give it a firm twist, and you hear a click as the door opens.\n"
	elif (item.type == "gem" and feature.type == "puzz"):
		feature.insertGem(player, item)
		return "message", "you insert the gem into one of the open slots on the statue, and it clicks in to place.\n"
	elif (item.type == "heal" and feature.type == "hand"):
		feature.dropItem(rooms)
		rooms[6].items.append(armor)
		armor.curRoom = 6
		return "message", "You press the scroll against the palm of the gargoyles hand. The statue briefly comes to life, before shattering, revealing a shining set of armor on the ground.\n"
	
	###############handle conditional cases###############
	if item.name == "goldcoin" and feature.name == "stall":
		player.dropItem(item)
		items.append(hotSauce)
		player.addItem(hotSauce)
		return "message", "You have bought the hot sauce"
	
	if item.name == "knife" and feature.name == "table":
		player.dropItem(item)
		items.append(heirloom)
		return "message", "An old pocketwatch appears on your plate"
		
	if item.name == "heirloom" and feature.name == "grave":
		player.dropItem(item)
		items.append(spirit)
		player.addItem(spirit)
		if (heart in player.getInventory()) and (workingbrain in player.getInventory()):
			return "room", "goodending"
		else:
			return "message", "A ghost rises from the grave and begins to follow you"
	########################################################
	
	return "error", "invalid action (or not yet  implemented)"
 
def initiateFight():
	player.inFight = True
	return "specialmessage", "reaper"
	
def reaperBattle():
	response = reaper.reaperAction(player)
	return "error", response
	
def switchTurn():
	if (player.pTurn == True):
		player.pTurn = False
	else:
		player.pTurn = True
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
	#textScreen.border(0)
	textScreen.addstr(3, 1, message, curses.color_pair(4))
	
	picScreen.clear()
	#picScreen.border(0)
	
	textScreen.refresh()
	picScreen.refresh()

#Function that displays animations
#picFiles is an array of picture.txt files
#colorArray is an integer array corresponding to the color_pairs to change the pic to
def specialMessage(textScreen, picScreen, message, picFiles, colorArray, MAX_LINES):
	textScreen.clear()
	textScreen.addstr(3, 1, message, curses.color_pair(4))
	
	numPics = len(picFiles)
	picIndex = 0
	for i in range(10):
		picScreen.clear()
		printFile(picFiles[picIndex], picScreen, 1, 1, colorArray[picIndex], MAX_LINES)
		textScreen.refresh()
		picScreen.refresh()
		time.sleep(.4)
		picIndex = (picIndex + 1) % numPics


	
def printInventory(nameScreen, picScreen, textScreen, invString):
		nameScreen.clear()
		#nameScreen.border(0)
		nameScreen.addstr(1,1, "PLAYER INVENTORY", curses.color_pair(1))
		
		picScreen.clear()
		#picScreen.border(0)
		
		textScreen.clear()
		textScreen.addstr(3,1, invString, curses.color_pair(4))
		#textScreen.border(0)
		
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

	#display screen settings on user's first visit
	if (not os.path.isfile("visited.txt")):
		with open("visited.txt", "w") as writeFile:
			writeFile.write("visited")
		stdscr.addstr(3, 3, "Screen Size: Height = 44 lines, Width = 155 characters.\n   Best played in fullscreen\n   Press any key to exit", curses.color_pair(1))
		stdscr.refresh()
		stdscr.getch()
		sys.exit()
		
	MAX_LINES = 15

	beginX = curses.COLS / 2 - 20
	beginY = 0
	height = 3
	width = 40
	captionWin = curses.newwin(height, width, beginY, beginX)
	#captionWin.border(0)
	captionWin.addstr(1, 8, "PROJECT POLKA", curses.color_pair(1))

	beginX = curses.COLS / 2 - 26
	beginY = 3
	height = 15
	width = 60
	picWin = curses.newwin(height, width, beginY, beginX)
	#picWin.border(0)
	welcomeFile = cwd + "/roomPics/welcome.txt"
	printFile(welcomeFile, picWin, 1, 1, 2, MAX_LINES)
	
	beginX = 0
	beginY = 17
	height = 20
	width = curses.COLS - 1
	textWin = curses.newwin(height, width, beginY, beginX)
	#textWin.border(0)
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
	#inputWin.border(0)
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
	
	#personalize center room.
	f = open(os.getcwd() + "/roomDescriptions/center.txt", 'w')
	f.write("You enter a cavernous room and see the devil, the Lord of Lies himself, in all his infernal glory.\n"
			+'"Welcome to your own personal hell, ' + player.name + '. Before you lie five doors, each leading to\n'
			+'a special hell. Go, explore the hells, and return to me when you have decided the hell you wish to\n'
			+'suffer until the end of time."\n\n'
			+'You see the following doors standing in front of you, seemingly attached to nothing:\n'
			+'pinkdoor: A multihued door decorated with skulls and crosses\n'
			+'greendoor: What looks like an ordinary, lime-colored, apartment door\n'
			+'yellowdoor: A door made out of what appears to be sandstone\n'
			+'golddoor: A large wooden door decorated with gems and inlaid with gold designs\n'
			+'purpledoor: Another seemingly ordinary door. This one is a light shade of purple, and has no adornments other than a handle\n')
			
	f.close()
	
	
	value = "start"
	type = "room"
	dead = False
	while value != "exit":
	
		if type == "error":
			errorMessage(errorWin, value)
		
		elif type == "message":
			message(textWin, picWin, value)

		elif type == "inventory":
			printInventory(captionWin, picWin, textWin,value)
		
		elif type == "specialmessage":
			if value == "workingbrain":
				specialMessage(textWin, picWin, WORKING_BRAIN_MESSAGE, WORKING_BRAIN_PIC_FILES, WORKING_BRAIN_COLOR_ARRAY, MAX_LINES)
			elif value == "reaper":
				specialMessage(textWin, picWin, REAPER_MESSAGE, REAPER_PIC_FILES, REAPER_COLOR_ARRAY, MAX_LINES)
				
		else:
			name = str(cwd) + "/" + type + "Names/" + value + ".txt"
			pic = str(cwd) + "/" + type + "Pics/" + value + ".txt"
			#code for short room descriptions
			if type == "room" and value != "start" and roomsVisited[str(value)]:
					text = str(cwd) + "/" + type + "Descriptions/" + value + "short.txt"
			else:
				roomsVisited[str(value)] = True
				text = str(cwd) + "/" + type + "Descriptions/" + value + ".txt"
				
			#clear windows and set up borders
			captionWin.clear()
			picWin.clear()
			textWin.clear()
			inputWin.clear()
			#captionWin.border(0)
			#picWin.border(0)
			#textWin.border(0)
			#inputWin.border(0)
		
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
		#inputWin.border(0)
		inputWin.addstr(1, 1, ">", curses.color_pair(3))
		inputWin.refresh()
		curses.echo()
		
		
			
		if ((player.inFight == True) and player.pTurn == False):
			userInput = "rTurn"
		elif (dead == True):
			userInput = "exit"
		else:
			userInput = inputWin.getstr()
		if userInput == "exit":
			break
		command = []
		command = userInput.split()
		if (not checkPlayerHealth()):
			dead = True;
			type, value = "message", "You have died. For real this time. The reaper strips the soul from your corpse and you feel not but pain and suffering"
		else:
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
