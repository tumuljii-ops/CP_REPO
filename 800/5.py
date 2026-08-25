t=int(input())
for _ in range(t):
    n,k=map(int,input().split())
    
    if n%2==0 or n%k==0:
        print('YES')
    elif k%2==0 and n%2==1:
        print("NO")
    elif 2+k>n:
        print("NO")
    elif k%2==1 and n%2==1:
        print("YES")
        
    
            
    
    