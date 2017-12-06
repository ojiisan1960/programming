# MagPi Issue 17 and 18
# Physical Computing

import RPi.GPIO as GPIO     # import GPIO functions
import time                 # import time functions

# initialize ports
GPIO.setmode(GPIO.BCM)      # set pins to gpio numbering mode
GPIO.setup(17, GPIO.IN)
GPIO.setup(18, GPIO.OUT)

try:
    print("Press the button")
    while True:
        input_value = GPIO.input(17)
        if input_value == False:
            print("Button pressed - led on")
            for x in range(0,3):
                GPIO.output(18, True)
                time.sleep(1)
                GPIO.output(18, False)
                time.sleep(1)
            while input_value == False:
                input_value = GPIO.input(17)
except KeyboardInterrupt:    # Ctrl+C
    GPIO.cleanup()          # program end and GPIO ports cleaned
finally:
    GPIO.cleanup()          # program end and GPIO ports cleaned
