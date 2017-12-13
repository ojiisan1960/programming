#!/usr/bin/env python
# Writen for common anode (+) RGB LED

from gpiozero import RGBLED
from time import sleep

led = RGBLED(14,15,18)

#led.red = 1 # full red
#sleep(1)
#led.red = 0.5  #
#sleep(1)

print("Red")
led.color = (0,1,1) # full red
sleep(1)
print("Green")
led.color = (1,0,1) # full green
sleep(1)
print("BLue")
led.color = (1,1,0) # full blue
sleep(1)

print("Magenta")
led.color = (0,1,0) # magenta
sleep(1)
print("Yellow")
led.color = (0,0,1) # yellow
sleep(1)
print("Cyan")
led.color = (1,0,0) # cyan
sleep(1)
print("White")
led.color = (0,0,0) # white
sleep(1)
print("Off")
led.color = (1,1,1) # off
sleep(1)

