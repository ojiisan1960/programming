#!/usr/bin/env python

"""
A nifty command line utility. What to do, on a Unix command line, if you
have files named file001 through file050, and you have to move the odd ones
to the directory Spam?

for i in `range 1 51 2 file%03d`; do mv $i Spam; done

This tiny thing makes range available for the command line, together with
a formatting string because I found that that was useful.
"""

import sys
import string

if len(sys.argv) < 3:
    print "Usage: range <from> <to> [<step>] [<format>]"

a = int(sys.argv[1])
b = int(sys.argv[2])
step = 1
format = "%d"

if len(sys.argv) >= 4:
    try:
	step = int(sys.argv[3])
    except:
	format = sys.argv[3]
if len(sys.argv) >= 5:
    format = sys.argv[4]

for l in range(a,b,step):
    print format % l

