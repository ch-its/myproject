def pow2(a):
    while a%2==0:
        a=a//2
    return a

t=int(input())
for i in range(t):
    a,b=list(map(int,input().split()))
    ans=0
    if (pow2(a)!=pow2(b)):
        print(-1)
    else:
        c=max(a,b)
        d=min(a,b)
        c=c//d
        while c>=8:
            c=c//8
            ans+=1
        if c>1:
            ans+=1
        print(ans)
        
      
    
        
    
