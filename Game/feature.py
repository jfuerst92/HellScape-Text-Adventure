#!/usr/bin/env python

class Feature(object):
    def __init__(self,name,desc, room):
        self.name = name
        self.desc = desc
        self.room = room
        
        #Items will have different effects. Not sure how that would work out, assigning different effects to. Maybe have a bunch of different item classes that inherit this one?? I dont know yet
        
    def getDescription():
        return description
        
        
        
     #inherits Feature, adds options for a door feature. this door has one connection and can either be locked or unlocked.   
class DoorFeature(Feature):
    def __init__(self,name,desc, room, conn, locked):
        self.type = "door"
        self.name = name
        self.desc = desc
        self.room = room
        self.conn = conn
        self.locked = locked
        
        #Items will have different effects. Not sure how that would work out, assigning different effects to. Maybe have a bunch of different item classes that inherit this one?? I dont know yet
    
    
