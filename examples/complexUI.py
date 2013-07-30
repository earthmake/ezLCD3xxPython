# Minimal ezLCD Python demo
#

import platform
import sys
import urllib2
import json
import time 
import calendar
import datetime

sys.path.append("..\module") 
from ezLCD3xx import *
def num (s):
	try:
		return int(s)
	except exceptions.ValueError:
		return float(s)
def ktof(t):
	return ((( t  -273) * 1.8) +32)

def drawGrid():
	LCD.lineType(2)
	LCD.xy(0,30)
	LCD.color(BLACK)
	LCD.box(300,150,1)

	LCD.xy(0,0)
	LCD.color(151)
	for y in range(11):
		LCD.xy(0,(y*10)+170)
		LCD.line(479,(y*10)+170)
	for x in range(24):
		LCD.xy(x*20,170)
		LCD.line(x*20,270)
	LCD.xy(479,170)
	LCD.line(479,270)
	LCD.lineType(0)
	LCD.color(WHITE)

def dt(u): 
	return datetime.datetime.utcfromtimestamp(u)

LCD = ezLCD(None) 
comPort =  LCD.findezLCD()

#check what OS we are on
#Windows
if platform.system() == 'Windows':
	for ez in range(0,len(comPort)):
		if comPort[ez][3] == 'Unit2':
			LCD = ezLCD(comPort[ez][0])
			break
#Mac
elif platform.system() == 'Dawrwin':
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
LCD.font('0')
#Pacific  = USTimeZone(-8, "Pacific",  "PST", "PDT")
#datetime.tzinfo=('PST')
datetime.timedelta(hours=-7)
#5358705
drawGrid()
while True:
	city = "huntingtonbeach" 
	url = "http://openweathermap.org/data/2.5/weather?id=5339840" #5339840 #5358705"
	try :
		request = urllib2.Request(url)
		response = urllib2.urlopen(request)
		weather = response.read()
	except:
		print 'none'
	data = json.loads(weather)
	LCD.lineType(2)
	LCD.xy(0,0)
	LCD.color(BLACK)
	LCD.box(300,150,1)
	LCD.color(WHITE)
	print data
	icon =  data['weather'][0]['icon']
	Time = dt( data['sys']['sunset'] )
	print Time
	pressure = data['main']['pressure']
	#windG = data['wind']['gust']
	windS = data['wind']['speed']
	windD = data['wind']['deg']		
	LCD.picture(icon + '.gif',400,10)
	temp = ktof(num(data['main']['temp']))
	tempmin = ktof(num(data['main']['temp_min']))
	tempmax = ktof(num(data['main']['temp_max']))
	humidity =data['main']['humidity']
	sky = data['weather'][0]['description']
	LCD.printString('Weather For %s' % data['name'], 0, 0)
	LCD.printString('Temp %d' % temp,0, 25)
	LCD.printString('Temp Low %d' % tempmin,0, 50)
	LCD.printString('Temp High %d' % tempmax,0, 75)
	LCD.printString('Humidity %s' % humidity,0, 100)
	LCD.printString('Pressure %s hpa' % pressure,0, 125)	

	LCD.printString('%s' % sky,170,25)
	#LCD.printString('Wind Gust %s' % windG,150,60)
	LCD.printString('Speed %s' % windS,170,100)
	if windD in range(348,11):
		windD = 'N'
	if windD in range(11,33):
		windD = 'NNE'
	if windD in range(33,56):
		windD = 'NE'
	if windD in range(56,78):
		windD = 'ENE'
	if windD in range(78,101):
		windD = 'E'
	if windD in range(101,123):
		windD = 'ESE'
	if windD in range(123,146):
		windD = 'SE'
	if windD in range(146,168):
		windD = 'SSE'
	if windD in range(168,191):
		windD = 'S'
	if windD in range(191,213):
		windD = 'SSW'
	if windD in range(213,236):
		windD = 'SW'
	if windD in range(236,258):
		windD = 'WSW'
	if windD in range(258,281):
		windD = 'W'
	if windD in range(281,303):
		windD = 'WNW'
	if windD in range(303,326):
		windD = 'NW'
	if windD in range(326,348):
		windD = 'NNW'



	LCD.printString('Direction %s' % windD,170,125)			


	time.sleep(360)
