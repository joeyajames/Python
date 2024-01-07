# Python: del vs pop vs remove from a list 
# (c) Joe James 2023

def get_dogs():
	return ['Fido', 'Rover', 'Spot', 'Duke', 'Chip', 'Spot']

dogs = get_dogs()
print(dogs)

# Use pop() to remove last item or an item by index and get the returned value. 
print('1. pop last item from list:')
myDog = dogs.pop() 
print(myDog, dogs)

dogs = get_dogs()
print('2. pop item with index 1:')
myDog = dogs.pop(1) 
print(myDog, dogs)

# Use remove() to delete an item by value. (raises ValueError if value not found)
dogs = get_dogs()
print('3. remove first Spot from list:')
dogs.remove('Spot')
print(dogs)

# Use del to remove an item or range of items by index. Or delete entire list.
dogs = get_dogs()
print('4. del item with index 3:')
del(dogs[3])
print(dogs)

dogs = get_dogs()
print('5. del items [1:3] from list:')
del(dogs[1:3])
print(dogs)

dogs = get_dogs()
print('6. del entire list:')
del(dogs)
print(dogs)








