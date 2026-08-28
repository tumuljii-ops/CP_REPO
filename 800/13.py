t=int(input())

for _ in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    
    
    sum=0
    
    for i in range(n):
        sum+=arr[i]
        
        
    if sum%2==0:
        print("YES")
    else:
        print("NO")