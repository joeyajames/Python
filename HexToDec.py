def getDecDigit(digit):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    return digits.index(digit)

def hexToDec(hexNum):
    decNum = 0
    power = 0
    for digit in hexNum:
        decNum = decNum + 16 ** power * getDecDigit(digit)
        power += 1
    return decNum

print(hexToDec("A5")) # should print 165
