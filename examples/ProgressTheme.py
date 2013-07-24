## Progress bar Python demo
# Ken Segler
# 
# This demo will display a progress bar and change the theme based on the value of the progress bar
# Starts with a green theme then at 30 changes to yellow then to red after 60
#

import platform
import sys
import time as timer
import random

sys.path.append('..\module') 
from ezLCD3xx import *

#check what OS we are on
#Windows
if platform.system() == 'Windows':
	LCD = ezLCD('com4') 
#Mac
elif platform.system() == 'Dawrwin':
	LCD = ezLCD('/dev/tty.usbsomething')
#Linux
elif platform.system() == 'Linux':
	LCD = ezLCD('/dev/ttyACM0')

# Bail out if comport error
if LCD.openSerial()==False:
	print 'Error Opening Port'
	raise SystemExit

# Turn verbose off 
LCD.verbose('off')
# Turn off button press info from ezLCD
LCD.wquiet(ON)
# Clear screen
LCD.cls()
# Use internal medium font
LCD.fontw(1,'0')
# Set draw color to red
LCD.color(RED)
# set x y to 0 
LCD.xy(0,0)
# draw box
LCD.box(320,240)
# set theme #1
LCD.theme(1, 155, 152, 0, 0, 0, 151, 8, 9, 0, 1)
# Set draw color to red
LCD.color(WHITE)
# Print string at coordinates x=80 and y=100
LCD.printString("Progress Bar Demo",80,10)
LCD.printString(" Update Theme Based On Value", 30,40)
LCD.progressBar(1, 20, 90, 280, 30, 1, 1, 100, 1, 1,' PSI')

value = 1

while True:
	timer.sleep(.1)
	value +=1
	# update widget 1 value
	LCD.wvalue(1, value)
	if value == 30:
		# change theme when value get to 30
		LCD.theme(1, 155, 152, 0, 3, 0, 151, 6, 6, 6, 1)
		# redraw widget 1		
		LCD.wstate(1, 3)
	if value == 60:
		# change theme when value get to 60
		LCD.theme(1, 155, 152, 3, 0, 3, 151, 4, 5, 0, 1)
		# redraw widget 1
		LCD.wstate(1,3)
	if value==100:
		# change theme when value get to 100		
		LCD.theme(1, 155, 152, 3, 0, 0, 151, 8, 9, 0, 1)
		value = 1
		# reset widget 1 to 0
		LCD.wvalue(1,value)
		# redraw widget 1
		LCD.wstate(1,3)
