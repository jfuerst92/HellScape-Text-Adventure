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
	
def readFile(room,fName):
	with open(fName) as f:
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
	roomArr = []
	
	roomArr.append(limboRoom = Room(" "," "," ",0,0," ", " "))
	roomArr.append(lustRoom = Room(" "," "," ",0,0," ", " "))
	roomArr.append(glutRoom = Room(" "," "," ",0,0," ", " "))
	roomArr.append(greedRoom = Room(" "," "," ",0,0," ", " "))
	roomArr.append(wrathRoom = Room(" "," "," ",0,0," ", " "))
	roomArr.append(heresyRoom = Room(" "," "," ",0,0," ", " "))
	roomArr.append(viRoom = Room(" "," "," ",0,0," ", " "))
	roomArr.append(fraudRoom = Room(" "," "," ",0,0," ", " "))
	roomArr.append(treachRoom = Room(" "," "," ",0,0," ", " "))
	roomArr.append(centerRoom = Room(" "," "," ",0,0," ", " "))
	
	fileArr = ["limboFile.txt","lustFile.txt","glutFile.txt","greedFile.txt","wrathFile.txt","heresyFile.txt",
				   "viFile.txt","fraudFile.txt","treachFile.txt","centerFile.txt"]
	
	for x in roomArr:
		readFile(roomArr[x],fileArr[x])
	
if __name__=="__main__": main()
		
	