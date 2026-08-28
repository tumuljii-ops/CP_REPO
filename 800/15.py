t=int(input())  

for _ in range(t):
    n,a,b=map(int,input().split())
    
    if n==1:
        if a==1 or b==1:
            print("YES")
            continue
        
    
    if n==a or n==b:
        print("NO")
        continue
    
    if n==a+b+1:
        print("NO")
        continue
    
    if n>a+b+1:
        print("YES")
        continue