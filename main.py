
DEBUG = False
VERBOSE = False
PYGAME =  True
GTK = True


VERSION = 0.100
import sys
if '-v' in sys.argv:
	VERBOSE = True

print("PROTASKMAN - Simple task management for Linux")
print("Version " + str(VERSION))


if ("-H" in sys.argv) or ("-h" in sys.argv): #Help info
	print()
	print('-v | Verbose mode (show more information in the terminal window)')
	print('-V | Output version information and exit')
	print('-H | Output help information and exit')
	sys.exit()
	
if "-V" in sys.argv: #Program information
	sys.exit()
	
if VERBOSE:
	print("Running in verbose mode")
else:
	print("For more information (verbose mode) you can run the program with the -v flag.")

print()	
try:
	import gi
	gi.require_version('Gtk', '3.0')
except:
	print("Gtk+3 is not available. Please make sure that you have GTK+ installed.")
	GTK = False
	if DEBUG:
		raise
	
	
try:
	import pygame
except ImportError:
	print("The module pygame is not available. Audio and sleep mode will not work.")
	if VERBOSE:
		print("Please install the package python3-pygame or install it via PIP3. For more information on installing pygame refer to https://www.pygame.org/wiki/GettingStarted")
	PYGAME = False
	if DEBUG:
		raise

if GTK == False:
	print('\nCannot continue withou GTK+... exiting')
	sys.exit()
	sys.exit()
