#Early Text Parser Concept
#Joseph Fuerst


# IMPORTANT: This is written in python, but it is, for all intents and purposes, pseudocode. It is not functional, and probably full of errors and faults on a conceptual 
# level. Do not try to run this, as it will not work. However, this is my early vision of the functionality that the text parser will have with the rest of the program. It 
# assumes that there are player, room, feature and item objects that it can interact with. and call the functions of. It also treats commands as strings, and works with
# strings in the place of objects at this point. But in it's next iteration it will bridge the gap between the relationship between the strings and objects they represent. If 
# this does not match the format of the room and player code and whatnot,I can change it easily, since it is in a very early stage.

#just some example words for reference
verbs = ['look', 'touch', 'go', 'help', 'pull', 'use', 'pickup', 'drop']
rooms = ['room1', 'room2', 'room3', 'room4']
items = ['stick', 'gun', 'key']
features = ['wall', 'door', 'lever', 'torch', 'statue']
	
	
	
def getInput():
    action = raw_input('What do you want to do?/n>>')
    if (action == 'exit'):
        return 0
    parse(action)
    return 1
    
    
def parse(action): #splits command into seperate words, verb room item etc
    #blablabla seperate into words by character and store into an array called command, will do this when I get off the plane and get internet access back
    return command


    
 
 
def checkVerb(verb): 
    for item in verbs:
        if (verb == item):
            return 1
        else:
            return 0
 
 #This function is not done. It will check which verb is being used, and branch of to one of the following functions accordingly. 
def interprit(command[])
    check = checkVerb(command[0])
    if (check == 0):
        print "Not a valid command...\n"
        return
    else:
        if (command[0] = "look"):  #This will call the appropriate command based on the verb that is used, then the individual functions will process the rest
            
        
            
        
#-------------------------------------------------------------------------------------------------------------------------------------------------------
# Function: look
# This function lets the user look at something.  By itself, it simply looks around the room, and the user gets a long description of the room they're in
# The player can also look at features and items, and permitted that they are in the room or in the players inventory, they can get a long description of 
# the item or feature.
# User input: pickup <item>
#------------------------------------------------------------------------------------------------------------------------------------------------------ 
def look(command[]): #the player object should be passed into the constructor, so we can get their current room and it's features

    #if player is trying to look at a feature
    for item in features:
        if (command[1] == item):
             roomFeatures = player.currentRoom.getFeatures() #get the features of the current room to look at.
             for feat in roomFeatures:
                if (command[1] == feat):
                    feature.inspect() #This function will display the description of the feature. If features are objects, then this may have to be passed in somehow 
                    return
            print "You look but you do not see this feature in the room\n"
    
    #if player is trying to look at an item
    for item in items:
         if (command[1] == item):
             roomItems = player.currentRoom.getItems() #get the items (not picked up) of the current room to look at.
             for item2 in roomItems:
                if (command[1] == item2):
                    item.inspect()#This function will display the description of the item. If items are objects, then this may have to be passed in somehow 
                    return
            print "You look but you do not see this item anywhere in the room.\n"
            return
    
    if (command[1] == NULL): #player just wants to look around, so describe everything, what features, and what items are in the room
        player.currentRoom.getDescription()
        return
    else: #The player has entered something that is not in the game, they will never find it.
        print "You cannot find what you are looking for.\n"
        return
            
#-------------------------------------------------------------------------------------------------------------------------------------------------------
# Function: pickup
# This function lets the user pick up an item on the ground and add it to their inventory. It checks that the item is valid and is also presently
# in the same room that the user is in. It will add the item to the player inventory and remove it from the room
# User input: pickup <item>
#------------------------------------------------------------------------------------------------------------------------------------------------------
def pickup(command[]): #the player object should be passed into the constructor, so we can get their current room and it's features

    #if player is trying to pick up an item
    for item in items:
         if (command[1] == item):
             roomItems = player.currentRoom.getItems() #get the items (not picked up) of the current room to look at.
             for item2 in roomItems:
                if (command[1] == item2):
                   player.addItem(item) #This function should add the item to the players inventory
                   player.currentRoom.removeItem(item)
                   print "You pick up the item and put it away in your bag.\n"
                   return
            print "You look but you do not see this item anywhere in the room.\n"
            return
    
    
   #The player has entered something that is not in the game, they will never find it.
    return "You cannot find what you are looking for.\n"
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------
# Function: drop
# This function lets the user drop an item from their inventory onto the ground. It checks that the item is valid and is also presently
# in the user's inventory. It will add the item to the room and remove it from the inventory. THere may be additional functionality, if we want to
#do that. For instance, drop a burning thing on the ground in a carpeted or otherwise flammable room, and you may have an issue.
# User input: drop <item>
#------------------------------------------------------------------------------------------------------------------------------------------------------
def drop(command[]): #the player object should be passed into the constructor, so we can get their current room and it's features

    #if player is trying to drop an item
    for item in items:
         if (command[1] == item):
             roomItems = player.getItems() #get the items in the players inventory.
             for item2 in roomItems:
                if (command[1] == item2):
                   player.dropItem(item) #This function should drop the item from the players inventory
                   player.currentRoom.addItem(item)
                   print "You drop the item on the floor\n"
                   player.currentRoom.dropEvent(item) #If dropping the item has some effect on the room, then this function would make that happen.
                   return
            print "You you do not have such an item do drop.\n"
            return
    
    
   #The player has entered something that is not in the game, they will never find it.
    return "You cannot find what you are looking for.\n"
    
#-------------------------------------------------------------------------------------------------------------------------------------------------------
# Function: use
# This is a hell of a function. It lets the player use things in the room. The player can attempt to use certain features of the room such as
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
             roomFeatures = player.currentRoom.getFeatures() #get the features of the current room to look at.
             for feat in roomFeatures:
                if (command[1] == feat):
                   feature.use() #This function will probably perform some kind of action on the feature? pull a lever, turn a knob, open a door etc. If an item is unusable currently it would say so. For instance, a locked door would remain locked. An unlit torch on the wall would do nothing. you cant 'use' a wall etc.
                    return
            print "You look but you do not see this feature in the room\n"
    
    #if player is trying to use an item
    for item in items:
         if (command[1] == item):
             roomItems = player.currentRoom.getItems() #get the items items in players inventory
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
                                
                                roomFeatures = player.currentRoom.getFeatures() #get the features of the current room to look at.
                                for feat in roomFeatures:
                                    if (command[3] == feat):
                                        feat.uses(item1) #item 1 is used on the feature
                                        return
                                print "You look but you do not see this in the room\n"
                                return
                    else:
                        player.currentRoom.use(item) #use the item by itself? it has to have some kind of effect on the room, so the room object that the player is visiting would need to have a use function that changes the room based on the used item. A dark room would be lit up by a flashlight, etc.
                        return
                print "You do not have this item"
    
    if (command[1] == NULL): #player just wants to look around, so describe everything, what features, and what items are in the room
        player.currentRoom.getDescription()
        return
    else: #The player has entered something that is not in the game, they will never find it.
        print "You cannot find what you are looking for.\n"
        return


     
