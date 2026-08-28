t=int(input())

for _ in range(t):
    
    n=int(input())
    
    s=input()
    
    
    i=0
    j=n-1
    
    while ((s[i]=='0' and s[j]=='1') or (s[i]=='1' and s[j]=='0')) and (i<=j) :
        i+=1
        j=j-1
        
    
            
            
    if j<i:
        print(0)
    else:
        print(j-i+1)
       
        
        