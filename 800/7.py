t=int(input())

for _ in range(t):
    
    a,b,c,d=map(int,input().split())
    
    step=0
    
    
    if d-b<0:
        print(-1)
    elif d-b>=0:
        step=step+(d-b)
        a=a+(d-b)
        
        if a-c<0:
            print(-1)
        else:
            step=step+abs(a-c)
            print(step)
    