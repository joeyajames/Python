# Python Flatten Nested Lists
# (c) Joe James 2023

# list comprehension method
def flatten1 (myList):
	return [i for j in myList for i in j]

# recursive method
def flatten2 (myList):
	flatList = []
	for item in myList:
		if isinstance(item, list):
			flatList.extend(flatten2(item))
		else:
			flatList.append(item)
	return flatList

list1 = [[0], [1, 2], [3, [4, 5]], [6], [7]]
list2 = [0, [1, 2], [3, [4, 5]], [6], 7]

print("flatten1(list1): ", flatten1(list1)) # works, but only flattens 1 layer of sublists
# print(flatten1(list2)) # error - can't work with list of ints and sublists of ints

print("flatten2(list1): ", flatten2(list1))
print("flatten2(list2): ", flatten2(list2))


