t=int(input())  
for _ in range(t):
    n,x=map(int,input().split())
    
    arr=list(map(int,input().split()))
    
    arr.append(x)
    
    arr.insert(0,0)
    
    
    maxi=-1
    
    for i in range(1,n+1):
        
        if arr[i]-arr[i-1]>maxi:
            maxi=arr[i]-arr[i-1]
            
    x=arr[n+1]-arr[n]
    
    x=x*2
            
    if x>maxi:
        print(x)
    else:
        print(maxi)
        