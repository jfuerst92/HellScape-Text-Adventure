#!/usr/bin/env python

#import item

'''
Very rough draft of room object. Getting
thoughts down.
'''

class Room(object):
  def __init__(self,name,longDesc,shortDesc,conn1,conn2,invItem,intItem):
	self.name = name
	self.longDesc = longDesc
	self.shortDesc = shortDesc
	self.conn1 = conn1
	self.conn2 = conn2
	self.invItem = invItem
	self.intItem = intItem
	
def readFile(room):
	with open("limboFile.txt") as f:
		f = f.read().splitlines()
		
	seg = [x for x in f if x and not x.strip().startswith('!')]
	
	room.name = seg[0]
	room.longDesc = seg[1]
	room.shortDesc = seg[2]
	room.conn1 = seg[3]
	room.conn2 = seg[4]
	room.invItem = seg[5]
	room.intItem = seg[6]
	
def main():
	limboRoom = Room(" "," "," ",0,0," "," ")
	
	readFile(limboRoom)
	
	print limboRoom.name
	print limboRoom.longDesc
	print limboRoom.shortDesc
	print limboRoom.conn1
	print limboRoom.conn2
	print limboRoom.invItem
	print limboRoom.intItem
	
if __name__=="__main__": main()
		
	