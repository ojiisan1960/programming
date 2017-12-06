#!/usr/bin/env python

import sys			#load the system module

marker = '::::::'

for name in sys.argv[1:]:	# for all command arguments
    input = open(name, 'r')	# open the next imput file
    print marker + name		# write a separator line
    print input.read(),		# adn write the file's contents
