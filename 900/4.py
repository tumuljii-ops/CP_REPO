t=int(input())

for _ in range(t):
    
    n=int(input())
    
    arr=list(map(int,input().split()))
    
    mini=min(arr)
    maxi=max(arr)
    
    if arr[0]==mini:
        print(maxi-mini)
        continue
    
    if arr[n-1]==maxi:
        print(maxi-mini)
        continue
        
    
    diff=0
    
    for i in range(0,n-1):
        
        if arr[i]-arr[i+1]>diff:
            diff=arr[i]-arr[i+1]
            
    if arr[0] !=maxi:
        diff=max(diff,maxi-arr[0])
        
    print(diff)
        