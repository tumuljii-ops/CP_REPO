t=int(input())
for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    
    mini=10000000000
    
    ans=True
    
    for i in range(1,n):
        
        if arr[i]<arr[i-1]:
            ans=False
            break
        else:
            if arr[i]-arr[i-1]<=mini:
                mini=arr[i]-arr[i-1]
    
    if ans==False:
        print(0)
        continue
    
    
    answer=mini//2
    
    print(answer+1)
    
    
    
    