#!/usr/bin/env python
# A simple example to blink and led with pwm

import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)    # use board pin numbers
GPIO.setup(7, GPIO.OUT)    # pin 7 is output

p = GPIO.PWM(7, 10)       # pin 7, freq in Hz
p.start(50)                  # duty cycle %
raw_input('Press return to stop:')
p.stop()
GPIO.cleanup()
