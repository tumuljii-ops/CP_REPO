t=int(input())

for _ in range(t):
    n=int(input())
    
    arr=list(map(int,input().split()))
    
    i=1
    j=0
    
    while i<len(arr) and j<len(arr):
        
        if arr[i]%arr[j] != 0:
            i=i+1
            j=j+1
        else:
            
            if arr[j]==1:
                
                arr[j]=arr[j]+1
                
                while arr[i]%arr[j] == 0:
                    arr[j]=arr[j]+1
                i=i+1
                j=j+1
                
            elif arr[j]%2==0 and arr[i]%2==0:
                arr[i]=arr[i]+1
                i=i+1
                j=j+1
            else:
                arr[i]=arr[i]+1
                i=i+1
                j=j+1
                
    print(*arr)
                
                
            
    
    