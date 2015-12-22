# computes Greatest Common Factor GCF / Greatest Common Divisor GCD of two numbers
# useful for reducing fractions

def gcf (num1, num2):
	if num1 > num2:
		num1, num2 = num2, num1

	for x in range (num1, 0, -1):
		if num1 % x == 0 and num2 % x == 0:
			return x
			
num1 = 18
num2 = 204
print (str(gcf(num1, num2)))
