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

tzData = ( 1, 0, 33,  2, 46, 33, 3, 92, 33, 4, 138, 33, 5, 184, 33, 6, 230, 33, 7, 276, 33, 
		   8, 0, 79, 9, 46, 79, 10, 92, 79, 11, 138, 79, 12, 184, 79, 13, 230, 79, 14, 276, 79,  
		  15, 0, 125, 16, 46, 125, 17, 92, 125, 18, 138, 125, 19, 184, 125, 20, 230, 125, 21, 276, 125) 

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
# Draw button widget with a ID of 1
LCD.picture('im.gif') 
LCD.color(RED)
LCD.xy(0,0)
LCD.box(320,240)
LCD.printString('TouchZone Demo', 80, 10)
tzX = 0
tzY = 33
for count in range(0, 63, 3):
	LCD.touchZone(tzData[count], tzData[count+1], tzData[count+2],43 ,43, ENABLE)

while True:
	(ID, Info, Data) = LCD.wstack(FIFO)
	if ID > 0 and Info ==4:
		ID -=1
		LCD.color(BLACK)
		LCD.xy(tzData[(ID*3)+1],tzData[(ID*3)+2] )
		LCD.box(43,45)
		string ='TouchZone ' + str(ID+1) +' Pressed'
		LCD.printString(string, 60, 200)
	if ID > 0 and Info ==1 or Info ==2:
		ID -=1
		LCD.color(WHITE)		
		LCD.xy(tzData[(ID*3)+1],tzData[(ID*3)+2] )
		LCD.box(43,45)
		LCD.printString(string, 60, 200)
		

