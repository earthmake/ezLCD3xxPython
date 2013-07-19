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
# Set widget font 0
LCD.fontw(0,'1')
# Set wodget font 1
LCD.fontw(1,'0')
# Set theme #1 
LCD.theme(1, 155, 152, 3, 0, 3, 24, 4, 5, 0, 1)
# Print string at coordinates x=80 and y=100
LCD.printString("Hello From Python",80,100)
# Draw button widget with a ID of 1
LCD.button( 1,  80, 150, 155, 50, 1, 0, 10, 1, 3, 'Press Here')
# Clear widget stack
LCD.wstack(CLEAR)

while True:
    # check widget stack this will return widget updates (button press ect.) last in first out order
    (ID, Info, Data) = LCD.wstack(LIFO)
    # check if ID = 1 widget 1 and info = pressed 
    if ID == 1 and Info == 4:
        # move cursor to x=35 y=30 and draw a black box to clear previous text
        # then print button data
        LCD.xy(35,30)
        LCD.color(BLACK)
        LCD.box(250,40,FILLED)
        LCD.color(YELLOW)
        LCD.printString('Button Pressed', 90, 30)
    # check if ID = 1 widget 1 and info = pressed and released
    if ID == 1 and Info == 1:
        # move cursor to x=35 y=30 and draw a black box to clear previous text
        # then print button data
        LCD.xy(35,30)
        LCD.color(BLACK)
        LCD.box(250,40,FILLED)
        LCD.color(YELLOW)        
        LCD.printString('Button Pressed and Released', 35, 30)
        LCD.snapshot(0,0,320,240,'button.bmp')
        