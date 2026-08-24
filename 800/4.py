t=int(input())

for _ in range(t):
    
    n=int(input())
    arr=list(map(int,input().split()))
    
    
    prod=1
    
    prefix=[]
    suffix=[]
    
    for i in range(n):
        prod=prod*arr[i]
        prefix.append(prod)
        
    mul=1
        
    for i in range(n-1,-1,-1):
        mul=mul*arr[i]
        suffix.append(mul)
        
    
    suffix.reverse()
    
    ind=-1
    
    for i in range(0,n-1):
        
        if prefix[i]==suffix[i+1]:
            
            ind=i+1
            break
        
    print(ind)
        
    
        