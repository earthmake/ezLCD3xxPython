#!/usr/bin/env python
# Python Serial library for ezLCD3xx
# http://www.ezlcd.com/
#
# You need the pySerial Library by Chris Liechti
# http://pyserial.wiki.sourceforge.net/pySerial
#


# END SerLCD Class Definition --------------------------------------

# Start Test Program -----------------------------------------------
import commands
import os
import re
import time as timer
import sys
import platform
import time
import psutil
	
sys.path.append('module') 
from ezLCD3xx import *

def drawGrid():
	LCD.lineType(2)
	LCD.xy(0,30)
	LCD.color(BLACK)
	LCD.box(300,110,1)
	LCD.xy(0,0)
	LCD.color(GREEN)
	LCD.printString('Core 1')
	LCD.color(YELLOW)
	LCD.printString('  Core 2')
	LCD.color(155)
	LCD.color(LIME)
	LCD.font('1')
	LCD.font('0')
	LCD.color(151)
	for y in range(6):
		LCD.xy(0,(y*20)+39)
		LCD.line(300,(y*20)+39)
	for x in range(16):
		LCD.xy(x*20,39)
		LCD.line(x*20,139)
	LCD.xy(300,39)
	LCD.line(300,139)
	LCD.lineType(0)
	
def drawTime(res):
	LCD.xy(10,140)
	LCD.color(BLACK)
	LCD.box(300,30, FILLED)
	LCD.color(WHITE)
	Time=str(res)+' Second(s) Per Div'
	LCD.printString(Time)

	LCD.string(5, str(res))
	LCD.wstate(7,REDRAW)

comPort = raw_input('Enter Com Port -> ')
#check what OS we are on
#Windows
if platform.system() == 'Windows':
	LCD = ezLCD(comPort) 
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

LCD.ping()
LCD.verbose('OFF')
LCD.wquiet(ON)
LCD.cls()
LCD.fontw(0,'1')
LCD.fontw(1,'0')
LCD.fontw(2,'serif24')
LCD.theme(1, 155, 152, 3, 0, 3, 24, 4, 5, 0, 1)
LCD.backlight(100, 5, 10)
LCD.cls()
LCD.font('0')
LCD.fonto(0)
info = ' '
LCD.string( 1, '%')
LCD.color(WHITE)
LCD.cfgio(8,'analog')
print LCD.xmax()
print LCD.ymax()
print LCD.string(65)
print LCD.string(66)


LCD.button( 5, 20, 200, 80, 30 , 1, 0, 10, 1, 2, 'MORE')
LCD.button( 6, 120, 200, 80, 30 , 1, 0, 10, 1, 3, 'LESS')
LCD.staticText(7, 10, 170, 220, 25, 8, 1, 5, 'test')
drawGrid()
x=0
y1=239
y2=239
lx=0
ly1=239
ly2=239
res=5
drawTime(res)	
LCD.wstack(CLEAR)	  
while True:

	oldinfo = info
	cores=psutil.cpu_percent(interval=1, percpu=True)
	y1 = 139 - cores[0]
	y2 = 139 - cores[1]
	if x!=0:
		LCD.color(GREEN)
		LCD.xy(lx,ly1)
		LCD.line(x, y1)
		LCD.color(YELLOW)
		LCD.xy(lx,ly2)
		LCD.line(x, y2)
	ly1 = y1
	ly2 = y2
	lx = x   
	x += 20/res
	
	if x >= 300:
		x=0
		y1=239
		y2=239
		lx =0
		ly1 =239
		ly2 =239
		drawGrid()
	(ID, info, data) = LCD.wstack(LIFO)
	LCD.wstack(CLEAR)
	if ID == 5 and info==1:
		res +=1
		drawTime(res)  
	if ID == 6 and info==1:
		if res > 1:
			res -=1
			drawTime(res)
LCD.closeSerial()
# End Test Program --------------------------------------
