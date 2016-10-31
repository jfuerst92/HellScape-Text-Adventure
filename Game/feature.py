#!/usr/bin/env python

class Feature(object):
    def __init__(self,name,desc, room):
        self.name = name
        self.desc = desc
        self.room = room
        
        #Items will have different effects. Not sure how that would work out, assigning different effects to. Maybe have a bunch of different item classes that inherit this one?? I dont know yet
        
    def getDescription():
        return description