# Button ezLCD Python demo
#

import platform
import sys
sys.path.append('module') 
from ezLCD3xx import *

LCD = ezLCD(None) 
comPort =  LCD.findezLCD()

#check what OS we are on
#Windows
if platform.system() == 'Windows':
	LCD = ezLCD(comPort[0][0])
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
LCD.verbose(OFF)
# Turn off button press info from ezLCD
LCD.wquiet(ON)
# CLear screen
LCD.cls()
# Set draw color to red
LCD.color(RED)
# Set widget font 0
LCD.fontw(0,'1')
# Set wodget font 1
LCD.fontw(1,'0')
# Set theme #1 
LCD.theme(1, 155, 152, 3, 0, 3, 24, 4, 5, 0, 1)
# Print string at coordinates x=80 and y=100
LCD.printString("Hello From Python",80,100)
# Draw button widget with a ID of 1
LCD.button( 1,  80, 150, 155, 50, 1, 0, 10, 6, 3,'Press Here')
# Draw a staticText box
LCD.staticText(2, 35, 30, 250, 30, 8, 1, 1,'Press Button')
# Clear widget stack
LCD.wstack(CLEAR)
while True:
	# check widget stack this will return widget updates (button press ect.) last in first out order
	(ID, Info, Data) = LCD.wstack(FIFO)
#	print ID, Info, Data
	# check if ID = 1 widget 1 and info = pressed 
	if ID == 1 and Info == 4:
		# clear the stack just to be safe
#		LCD.wstack(CLEAR)
		# change draw color to yellow
		LCD.color(YELLOW)
		# change change string 1 for text on static text ID 2
		LCD.string(1,'Button Pressed')
		# redraw static text box ID 2 3=redraw		
		LCD.wstate(2, 3)
	# check if ID = 1 widget 1 and info = pressed and released
	if ID == 1 and Info == 1:
		# clear the stack just to be safe
#		LCD.wstack(CLEAR)
		# change draw color to yellow
		LCD.color(YELLOW)
		# change change string 1 for text on static text ID 2
		LCD.string(1,'Button Pressed and Released')
		# redraw static text box ID 2 3=redraw
		LCD.wstate(2, 3)

		