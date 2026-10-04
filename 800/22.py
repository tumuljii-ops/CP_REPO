t=int(input())

for _ in range(t):
    n,k,x=map(int,input().split())
    
    
    if x!=1:
        print("YES")
        print(n)
        
        for i in range(n):
            print(1,end=" ")
        print()
        continue
    
    if x==1 and k==1:
        print('NO')
        continue
    
    if x==1 and k==2:
        if n%2==0:
            print("YES")
            print(n//2)
            
            for i in range(n//2):
                print(2,end=" ")
            print()
                
        else:
            print("NO")
    elif x==1 and k>=3:
        if n%2==0:
            print("YES")
            print(n//2)
                    
            for i in range(n//2):
                print(2,end=" ")
            print()
        else:
            if n==3:
                print("YES")
                print(1)
                print(3)
            else:
                print("YES")
                print(n//2)
                
                x=n//2
                
                for i in range(x-1):
                    print(2,end=" ")
                print(3)
        
        
    
    
    