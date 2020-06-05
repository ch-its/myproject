t=int(input())
for i in range(t):
    a=[list(map(int,input().split())) for i in range(9)]
    
    x=set(i for i in range(1,10))
    for i in range(9):
        for j in range(9):
            if a[i][j]==0:
                y=set(a[i])
                d=[a[i][j] for i in range(9)]
                b=set(d)
                c=x-(y.union(b))
                for k in c:
                    if k!=0:
                        a[i][j]=k
    for i in range(9):
        for j in range(9):
            print(a[i][j],end=" ")
        print("\n")
