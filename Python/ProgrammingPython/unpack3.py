#!/usr/bin/env python2

from sys import *
from textpack1 import marker
mlen = len(marker)

def unpack_file(name):
    try:    
	input = open(name, 'r')
	unpack_stream(input)
    except:
	import sys
	print 'unpack error!'; sys.exc_type, sys.exc_value

def unpack_stream(input, output=stdout):
    while 1:
	line = input.readline()
	if not line:
	    break
	elif line[:mlen] != marker:
	    print 'creating:', name
	    output.write(line)
	else: 
	    name = line[mlen:-1]
	    print 'creating:' , name
	    output = open(name, 'w')
	
if __name__ == '__main__':
    if len(argv) == 2:
	unpack_file(argv[1])
    else:
	print 'usage: unpack filename'; exit(1)
