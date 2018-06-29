#---------------------------------------
# Insertion Sort
#---------------------------------------
# not optimized, equiv to while version below, but uses for loop
def insertion_sort1(A):
	for i in range(1, len(A)):
		for j in range(i-1, -1, -1):
			if A[j] > A[j+1]:
				A[j], A[j+1] = A[j+1], A[j]
			else:
				break

# not optimized, equiv to break version, but uses while loop		
def insertion_sort2(A):
	for i in range(1, len(A)):
		j = i-1
		while A[j] > A[j+1] and j >= 0:
			A[j], A[j+1] = A[j+1], A[j]
			j -= 1

# optimized - shifts instead of swapping		
def insertion_sort3(A):
	for i in range(1, len(A)):
		curNum = A[i]
		k = 0
		for j in range(i-1, -2, -1):
			k = j
			if A[j] > curNum:
				A[j+1] = A[j]
			else:
				break
		A[k+1] = curNum
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
insertion_sort1(A)
print(A)