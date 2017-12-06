#!/usr/bin/env python2
# reads one line at a time 

import sys 

marker = '::::::'

while 1:
    line = sys.stdin.readline()		#read the next line
    if not line:			# end of file
	break				# exit
    elif line[:6] != marker
	print line			# print line
    else:
	sys.stdout = open(line[6:-1], 'w')  # new output file
