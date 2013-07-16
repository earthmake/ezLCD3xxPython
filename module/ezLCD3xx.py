""" Python Module for earthlcd.com ezLCD 3xx line of displays
http://earthlcd.com

(c)2013 ken segler
ken@earthlcd.com 
requires pySerial http://pyserial.sourceforge.net/
"""

import serial
import io
import inspect
import traceback
'''
## Here is a snapshot of my new application:
#  \image html C:\Users\codeman\Documents\ezLCDPython\doxygen\python.png
#  \image latex application.eps "My application" width=10cm
#   
## ezLCD
#
#
'''
BLACK = 0
GRAY  = 1
SILVER= 2
WHITE = 3
RED = 4
MAROON = 5
YELLOW = 6
OLIVE = 7
LIME = 8
GREEN = 9
AQUA = 10
TEAL = 11
BLUE = 12
NAVY = 13
FUCHISA = 14
PURPLE = 15

FILLED =1

ON = 1
OFF = 0

FIFO = 0
LIFO = 1
CLEAR = 2


class ezLCD(object):
## ezLCD object
#
#
	##
	#
	#
	def __init__(self, interface):
		self.interface = interface
		self.ser = None

	## open serial port
	# @var self.interface 123
	# @var self.ser 123
	# @var self.sio 123
	def openSerial(self):
		self.ser = serial.Serial()
		self.ser.baudrate = 115200 
		self.ser.port = self.interface
		self.ser.timeout = .1
		try:
			self.ser.open()
			self.sio = io.TextIOWrapper( io.BufferedRWPair( self.ser, self.ser)) # TextWrapper
			print "ezLCD3xx "+ str(self.interface) +" open"	
			return True
		except :
			print "ezLCD3xx "+ str(self.interface) +" failed"
			return False

	def closeSerial(self):
		'''
		close
		'''
		self.ser.close()
		print "ezLCD3xx "+ str(self.interface) +" close"


	## This is a internal use function
	# 
	#
	def WaitForCR(self):
		cr = self.ser.read(1)
		if cr == '1':
			print 'Command Returned Error'
			frame = inspect.currentframe()
			stack_trace = traceback.format_stack(frame)
			print ''.join(stack_trace[:-2])
			
# General --------------------------------------------------------------------

	##
	#   \defgroup General Commands
	#   @{

	## The Verbose command will turn on or off more verbose errors
	# @param state 0=off 1=on
	#
	def verbose(self, state ):
		self.ser.write('verbose ' + state + '\r')
		self.WaitForCR()

	## The xmax command will return the max x of current display
	# @return x-horizontal resolution in pixels starting from 0
	#
	def xmax(self):
		self.ser.write('xmax\r')
		return self.ser.readline()

	## The ymax command will return the max y of current display
	# @return y-vertical resolution in pixels starting from 0
	#
	def ymax(self):
		self.ser.write('ymax\r')
		return self.ser.readline()

	## the ping command
	# @return 0 
	#
	def ping(self):
		self.ser.write('ping\r')
		return self.ser.readline()
	
	## The backlight command will set backlight brightness and timeout
	# @param brightness 1
	# @param timeout 2
	# @param level 3
	#
	def backlight(self, brightness, timeout = None, level = None ):
		if timeout == None and level == None:
			self.ser.write('light %d\r' % (brightness))
			self.WaitForCR()
		else:
			self.ser.write('light %d %d %d\r' % (brightness, timeout, level))
			self.WaitForCR()
			
	## The wquiet command disables the touch event data being sent to the console port.
	# @param state 0=off 1=on
	#
	def wquiet(self, state):
		self.ser.write('wquiet %d\r' % (state)) 
		self.WaitForCR()

	## The cfgio command will configure io pins 
	# @param pin
	# @param function
	#
	def cfgio(self, pin, function):
		self.ser.write('cfgio %d "%s"\r' % (pin, function))
		self.WaitForCR()

	## The io command use to set and clear io pins
	# @param pin
	# @param level
	#
	def io(self, pin, level=None):	
		if level == None:
			self.ser.write('io %d\r' % (pin))
			return self.ser.readline()	
		else:		
			self.ser.write('io %d %d\r' % (pin, level))
			self.WaitForCR()
			
	## The play command will play a macro stored on the drive of the ezLCD
	# @param macro filename
	#
	def play(self, filename):	
		self.ser.write('play %s\r' % (filename))
		self.WaitForCR()

	## The run command will run a macro stored on the drive of the ezLCD
	# @param macro filename 
	#
	def run(self, filename):	
		self.ser.write('run %s\r' % (filename))
		self.WaitForCR()

	## The reset command will reset the ezLCD and run startup.ezm same as power up
	#
	#
	def reset(self):
		self.ser.write('reset\r')
		self.WaitForCR()

	## The snapshot command will write a copy of the current display to the flash drive as a bmp
	# @param x	starting x position
	# @param y	starting y position 
	# @param w	width 
	# @param h  height
	# @param filename.bmp
	#		
	def snapshot(self, x, y, w, h, filename):
		self.ser.write('snapshot %d %d %d %d %s\r' % (x, y, w, h, filename))
		self.WaitForCR()
			
	##
	# @}
	#
	
# Drawing --------------------------------------------------------------------

	##
	#   \defgroup Drawing Primitve Drawing Commands
	#   @{
	
	## The cls command will clear the screen to black it no color is given
	# @param Color color to clear screen to 
	def cls(self, Color = None):
		if Color == None:
				self.ser.write('cls\r')
		else:
				self.ser.write('cls %d\r' % (Color))
		self.WaitForCR()
	
	## The color command 
	# see ezLCD3xx manual for colors
	# @param color number 
	# @return color as a tuple
	def color(self, color=None):
		if color == None:
			self.ser.write('color\r')
			return self.ser.readline().split()
		else:
			self.ser.write('color %d\r' % (color))
			self.WaitForCR()

	## The colorId command
	# @param R	Red Value
	# @param G	Green Value
	# @param B	Blue Value
	# @return color as a tuple if r g b is None 
	def colorId(self,ID ,R=None, G=None, B=None):
		if R == None and G == None and B == None:
			self.ser.write('colorid %d\r' % (ID))
			return self.ser.readline().split()
		else:
			self.ser.write('colorid %d %d %d %d\r' % (ID, R, G, B))
			self.WaitForCR()

	## The xy command will set or return the x y coordinates
	# @param x x position
	# @param y y position
	# @return x y if x and y are used
	def xy(self, x = None , y = None):
		if x == None:
			self.ser.write('xy\r')
			return self.ser.readline()
		else:
			self.ser.write('xy %d %d \r' % (x, y))			
			self.WaitForCR()

	## The plot command will set a pixel to current color and if used x y
	# @param x  optional
	# @param y optional
	def plot(self, x = None, y = None):
		if x == None:
			self.ser.write( 'plot \r' )
			self.WaitForCR()
		else:
			self.ser.write('plot %d %d \r' % (x, y))
			self.WaitForCR()

	## The lineType Command will set the line type for the line command
	# @param option 0 = solid, 1= dotted (1 pixel spacing between dots), 2 = dashed (2 pixel spacing between dashes)
	#
	def lineType(self, option):
		self.ser.write( 'lineType %d\r' % (option))
		self.WaitForCR()

	## The lineWidth Command will set the line width for the line command
	# @param width thin line (width = 1) or a thick line (width =3). Only [width] = 1 or 3 are available.
	#
	def lineWidth(self, width):
		self.ser.write( 'linewidth %d\r' % (width))
		self.WaitForCR()
		
	## The line command will draw a line from current xy to line(x,y)
	# @param x 
	# @param y
	#
	def line(self, x, y):
		self.ser.write( 'line %d %d\r' % (x,y))
		self.WaitForCR()

	## The box command will draw a box starting from the current xy in width and height with option for filled
	# @param width width of box in pixels
	# @param height height of box in pixels
	# @param fill 1=filled box 0=outline only *optional defaults to outline
	#
	def box(self, width, height, fill = 0):
		self.ser.write('box %d %d %d\r' % (width, height, fill))
		self.WaitForCR()

	## The circle command will draw a circle in the current xy with radius and optional filled
	# @param radius radius of circle 
	# @param fill 1=filled circle 0=outline only *optional defaults to outline
	def circle(self, radius, fill = 0):
		self.ser.write('circle %d %d\r' % (radius, fill))
		self.WaitForCR()

	## The pie command will draw a pie slice at current xy 
	# @param radius radius of pie
	# @param start	start angle
	# @param end	end angle
	#
	def pie(self, radius, start, end ):
		self.ser.write('pie %d %d %d\r' % (radius, start, end))
		self.WaitForCR()
		
	## The arc command will draw a arc i the current xy optional filled
	# @param radius radius of arc 
	# @param start	start angle
	# @param end	end angle
	# @param fill 1=filled arc 0=outline only *optional defaults to outline
	#
	def arc(self, radius, start, end, fill = 0):
		self.ser.write('box %d %d %d\r' % ( radius, start, end, fill))
		self.WaitForCR()
		
	## The cliparea command allows you to designate a rectangular/box area that you can draw in.\n
	#  Any surrounding area will be protected and no changes can be made to it
	# @param left
	# @param top
	# @param right
	# @param bottom
	#
	def clipArea(self, left, top, right, bottom):
		self.ser.write('cliparea %d %d %d %d\r' % (left, top, right, bottom))
		self.WaitForCR()
	
	## The clipenable command enables or disables cliparea
	# @param enable 0=off 1=on
	#	
	def clipEnable(self, enable):
		self.ser.write('clipenable %d\r' % (enable))
		self.WaitForCR()
					
	##
	# @}
		
# Widgets -------------------------------------------------------------------
	##
	#   \defgroup Widgets Widgets
	#   @{
	
	## The ameter widget
	# @param ID 
	# @param x
	# @param y
	# @param width
	# @param height
	# @param options
	# @param value
	# @param minV
	# @param maxV
	# @param theme
	# @param stringID
	# @param meterType
	#												
	def ameter(self, ID, x, y, width, height, options, value, minV, maxV, theme, stringID, meterType = 0):
		"""
		ameter [ID][x][y][width][height][options][value][minV][maxV][theme][stringID][type]
		"""
		self.ser.write('ameter %d %d %d %d %d %d %d %d %d %d %d %d\r' % (ID, x, y, width, height, options, value, minV, maxV, theme, stringID, meterType))
		self.WaitForCR()

	## The ameter_color command 
	# @param ID
	# @param color1
	# @param color2
	# @param color3
	# @param color4
	# @param color5
	# @param color6				
	#
	def ameter_color(self, ID, color1, color2, color3, color4, color5, color6):
		self.ser.write('ameter_color %d %d %d %d %d %d %d\r' % (ID, color1, color2, color3, color4, color5, color6))
		self.WaitForCR()

	## The dmeter widget
	# @param ID 
	# @param x
	# @param y
	# @param width
	# @param height
	# @param options
	# @param value
	# @param digits
	# @param dp
	# @param theme
	#												
	def dmeter(self, ID, x, y, width, height, options, value, digits, dp, theme ):
		self.ser.write('dmeter %d %d %d %d %d %d %d %d %d %d\r' % (ID, x, y, width, height, options, value, digits, dp, theme))
		self.WaitForCR()
		
		
	## The button command
	# @param ID 
	# @param x
	# @param y
	# @param width
	# @param height
	# @param options
	# @param align
	# @param radius
	# @param theme
	# @param stringID
	# @param text optional text for button												
	def button(self, ID, x, y, width, height, options, align, radius, theme, stringID, text = None):
		if text!=None:
			self.string(stringID,text)
		self.ser.write('button %d %d %d %d %d %d %d %d %d %d\r' % (ID, x, y, width, height, options, align, radius, theme, stringID))			
		self.WaitForCR()
		
	## The choice widget allows you to print a string and display buttons for the user to choose a response.
	# @param string the text about the buttons
	# @param theme the theme ID
	# @param string1 string for left button *optional defaults to YES
	# @param string2 string for center button *optional defaults to NO
	# @param string3 string for right button *optional defaults to CANCEL
	# @return 1=left button 
	# @return 0=center button 
	# @return -1=right button
	#
	def choice(self, string, theme, string1=None, string2=None, string3=None):
		if string1==None and string2==None and string3==None:
			self.ser.write('choice "%s" %d\r' % (string, theme))
		else:
			self.string(61, string1)
			self.string(62, string2)
			self.string(63, string3)	
			self.ser.write('choice "%s" %d\r' % (string, theme))
		return self.ser.readline()
										
	## The groupBox widget
	# @param ID 
	# @param x
	# @param y
	# @param width
	# @param height
	# @param options
	# @param theme
	# @param stringID
	#												
	def groupBox(self, ID, x, y, width, height, options, theme, stringID ):
		self.ser.write('gbox %d %d %d %d %d %d %d %d\r' % (ID, x, y, width, height, options, theme, stringID))
		self.WaitForCR()

	## The radioButton widget
	# @param ID 
	# @param x
	# @param y
	# @param width
	# @param height
	# @param options Options: 1=draw , 2=disabled, 3=checked, 4=first, 5=first and checked.
	# @param theme
	# @param stringID
	#												
	def radioButton(self, ID, x, y, width, height, options, theme, stringID ):
		self.ser.write('radio %d %d %d %d %d %d %d %d\r' % (ID, x, y, width, height, options, theme, stringID))
		self.WaitForCR()

	## The staticText widget
	# @param ID 
	# @param x
	# @param y
	# @param width
	# @param height
	# @param options Options: 1=left, 2=disabled , 3=right , 4=center, 5=left framed, 6=disabled framed, 7=right framed, 8=center framed , 9=redraw text.
	# @param theme
	# @param stringID
	#												
	def staticText(self, ID, x, y, width, height, options, theme, stringID ):
		self.ser.write('static %d %d %d %d %d %d %d %d\r' % (ID, x, y, width, height, options, theme, stringID))
		self.WaitForCR()				

	## The slider command
	# @param ID 
	# @param x
	# @param y
	# @param width
	# @param height
	# @param options
	# @param rrange
	# @param resolution
	# @param value
	# @param theme
	#												
	def slider(self, ID, x, y, width, height, options, rrange, resolution, value, theme):
		self.ser.write('slider %d %d %d %d %d %d %d %d %d %d\r' % (ID, x, y, width, height, options, rrange, resolution, value, theme))
		self.WaitForCR()

	## The progressBar command
	# @param ID 
	# @param x
	# @param y
	# @param width
	# @param height
	# @param options
	# @param value
	# @param mmax
	# @param theme
	# @param stringID
	#												
	def progressBar(self, ID, x, y, width, height, options, value, mmax, theme, stringID):
		self.ser.write('progress %d %d %d %d %d %d %d %d %d %d\r' % (ID, x, y, width, height, options, value, mmax, theme, stringID))
		self.WaitForCR()

	## The touchZone command
	# @param ID 
	# @param x
	# @param y
	# @param width
	# @param height
	# @param options
	#	
	def touchZone(self, ID, x, y, width, height, options):
		self.ser.write('touchzone %d %d %d %d %d %d\r' % (ID, x, y, width, height, options))
		self.WaitForCR()

	## The dial command
	# @param ID 
	# @param x
	# @param y
	# @param radius
	# @param option
	# @param resolution
	# @param value
	# @param mmax
	# @param theme
	#	
	def dial(self, ID, x, y, radius, option, resolution, value, maxx, theme):
		"""
		dial [ID][x][y][radius][option][resolution][value][max][theme]
		"""
		self.ser.write('dial %d %d %d %d %d %d %d %d %d\r' % (ID, x, y, radius, option, resolution, value, maxx, theme))
		self.WaitForCR()

	## The theme command sets the colors for widgets 
	# @param ID			   Theme ID
	# @param EmbossDkColor	Dark color for 3d effect
	# @param EmbossLtColor	Light color for 3d effect
	# @param TextColor0		
	# @param TextColor1
	# @param TextColorDisabled
	# @param Color0
	# @param Color1
	# @param ColorDisabled
	# @param CommonBkColor
	# @param Fontw			widget font for theme
	#
	#
	def theme(self, ID, EmbossDkColor, EmbossLtColor, TextColor0, TextColor1, TextColorDisabled, Color0, Color1, ColorDisabled, CommonBkColor, Fontw):
		self.ser.write('theme %d %d %d %d %d %d %d %d %d %d %d\r' % (ID, EmbossDkColor, EmbossLtColor, TextColor0, TextColor1, TextColorDisabled, Color0, Color1, ColorDisabled, CommonBkColor, Fontw ))
		self.WaitForCR()
		
	## The fontW command will set the font for widget
	# @param fontnumber number of the font
	# @param name filename of font
	# \n '0' and '1' are internal fonts
	#
	def fontw(self, fontnumber, name):
		self.ser.write('fontw %d %s\r' % (fontnumber, name))
		self.WaitForCR()

	## The string command will set or return a internal string
	# @param stringNumber number of string to set or return
	# @param string string to set optional
	# \n internal strings are used for text on buttons and other widgets
	# \n Strings are defined as 128 characters.  There are 64 strings (0 to 63).
	# \n String 61-63 are used by the CHOICE command.
	# \n String 64 is temp location.
	# \n String 65 is the product string
	# \n String 66 is the firmware string
	def string(self, stringNumber, string = None):
		if string !=None:
			self.ser.write('string %d "%s"\r' % (stringNumber, string))
			self.WaitForCR()
		else:
			self.ser.write('string %d\r' % (stringNumber))
			return self.ser.readline()

	## The wstack command will return the stack of widgets pressed
	# @param option 0=FIFO 1=LIFO 2=CLEAR
	#
	def wstack(self, option):
			self.ser.flushInput()
			self.ser.write('wstack %d\r' % (option))		
			return self.ser.readline()
		
	## The wvalue command will set or return a value to or from a widget
	# @param ID
	# @param value
	#
	def wvalue(self, ID, value = None):
		if value == None:
			self.ser.flushInput()
			self.ser.write('wvalue %d\r' % (ID))
			return self.ser.read(3)
		else:
			self.ser.write('wvalue %d %d\r' % (ID, value))
			self.WaitForCR()

	## The wstate command
	# @param ID
	#
	def wstate(self, ID):
		self.ser.flushInput()
		self.ser.write('wstate %d\r' % (ID))
		return self.ser.read(5)

	##
	# @}

# Bitmap --------------------------------------------------------------------

	##
	#   \defgroup BitmapFont Bitmaps and Fonts 
	#   @{
	
	## The picture command will display a bitmap in bmp, jpg, gif formats with optional coordinates
	# @param image filename of image 'logo.gif'
	# @param x x coordinates 
	# @param y y coordinates 
	# \n x y  are optional and if not supplied will display image at current xy 
	def picture(self, image, x=None, y=None):
		if x!=None:
			self.ser.write('image %x %y %s\r' % (x, y, image))
		else:
			self.ser.write('image %s\r' % (image))
		self.WaitForCR()

# Text --------------------------------------------------------------------

	## The font command will set current font to use 
	# @param font font name
	#\n '0' and '1' are internal fonts
	def font(self, font):
		self.ser.write('font %s\r' % (font))
		self.WaitForCR()

	## The FONTO command will change the orientation or direction the text prints.  
	# @param orientation 0=0 1=90 2=180 3=270 
	def fonto(self, orientation):
		self.ser.write('fonto %d\r' % (orientation))
		self.WaitForCR()
		
	def printChar(self, character):
		self.ser.write('print %c\r' % (character))
		self.WaitForCR()

	## print string in current color and font and optional coordinates
	# @param string string to print
	# @param x x coordinates 
	# @param y y coordinates 
	# \n x y  are optional and if not supplied will print string at current xy 
	def printString(self, string, x=None, y=None ):
		if x != None:
			self.xy(x, y)
		self.ser.write('print "%s"\r' % (string))			
		self.WaitForCR()
	##
	# @}
