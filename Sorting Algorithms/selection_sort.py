#---------------------------------------
# Selection Sort
#---------------------------------------			
def selection_sort(A):
	for i in range (0, len(A) - 1):
		minIndex = i
		for j in range (i+1, len(A)):
			if A[j] < A[minIndex]:
				minIndex = j
		if minIndex != i:
			A[i], A[minIndex] = A[minIndex], A[i]
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
selection_sort(A)
print(A)