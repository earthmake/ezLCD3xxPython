# Minimal ezLCD Python demo
#

import platform
import sys


sys.path.append("C:\Users\codeman\Documents\GitHub\ezLCD3xxPython\module") 
from ezLCD3xx import *

#check what OS we are on
#Windows
if platform.system() == 'Windows':
    LCD = ezLCD('com6') 
#Mac
elif platform.system() == 'Dawrwin':
    LCD = ezLCD('/dev/tty.usbsomething')
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
# Print string at coordinates x=80 and y=100
LCD.printString("Hello From Python",80,100)

