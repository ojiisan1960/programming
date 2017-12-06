#!/usr/bin/env python2.1

"""
mbeep - a small app to remind you to take a break, do some yoga exercises,
etc.

    When it's running, 'enter' turns on cymbaline cy_pause mode - it sends pause
    command to cymbaline when stretch and work periods are over.

 Copyright (C) 2001 Andrei Kulakov <ak@silmarill.org>
 Licence: GPL [see http://www.gnu.org/copyleft/gpl.html]
"""

import time, sys, os
from threading import *

# time in minutes
work_time = 15  
stretch_time = 4

pause_between_beeps = 0.5 # in seconds
# pause cymbaline?
#cy_pause = 1

#cycmd = os.path.expanduser("~/.cymbaline/cmd")

def beep(times):
    """Beep computer speaker given number of times."""
    for i in range(times):
        print "\a\r",
        sys.stdout.flush()
        time.sleep(pause_between_beeps)

def process(seconds):
    """Take in seconds; return min:sec."""
    mins = seconds / 60
    secs = seconds % 60
    return "%d:%02d" % (mins, secs)

def sleep(min):
    """Sleep x minutes, printing elapsed time."""
    for i in range(min*60):
        print "\r", process(i),
        sys.stdout.flush()
        time.sleep(1)

def main():
    while 1:
        print "\rwork:"
#        if cy_pause and os.path.exists(cycmd):
#            os.system("echo 'z' > %s" % cycmd)
        beep(2)
        sleep(work_time)
        print "\rstretch:"
        if cy_pause and os.path.exists(cycmd):
            os.system("echo 'z' > %s" % cycmd)
        beep(3)
        os.system("xlock")
        sleep(stretch_time)

print '\n'*24
th = Thread(None, main)
th.start()

try:
    while 1:
        ans = raw_input()
        if not ans:
            if cy_pause:
                cy_pause = 0
                print "cymbaline pause off"
            else:
                cy_pause = 1
                print "cymbaline pause on"
except KeyboardInterrupt:
    sys.exit()
