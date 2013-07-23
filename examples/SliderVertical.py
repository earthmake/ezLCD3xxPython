# Button Align ezLCD Python demo
#

import platform
import sys
sys.path.append('..\module') 
from ezLCD3xx import *

#check what OS we are on
#Windows
if platform.system() == 'Windows':
	LCD = ezLCD('com58') 
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
LCD.printString('Vertical Sliders Demo', 70, 10)
LCD.fonto(90)
LCD.color(WHITE)
LCD.slider(1, 30, 40, 40, 180, 3, 100, 5, 50, 6)
LCD.printString("Option = 1", 10, 210)
LCD.slider(2, 100, 40, 40, 180, 4, 100, 5, 50, 6)
LCD.printString("Option = 2", 80, 210)
LCD.slider(3, 170, 40, 40, 180, 7, 100, 5, 50, 6)
LCD.printString("Option = 5", 150, 210)
LCD.slider(4, 240, 40, 40, 180, 8, 100, 5, 50, 6)
LCD.printString("Option = 6", 220, 210)
LCD.snapshot(0,0,320,240,'SliderV.bmp')
