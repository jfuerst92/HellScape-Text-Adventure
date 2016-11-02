#!/usr/bin/env python

#import item

'''
Very rough draft of room object. Getting
thoughts down.
'''

class Room(object):
	def __init__(self,name,longDesc,shortDesc,conn1,conn2, fname):
		self.name = name
		self.fname = fname		#file name used to load text files.
		self.longDesc = longDesc
		self.shortDesc = shortDesc
		self.conn1 = conn1
		self.conn2 = conn2
		self.items = []
	
def readFile():
	fileArr = ["limboFile.txt","lustFile.txt","glutFile.txt","greedFile.txt","wrathFile.txt","heresyFile.txt",
				   "viFile.txt","fraudFile.txt","treachFile.txt","centerFile.txt"]
	roomList = []
	initRooms(roomList)
	for x in range(len(fileArr)):
		tempFile = fileArr[x]
		with open(tempFile) as f:
			f = f.read().splitlines()
		seg = [i for i in f if i and not i.strip().startswith('!')]
		roomList[x].name = seg[0]
		roomList[x].longDesc = seg[1]
		roomList[x].shortDesc = seg[2]
		roomList[x].conn1 = seg[3]
		roomList[x].conn2 = seg[4]
		roomList[x].items.append(seg[5])
		roomList[x].items.append(seg[6])
		#get filename
		index = fileArr[x].find("F")
		roomList[x].fname = fileArr[x][0:index]
	return roomList
		
def initRooms(rooms):
	for x in range(10):
		tempRoom = Room(" "," "," ",0,0, " ")
		rooms.append(tempRoom)
	