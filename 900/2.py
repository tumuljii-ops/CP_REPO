t=int(input())

for _ in range(t):
    
    n,k=map(int,input().split())
    
    l=n*k
    arr=list(map(int,input().split()))
    
    arr.sort()
    
    if k==1:
        if l%2==0:
            x=l//2
            
            print(arr[x-1])
        else:
            x=l//2
            
            print(arr[x])
        continue
    
    
    array=[]
    
    array1=[]
    
    for i in range(k):
        array.append(arr[i])
        
    j=k
    
    for j in range(l):
        array1.append(arr[j])
        
    ans=[]
    
    i=0
    j=0
    
    siz=len(array1)
    
    while i<k:
        
        ans.append(array[i])
        count=k-1
        
        
        while j<siz  and count>=0 :
            
            ans.append(array[j])
            j=j+1
            count=count-1
        
        i=i+1
        
    ind=0
    
    if k%2==0:
        ind=k//2
        ind=ind-1
    else:
        ind=k//2
        
    
    median=0
    
    while ind+k<len(ans):
        median=median+ans[ind]
        ind=ind+k
        
    print(median)
            
            
    
    