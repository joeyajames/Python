def countsort(a):
    """ count sort implementation
    >>> countsort([6,4,8,2,1,9,10])
    [1,2,4,6,8,9,10]
    """
    #to figure out the range of numbers in the array
    maxval=max(a)
    minval=min(a)
    numberOfElements=maxval-minval+1
    countArray=[0]*numberOfElements
    resultArray=[0]*len(a)
    
    #finding count of each element in the array and storing them in count array
    for item in a:
        countArray[item-minval]+=1
    for item in range(1,len(countArray)):
        countArray[item]+=countArray[item-1]
        
    #storing in result array
    for item in range(len(a)-1,-1,-1):
        resultArray[countArray[a[item]-minval]-1]=a[item]
        countArray[a[item]-minval]-=1
    #sorted input array
    for item in range(len(a)):
        a[item]=resultArray[item]
    output=""
    for i in range(len(a)):
    	output+=str(a[i])+","
    print(output.split(","))
    return a
    
def main():
    inputArray=[6,4,8,2,1,9,10]
    print(countsort(inputArray))
    
if __name__ == "__main__":
    main()
