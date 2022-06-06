from abc import ABC, abstractmethod

class Shape(ABC):

	@abstractmethod
	def printarea(self):
		return 0
	
class Rectangle(Shape):
	type = "Rectangle"
	sides = 4

	def __init__(self):
		self.breadth = 6
		self.length = 7
	
	def printarea(self):
		return self.breadth * self.length
	
	def __repr__(self):
	    return f"The area of the traingle is {self.breadth}*{self.length}"
rect1 = Rectangle()
print(rect1.printarea())

