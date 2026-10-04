t=int(input())

for _ in range(t):
    
    n,k=map(int,input().split())
    
    arr=list(map(int,input().split()))
    
    
    x=sorted(arr)
    
    if x==arr:
        print("YES")
        continue
    
    if k==1 and x!=arr:
        print("NO")
    elif k==1 and x==arr:
        print("YES")
    else:
        print("YES")