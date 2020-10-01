# prime number calculator: find all primes up to n


def SieveOfEratosthenes(n):
    primes = []
    # Create a boolean array "prime[0..n]" and initialize
    #  all entries it as true. A value in prime[i] will
    # finally be false if i is Not a prime, else true.
    prime = [True for i in range(n+1)]
    p = 2
    while (p * p <= n):

        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):

            # Update all multiples of p
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1

    # Print all prime numbers
    for p in range(2, n+1):
        if prime[p]:
            primes.append(p)
    return primes


max = int(input("Find primes up to what number? : "))
# I used a shortcut method to find the prime numbers calles SieveOfEratosthenes
# to find more search in internet about SieveOfEratosthenes
# it is more faster than the below while loop.


primeList = SieveOfEratosthenes(max)



# #for loop for checking each number
# for x in range(2, max + 1):
# 	isPrime = True
# 	index = 0
# 	root = int(x ** 0.5) + 1

# 	while index < len(primeList) and primeList[index] <= root:
# 		if x % primeList[index] == 0:
# 			isPrime = False
# 			break
# 		index += 1

# 	if isPrime:
# 		primeList.append(x)



print(primeList)


# -------------------------------------------------------------
# prime number calculator: find the first n primes

count = int(input("Find how many primes?: "))
primeList = []
x = 2

while len(primeList) < count:
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

    x += 1

print(primeList)
