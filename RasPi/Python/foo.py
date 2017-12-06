#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(18, GPIO.OUT)

def my_callback(channel):
    print('Detected button push')
    GPIO.output(18, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(18, GPIO.LOW)

GPIO.add_event_detect(17,GPIO.FALLING, callback=my_callback)

try:
    while True:
        pass
except KeyboardInterrupt:
    GPIO.cleanup()
print('End of program')
