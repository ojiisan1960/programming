#!/usr/bin/env python

from Tkinter import *
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)

pwmRed = GPIO.PWM(14, 500)
pwmRed.start(100)
pwmGreen = GPIO.PWM(15, 500)
pwmGreen.start(100)
pwmBlue = GPIO.PWM(18, 500)
pwmBlue.start(100)

class App:
    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        Label(frame, text='Red').grid(row=0, column=0)
        Label(frame, text='Green').grid(row=1, column=0)
        Label(frame, text='Blue').grid(row=2, column=0)

        scaleRed = Scale(frame, from_=0, to=100,
                orient=HORIZONTAL, command=self.updateRed)
        scaleRed.grid(row=0, column=1)

        scaleGreen = Scale(frame, from_=0, to=100,
                orient=HORIZONTAL, command=self.updateGreen)
        scaleGreen.grid(row=1, column=1)

        scaleBlue = Scale(frame, from_=0, to=100,
                orient=HORIZONTAL, command=self.updateBlue)
        scaleBlue.grid(row=2, column=1)

    def updateRed(self, duty):
        pwmRed.ChangeDutyCycle(float(duty))

    def updateGreen(self, duty):
        pwmGreen.ChangeDutyCycle(float(duty))

    def updateBlue(self, duty):
        pwmBlue.ChangeDutyCycle(float(duty))

root = Tk()
root.wm_title('RGB LED Control')
app = App(root)
root.geometry("200x150+0+0")

try:
    root.mainloop()

finally:
    print("Cleaning up GPIO...")
    GPIO.cleanup()

