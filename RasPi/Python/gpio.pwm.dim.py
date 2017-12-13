#!/usr/bin/env python
# A simple example to dim an led with pwm

import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)    # use board pin numbers
GPIO.setup(7, GPIO.OUT)    # pin 7 is output

p = GPIO.PWM(7, 50)       # pin 7,  50 Hz
p.start(0)                  # duty cycle
try:
    while 1:
        for dc in range(0, 101, 5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
        for dc in range(100, -1, -5):
            p.ChangeDutyCycle(dc)
            time.sleep(0.1)
except KeyboardInterrupt:
    pass
p.stop()
GPIO.cleanup()
