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
	LCD.xy(0,30)
	LCD.color(BLACK)
	LCD.box(319,110,1)
	LCD.xy(0,0)
	LCD.color(GREEN)
	LCD.printString('Core 1')
	LCD.color(YELLOW)
	LCD.printString('Core 2')
	LCD.color(155)

	for y in range(6):
		LCD.xy(0,(y*20)+39)
		LCD.line(319,(y*20)+39)
	for x in range(16):
		LCD.xy(x*20,39)
		LCD.line(x*20,139)
	LCD.xy(319,39)
	LCD.line(319,139)

def drawTime(res):
	LCD.xy(0,140)
	LCD.color(BLACK)
	LCD.box(319,40, FILLED)
	LCD.color(WHITE)
	Time=str(res)+' Second(s) Per Div'
	LCD.printString(Time)
		  
if platform.system() == 'Windows':
	LCD = ezLCD('com58') 
elif platform.system() == 'Dawrwin':
	LCD = ezLCD('/dev/tty.usbsomething')
if LCD.openSerial()==False:
	print 'Error Opening Port'
	raise SystemExit   
	
LCD.verbose('off');
LCD.fontw(0,'1')
LCD.fontw(1,'0')
LCD.fontw(2,'serif24')
LCD.theme(1, 155, 152, 3, 3, 3, 24, 4, 5, 0, 2)
LCD.backlight(100, 5, 10)
LCD.cls()
LCD.font('0')
LCD.fonto(0)
info = ' '
LCD.string( 1, '%')
LCD.string(2,'+')
LCD.string(3,'-')
LCD.color(WHITE)
LCD.cfgio(8,'analog')

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
LCD.button( 5, 20, 200, 80, 30 , 1, 0, 10, 1, 2)
LCD.button( 6, 120, 200, 80, 30 , 1, 0, 10, 1, 3)
#LCD.ameter(1, 0, 40, 400, 200, 3, 0, 0 , 100, 1, 1, 1 )
#   ameter 1  50  30  200  200  1 10  0   120  0  1
#LCD.printString('Total Physical Memory ' +  str(psutil.TOTAL_PHYMEM), 0, 0)
#LCD.printString('Number Of CPU Cores ' + str(psutil.NUM_CPUS),0 ,20)
print LCD.xmax()
print LCD.ymax()
LCD.xy(100,100)
print LCD.xy()
(r,g,b)=LCD.colorId(3)
print r,g,b
print LCD.string(65)
print LCD.string(66)
print LCD.color()
drawGrid()
x=0
y1=239
y2=239
lx=0
ly1=239
ly2=239
res=1
drawTime(res)		  
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
	
	if x >= 320:
		x=0
		y1=239
		y2=239
		lx =0
		ly1 =239
		ly2 =239
		drawGrid()
	touch = LCD.wstack(LIFO).split()
	if touch[0] == '5' and touch[2]=='4':
		res +=1
		drawTime(res)  
	if touch[0] == '6' and touch[2]=='4':
		if res > 1:
			res -=1
			drawTime(res)
#	LCD.wvalue(1, cores[0])
#	LCD.wvalue(2, cores[1])
#	LCD.setWvalue(3, cores[2])
#	LCD.setWvalue(4, cores[3])
LCD.closeSerial()
# End Test Program --------------------------------------


