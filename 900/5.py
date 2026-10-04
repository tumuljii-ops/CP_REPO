
def solve(ans,ind,answer,ans1):
    
    if ind>=len(ans):
        ans1.append(answer)
        return 
    
    answer.append(ans[ind])
    solve(ans,ind+1,answer,ans1)
    answer.pop()
    solve(ans,ind+1,answer,ans1)
    
    
t=int(input())
for _ in range(t):
    
    n=int(input())
    
    ans=[]
    
    while n>0:
        x=n%10
        ans.append(x)
        
        n=n//10
        
    ans.reverse()
    
    answer=""
    ans1=[]
    
    solve(ans,0,answer,ans1)
    
    for i in range(len(ans1)):
        
        x=
    
    
    
    
        