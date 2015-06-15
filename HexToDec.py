# Python Hexadecimal to Decimal Conversion

def __getDecDigit(digit):
	digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
		'A', 'B', 'C', 'D', 'E', 'F']
	for x in range(len(digits)):
		if digit == digits[x]:
			return x
			
def hexToDec(hexNum):
	decNum = 0
	power = 0
	for digit in range(len(hexNum), 0, -1):
		decNum = decNum + 16 ** power * __getDecDigit(hexNum[digit-1])
		power += 1
	print(str(decNum))
	
hexToDec("A5")