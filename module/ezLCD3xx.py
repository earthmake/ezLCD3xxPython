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

# General --------------------------------------------------------------------

    def WaitForCR(self):
        '''
        wait
        '''
        cr = self.ser.read(1)
        if cr == '1':
            print 'Command Returned Error'
            frame = inspect.currentframe()
            stack_trace = traceback.format_stack(frame)
            print ''.join(stack_trace[:-2])
            
    def verbose(self, state ):
        """
        turn verbose on and off . use off in this module
        """
        self.ser.write('verbose ' + state + '\r')
        self.WaitForCR()

    def getXmax(self):
        """
        return the width of display in pixels
        """
        self.ser.write('xmax\r')
        return self.ser.read(4)

    def getYmax(self):
        """
        return the height of the display in pixels
        """
        self.ser.write('ymax\r')
        return self.ser.read(4)

    def ping(self):
        """
        sends a status check -> ezLCD responds with pong
        """
        self.ser.write("ping")

# Light ----------------------------------------------------------------------

    ## The backlight command will set backlight brightness and timeout
    # @param brightness 1
    # @param timeout 2
    # @param level 3
    def backlight(self, brightness, timeout = None, level = None ):
        if timeout == None and level == None:
            self.ser.write('light %d\r' % (brightness))
            self.WaitForCR()
        else:
            self.ser.write('light %d %d %d\r' % (brightness, timeout, level))
            self.WaitForCR()
            

# Drawing --------------------------------------------------------------------
    ##
    #   \defgroup Drawing Primitve Drawing Commands
    #   @{
    
    ## The cls command will clear the screen to black it no color is given
    # @param Color color to clear screen to 
    def cls(self, Color = None):
        if Color != None:
                self.ser.write('cls %d\r' % (Color))
        else:
                self.ser.write('cls \r')
        self.WaitForCR()
    
    ## The color command 
    # see ezLCD3xx manual for colors
    # @param color number 
    def color(self, color):
        self.ser.write('color %d\r' % (color))
        self.WaitForCR()

    def colorId(self,ID ,R, G, B):
        """
        set colorid to rgb vaules
        """
        self.ser.write( 'colorid %d %d %d %d\r' % (ID, R, G, B))
        self.WaitForCR()

    ## The xy command will set or return the x y coordinates
    # @param x optional
    # @param y optional
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

    def lineType(self, option):
        """
        Options: 0 = solid, 1= dotted (1 pixel spacing between dots), 2 = dashed (2 pixel spacing between dashes)
        """
        self.ser.write( 'lineType %d\r' % (option))
        self.WaitForCR()

    def lineWidth(self, width):
        """
        The LINEWIDTH command allows you to draw either a thin line (width = 1) or a thick line (width =3). Only [width] = 1 or 3 are available.
        """
        self.ser.write( 'linewidth %d\r' % (width))
        self.WaitForCR()
        
    def line(self, x, y):
        """
        draw a horizontal line from current position to x, y
        """
        self.ser.write( 'line %d %d\r' % (x,y))
        self.WaitForCR()

    def box(self, width, height, fill = 0):
        """
        draw a box of 'width' and 'height' from current coordinates 
        fill =1 will draw a filled box
        """
        self.ser.write('box %d %d %d\r' % (width, height, fill))
        self.WaitForCR()

    def circle(self, width, radius, fill = 0):
        """
        draw a circle with radius in pixels
        fill =1 will draw a filled circle
        """
        self.ser.write('box %d %d %d\r' % (width, radius, fill))
        self.WaitForCR()

    def pie(self, radius, start, end ):
        """
        The PIE command draws a section of a circle (pie slice) at current xy position.
        """
        self.ser.write('pie %d %d %d\r' % (radius, start, end))
        self.WaitForCR()
        
    def arc(self, radius, start, end, fill = 0):
        """
        The ARC command draws an arc at current XY position. Replace {R} with the desired radius of the arc, in pixels.
        fill =1 will draw a filled circle
        """
        self.ser.write('box %d %d %d\r' % ( radius, start, end, fill))
        self.WaitForCR()
    ##
    # @}
        
# Widgets -------------------------------------------------------------------
    ##
    #   \defgroup Widgets Widgets
    #   @{
    
    def ameter(self, ID, x, y, width, height, options, value, minV, maxV, theme, stringID, meterType = 0):
        """
        ameter [ID][x][y][width][height][options][value][minV][maxV][theme][stringID][type]
        """
        self.ser.write('ameter %d %d %d %d %d %d %d %d %d %d %d %d\r' % (ID, x, y, width, height, options, value, minV, maxV, theme, stringID, meterType))
        self.WaitForCR()
                
    def button(self, ID, x, y, width, height, options, align, radius, theme, stringID):
        """
        button [ID][x][y][width][height][options][align][radius][theme][stringID]
        """
        self.ser.write('button %d %d %d %d %d %d %d %d %d %d\r' % (ID, x, y, width, height, options, align, radius, theme, stringID))
        self.WaitForCR()

    def slider(self, ID, x, y, width, heigth, options, rrange, resolution, value, theme):
        """
        makes a slider
        """
        self.ser.write('slider ' + str(ID) + ' ' + str(x) + ' ' + str(y) + ' ' + str(width) + ' ' + str(heigth) + ' ' + str(options) + ' ' + str(rrange) + ' ' + str(resolution) + ' ' + str(value) + ' ' + str(theme) + '\r')
        self.WaitForCR()

    def progressBar(self, ID, x, y, width, heigth, options, value, max, theme, stringID):
        """
        progress [ID][x][y][width][height][option][value][max][theme]{stringid}
        makes a progressBar
        """
        self.ser.write('progress ' + str(ID) + ' ' + str(x) + ' ' + str(y) + ' ' + str(width) + ' ' + str(heigth) + ' ' + str(options) + ' ' + str(value) + ' ' + str(max) + ' ' + str(theme) + ' ' + str(stringID) + '\r')
        self.WaitForCR()

    def touchZone(self, ID, x, y, width, heigth, options):
        """ 
        best widget here 
        """
        self.ser.write('touchzone ' + str(ID) + ' ' + str(x) + ' ' + str(y) + ' ' + str(width) + ' ' + str(heigth) + ' ' + str(options) + '\r')
        self.WaitForCR()

    def dial(self, ID, x, y, radius, option, resolution, value, maxx, theme):
        """
        dial [ID][x][y][radius][option][resolution][value][max][theme]
        """
        self.ser.write('dial ' + str(ID) + ' ' + str(x) + ' ' + str(y) + ' ' + str(radius) + ' ' + str(option) + ' ' + str(resolution) + ' ' + str(value) + ' ' + str(maxx) + ' ' + str(theme) + '\r')
        self.WaitForCR()

    ## The fontW command will set the font for widget
    # @param fontnumber number of the font
    # @param name filename of font
    # \n '0' and '1' are internal fonts
    # @ingroup Widgets
    def fontW(self, fontnumber, name):
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
            self.ser.write('string %d \"%s\"\r' % (stringNumber, string))
            self.WaitForCR()
        else:
            self.ser.write('string %s\r' % (stringNumber))
            return self.ser.readline()

    ## The wstack command will return the stack of widgets pressed
    # @param option 0=FIFO 1=LIFO 2=CLEAR
    #
    def wstack(self, option):
            self.ser.flushInput()
            self.ser.write('wstack %d\r' % (option))        
            return self.ser.readline()
        
    def wvalue(self, ID, value = None):
        '''
        set
        '''
        if value == None:
            self.ser.flushInput()
            self.ser.write('wvalue %d\r' % (ID))
            return self.ser.read(3)
        else:
            self.ser.write('wvalue %d %d\r' % (ID, value))
            self.WaitForCR()

    def wstate(self, ID):
        """
        return state of widget button presses ect.
        """
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
        '''
        add here
        '''
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
        self.ser.write('print " %s "\r' % (string))            
        self.WaitForCR()
    ##
    # @}
