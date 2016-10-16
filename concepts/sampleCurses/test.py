#!/usr/bin/env python

import curses
from curses import wrapper
import os

def printFile(fileName, printScreen, startY, startX, color, maxLength):
	yOffset = 0
	with open(fileName, "r") as readFile:
		for line in readFile:
			#display only enough data as can fit on screen
			if yOffset == maxLength - 1:
				printScreen.addstr(startY + yOffset, startX, "-----Press any key to continue-----")
				printScreen.getch()
				printScreen.clear()
				yOffset = 0

			printScreen.addstr(startY + yOffset, startX, line, curses.color_pair(color))
			yOffset += 1

'''	
cwd = os.getcwd()
roomName1 = str(cwd) + "/roomNames/rName1.txt"
roomPic1 = str(cwd) + "/roomPics/rPic1.txt"
s = 4
printFile(roomName1, s, 1, 1, 1)
printFile(roomPic1, s, 1, 1, 1)

'''
def main(stdscr):		
	stdscr.clear()

	curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
	curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)

	MAX_LINES = 15

	beginX = curses.COLS / 2 - 20
	beginY = 0
	height = 3
	width = 40
	captionWin = curses.newwin(height, width, beginY, beginX)
	captionWin.border(0)
	captionWin.addstr(1, 15, "Room Name Here", curses.color_pair(1))

	beginX = curses.COLS / 2 - 26
	beginY = 3
	height = 15
	width = 60
	picWin = curses.newwin(height, width, beginY, beginX)
	picWin.border(0)
	picWin.addstr(5, 18, "ASCII pic here", curses.color_pair(2))

	beginX = 0
	beginY = 20
	height = 20
	width = curses.COLS - 1
	textWin = curses.newwin(height, width, beginY, beginX)
	textWin.border(0)
	textWin.addstr(10, curses.COLS / 2 - 5, "Text here", curses.color_pair(4))

	beginX = 2
	beginY = 41
	height = 3
	width = curses.COLS - 3
	inputWin = curses.newwin(height, width, beginY, beginX)
	inputWin.border(0)
	inputWin.addstr(1, 1, ">", curses.color_pair(3))

	stdscr.refresh()
	picWin.refresh()
	captionWin.refresh()
	textWin.refresh()
	inputWin.refresh()
	
	stdscr.getch()

	userInput = "temple"
	while userInput != "exit":
	
		cwd = os.getcwd()
		roomName1 = str(cwd) + "/roomNames/" + userInput + ".txt"
		roomPic1 = str(cwd) + "/roomPics/" + userInput + ".txt"
		roomText1 = str(cwd) + "/roomDescriptions/" + userInput + ".txt"
	
		#clear windows and set up borders
		captionWin.clear()
		picWin.clear()
		textWin.clear()
		inputWin.clear()
		captionWin.border(0)
		picWin.border(0)
		textWin.border(0)
		inputWin.border(0)
	
		#load rooms from file
		printFile(roomName1, captionWin, 1, 1, 1, 10)
		printFile(roomPic1, picWin, 1, 1, 2, MAX_LINES) 
		captionWin.refresh()
		picWin.refresh()
		inputWin.refresh()
		printFile(roomText1, textWin, 1, 1, 4, MAX_LINES)	
		textWin.refresh()

		#get input from user
		inputWin.addstr(1, 1, ">", curses.color_pair(3))
		inputWin.refresh()
		curses.echo()
		userInput = inputWin.getstr()
		curses.noecho()

		stdscr.refresh()	
		picWin.refresh()
		captionWin.refresh()
		textWin.refresh()
		inputWin.refresh()

	stdscr.getch()	

wrapper(main)

