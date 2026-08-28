

n=int(input())
arr=list(map(int,input().split()))

MAXI=1000000

for i in range(n):
    
    if abs(arr[i]-0)<=MAXI:
        MAXI=abs(arr[i]-0)
        
print(MAXI)
    