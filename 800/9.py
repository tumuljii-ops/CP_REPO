t=int(input())
for _ in range(t):
    
    n=int(input())
    arr=list(map(int,input().split()))
    
    maxi=0
    
    count=0
    
    for i in range(1,n):
        
        if arr[i]==arr[i-1] and arr[i]==0:
            count+=1
        else:
            maxi=max(maxi,count)
            count=0
            
    print(maxi)