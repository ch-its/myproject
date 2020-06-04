t=int(input())
for i in range(t):
    n,k=list(map(int,input().split()))
    
    arr=list(map(int,input().split()))
    d=[0 for i in range(n)]
    
    
    for i in range(1,n-1):
        if arr[i]>arr[i-1] and arr[i]>arr[i+1]:
            d[i]=1
    pref=[0 for i in range(n)]
    for i in range(1,n):
        pref[i]=pref[i-1]+d[i]
    ans=0
    index=0
    anst=0
    for l in range(n-k+1):
        if pref[l+k-2]-pref[l]>ans:
            ans=pref[l+k-2]-pref[l]
            index=l
        
        
    print(ans+1,index+1)
        
    