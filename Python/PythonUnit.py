#!/usr/bin/env python

import sys                      # python system modules 

from testCase import TestCase   # note file name, class name
from PenguinPen import PenguinPen

class testPenguinPen(TestCase):
	def __init__(self, name):
		self.name = name

	def setUp(self):
		"""Create a new Penguin Pen"""
		myPen = PenguinPen()

	def tearDown(self):
		"""Delete the Penguin Pen"""
		myPen = None				
	def testNewPen(self):
		"""A new pen should be empty"""
		should(myPen.population == 0)
	def testAdd(self):
		"""Adding without saying how many will only add one"""
		should(myPen.add() == 1)
	def testRemove(self):
		"""Removing without saying how many will only remove one"""
		should(myPen.remove() == -1)

if __name__ == '__main__':
	stuff = testPenguinPen('unit test')
	stuff.setUp
	stuff.testNewPen
	stuff.tearDown
	stuff.setUp
	stuff.testAdd
	stuff.tearDown
	stuff.setUp
	stuff.testRemove
	stuff.tearDown
	print "No news is good news"

