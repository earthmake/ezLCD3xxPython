# Minimal ezLCD Python demo
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
elif platform.system() == 'Darwin':
    LCD = ezLCD('/dev/tty.usbsomething')
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
LCD.color(BLUE)
# Print string at coordinates x=80 and y=100
LCD.printString("Hello From Python",80,100)
# Close serial port
LCD.closeSerial()

