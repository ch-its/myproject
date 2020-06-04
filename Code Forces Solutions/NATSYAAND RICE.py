t=int(input())
for i in range(t):
    n,a,b,c,d=list(map(int,input().split()))
    if   (a-b)*n<=c+d and (a+b)*n>=c-d: 
        print("YES")
    else:
        print("NO")
        
    