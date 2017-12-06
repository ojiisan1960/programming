#!/usr/bin/env python

# using interrupt to detect a button press

import RPi.GPIO as GPIO     # import GPIO functions

GPIO.setmode(GPIO.BCM)      # set pins to GPIO numbering mode
GPIO.setup(17, GPIO.IN)

def buttonEvent(channel):
    print'Detected button press on pin %s', channel
    print 'state of port 17:', GPIO.input(17)
#GPIO.add_event_callback(17, buttonEvent)

GPIO.add_event_detect(17, GPIO.FALLING, callback=buttonEvent)

try:
    while True:
        pass
except KeyboardInterrupt:
    GPIO.cleanup()

print('End of program')

