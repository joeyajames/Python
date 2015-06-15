# prime number calculator

max = int(input("Find primes up to what number? : "))
primeList = []

for x in range(2, max + 1):
	isPrime = True
	index = 0
	root = int(x ** 0.5) + 1
	
	while index < len(primeList) and primeList[index] <= root:
		if x % primeList[index] == 0:
			isPrime = False
			break
		index += 1
			
	if isPrime:
		primeList.append(x)
		
print(primeList)
		