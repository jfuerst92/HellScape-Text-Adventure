#!/usr/bin/env python

import curses
from curses import wrapper

def main(stdscr):
	stdscr.clear()

	curses.init_pair(1, curses.COLOR_RED, curses.COLOR_WHITE)
	curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
	curses.init_pair(4, curses.COLOR_BLUE, curses.COLOR_BLACK)

	beginX = curses.COLS / 2 - 20
	beginY = 0
	height = 3
	width = 40
	captionWin = curses.newwin(height, width, beginY, beginX)
	captionWin.border(0)
	captionWin.addstr(1, 15, "Room name", curses.color_pair(1))

	beginX = curses.COLS / 2 - 26
	beginY = 3
	height = 10
	width = 50
	picWin = curses.newwin(height, width, beginY, beginX)
	picWin.border(0)
	picWin.addstr(5, 18, "ASCII pic here", curses.color_pair(2))

	beginX = 0
	beginY = 13
	height = 20
	width = curses.COLS - 1
	textWin = curses.newwin(height, width, beginY, beginX)
	textWin.border(0)
	textWin.addstr(10, curses.COLS / 2 - 5, "Text here", curses.color_pair(4))

	beginX = 2
	beginY = 33
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
	
	#stdscr.border(0)
	#stdscr.addstr(12,25, "Python curses in action!")
	#stdscr.refresh()
	stdscr.getch()

wrapper(main)
