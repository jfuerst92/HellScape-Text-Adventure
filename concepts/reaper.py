#!/usr/bin/python


#This file is non-functioning and is intended to represent the logic of the grim reaper
from random import randint

class Reaper(object):


    def __init__(self, startRoom):
        self.curRoom = startRoom
        startRoom.reaperPresent = true
        self.stunned = false
        self.sTime = 0

        
        
    def changeRoom():     
        curRoom.reaperPresent = false  #Not entirely sure how these objects are going to be referenced and otherwise handled. but this is at least the logic of what will happen
        int decision = randint(0,1)
        #I wrote this going with the current idea of there being two connections for each room. But this may end up with the reaper going back and forth between two rooms which would
        #be annoying for the player. Thus, I may change it so that it visits a completely random room, perhaps provided that we have some list of room objects to work with. 
        if decision == 0:
            self.curRoom = curRoom.conn1
            curRoom.conn1.reaperPresent = true
        else:
            self.curRoom = curRoom.conn2
            curRoom.conn2.reaperPresent = true
    
    
    def attackPlayer(player):
    
        #Here we might check that the player doesnt have a defensive item in their inventory?
        for item in player.inventory:
            if item = defensiveItem: #this will be some item that prevents attacks and repels the reaper
                print "The dark figure flees at the sight of your " +  item + "! It has fled the room, for now..."
                changeRoom()
                return
        print "The cloaked figure reveals its razor sharp weapon and swings at you, your health is lowered. You must escape."
        player.health -= 10
        return
    
    
    def reaperAction(player):
        if not stunned:
            if player.curRoom == self.curRoom:
                attackPlayer(player):
                return
            else:
                changeRoom();
                return
        else:
            if not player.curRoom == self.curRoom:
                self.stunned = false
                changeRoom()
            else:
                if sTime >= 10:
                    print "The reaper awakens from it's state, it rushes to attack you!"
                    self.sTime = 0
                    self.stunned = false
                    attackPlayer();
                print "The dark figure seems to still be stunned, for now... I wouldn't wait around too long though.."
                self.sTime += 1
            