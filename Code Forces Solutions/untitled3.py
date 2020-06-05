
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    sum1=0
    for i in range(n):
        cur=a[i]
        j=i
        while j<n and a[j]//abs(a[j])==a[i]//abs(a[i]):
            cur=max(cur,a[j])
            j+=1
        sum1+=cur
        j=i-1
    print(sum1)
    

        
   