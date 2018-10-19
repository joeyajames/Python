class Shape:
	def __init__(self, color=None):
		self.color = color
		
	def get_color(self):
		return self.color
		
	def __str__(self):
		return self.get_color() + ' Shape'
