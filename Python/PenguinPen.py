
class PenguinPen:
	def __init__(self):
		self.penguinCount = 0

	def add (self, number = 1):
		""" Add one or more penguins to the pen
		The default number of penguins to add is 1 """
		self.penguinCount = self.penguinCount + number

	def remove (self, number = 1):
		""" Remove one or more  penguins from the pen """
		self.penguinCount = self.penguinCount - number

	def population (self):
		""" How many penguins in the pen? """
		return self.penguinCount
