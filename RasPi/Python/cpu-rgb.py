#!/usr/bin/env python

# Writen for common anode (+) RGB LED

from gpiozero import RGBLED
import psutil, time

myled = RGBLED(14,15,18)

while True:
    cpu = psutil.cpu_percent()
    print cpu
    r = (100 - cpu)/100.0
    print "r = %.3f" % r
    g = cpu / 100.0
    print "g = %3f" % g
    b = 1
    myled.color = ( r, g, b )
    time.sleep(1)
