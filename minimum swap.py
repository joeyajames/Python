def minimumSwaps(arr):
    n=len(arr)
    s=0
    for i in range(0,n):
         while arr[i]!=i+1:
            temp=arr[i]-1
            arr[i],arr[temp]=arr[temp],arr[i]
            s=s+1
    return s
           


n = int(input())
arr = list(map(int, input().rstrip().split(" ")))

res = minimumSwaps(arr)
print(res)
