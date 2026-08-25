t=int(input())

for _ in range(t):
    
    n=int(input())
    arr=list(map(int,input().split()))
    
    
    arr.sort()
    
    ans=True
    
    for i in range(1,n):
        if arr[i]==arr[i-1]:
            ans=False
            break
    
    if ans==False:
        print(-1)
        continue
    
    xorr=0
    
    for i in range(n):
        xorr=xorr^arr[i]
        
    
    if xorr==0 and arr[0]==0:
        print(arr[n-1])
    else:
        print(xorr)