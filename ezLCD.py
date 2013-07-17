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
import wmi
import time
import psutil
	
sys.path.append("C:\Users\segler\Documents\GitHub\ezLCD3xxPython\module") 
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
	LCD.printString('Core 2')
	LCD.color(155)
	LCD.color(LIME)
#	LCD.fonto(270)
	LCD.font('1')
#	LCD.printString('< 0 TO 100 Percent>',300,140)
	LCD.font('0')
#	LCD.fonto(0)
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
	LCD.xy(0,140)
	LCD.color(BLACK)
	LCD.box(319,30, FILLED)
	LCD.color(WHITE)
	Time=str(res)+' Second(s) Per Div'
	LCD.printString(Time)

	LCD.string(5, str(res))
	LCD.wstate(7,REDRAW)
			
if platform.system() == 'Windows':
	LCD = ezLCD('com4') 
elif platform.system() == 'Dawrwin':
	LCD = ezLCD('/dev/tty.usbsomething')
if LCD.openSerial()==False:
	print 'Error Opening Port'
	raise SystemExit   
	
LCD.verbose('off')
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
LCD.xy(100,100)
(x,y) = LCD.xy()
print int(x), int(y)
(r,g,b)=LCD.colorId(3)
print r,g,b
print LCD.string(65)
print LCD.string(66)
print LCD.color()
print LCD.io(8)


#print LCD.choice('test the choice', 1)
#LCD.printString('Core 1', 16, 85)
#LCD.printString('Core 2', 16, 125)
#LCD.printString('Core 3', 16, 165)
#LCD.printString('Core 4', 16, 205)
#LCD.progressBar( 1, 80, 80,  120, 30, 1, 1, 100, 1, 1)
#LCD.progressBar( 2, 80, 120, 120, 30, 1, 1, 100, 1, 1)
#LCD.progressBar( 3, 80, 160, 120, 30, 1, 1, 100, 1, 1)
#LCD.progressBar( 4, 80, 200, 120, 30, 1, 1, 100, 1, 1)
LCD.button( 5, 20, 200, 80, 30 , 1, 0, 10, 1, 2, 'MORE')
LCD.button( 6, 120, 200, 80, 30 , 1, 0, 10, 1, 3, 'LESS')
#LCD.ameter(1, 0, 40, 400, 200, 3, 0, 0 , 100, 1, 1, 1 )
#   ameter 1  50  30  200  200  1 10  0   120  0  1
#LCD.printString('Total Physical Memory ' +  str(psutil.TOTAL_PHYMEM), 0, 0)
#LCD.printString('Number Of CPU Cores ' + str(psutil.NUM_CPUS),0 ,20)
LCD.staticText(7, 0, 170, 220, 25, 8, 1, 5, 'test')
LCD.slider( 8, 200,200,200,50,1, 75, 5, 25, 1)
#sys.exit()
drawGrid()
x=0
y1=239
y2=239
lx=0
ly1=239
ly2=239
res=1
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
#	LCD.plot(x,239-y)

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
#	LCD.wvalue(1, cores[0])
#	LCD.wvalue(2, cores[1])
#	LCD.setWvalue(3, cores[2])
#	LCD.setWvalue(4, cores[3])
LCD.closeSerial()
# End Test Program --------------------------------------


