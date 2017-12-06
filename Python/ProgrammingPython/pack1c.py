#!/usr/bin/env python2
#

from sys import argv

marker = '::::::'

output = open('packed.out', 'w')

for name in argv[1:]:
    input = open(name, 'r')
    output.write(marker + name + '\n')
    output.write(input.read())
