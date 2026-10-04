n=int(input())

y=0

for _ in range(n):
    x=input()
    
    
    if x[1]=='+' and x[2]=='+':
        y=y+1
    elif x[0]=='+' and x[1]=='+':
        y=y+1
    elif x[1]=='-' and x[2]=='-':
        y=y-1
    elif x[0]=='-' and x[1]=='-':
        y=y-1
        
print(y)