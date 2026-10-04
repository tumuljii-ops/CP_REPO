t=int(input())

for _ in range(t):
    n=int(input())
    
    arr=list(map(int,input().split()))
    
    
    x=sorted(arr)
    
    if(arr==x):
        print("YES")
        continue
    
    for i in range(n):
        
        for j in range(1,n-1):
            
            if arr[j]>arr[j-1] and arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
                
    
    if arr==x:
        print("YES")
    else:
        print("NO")
                
                
    