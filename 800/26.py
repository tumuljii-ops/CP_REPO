t=int(input())

for  _ in range(t):
    x,k=map(int,input().split())
    
    if x%k!=0:
        print(1)
        print(x)
        continue
    
    
    u=k+1
    
    print(2)
    
    print(x-u,end="")
    print(u)
    