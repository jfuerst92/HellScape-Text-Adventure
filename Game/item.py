#!/usr/bin/env python

class Item(object):
	def __init__(self, type, name,desc, curRoom):
		self.type = type
		self.name = name
		self.desc = desc
		self.curRoom = curRoom
		self.uses = 4
		
		#Items will have different effects. Not sure how that would work out, assigning different effects to. Maybe have a bunch of different item classes that inherit this one?? I dont know yet
		
	def getDescription(self):
		print self.desc

	def broken(self):
		if (self.uses > 0):
			return False
		else:
			return True
	
	def decUses(self):
		self.uses -= 1
			
"""
def getItemList():
	doru = Item("Doru", "A sharp tipped spear sits firmly planted in the sternum of some demonic skeleton. If this spear killed such a monster, I may benefit by holding on to this.", 0)
	scroll = Item("Scroll", "An old scroll that contains odd pictures and characters. It seems to hum with power. There is a spot with the outline of a hand...", 3)
	relic = Item("Relic", "An small pendant with a vial containing the dry blood of a long-passed Saint. Perhaps it may repel what evil lurks here... ", 4)
	key = Item("Key", "An old, bronze, slightly bent key that looks to unlock a door somewhere. I'm not sure this would still fit even.", 6)
	torch = Item("Torch", "At last! A way to see in this damnable darkness! But how long will it stay lit for?", 2)
	items = []
	items.append(doru)
	items.append(scroll)
	items.append(relic)
	items.append(key)
	items.append(torch)
	return items
"""
