# something more about try except
# basic syntax
'''
try:
	code1

except:
	some code that will execute if code 1 fails or raise some error

else:
	this code is executed only if try was succesful i.e no error in code1

finally:
	
	this code will execute in every situation if try fails or not
'''

filename = 'exception_data.txt'
# Outer try block catches file name or file doesn't exist errors.
try:
	with open(filename) as fin:
		for line in fin:
			# print(line)
			items = line.split(',')
			total = 0
			
			# Inner try bock catches integer conversion errors.
			try:
				for item in items:
					num = int(item)
					total += num
				print('Total = ' + str(total))
			except:
				print('Error converting to integer. ', items)
except:
	print('Error opening file. ' + filename)
	
finally:
	print('This is our optional finally block. Code here will execute no matter what.')
	
	
# Second example: name Error type in except block; call function from try block.
def this_fails():
	x = 1/0
try:
	this_fails()
except ZeroDivisionError as err:
	print('Handling run-time error:', err)
	

def divide_me(n):
	x = 1/n

i = int(input('enter a number '))
try:
	divide_me(i)

except Exception as e:
	print(e)  # this will print the error msg but don't kill the execution of program

else:
	print('Your Code Run Successfully') # this will execute if divide_me(i) run sucessfully without an error

finally:
	print('thanks') # this will execute in every condition
	
