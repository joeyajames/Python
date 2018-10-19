# from shape_class import *

class Shape:
	def __init__(self, color=None):
		self.color = color
		
	def get_color(self):
		return self.color
		
	def __str__(self):
		return self.get_color() + ' Shape'
		
class Rectangle(Shape):
	def __init__(self, color, length, width):
		super().__init__(color)
		self.length = length
		self.width = width
		
	def get_area(self):
		return self.length * self.width
		
	def get_perimeter(self):
		return 2 * (self.length + self.width)
		
	def __str__(self):
		return self.get_color() + ' ' + str(self.length) + 'x' + str(self.width) + ' ' + type(self).__name__

from math import pi		
class Circle(Shape):
	def __init__(self, color, radius):
		super().__init__(color)
		self.radius = radius
		
	def get_area(self):
		return pi * self.radius ** 2
		
	def get_perimeter(self):
		return 2 * pi * self.radius
		
def print_shape_data(self):
	print('Shape:    ', type(self).__name__)
	print('Color:    ', self.get_color())
	print('Area:     ', self.get_area())
	print('Perimeter:', self.get_perimeter())
	
shape = Shape('red')
print('shape is', shape.get_color())

rect = Rectangle('blue', 6, 4)
print('rect is', rect.get_color(), ' with area:', rect.get_area(), ' and perimeter:', rect.get_perimeter())

circ = Circle('green', 5)
print('circ is', circ.get_color(), ' with area:', circ.get_area(), ' and perimeter:', circ.get_perimeter())

print('rect is a', type(rect).__name__)
print('circ is a', type(circ).__name__, '\n')

	
my_new_shape = Rectangle('yellow', 17, 9)
print_shape_data(my_new_shape)

print(type(my_new_shape))
print(my_new_shape)







