t=int(input())

for _ in range(t):
    n=int(input())
    
    arr=list(map(int,input().split()))
    
    mpp={}
    
    for i in range(n):
        mpp[arr[i]]=i
        
    b=[0]*n
    
    count=n
    
    for i in range(1,n+1):
        
        k=mpp[i] 
        b[k]=count
        count=count-1
        
    
    for i in range(n):
        print(b[i],end="")
    print()