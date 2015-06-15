# Python: Binary to Decimal Conversion
# binToDec and decToBin functions are rendered obsolete by the universal convert function

def binToDec(binNum):
	decNum = 0
	power = 0
	while binNum > 0:
		decNum += 2 ** power * (binNum % 10)
		binNum //= 10
		power += 1
	return decNum
	
def decToBin(decNum):
	binNum = 0
	power = 0
	while decNum > 0:
		binNum += 10 ** power * (decNum % 2)
		decNum //= 2
		power += 1
	return binNum
	
def convert(fromNum, fromBase, toBase):
	toNum = 0
	power = 0
	while fromNum > 0:
		toNum += fromBase ** power * (fromNum % toBase)
		fromNum //= toBase
		power += 1
	return toNum

# print (str(binToDec(101011)))
# print (str(decToBin(128)))
print (str(convert(127, 10, 8)))	# converts 127 in  base 10 to base 8
print (str(convert(101001, 2, 2)))	