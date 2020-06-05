t=int(input())
for i in range(t):
    n=int(input())
    arr=list(map(int,input().split()))
    pos=0
    neg=0
    flag=arr[0]//abs(arr[0])
    
    ans=0
    num=0
    for i in arr:
        if i>0:
            pos+=1
        else:
            neg+=1
    a=[]
    b=[]
    if arr[0]>0:
        pos-=1
        flag=1
        ans+=arr[0]
        num+=1
        a[0]=arr[0]
    else:
        neg-=1
        flag=-1
        ans+=arr[i]
        num+=1
        b[0]=arr[0]
    
    for i in range(1,len(arr)):
        if arr[i]>0:
            pos-=1
            if flag==1:
                if len(a)!=0:
                    if arr[i]>a[0]:
                        ans-=a[0]
                        ans+=arr[i]
                        a[0]=arr[i]
        
            if flag==-1:
                if neg>0:
                    ans+=arr[i]
                    a[0]=arr[i]
                    num+=1
            flag=1
        if arr[i]<0:
            neg-=1
            if flag==-1:
                if len(b)!=0:
                    if arr[i]>b[0]:
                        ans-=b[0]
                        ans+=arr[i]
                        b[0]=arr[i]
            if flag==1:
                if pos>0:
                    ans+=arr[i]
                    b[0]=arr[i]
                    num+=1
            flag=-1
    if num<2:
        print(-1)
    else:
        print(ans)
    
                
            

