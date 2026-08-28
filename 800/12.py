t=int(input())

for _ in range(t):
    n=int(input())
    
    arr=list(map(int,input().split()))
    
    
    even=0
    odd=0
    
    for i in range(n):
        if arr[i]%2==0:
            even+=1
        else:
            odd+=1
            
    if even==n:
        print(-1)
        continue
    
    if odd==n:
        print(odd-1,"",1)
        print(arr[0:odd-1:1])
        print(arr[odd-1])
        
    
    even_element={}
    odd_element={}
    
    for i in range(n):
        if arr[i]%2==0:
            even_element.append(arr[i])
            
        else:
            odd_element.append(arr[i])
            
    
    lb=odd_element.len()
    lc=even_element.len()
    
    print(lb,"",lc)
    print(odd_element)
    print(even_element)