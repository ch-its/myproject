#include <bits/stdc++.h>
using namespace std;
int func(int n)
{
    return ((pow(2,n))-1);
}
int main()
{
    int t;
    cin>>t;
    for (int i=0;i<t;i++)
    {
        int n{2},ans{0};
        int a;cin>>a;
        while (a%func(n)!=0)
        {
            n+=1;
        }
        ans=a/func(n);
        cout<<ans<<"\n";

    }
    


    return 0;
}