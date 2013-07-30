# Calibrate Touch ezLCD Python demo
#

import platform
import sys


sys.path.append('module') 
from ezLCD3xx import *

LCD = ezLCD(None) 
comPort = LCD.findezLCD()

# check what OS we are on
# Windows
if platform.system() == 'Windows':
	LCD = ezLCD(comPort[0][0])
#Mac
elif platform.system() == 'Dawrwin':
	LCD = ezLCD('/dev/tty.usbsomething')
# Bail out if comport error
if LCD.openSerial()==False:
	print 'Error Opening Port'
	raise SystemExit

LCD.calibrate()
