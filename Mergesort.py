# revised Mergesort. updated 1/31/2017 based on feedback from users.

import sys
	
def merge_sort(A, first=0, last=len(A)-1):
	if first < last:
		middle = (first + last)//2
		merge_sort(A, first, middle)
		merge_sort(A, middle+1, last)
		merge(A, first, middle, last)
		
def merge(A, first, middle, last):
	L = A[first:middle+1]
	R = A[middle+1:last+1]
	L.append(sys.maxsize)
	R.append(sys.maxsize)
	i = j = 0
	
	for k in range (first, last+1):
		if L[i] <= R[j]:
			A[k] = L[i]
			i += 1
		else:
			A[k] = R[j]
			j += 1
			
A = [5,9,1,2,4,8,6,3,7]
print(A)
merge_sort(A)
print(A)