class Node(object):

	def __init__ (self, d, n = None):
		self.data = d
		self.next_node = n

	def get_next (self):
		return self.next_node

	def set_next (self, n):
		self.next_node = n
		
	def get_data (self):
		return self.data

	def set_data (self, d):
		self.data = d
		
	def __str__(self):
		return "Node value: " + str(self.data)

class CircularLinkedList (object):

	def __init__ (self, r = None):
		self.root = r
		self.size = 0

	def get_size (self):
		return self.size

	def add (self, d):
		if self.get_size() == 0:
			self.root = Node(d)
			self.root.set_next(self.root)
		else:
			new_node = Node (d, self.root.get_next())
			self.root.set_next(new_node)
		self.size += 1

	def remove (self, d):
		this_node = self.root
		prev_node = None

		while True:
			if this_node.get_data() == d:	# found
				if prev_node is not None:
					prev_node.set_next(this_node.get_next())
				else:
					while this_node.get_next() != self.root:
						this_node = this_node.get_next()
					this_node.set_next(self.root.get_next())
					self.root = self.root.get_next()
				self.size -= 1
				return True     # data removed
			elif this_node.get_next() == self.root:
				return False	# data not found
			prev_node = this_node
			this_node = this_node.get_next()

	def find (self, d):
		this_node = self.root
		while True:
			if this_node.get_data() == d:
				return d
			elif this_node.get_next() == self.root:
				return False
			this_node = this_node.get_next()
		
	def print_list (self):
		print ("Print List..........")
		if self.root is None:
			return
		this_node = self.root
		print (this_node)
		while this_node.get_next() != self.root:
			this_node = this_node.get_next()
			print (this_node)

def main():
	myList = CircularLinkedList()
	myList.add(5)
	myList.add(7)
	myList.add(3)
	myList.add(8)
	myList.add(9)
	print("Find 8", myList.find(8))
	print("Find 12", myList.find(12))

	cur = myList.root
	print (cur)
	for i in range(8):
		cur = cur.get_next();
		print (cur)

	print("size="+str(myList.get_size()))
	myList.print_list()
	myList.remove(8)
	print("size="+str(myList.get_size()))
	print("Remove 15", myList.remove(15))
	print("size="+str(myList.get_size()))
	myList.remove(5)	# delete root node
	myList.print_list()
	
main()












