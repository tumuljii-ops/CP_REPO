t=int(input())

for _ in range(t):
    n=int(input())
    s=input()
    
    total_dots=0
    consequitive_dots=0
    
    three_consequitive_dots=False
    
    
    for i in range(n):
        
        if s[i]=='.':
            total_dots+=1
            consequitive_dots+=1
            
            if consequitive_dots==3:
                three_consequitive_dots=True
                
        else:
            consequitive_dots=0
            
            
    
    if three_consequitive_dots:
        print(2)
    else:
        print(total_dots)
        
            
        
        
        
        