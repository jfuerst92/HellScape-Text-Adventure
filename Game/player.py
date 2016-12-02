#!/usr/bin/env python

import room

class Player(object):

	inventory = []
	

	def __init__(self):
		self.curRoom = 0
		self.health = 10
		self.space = 0
		self.inFight = False
		self.pTurn = True
		#self.inventory = [None] *10
		
	def setName(self, name):
		self.name = name
	def getInventory(self):
		return self.inventory

	def changeRooms(self, room):
		self.curRoom = room
	
	def addItem(self, item):
		self.inventory.append(item)
		item.curRoom = -1
		self.space += 1

	def dropItem(self, item):
		self.inventory.remove(item)
		self.space -= 1
		
	def invHasSpace(self):
		if (self.space < 4):
			return True
		else:
			return False
		
