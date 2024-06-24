def twoArrays(k, A, B,n):
    A.sort()
    B.sort(reverse=True)
    a=1
    for i in range(n):
        if A[i]+B[i]<k:
            a=0
    if a:
        return "YES"
    else:
        return "NO"
  

q = int(input())
for q_itr in range(q):
    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])
    A = list(map(int, input().rstrip().split()))
    B = list(map(int, input().rstrip().split()))
    result = twoArrays(k, A, B,n)
    print(result)

    
