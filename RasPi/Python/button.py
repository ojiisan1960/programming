# MagPi Issue 17 and 18
# Physical Computing

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

while True:
    input_value = GPIO.input(17)
    if input_value == False:
        print("Who pressed my button?")
        while input_value == False:
            input_value = GPIO.input(17)
	
