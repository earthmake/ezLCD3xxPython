#!/usr/bin/env python

import os
import re
import time as zeit
import sys
import urllib2
import tempfile
import shutil
import PIL
from PIL import Image

fifoName = '/tmp/ezLCD'
pandora_icon = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                            "pandora-icon-cc-by-sa-rossr.png")

command = sys.argv[1]

params = {}

for s in sys.stdin.readlines():
	param, value = s.split("=", 1)
	params[param.strip()] = value.strip()


info = {}
info["song"] = params["title"]
info["artist"] = params["artist"]
info["album"] = params["album"]
info["stationCount"] = params["stationCount"]
info["stationName"] = params["stationName"]
info["coverArt"] = params["coverArt"]
stations = []
growl_image = pandora_icon
for i in range(0, int(params["stationCount"])):
	stations.append(params["station"+str(i)])
	info["stations"] = stations
print ('Command ->')
print (command)
if command == "usergetstations":
	print (info["stations"])
	f = open('/tmp/station.lst','w')
	f.write("\n".join(info['stations']))
	f.close()
if command == "songstart":

	cover_art_url = info["coverArt"].strip()
    #if len(cover_art_url) > 0:
        (imgfp, growl_image) = tempfile.mkstemp(prefix="pianobar",suffix=".jpg")

        try:
            urlfp = urllib2.urlopen(cover_art_url)
            os.write(imgfp, urlfp.read())
        except ValueError, e:
            os.unlink(growl_image)
            growl_image = pandora_icon
        except urllib2.URLError, e:
            os.unlink(growl_image)
            growl_image = pandora_icon
        finally:
            os.close(imgfp)
            basewidth = 200
            img = Image.open(growl_image)
            wpercent = (basewidth/float(img.size[0]))
            hsize = int((float(img.size[1])*float(wpercent)))
            img = img.resize((basewidth,hsize), PIL.Image.ANTIALIAS)
            img.save(growl_image)
			
            shutil.copy(growl_image, "/media/codeman/EZLCD-304/EZUSER/IMAGES/temp.jpg")
            fifo = open(fifoName, 'w')
            fifo.write(info["stationName"] + '\n' + info["artist"] + '\n' + info["song"])
            fifo.close()
			
			
#/media/codeman/EZLCD-304/EZUSER/IMAGES/
            

