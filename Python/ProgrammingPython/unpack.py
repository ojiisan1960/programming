#!/usr/bin/env python
#
import sys

marker = '::::::'

for line in sys.stdin.readlines():	    #for all input lines
    if line[:6] != marker:  
	print line,			    #write real line
    else:
	sys.stdout = open(line[6:-1], 'w')  # or make new output file
