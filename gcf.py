# computes Greatest Common Factor GCF / Greatest Common Divisor GCD of two numbers
# useful for reducing fractions

def gcf(num1, num2):
	while num2:
		num1, num2 = num2, num1 % num2
	return num1
			
num1 = 18
num2 = 204
print (str(gcf(num1, num2)))
