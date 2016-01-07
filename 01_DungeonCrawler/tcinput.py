#!/usr/bin/python

try:
	import msvcrt
	def getkey():  # define a Windows version
		return msvcrt.getch()
except ImportError:
	def getkey():   # define non-Windows version
		import sys, tty, termios
		fd = sys.stdin.fileno()
		old_settings = termios.tcgetattr(fd)
		try:
			tty.setraw(sys.stdin.fileno())
			ch = sys.stdin.read(1)
		finally:
			termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
		return ch