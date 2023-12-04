#---------------------------------------
# Quick Sort
#---------------------------------------
def quick_sort(ArrayToSort):
	quick_sort2(ArrayToSort, 0, len(ArrayToSort)-1)
	
def quick_sort2(ArrayToSort, low, hi, threshold = 10):
	if hi-low < threshold and low < hi:
		quick_selection(ArrayToSort, low, hi)
	elif low < hi:
		p = partition(ArrayToSort, low, hi)
		quick_sort2(ArrayToSort, low, p - 1)
		quick_sort2(ArrayToSort, p + 1, hi)
	
def get_pivot(ArrayToSort, low, hi):
	mid = (hi + low) // 2
	s = sorted([ArrayToSort[low], ArrayToSort[mid], ArrayToSort[hi]])
	if s[1] == ArrayToSort[low]:
		return low
	elif s[1] == ArrayToSort[mid]:
		return mid
	return hi
	
def partition(ArrayToSort, low, hi):
	pivotIndex = get_pivot(ArrayToSort, low, hi)
	pivotValue = ArrayToSort[pivotIndex]
	ArrayToSort[pivotIndex], ArrayToSort[low] = ArrayToSort[low], ArrayToSort[pivotIndex]
	border = low

	for i in range(low, hi+1):
		if ArrayToSort[i] < pivotValue:
			border += 1
			ArrayToSort[i], ArrayToSort[border] = ArrayToSort[border], ArrayToSort[i]
	ArrayToSort[low], ArrayToSort[border] = ArrayToSort[border], ArrayToSort[low]

	return (border)
	
def quick_selection(x, first, last):
	for i in range (first, last):
		minIndex = i
		for j in range (i+1, last+1):
			if x[j] < x[minIndex]:
				minIndex = j
		if minIndex != i:
			x[i], x[minIndex] = x[minIndex], x[i]
			
ArrayToSort = [5,9,1,2,4,8,6,3,7]
print(ArrayToSort)
quick_sort(ArrayToSort)
print(ArrayToSort)