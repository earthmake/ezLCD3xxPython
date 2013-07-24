# Button Options ezLCD Python demo
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
LCD.color(WHITE)
LCD.printString('Button Options',90,4)
LCD.color(RED)
LCD.xy(0,0)
LCD.box(319,239)
LCD.button( 1,  30, 25, 250, 30, 1, 0, 10, 6, 3,'1 = Draw')
LCD.button( 2,  30, 60, 250, 30, 1, 0, 10, 6, 4,'2 = Disabled')
LCD.button( 3,  30, 95, 250, 30, 1, 0, 10, 6, 5,'3 = Pressed')
LCD.button( 4,  30, 130, 250, 30, 1, 0, 10, 6, 6,'4 = Not Pressed')
LCD.button( 5,  30, 165, 250, 30, 1, 0, 10, 6, 7,'5 = Pressed Disabled')
LCD.button( 6,  30, 200, 250, 30, 1, 0, 10, 6, 7,'6 = Not Pressed Disabled')


