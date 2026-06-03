# Python Hexadecimal to Decimal Conversion

def __getDecDigit(digit):
	digits = {
		'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 
		'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15
	}
	return digits.get(digit.upper())
			
def hexToDec(hexNum):
	decNum = 0
	power = 0
	for digit in range(len(hexNum), 0, -1):
		val = __getDecDigit(hexNum[digit-1])
		if val is None:
			raise ValueError(f"Invalid hexadecimal digit: {hexNum[digit-1]}")
		decNum = decNum + 16 ** power * val
		power += 1
	return decNum
	
print("A5 in decimal: " + str(hexToDec("A5")))
print("3c in decimal: " + str(hexToDec("3c")))