t=int(input())

for _ in range(t):
    n=int(input())
    
    arr=list(map(int,input().split()))
    
    
    arr.sort()
    
    i=0
    j=n-1
    
    x=[]
    
    while i<=j:
        
        if i==j:
            x.append(arr[i])
        else:
            x.append(arr[i])
            x.append(arr[j])
        i=i+1
        j=j-1
        
    if n==2:
        print("YES")
        continue
    
    sum=x[0]+x[1]
    
    ans=True
        
    
    for i in range(2,n):
        
        if x[i]+x[i-1]!=sum:
            ans=False
            break
        
    
    if ans==True:
        print("YES")
    else:
        print("NO")                                   
        
    
    
            
        
    