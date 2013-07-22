# Progress bar Python demo
#

import platform
import sys
import time as timer
import random

sys.path.append('module') 
from ezLCD3xx import *

#check what OS we are on
#Windows
if platform.system() == 'Windows':
	LCD = ezLCD('com9') 
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
# CLear screen
LCD.cls()
LCD.fontw(1,'0')

LCD.theme(1, 155, 152, 0, 0, 0, 151, 8, 9, 0, 1)
# Set draw color to red
LCD.color(WHITE)
# Print string at coordinates x=80 and y=100
LCD.printString("Progress Bar Demo",80,10)
LCD.progressBar(1, 20, 40, 280, 30, 1, 1, 100, 1, 1,'V')
value = 1
while True:
#	timer.sleep(.1)
	'''
	if value == 30:
		LCD.theme(1, 155, 152, 0, 3, 0, 151, 6, 6, 6, 1)
		LCD.wstate(1, 3)
	if value == 60:
		LCD.theme(1, 155, 152, 3, 0, 3, 151, 4, 5, 0, 1)
		LCD.wstate(1,3)
	if value==100:
		LCD.theme(1, 155, 152, 3, 0, 0, 151, 8, 9, 0, 1)
		value =0
		LCD.wvalue(1,value)
		LCD.wstate(1,3)
	'''		
	LCD.wvalue(1,random.randrange(0,100))		

	
