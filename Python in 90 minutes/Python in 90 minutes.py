# INTRODUCTION TO PYTHON
# ------------------------------------------------
# to print, put text inside single or double quotes, inside parentheses.
print('Hello World')

# VARIABLES 
# ------------------------------------------------
# variables are used for temporary storage of data that may change
# a single equals sign is the assignment operator
age = 26
first_name = 'Shivika'
gpa = 3.99

# here we can see three different types of data stored in variables: an integer, a string, and a float.
# You do not have to declare the data type stored in each variable. Python does that for you.
# You can see what type of data is in a variable using the type() function
print(type(age))
print(type(first_name))
print(type(gpa))

# variables are "dynamically typed" -- Python checks the type at runtime
age = 26.2
print(type(age))
print(age, type(age))

# variable naming tips: 
#	naming can have letters, numbers and underscore, but cannot start with a digit
#	some Python reserved words cannot be used
#	use descriptive variable names
#	Case Matters
#	constants in all caps: PI = 3.14159
# every Python variable is a pointer to the data stored somewhere in memory
# get memory location of a variable using id() function
print(id(age))

# to swap variable values:
x = 5
y = 10
x, y = y, x
print('x =', x, 'y =', y)

# BOOLEAN VALUES - True or False
# ------------------------------------------------
# These all evaluate to False: 0, 0.0, [], "", None
# These are all True: any non-zero number, any non-empty string, list or set
print(bool(1))    # True
print(bool('dog'))
print(bool(10.78))
print(bool(0 or 1))

print(bool(0))    # False
print(bool(''))
print(bool(0 and 1))

# MATH FUNCTIONS
# ------------------------------------------------
# built-in arithmetic functions are: add, subtract, multiply, divide, power, integer division, and modulus (AKA: mod or remainder)
#	+  Addition
# 	-  Subtraction
# 	*  Multiplication
# 	/  Division
# 	// Integer Division
# 	%  Modulus (division remainder)
# 	** Power
x = 5 + 7
print(x, type(x))
x = 5 - 7
print(x, type(x))
x = 7 / 4
print(x, type(x))
x = 7 // 4
print(x, type(x))
x = 7 % 4
print(x)
x = 4 ** 3
print(x)

# x += 5 is the same as saying x = x + 5
x = 2
x = x + 5
print(x)

x = 2
x += 5
print(x)

# Order of Operations
#	1. ( )
#	2. **
#	3. * / // %
#	4. + -
#	Example: 1 + 5 ** (3 // 2) - 6 % 4 => 4
x = 1 + 5 ** (3 // 2) - 6 % 4
print(x)

# CONSOLE INPUT
# ------------------------------------------------
# Get user input from the keyboard at the command prompt
name = input('What is your name? ')
print("Hello,", name)
age = eval(input('How old are you? '))
print('Age =', age, type(age))

# With what we know so far we can write a program to get user input and compute the area of a triangle.
base = eval(input('Enter the base: '))
height = eval(input('Enter the height: '))
area = base * height / 2
print ('Area = ', area)

# COMMENTS
# ------------------------------------------------
# Hash tag for single line comment
'''
Three sets of quotes 
for multi-line comments
'''
""" double quotes work too """

# IF-ELIF-ELSE STATEMENTS
# ------------------------------------------------
# requires a boolean expression 
x = 69
print(x > 50)
print(x == 50)
print(x != 50)

my_age = 19
print(my_age > 21)
if my_age >= 21:
    print("Old enough.")
else:
    print("Not old enough.")
    print("Maybe next year.")

score = 72
if score > 90:
    print('Grade: A')
elif score > 80:
    print('Grade: B')
elif score > 70:
    print('Grade: C')
elif score > 60:
    print('Grade: D')
else:
    print('Grade: F')
	
# can have multiple conditions in an if, using and/or
my_age = 19
grade = 'C'
if my_age > 18 and grade == 'A':
    print('I can go to the party!')

# nested if statements -- both conditions must be True
my_age = 19
grade = 'C'
if my_age > 18:
    if grade == 'A':
        print('I can go to the party!')

# if ternary
x = 10
y = 20
#  action/ if condition true/ else condfition false
z = x + y if x > y else y - x
print(z)
# result 10


# STRINGS
# ------------------------------------------------
# a string is a sequence of characters (ie. text)
s = 'Howdy'
print(s)
print(len(s))
print(s[3])
print(s[1:3])
t = ' dude! '
s += t
print(s + '|')
print(s.strip() + '|')
s = s.rstrip('! ')
print(s)

s = 'Howdy dude!'
print(s.lower())
print(s.upper()[:5])
print(s.title())
print(s.replace('Howdy', 'Greetings'))
print(s)
print(s.count('d'))
print(s.find('w'))
print('dud' in s)
print('X' not in s)
print(s.startswith('How'))
print(s.endswith('cat'))
print(s > 'Honk')
print(s.isalpha())
print(s[0:4].isalpha())
print(s.isnumeric())

print(s.split())
print('5,7,9'.split(','))
print('73.294'.split('.'))

print(s[0], '\t', s[1], '\t', s[2])
print(s[:s.find(' ')] + '\n' + s[s.find(' ')+1:])

# LOOPS -- FOR, WHILE
# ------------------------------------------------
# used to iterate through the items of a string or list
# indention is important. 
# every statement indented from for will be executed each iteration
s = 'Raj'
for letter in s:
    print(letter)
for letter in s:
    print(letter, end='')
print()

# if inside a for loop. indention is important.
for pig in s:
    if pig != 'a':
        print(pig, end='')
print()
for i in range(len(s)):
    print(i, end='')
print()
for i in range(len(s)):
    print(s[i])
for i in range(len(s)-1, -1, -1):
    print(s[i])
print(s[::-1])

# while loops are an alternative to for loops
# they check a boolean each iteration, and exit the loop when the bool is False
x = 2
while x < 5:
    print('ha')
    x += 1

# DATA STRUCTURES
# ------------------------------------------------
# These functions all work on String, List, and Tuple

# Indexing -- access any item in the sequence using its index
x = 'frog'
print (x[3])			# prints 'g'

x = ['pig', 'cow', 'horse']
print (x[1])			# prints 'cow'

# Slicing -- slice out substrings, sublists, subtuples using indexes
# [start : end+1 : step]
x = 'computer'
print(x[1:4])			# items 1 to 3, 'omp'
print(x[1:6:2])			# items 1, 3, 5, 'opt'
print(x[3:])			# items 3 to end, 'puter'
print(x[:5])			# items 0 to 4, 'compu'
print(x[-1])			# last item, 'r'
print(x[-3:])			# last 3 items, 'ter'
print(x[:-2])			# all except last 2 items, 'comput'

# Adding / Concatenating -- combine 2 sequences of the same type using +
x = 'horse' + 'shoe'
print (x)				# prints 'horseshoe'	

x = ['pig', 'cow'] + ['horse']
print (x)				# prints ['pig', 'cow', 'horse']

# Multiplying -- multiply a sequence using *
x = 'bug' * 3
print (x)				# prints 'bugbugbug'

x = [8, 5] * 3
print (x)				# prints [8, 5, 8, 5, 8, 5]

# Checking Membership -- test whether an item is in or not in a sequence
x = 'bug'
print ('u' in x)		# prints True

x = ['pig', 'cow', 'horse']
print ('cow' not in x)	# prints False

# Iterating	-- iterate through the items in a sequence
x = [7, 8, 3]
for item in x:
	print (item * 2)	# prints 14, 16, 6
	
x = [7, 8, 3]
for index, item in enumerate(x):
	print (index, item)	# prints 0 7, 1 8, 2 3

# Length -- count the number of items in a sequence
x = 'bug'
print (len(x))			# prints 3

x = ['pig', 'cow', 'horse']
print (len(x))			# prints 3

# Minimum -- find the minimum item in a sequence lexicographically
# alpha or numeric types, but cannot mix types
x = 'bug'
print (min(x))			# prints 'b' 

x = ['pig', 'cow', 'horse']
print (min(x))			# prints 'cow'

# Maximum -- find the maximum item in a sequence
# alpha or numeric types, but cannot mix types
x = 'bug'
print (max(x))			# prints 'u' 

x = ['pig', 'cow', 'horse']
print (max(x))			# prints 'pig'

# Sum -- find the sum of items in a sequence
# entire sequence must be numeric type
x = [5, 7, 'bug']
print (sum(x))			# error!

x = [2, 5, 8, 12]
print (sum(x))			# prints 27
print (sum(x[-2:])) 	# prints 20	

# Sorting -- returns a new list of items in sorted order
# sorted does not change the original list
x = 'bug'
print (sorted(x))		# prints ['b', 'g', 'u']

x = ['pig', 'cow', 'horse']
print (sorted(x))	    # prints ['cow', 'horse', 'pig']

# count (item)	
# Returns count of an item
x = 'hippo'
print (x.count('p'))	# prints 2

x = ['pig', 'cow', 'horse', 'cow']
print (x.count('cow'))	# prints 2

# index (item)	
# Returns the index of the first occurrence of an item
x = 'hippo'
print (x.index('p'))	# prints 2

x = ['pig', 'cow', 'horse', 'cow']
print (x.index('cow'))	# prints 1

# Unpacking	- unpack the n items of a sequence into n variables
x = ['pig', 'cow', 'horse']
a, b, c = x				# now a is 'pig', b is 'cow', c is 'horse'

# LISTS
# ------------------------------------------------
# constructors – creating a new list
x = list((1, 2, 3))		# note double parens
x = ['a', 25, 'dog', 8.43]
x = list(tuple1)

# list creation using comprehensions
x = [m for m in range(8)]
# resulting list: [0, 1, 2, 3, 4, 5, 6, 7]
x = [z**2 for z in range(10) if z>4]
# resulting list: [25, 36, 49, 64, 81]

# Delete -- delete a list or an item from a list
x = [5, 3, 8, 6]
del(x[1])				# [5, 8, 6]
del(x)					# deletes list x

# Append -- append an item to a list
x = [5, 3, 8, 6]
x.append(7)				# [5, 3, 8, 6, 7]

# Extend -- append an sequence to a list
x = [5, 3, 8, 6]
y = [12, 13]
x.extend(y)				# [5, 3, 8, 6, 7, 12, 13]

# Insert -- insert an item at given index.	x.insert(index, item)
x = [5, 3, 8, 6]
x.insert(1, 7)			# [5, 7, 3, 8, 6]
x.insert(1,['a','m'])	# [5, ['a', 'm'], 7, 3, 8, 6] 

# Pop -- pops last item off the list, and returns item
x = [5, 3, 8, 6]
x.pop()					# [5, 3, 8]. and returns the 6
print(x.pop())			# [5, 3]. and prints 8 

# Remove -- remove first instance of an item
x = [5, 3, 8, 6, 3]
x.remove(3)				# [5, 8, 6, 3]

# Reverse -- reverse the order of the list
x = [5, 3, 8, 6]
x.reverse()				# [6, 8, 3, 5]

# Sort -- sort the list in place
# sorted(x) returns a new sorted list without changing the original list x. 
# x.sort() puts the items of x in sorted order (sorts in place).
x = [5, 3, 8, 6]
x.sort()				# [3, 5, 6, 8]

# Clear	-- delete all items from the list
x = [5, 3, 8, 6]
x.clear()				# []

# TUPLES
# ------------------------------------------------
# constructors – creating a new tuple
x = ()					# no-item tuple
x = (1,2,3)
x = 1, 2, 3				# parenthesis are optional
x = 2, 					# single-item tuple
list1 = [5, 7, 7]
x = tuple(list1)		# tuple from list

# Tuples are Immutable, but member objects may be mutable
x = (1, 2, 3)
del(x[1])				# error!
x[1] = 8				# error!

x = ([1,2], 3)			# 2-item tuple: list and int
del(x[0][1])			# ([1], 3)

# SETS
# ------------------------------------------------
# constructors – creating a new set
x = {3,5,3,5}			# {5, 3}
x = set()				# empty set
list1 = [5, 7, 7]
x = set(list1)			# new set from list. strips duplicates, {5, 7}

# Set Comprehension
x = {3*x for x in range(10) if x>5} 
# resulting set: {18, 21, 24, 27} but in random order

# DICTIONARIES
# ------------------------------------------------
# constructors – creating a new dict
x = {'pork':25.3, 'beef':33.8, 'chicken':22.7}
x = dict([('pork', 25.3),('beef', 33.8),('chicken', 22.7)])
x = dict(pork=25.3, beef=33.8, chicken=22.7)

# Accessing keys and values in a dict
x.keys()				# returns list of keys in x
x.values()				# returns list of values in x
x.items()				# returns list of key-value tuple pairs in x

item in x.values()		# tests membership in x, returns boolean

# Iterating a Dict
for key in x:			# iterate keys
    print(key, x[key])	# print all key/value pairs

for k, v in x.items():	# iterate key/value pairs
    print(k, v)			# print all key/value pairs

# FUNCTIONS
# ------------------------------------------------
# use the def keyword to create a function
# give the function a name, followed by parentheses and a colon
# you can pass in 0 or more variables. here we pass in num.
# you can return 0 or more variables. here we return the cube of num
# indention is important.
def cuber(num):
	num_cubed = num * num * num
	return num_cubed
	
# to call the function, and pass in 5:
cuber(5)

# but if you want to assign the return value (125) to a variable,
x = 5
x_cubed = cuber(x)
print(x, x_cubed)

# you can set default values for parameters
def cuber(num = 2):
	num_cubed = num * num * num
	return num_cubed
	
print(cuber())		# uses the default 2
print(cuber(3))		# 3 overrides the default

# you can pass in multiple values, and return multiple values
# but order is important
def solve_triangle(base, height, side1, side2, side3):
	area = base * height / 2
	perimeter = side1 + side2 + side3
	return area, perimeter
	
area, perim = solve_triangle(3, 4, 5, 3, 4)	# b=3, h=4, s1=5, s2=3, s3=4
print('Area:', area, ' Perimeter:', perim)

# above are all called "positional arguments", and order matters
# you can also pass in "keyword arguments" when calling a function
a, p = solve_triangle(side1=5, side2=3, side3=4, height=4, base=3)
print(a, p)

# or use a combination of both, but positional arguments must come first
a, p = solve_triangle(3, 4, side3=4, side2=3, side1=5)
print(a, p)
	
# CLASSES & OBJECTS
# ------------------------------------------------
# Use classes to model real-world things. 
# Keep related data (variables) and actions (functions) in one block of code.
class Circle:
	# Circle constructor -- __init__ method creates a new Circle object
	def __init__(self, r = 1):
		self.radius = r
		
	def getPerimeter(self):
		return 2 * self.radius * 3.14
		
	def getArea(self):
		return self.radius ** 2 * 3.14
# all methods have the self parameter, which is Python's reference to the object that invoked the method

# this calls the __init__ method, which creates the new Circle
circle1 = Circle(3)		
# you can access the circle's attributes and methods using the dot operator
print("Radius =", circle1.radius)
print("Perimeter =", circle1.getPerimeter())	

# IMPORTS
# ------------------------------------------------
# Python has many many classes already written that you can use
# To access methods and data from another class you must import it
import math
print(math.pi)

import random
print(random.randint(1,5))

# shorter version, using as to abbreviate module name
import math as m
print(m.pi)

import random as rd
print(rd.randint(1,5))

# import just one or two functions or constants rather than a whole module
# easier for coding, but need to beware names don't conflict
from math import pi
print(pi)

from random import randint, shuffle
print(randint(1,5))
x = ['a', 'b', 'c']
shuffle(x)
print(x)

# can rename an imported function if you want
x = ['a', 'b', 'c']
from random import shuffle as sf
sf(x)
print(x)

# can also import whole module using *
from random import *
print(randint(1,5))

# FILE READ & WRITE
# ------------------------------------------------
filename = 'city_data.txt'

# this opens a file handle called fin, iterates the lines of the file, and prints each line
with open(filename) as fin:
    for line in fin:
        print(line)

# we can grab words from a line by using split, which turns each line into a list called row
with open(filename) as fin:
    fin.readline()
    for line in fin:
        row = line.split(',')
        print('Country:', row[1], ' City:', row[2])

# use the w parameter to write to an output file
with open('Cities.txt', 'w') as fout:
    with open(filename) as fin:
        fin.readline()
        for line in fin:
            row = line.split(',')
            fout.write(row[2] + '\n')









