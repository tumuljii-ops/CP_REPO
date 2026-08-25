t=int(input())

for _ in range(t):
    
    n=int(input())
    arr=list(map(int,input().split()))
    
    minus_one=0
    plus_one=0
    
    for i in range(n):
        if arr[i]==-1:
            minus_one+=1
        else:
            plus_one+=1
            
    ans=0
            
    if plus_one>minus_one and minus_one%2==0:
        print(0)
    else:
        ans=minus_one-plus_one
        minus_one=minus_one-ans
        
        if minus_one%2==0:
            print(ans)
        else:
            print(ans+1)