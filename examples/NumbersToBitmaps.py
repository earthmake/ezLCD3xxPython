# Button Align ezLCD Python demo
#

import platform
import sys
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

filenames =['zero.gif','one.gif','two.gif','three.gif','four.gif','five.gif','six.gif','seven.gif','eight.gif','nine.gif','blank.gif']
# Turn verbose off 
LCD.verbose('off')
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
LCD.color(RED)
LCD.xy(0,0)
LCD.box(320,240)
LCD.printString('TouchZone Demo', 80, 10)
LCD.picture(filenames[1], 0, 0)
LCD.picture(filenames[2], 70, 0)
LCD.picture(filenames[3], 140,0)
LCD.picture(filenames[4], 210, 0)