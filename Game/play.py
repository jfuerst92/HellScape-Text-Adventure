#Author: Joseph Fuerst
#This is actually functioning now, so you can run it. Simply type python Play.py.
#Still requires additional function implementation as well as player/room/feature/item object integration. But the text parser works, and it
# is now very simple to add any new functionality when we want. Simply add words to the dictionary, another elif to the interprit function, and
# another function that does the desired functionality.

from player import Player
from reaper import Reaper
from item import Item
from feature import Feature
#from feature import getItemList
from room import Room
from room import readFile
import os


rooms = readFile()
player = Player()
#items = Item.getItemList()

doru = Item("doru", "A sharp tipped spear sits firmly planted in the sternum of some demonic skeleton. If this spear killed such a monster, I may benefit by holding on to this.", 0)
rooms[0].items.append(doru)
scroll = Item("scroll", "An old scroll that contains odd pictures and characters. It seems to hum with power. There is a spot with the outline of a hand...", 3)
rooms[3].items.append(scroll)
relic = Item("relic", "An small pendant with a vial containing the dry blood of a long-passed Saint. Perhaps it may repel what evil lurks here... ", 4)
rooms[4].items.append(relic)
key = Item("key", "An old, bronze, slightly bent key that looks to unlock a door somewhere. I'm not sure this would still fit even.", 6)
rooms[6].items.append(key)
torch = Item("torch", "At last! A way to see in this damnable darkness! But how long will it stay lit for?", 2)
rooms[2].items.append(torch)
items = []
items.append(doru)
items.append(scroll)
items.append(relic)
items.append(key)
items.append(torch)


reaper = Reaper(9, rooms)
#The current game dictionary. It recognizes these words. 
verbs = ['look', 'touch', 'go', 'help', 'pull', 'use', 'pickup', 'pick', 'drop']
#rooms = ['room1', 'room2', 'room3', 'room4']
#items = ['stick', 'gun', 'key']
features = ['wall', 'door', 'lever', 'torch', 'statue']

#p1 = Player()  #the player object will be globally accessable to the play functions since they should be able to control and access everything

#

def checkItemInRoom(item):
    
    if item.curRoom == player.curRoom:
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
     
 #This function is not done. It will check which verb is being used, and branch of to one of the following functions accordingly. 
def interprit(command):
    words = 0
    for word in command:
        words += 1
    if (words == 0):
        return
    check = checkVerb(command[0])
    if (check == 0):
        print "Not a valid command...\n"
        return
    else:
        if (command[0] == "look"):  #This will call the appropriate command based on the verb that is used, then the individual functions will process the rest
            look(command, words)
        elif (command[0] == "pick" or command[0] == "pickup"):
            pickup(command, words)
        elif (command[0] == "drop"):
            drop(command, words)
        elif (command[0] == "go"):
            go(command, words)
        
    return
            
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
        
        rooms[player.curRoom].getLongDesc()
        return
    #if player is trying to look at a feature
    if (command[1] == "at"):
        lookAt = command[2]
    else:
        lookAt = command[1]
    """Not sure how features will work yet, like doors, bookshelves, levers etc.
    for feature in features:
        if (lookAt == feature.name):
             roomFeatures = rooms[player.curRoom].getFeatures() #get the features of the current room to look at.
             #print "You looked at the " + feature + ". This is placeholder text for the feature description. This will be contained in a feature object that will have a get method to obtain the info"
             
             for feat in roomFeatures:
                if (command[1] == feat.name):
                    feature.getDescription() #This function will display the description of the feature. If features are objects, then this may have to be passed in somehow 
                    return
    
    """   
    #if player is trying to look at an item
    for item in items:
        if (lookAt == item.name):
            if checkItemInRoom(item):
            #roomItems = rooms[player.curRoom].getItems() #get the items (not picked up) of the current room to look at.
            #print "You looked at the " + item.name + ". This is placeholder text for the item description. This will be contained in an item object that will have a get method to obtain the info"
                item.getDescription()#This function will display the description of the item. 
                return
    print "You look but you do not see this anywhere in the room.\n"
    return
    

#-------------------------------------------------------------------------------------------------------------------------------------------------------
# Function: pickup
# This function lets the user pick up an item on the ground and add it to their inventory. It checks that the item is valid and is also presently
# in the same room that the user is in. It will add the item to the player inventory and remove it from the room
# User input: pickup <item>
#------------------------------------------------------------------------------------------------------------------------------------------------------
def pickup(command, words): #the player object should be passed into the constructor, so we can get their current room and it's features
    tItem = ""
    if (words == 1):
        print "You must indicate an item to pick up\n"
        return
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
                print "You pick up the " + item.name + " and put it away in your bag.\n"
                return
    print "You look but you do not see this item anywhere in the room.\n"
    return
  
  
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
        print "You must indicate an item to drop\n"
        return
    
    tItem = command[1]
    #if player is trying to drop an item
    for item in items:
        if (tItem == item.name):
            playerItems = player.getInventory() #get the items in the players inventory.
            #print "You drop the " + item + ". This is placeholder text an item drop. This will call the player object to drop the item object into their inventory and add it to the room's 'inventory' \n"
           
            for item2 in playerItems:
                if (command[1] == item2.name):
                   player.dropItem(item2) #This function should drop the item from the players inventory
                   rooms[player.curRoom].addItem(item)
                   print "You drop the " + item2.name + " on the floor\n"
                   #player.curRoom.dropEvent(item) #If dropping the item has some effect on the room, then this function would make that happen.
                   return
    print "You you do not have such an item do drop.\n"
    return
    
    
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------
# Function: go
# This function ahs the user go to a new room. This isnt final, because the user may not know the names of the connecting rooms, but 
# it works for now.
#------------------------------------------------------------------------------------------------------------------------------------------------------
def go(command, words): #the player object should be passed into the constructor, so we can get their current room and it's features
    room = ""
    if (words == 1):
        print "You must indicate a place to go\n"
        return
    
    gRoom = command[1]
    
    i = 0
    for room in rooms:

        if (gRoom == room.name):
            roomCons = rooms[player.curRoom].getCons() #get the items in the players inventory.
            #print "You drop the " + item + ". This is placeholder text an item drop. This will call the player object to drop the item object into their inventory and add it to the room's 'inventory' \n"
            rmNum = i
            for item2 in roomCons:
                if (gRoom == rooms[item2].name):
                   player.changeRoom(i) #This function should drop the item from the players inventory
                   
                   rooms[player.curRoom].getLongDesc()
                   
                   return
    i += 1
    print "You you do not have such an item do drop.\n"
    return
   
   
"""
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
def use(command[]): #the player object should be passed into the constructor, so we can get their current room and it's features
    #if player is trying to use a feature
    for item in features:
        if (command[1] == item):
             roomFeatures = player.curRoom.getFeatures() #get the features of the current room to look at.
             for feat in roomFeatures:
                if (command[1] == feat):
                   feature.use() #This function will probably perform some kind of action on the feature? pull a lever, turn a knob, open a door etc. If an item is unusable currently it would say so. For instance, a locked door would remain locked. An unlit torch on the wall would do nothing. you cant 'use' a wall etc.
                    return
            print "You look but you do not see this feature in the room\n"
    
    #if player is trying to use an item
    for item in items:
         if (command[1] == item):
             roomItems = player.curRoom.getItems() #get the items items in players inventory
             for item2 in roomItems:
                if (command[1] == item2):
                    if (command[2] == "on"): #player is using an item on something else
                        for item in items:
                            if (command[3] == item):
                                playerItems = player.getItems() #get the items in player's inventory.
                                for item3 in playerItems:
                                    if (command[3] == item3):
                                    item3.uses(item1) #item1 is used on item 3
                                    return
                                
                                roomFeatures = player.curRoom.getFeatures() #get the features of the current room to look at.
                                for feat in roomFeatures:
                                    if (command[3] == feat):
                                        feat.uses(item1) #item 1 is used on the feature
                                        return
                                print "You look but you do not see this in the room\n"
                                return
                    else:
                        player.curRoom.use(item) #use the item by itself? it has to have some kind of effect on the room, so the room object that the player is visiting would need to have a use function that changes the room based on the used item. A dark room would be lit up by a flashlight, etc.
                        return
                print "You do not have this item"
    
    if (command[1] == NULL): #player just wants to look around, so describe everything, what features, and what items are in the room
        player.curRoom.getDescription()
        return
    else: #The player has entered something that is not in the game, they will never find it.
        print "You cannot find what you are looking for.\n"
return
 """   
            
def main():

    #os.system('cls') #FOr windows atm. will switch to linux

    pName = raw_input("Enter a name for your character:")
    player.setName(pName)
    
    #placeholder items for the moment.
   
    
    
    print "You wake up with an aching headache and no idea where you are. Unsure of the disturbing reality that now surrounds you, you stand and rub your eyes. "
    print " Suddenly, a voice whispers in your ear : \"Welcome to hell, " + player.name + ". I am coming.\" You can feel pure terror surrounding you. You must get out."
    print "Type \"help\" to get a list of commands."
    command = []
    command = getInput()
    while (command != "exit" and player.health > 0):
        #for item in command:
            #print item
        interprit(command)
        command = []
        command = getInput()
        
      
        
    return 0

if __name__ == "__main__":
    main()