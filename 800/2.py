t=int(input())

for _ in range(t):
    
    n=int(input())
    
    arr=list(map(int,input().split()))
        
    
    count=0
    
    for i in range(1,n):
        
        if arr[i]%2==0 and arr[i-1]%2==0:
            count=count+1
        elif arr[i]%2==1 and arr[i-1]%2==1:
            count=count+1
        else :
            continue
        
    print(count)
    
    
    
    
    
    
    
    
    
    