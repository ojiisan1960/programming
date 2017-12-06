#!/usr/bin/env python

import RPi.GPIO as GPIO     # import GPIO functions
import time                 # import time functions

def main():

# initialize ports
    GPIO.setmode(GPIO.BCM)      # set pins to gpio numbering mode
    GPIO.setup(18, GPIO.OUT)

    for x in range(0,3):
        GPIO.output(18, True)
        time.sleep(0.5)
        GPIO.output(18, False)
        time.sleep(0.5)

    GPIO.cleanup()          # program end and GPIO ports cleaned


if __name__=='__main__':
    main()