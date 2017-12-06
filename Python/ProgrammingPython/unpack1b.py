#!/usr/bin/env python2

from sys import *

marker = '::::::'

output = stdout

for line in stdin.readlines():
    if line[:6] != marker:
	output.write(line)
    else:
	output = open(line[6:-1], 'w')
