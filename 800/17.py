import math
t=int(input())

for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    
    a=math.gcd(arr[0],arr[1])
    
    for i in range(2,n):
        a=math.gcd(a,arr[i])
        
    
    if a>len(arr):
        print("NO")
        continue
    
    
    arr.sort()
    
    b=math.gcd(arr[0],arr[1])
    
    ans=True
    
    
    for i in range(2,n):
        
        b=math.gcd(arr[i],b)
        
        if b>len(arr):
            print("NO")
            ans=False
            break
        
        
    if ans:
        print("YES")
    
        
        
    
        
    
    
    
        
        
        
        