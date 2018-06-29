#---------------------------------------
# Quick Sort
#---------------------------------------
def quick_sort(A):
	quick_sort2(A, 0, len(A)-1)
	
def quick_sort2(A, low, hi):
	if hi-low < threshold and low < hi:
		quick_selection(A, low, hi)
	elif low < hi:
		p = partition(A, low, hi)
		quick_sort2(A, low, p - 1)
		quick_sort2(A, p + 1, hi)
	
def get_pivot(A, low, hi):
	mid = (hi + low) // 2
	s = sorted([A[low], A[mid], A[hi]])
	if s[1] == A[low]:
		return low
	elif s[1] == A[mid]:
		return mid
	return hi
	
def partition(A, low, hi):
	pivotIndex = get_pivot(A, low, hi)
	pivotValue = A[pivotIndex]
	A[pivotIndex], A[low] = A[low], A[pivotIndex]
	border = low

	for i in range(low, hi+1):
		if A[i] < pivotValue:
			border += 1
			A[i], A[border] = A[border], A[i]
	A[low], A[border] = A[border], A[low]

	return (border)
	
def quick_selection(x, first, last):
	for i in range (first, last):
		minIndex = i
		for j in range (i+1, last+1):
			if x[j] < x[minIndex]:
				minIndex = j
		if minIndex != i:
			x[i], x[minIndex] = x[minIndex], x[i]
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
quick_sort(A)
print(A)