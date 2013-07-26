# Button Align ezLCD Python demo
#

import platform
import sys
import time as timer
sys.path.append('..\module') 
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
LCD.printString('Number To Bitmap', 80, 10)
value = 0
string = '0000'
LCD.picture(filenames[int(string[0])], 60, 40)
LCD.picture(filenames[int(string[1])], 105, 40)
LCD.picture(filenames[int(string[2])], 170,40)
LCD.picture(filenames[int(string[3])], 215, 40)
oldDigit1 = 0
oldDigit2 = 0
oldDigit3 = 0
oldDigit4 = 0	
while True:
	timer.sleep(1)
	string = ('%04d' % value)
	digit1 = int(string[0])
	digit2 = int(string[1])
	digit3 = int(string[2])
	digit4 = int(string[3])
	'''
	if digit1 ==1 and digit2 ==2 and digit3 == 6 and digit4 ==0:
		digit1 =0
		digit2 =1
	if digit3 == 6 and digit4 == 0:
		if digit1 !=0 and digit2 !=1:
			digit2 +=1
		digit3 = 0

	value = (int(digit1*1000+digit2*100+digit3*10+digit4))
	'''
#	if digit1 == 0:
#		LCD.picture(filenames[10], 60, 40)
	if digit1 != oldDigit1:
		print 'Digit1 %d' % (digit1)
		LCD.picture(filenames[digit1], 60, 40)
	if digit2 != oldDigit2:
		print 'Digit2 %d' % (digit2)
		LCD.picture(filenames[digit2], 105, 40)
	if digit3 != oldDigit3:
		print 'Digit3 %d' % (digit3)
		LCD.picture(filenames[digit3], 170,40)
	if digit4 != oldDigit4:
		print 'Digit4 %d' % (digit4)
		LCD.picture(filenames[digit4], 215, 40)
	oldDigit1 = digit1
	oldDigit2 = digit2
	oldDigit3 = digit3
	oldDigit4 = digit4			
	value +=1
	if value == 9999:
		value = 0
