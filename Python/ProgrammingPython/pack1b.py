#!/usr/bin/env python2
#

from sys import argv, stdout

marker = '::::::'

for name in argv[1:]:
    input = open(name, 'r')
    stdout.write(marker + name + '\n')
    stdout.write(input.read())
