
t=int(input())
for i in range(t):
    n=int(input())
    b=set(map(int,input().split()))
    ans=-1
    for k in range(1,1025):
        flag=1
        for i in b:
            if i^k not in b:
                flag=0
        if flag==1:
            ans=k
            break
    print(ans)
        
      