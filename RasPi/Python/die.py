#!/usr/bin/env python
# push the button and roll the die
#
import RPi.GPIO as GPIO
import time
import random

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)
GPIO.setup(18, GPIO.OUT)

try:
    while True:			# loop waiting for the button push
	print 'Push the button'
	if GPIO.input(17):
		flash = random.randint(1,6)	# set a random number from 1 - 16
		print'Flashing ', flash 
		while GPIO.input(17):
			GPIO.output(18, False)
		while flash > 0:
			GPIO.output(18, True)
			time.sleep(.5)
			GPIO.output(18, False)
			time.sleep(.5)
			flash -= 1

        pass
except KeyboardInterrupt:
    GPIO.cleanup()
print 'End of program'

