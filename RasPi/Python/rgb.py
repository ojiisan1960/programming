#!/usr/bin/env python

import RPi.GPIO as GPIO     # import GPIO functions
import time                 # import time functions

def main():

# initialize ports
    GPIO.setmode(GPIO.BCM)      # set pins to gpio numbering mode
    GPIO.setup(14, GPIO.OUT)    # Red
    GPIO.setup(15, GPIO.OUT)    # Green
    GPIO.setup(18, GPIO.OUT)    # Blue

    for x in range(0,3):
        GPIO.output(14, False)
        GPIO.output(15, True)
        GPIO.output(18, True)
        time.sleep(0.5)
        GPIO.output(14, True)
        GPIO.output(15, True)
        GPIO.output(18, True)
        time.sleep(0.5)

    GPIO.cleanup()          # program end and GPIO ports cleaned


if __name__=='__main__':
    main()
