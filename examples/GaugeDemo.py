# # Gauge Python demo
# Ken Segler
# 
#

import platform
import sys
import time as timer
import random

sys.path.append('..\module') 
from ezLCD3xx import *

LCD = ezLCD(None) 
comPort =  LCD.findezLCD()

#check what OS we are on
#Windows
if platform.system() == 'Windows':
	LCD = ezLCD(comPort[0][0])
# Mac
elif platform.system() == 'Dawrwin':
	LCD = ezLCD('/dev/tty.usbsomething')
# Linux
elif platform.system() == 'Linux':
	LCD = ezLCD('/dev/ttyACM0')

# Bail out if comport error
if LCD.openSerial() == False:
	print 'Error Opening Port'
	raise SystemExit

# Turn verbose off 
LCD.verbose('off')
# Turn off button press info from ezLCD
LCD.wquiet(ON)
# Clear screen
LCD.cls()
# Use internal medium font
LCD.fontw(1, '0')
# Set draw color to red
LCD.color(RED)
# set x y to 0 
LCD.xy(0, 0)
# draw box
LCD.box(320, 240)
# set theme #1
LCD.theme(1, 155, 152, 0, 0, 0, 151, 8, 9, 0, 1)
# Set draw color to red
LCD.color(WHITE)
# Print string at coordinates x=80 and y=100
LCD.printString("Gauge Demo", 100, 10)
# LCD.printString(" Update Theme Based On Value", 30,40)
# 	def gauge(self, ID, x, y, width, height, options, initial, mmin, mmax, theme, stringID = None, text = None ):
LCD.gauge(1, 20, 90, 280, 30, 1, 1, 1, 200, 1, 1, ' Degrees F')
value = 1
low = -1
high = -1
average = -1
while True:
	value +=1
	if value >200:
		value =0
	timer.sleep(.1)
	LCD.wvalue(1, value)




