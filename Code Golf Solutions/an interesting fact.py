n=10**6
pr = [1 for i in range(n+1)] 
p = 2
while (p * p <= n): 
    if (pr[p] == 1): 
        for i in range(p * p, n+1, p): 
            pr[i] = 0
    p += 1
d=[i for i in range(n+1)]
for i in range(n+1):
    if pr[i] and pr[int(str(i)[::-1])] and str(i)!=str(i)[::-1]:

        d[i]=d[i-1]+1
    else:
        d[i]=d[i-1]


t=int(input())
for i in range(t):
    a,b=list(map(int,input().split()))
    print(d[b]-d[a-1])