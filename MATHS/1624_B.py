def solve():
    a,b,c=map(int,input().split())
    
    result_a=2*b-c
    
    if result_a>0 and result_a%a==0:
        print("YES")
        return
    
    result_c=2*b-a
    
    if result_c>0 and result_c%c==0:
        print("YES")
        return 
    
    if (a+c)%2==0:
    
        result_b=(a+c)//2
    
        if result_b>0 and result_b%b==0:
            print("YES")
            return 
    
    print("NO")
    
    
t=int(input())
for _ in range(t):
    solve()