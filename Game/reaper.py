#!/usr/bin/python



from random import randint

class Reaper(object):


    def __init__(self, startRoom):
        self.curRoom = startRoom
        #startRoom.reaperPresent = True
        self.stunned = False
        self.sTime = 0

        
        
    def changeRoom():     
        curRoom.reaperPresent = False  
        decision = randint(0,1)
        #I wrote this going with the current idea of there being two connections for each room. But this may end up with the reaper going back and forth between two rooms which would
        #be annoying for the player. Thus, I may change it so that it visits a completely random room, perhaps provided that we have some list of room objects to work with. 
        if decision == 0:
            self.curRoom = curRoom.conn1
            curRoom.conn1.reaperPresent = True
        else:
            self.curRoom = curRoom.conn2
            curRoom.conn2.reaperPresent = True
    
    
    def attackPlayer(player):
    
        
        for item in player.inventory:
            if item.type == "defense": #this will be some item that prevents attacks and repels the reaper
                print "The dark figure flees at the sight of your " +  item + "! It has fled the room, for now..."
                changeRoom()
                return
        print "The cloaked figure reveals its razor sharp weapon and swings at you, your health is lowered. You must escape."
        player.health -= 1
        return
    
    
    def reaperAction(player):
        if not stunned:
            if player.curRoom == self.curRoom:
                attackPlayer(player)
                return
            else:
                changeRoom();
                return
        else:
            if not player.curRoom == self.curRoom:
                self.stunned = False
                changeRoom()
            else:
                if sTime >= 10:
                    print "The reaper awakens from it's state, it rushes to attack you!"
                    self.sTime = 0
                    self.stunned = False
                    attackPlayer();
                print "The dark figure seems to still be stunned, for now... I wouldn't wait around too long though.."
        self.sTime += 1
        
        
    def getAttacked():
        print "As the weapon comes in to contact with the reaper, intense magical energy pours forth from it and stuns it. ."
        changeRoom()
        return
       