#!/usr/bin/env python

from room import *
from player import *

'''
test main for testing
'''
def main():
	listRooms = readFile()
	for x in range(10):
		print listRooms[x].name
		print listRooms[x].longDesc
		print listRooms[x].shortDesc
		print listRooms[x].conn1
		print listRooms[x].conn2
		print listRooms[x].invItem
		print listRooms[x].intItem
	
if __name__=="__main__": main()