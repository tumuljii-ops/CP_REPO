t=int(input())
for _ in range(t):
    
    n,k=map(int,input().split())
    
    arr=list(map(int,input().split()))
    
    
    present=False
    
    for i in range(n):
        if arr[i]==k:
            present=True
            break
        
    if present==True:
        print("YES")
    else:
        print("No")
            