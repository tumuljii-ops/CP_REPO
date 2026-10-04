t=int(input())

for _ in range(t):
    n=int(input())
    
    arr=list(map(int,input().split()))
    
    mini=1000000007
    
    
    for i in range(n):
        
        k=i
        l=n-1
        
        ans=[*0]
        
        while k<=l:
            
            if k==l:
                ans.append(arr[l])
            else:
                x=arr[k]&arr[l]
                ans[k]=x
                ans[l]=x
    u=max(ans)
    
    mini=min(mini,u)
    
    
    print(arr)
    print()
    
    
        
    
                
            