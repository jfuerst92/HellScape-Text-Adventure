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
		
		
	
	#similar to a door, but requires three gems to be inserted. These are gem-type items that may be scattered around in different rooms.
class PuzzFeature(Feature):
	def __init__(self, name, desc, room, conn):
		self.type = "puzz"
		self.name = name
		self.desc = desc
		self.room = room
		self.conn = conn
		self.slots = 3
		
	def insertGem(self, player, item): #insert a gem, open slots drops by 1
		self.slots -= 1
		player.dropItem(item);
			
	def getEmptySlots(self):
		return self.slots
		
		
class HandFeature(Feature):
	def __init__(self, name, desc, room, item):
		self.type = "hand"
		self.name = name
		self.desc = desc
		self.room = room
		self.item = item
		
		
	def dropItem(self, rooms):
		rooms[self.room].items.append(self.item)
		
		
class LookFeature(Feature):
	def __init__(self, name, desc, room):
		self.type = "look"
		self.name = name
		self.desc = desc
		self.room = room
		