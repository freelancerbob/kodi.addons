# -*- coding: utf-8 -*-
import xbmcaddon
import xbmcgui
import os
# # check venv packages 
# print("aaaa")
# os.system("pip list")

addon       = xbmcaddon.Addon()
addonname   = addon.getAddonInfo('name')
 
line1 = "Hello World!4"
line2 = "We can write anything we want here"
line3 = "Using Python"
 
xbmcgui.Dialog().ok(addonname, line1)
