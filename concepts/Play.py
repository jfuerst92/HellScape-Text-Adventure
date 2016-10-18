#Author: Joseph Fuerst
#This is actually functioning now, so you can run it. Simply type python Play.py.
#Still requires additional function implementation as well as player/room/feature/item object integration. But the text parser works, and it
# is now very simple to add any new functionality when we want. Simply add words to the dictionary, another elif to the interprit function, and
# another function that does the desired functionality.


#The current game dictionary. It recognizes these words. 
verbs = ['look', 'touch', 'go', 'help', 'pull', 'use', 'pickup', 'pick', 'drop']
rooms = ['room1', 'room2', 'room3', 'room4']
items = ['stick', 'gun', 'key']
features = ['wall', 'door', 'lever', 'torch', 'statue']

#p1 = Player()  #the player object will be globally accessable to the play functions since they should be able to control and access everything

#
    
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
        print "This is a placeholder for the general description of the current room. It will describe the room as well as any features and items present in the room\n"
        return
    #if player is trying to look at a feature
    if (command[1] == "at"):
        lookAt = command[2]
    else:
        lookAt = command[1]
    for item in features:
        if (lookAt == item):
             #roomFeatures = player.currentRoom.getFeatures() #get the features of the current room to look at.
             print "You looked at the " + item + ". This is placeholder text for the feature description. This will be contained in a feature object that will have a get method to obtain the info"
             return
             #for feat in roomFeatures:
                #if (command[1] == feat):
                    #feature.inspect() #This function will display the description of the feature. If features are objects, then this may have to be passed in somehow 
                    #return
    
    
    #if player is trying to look at an item
    for item in items:
         if (lookAt == item):
             #roomItems = player.currentRoom.getItems() #get the items (not picked up) of the current room to look at.
            print "You looked at the " + item + ". This is placeholder text for the item description. This will be contained in an item object that will have a get method to obtain the info"
            return
            #for item2 in roomItems:
                #if (command[1] == item2):
                    #item.inspect()#This function will display the description of the item. If items are objects, then this may have to be passed in somehow 
                    #return
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
        if (tItem == item):
         
            #roomItems = player.currentRoom.getItems() #get the items (not picked up) of the current room to look at.
            print "You pick up the " + item + ". This is placeholder text an item pick up. This will call the player object to add the item object into their inventory and remove it from the room's 'inventory' \n"
            return
            #for item2 in roomItems:
                #if (command[1] == item2):
#                   player.addItem(item) #This function should add the item to the players inventory
  #                 player.currentRoom.removeItem(item)
    #               print "You pick up the item and put it away in your bag.\n"
      #             return
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
        if (tItem == item):
             #roomItems = player.getItems() #get the items in the players inventory.
            print "You drop the " + item + ". This is placeholder text an item drop. This will call the player object to drop the item object into their inventory and add it to the room's 'inventory' \n"
            return
#             for item2 in roomItems:
  #              if (command[1] == item2):
    #               player.dropItem(item) #This function should drop the item from the players inventory
      #             player.currentRoom.addItem(item)
        #           print "You drop the item on the floor\n"
          #         player.currentRoom.dropEvent(item) #If dropping the item has some effect on the room, then this function would make that happen.
            #       return
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
 """   
            
def main():
    command = []
    command = getInput()
    while (command != None):
        for item in command:
            print item
        interprit(command)
        command = []
        command = getInput()
        
      
        
    return 0

if __name__ == "__main__":
    main()
