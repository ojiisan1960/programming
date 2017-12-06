#!/usr/bin/env python
#
# A simple password generator

#
import random
import string

# make a list of characters minus the last 5 (tabs etc...)
list = string.printable[:-5]

# Select 8 characters
for i in range(8):
	print list[random.randrange(len(list))],

