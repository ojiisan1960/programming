#!/usr/bin/env python

from PenguinPen import *

myPen = PenguinPen()    # call the class as a function to make an instance
print 'There are ' + `myPen.population()` + ' pigs '
print 'Add one...'
myPen.add()             # default, add one penguin
print 'Now there is ' + `myPen.population()` + ' pig'  # will print 1
print 'Lets add another...'
myPen.add()
print 'Now there are ' + `myPen.population()` + ' pigs'

