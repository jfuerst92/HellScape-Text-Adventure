#!/usr/bin/env python

from room import *
from player import *

'''
test main for testing
'''
def main():
	listRooms = readFile()
	userName = raw_input("Please enter a username: ")
	user = Player(userName,1)
	for x in range(15):
		print listRooms[x].name
		print listRooms[x].longDesc
		print listRooms[x].shortDesc
		print listRooms[x].conn1
		print listRooms[x].conn2
		print listRooms[x].invItem
		print listRooms[x].intItem
	print user.name
	print user.curRoom
	
if __name__=="__main__": main()