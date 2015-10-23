#!/usr/bin/env python
# Name:     nocommonssids.py
# Purpose:  Removes Common SSID's From OSX. 
# By:       Jerry Gamblin
# Date:     23.10.15
# Modified  23.10.15
# Rev Level 0.5
# -----------------------------------------------

from contextlib import closing
from urllib import urlopen
import os
import re
import time
import sys
from time import sleep


def color(text, color_code):
    if sys.platform == "win32" and os.getenv("TERM") != "xterm":
        return text

    return '\x1b[%dm%s\x1b[0m' % (color_code, text)


def red(text):
    return color(text, 31)

def blue(text):
    return color(text, 34)
    
ssids =["linksys",
		"xfinitywifi",
		"NETGEAR",
		"BTWiFi-with-FON",
		"dlink",
		"default",
		"hpsetup",
		"Ziggo",
		"FreeWifi",
		"BTWIFI",
		"FreeWifi_secure",
		"BTWifi-X",
		"TELENETHOMESPOT",
		"eduroam",
		"UPC Wi-Free",
		"optimumwifi",
		"AndroidAP",
		"belkin54g",
		"SFR WiFi Mobile",
		"cablewifi",
		"wireless",
		"Home",
		"asus",
		"SFR WiFi FON",
		"KPN Fon",
		"orange",
		"BTOpenzone",
		"UPC WifiSpots",
		"Guest",
		"WLAN",
		"attwifi",
		"setup",
		"internet",
		"TWCWiFi",
		"SFR WiFi Public",
		"portthru",
		"Tp-link",
		"Free Public WiFi",
		"hhonors",
		"iPhone",
		"SMC",
		"BTOpenzone-B",
		"MyPlace",
		"TWCWiFi-Passpoint",
		"airportthru",
		"orange12",
		"wlan-ap",
		"D-Link",
		"dd-wrt",
		"Orange_FunSpot",
		"MSHOME",
		"HomeNet",
		"Google Starbucks",
		"skynet",
		"3COM",
		"netgear-guest",
		"office",
		"tsunami",
		"TrendNET",
		"tmobile",
		"Target Guest Wi-Fi",
		"Linksys-G",
		"Fon",
		"mobile",
		"Home Network",
		"Marriott_Guest",
		"Private",
		"Network",
		"Voice",
		"02 WIFI",
		"admin",
		"FON_FREE_EAP",
		"Horizon Wi-Free",
		"NETGEAR1",
		"belkin",
		"pretty fly for a wifi",
		"coxwifi",
		"freebox",
		"ASUS_5G",
		"Connectify-me",
		"plusnetwireless",
		"david",
		"Apple",
		"Hotspot",
		"staff",
		"steel",
		"xerox",
		"Visitor",
		"Wi-Fi",
		"DLINK_WIRELESS",
		"Airlive",
		"netgear11",
		"Wireless Network",
		"OTE WiFi Fon",
		"net",
		"Home1",
		"HomeDepot Public Wi-Fi",
		"OutOfService",
		"GIGABYTE",
		"gogoinflight",
		"Admirals_Club",
		"Google Starbucks",
		"AUS Free Wifi",
		"DellWorld15"]

print (red("Your MAC Autoconnects To Following Wireless Networks:"))
os.system("networksetup -listpreferredwirelessnetworks en0")	
print "\n"
print "\n"
print (red("Removing The 100 Most Common SSIDS"))
for ssid in ssids: 
	os.system("networksetup -removepreferredwirelessnetwork en0 %s > /dev/null" % (ssid) )
print "\n"
print "\n"
print (blue("Your MAC Now Autoconnects To Following Wireless Networks:"))
os.system("networksetup -listpreferredwirelessnetworks en0")	
