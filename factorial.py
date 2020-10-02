def get_recursive_factorial(n):
	if n < 0:
		return -1
	elif n < 2:
		return 1
	else:
		return n * get_recursive_factorial(n-1)
		
def get_iterative_factorial(n):
	if n < 0:
		return -1
	else:
		fact = 1
		for i in range(1, n+1):
			fact *= i
		return fact
print("input should be an integer")		
print(get_recursive_factorial(6))
print(get_iterative_factorial(6))
