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