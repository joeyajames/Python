# Python: Binary to Decimal Conversion
# binToDec and decToBin functions are rendered obsolete by the universal convert function

def binToDec(binNum): #function created to convert binary to decimal with parametere binNum
	decNum = 0
	power = 0
	while binNum > 0: #loop will run till binNum is greater than 0
		decNum += 2 ** power * (binNum % 10) 
		binNum //= 10 # reducing binNum everytime by 1 digit	
		power += 1 # increasing power by 1 each loop
	return decNum
	
def decToBin(decNum): #function created to convert decimal to binary with parametere decNum
	binNum = 0
	power = 0
	while decNum > 0:#loop will run till decNum is greater than 0
		binNum += 10 ** power * (decNum % 2)
		decNum //= 2 # reducing decNum everytime by 1 digit
		power += 1 # increasing power by 1 each loop
	return binNum
	
def convert(fromNum, fromBase, toBase): #function for converting from any base to any other base
	# Step 1: Convert fromNum (represented as an integer using digits of fromBase) to a standard base 10 integer
	val = 0
	power = 0
	temp = fromNum
	while temp > 0:
		digit = temp % 10
		if digit >= fromBase:
			raise ValueError(f"Digit {digit} is invalid for base {fromBase}")
		val += digit * (fromBase ** power)
		temp //= 10
		power += 1

	# Step 2: Convert standard base 10 integer to the target base (represented using base 10 digits)
	toNum = 0
	power = 0
	while val > 0:
		digit = val % toBase
		toNum += digit * (10 ** power)
		val //= toBase
		power += 1
	return toNum

print("101011 in base 2 to base 10: " + str(binToDec(101011)))
print("128 in base 10 to base 2: " + str(decToBin(128)))
print("127 in base 10 to base 8: " + str(convert(127, 10, 8)))	# converts 127 in base 10 to base 8
print("177 in base 8 to base 2: " + str(convert(177, 8, 2)))	# converts 177 in base 8 to base 2

