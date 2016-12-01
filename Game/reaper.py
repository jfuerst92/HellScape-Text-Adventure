#!/usr/bin/python



from random import randint

class Reaper(object):
	

	def __init__(self, startRoom):
		self.curRoom = startRoom
		#startRoom.reaperPresent = True
		self.stunned = False
		self.sTime = 0

		
		
	def changeRoom(self):	 
		
		decision = randint(0,14)
		self.curRoom = decision

	
	
	def attackPlayer(self, player):
		for item in player.inventory:
			if item.type == "defense": #this will be some item that prevents attacks and repels the reaper
				response = "The dark figure flees at the sight of your " +  item.name + "! It has fled the room, for now..."
				player.pTurn = True
				player.inFight = False
				self.changeRoom()
				return response
		response = "The cloaked figure reveals its razor sharp weapon and swings at you, your health is lowered. You must escape."
		player.health -= 1
		return response
	
	
	def reaperAction(self, player):
		if not self.stunned:
			if (player.curRoom == self.curRoom):
				
				return self.attackPlayer(player)
			else:
				self.changeRoom();
				return
		else:
			if (not player.curRoom == self.curRoom):
				self.stunned = False
				self.changeRoom()
			else:
				if (self.sTime >= 10):
					response =  "The reaper awakens from it's state, it rushes to attack you!"
					self.sTime = 0
					self.stunned = False
					self.attackPlayer(player);
					return response
				else:
					response =  "The dark figure seems to still be stunned, for now... I wouldn't wait around too long though.."
					self.sTime += 1
					return response
		
	def getAttacked(self):
		response =  "As the weapon comes in to contact with the reaper, intense magical energy pours forth from it and stuns it. ."
		self.stunned = True
		return response
	   
