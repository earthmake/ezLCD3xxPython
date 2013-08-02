# Button Align ezLCD Python demo
#

import platform
import sys
import time 
sys.path.append('..\module') 
from ezLCD3xx import *

LCD = ezLCD(None) 

# @returns comport device firmware string59
comPort = LCD.findezLCD()

# check what OS we are on
# Windows
if platform.system() == 'Windows':
	for ez in range(0,len(comPort)):
		if comPort[ez][3] == 'Unit2':
			LCD = ezLCD(comPort[ez][0])
#		break
# Mac
elif platform.system() == 'Darwin':
	LCD = ezLCD('/dev/tty.usbsomething')
# Linux
elif platform.system() == 'Linux':
	LCD = ezLCD('/dev/ttyACM0')

# Bail out if comport error
if LCD.openSerial() == False:
	print 'Error Opening Port'
	raise SystemExit

filenames = ['b0.gif', 'b1.gif', 'b2.gif', 'b3.gif', 'b4.gif', 'b5.gif', 'b6.gif', 'b7.gif', 'b8.gif', 'b9.gif', 'bb.gif', 'bs.gif']
#filenames = ['g0.gif', 'g1.gif', 'g2.gif', 'g3.gif', 'g4.gif', 'g5.gif', 'g6.gif', 'g7.gif', 'g8.gif', 'g9.gif', 'gb.gif', 'gs.gif']
skullFileName = ['skull.gif','skull-90.gif','skull-18.gif','skull-27.gif']
# Turn verbose off 
LCD.verbose(OFF)
# Turn off button press info from ezLCD
LCD.wquiet(ON)
# CLear screen
LCD.cls()
# Set draw color to red
LCD.color(RED)
# Set widget font 0
LCD.fontw(0, '1')
# Set wodget font 1
LCD.fontw(1, '0')
# Set theme #1 
LCD.theme(1, 155, 152, 3, 0, 3, 24, 4, 5, 0, 1)
LCD.color(RED)
LCD.xy(0, 0)
LCD.box(320, 240)
LCD.printString('Number To Bitmaps', 80, 10)
value = 0
string = '0000'
# LCD.picture(filenames[int(string[0])], 60, 40)
# #LCD.picture(filenames[int(string[1])], 105, 40)
# LCD.picture(filenames[int(string[2])], 170,40)
# LCD.picture(filenames[int(string[3])], 215, 40)
oldDigit1 = 0
oldDigit2 = 0
oldDigit3 = 0
oldDigit4 = 0	
startx = 70
second = True
skull = 0
while True:
#	x=LCD.touchX()
#	y=LCD.touchY()
#	s=LCD.touchS()
	time.sleep(1)
	clock = time.localtime()
	hour = clock[3]
	if hour > 12:
		hour -= 12
	value = (hour * 100 + clock[4])
	string = ('%04d' % value)
	digit1 = int(string[0])
	digit2 = int(string[1])
	digit3 = int(string[2])
	digit4 = int(string[3])
	if digit1 == 0:
		LCD.picture(filenames[10], startx, 40)
	else:
#		if digit1 != oldDigit1:
		LCD.picture(filenames[digit1], startx, 40)		
#	if digit2 != oldDigit2:
	LCD.picture(filenames[digit2], startx + 34, 40)

	if second == True:
		LCD.picture(filenames[11], startx + 34 * 2, 40)
		LCD.picture(skullFileName[skull],120,120)
		skull +=1
		if skull > 3:
			skull =0
		second = False
	else:
		LCD.picture(filenames[10], startx + 34 * 2, 40)
		second = True
#	if digit3 != oldDigit3:
	LCD.picture(filenames[digit3], startx + 34 * 3, 40)
#	if digit4 != oldDigit4:
	LCD.picture(filenames[digit4], startx + 34 * 4, 40)
	oldDigit1 = digit1
	oldDigit2 = digit2
	oldDigit3 = digit3
	oldDigit4 = digit4			

