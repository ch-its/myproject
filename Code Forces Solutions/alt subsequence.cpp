#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int func(int n)
{
    if (n>0)
    {
        return 1;
    }
    else
    {
        return -1;
    }
}
int main()
{
    int t;
    cin>>t;
    for (int i=0;i<t;i++)
    {
        int n;
        cin>>n
        vector<int> v(n)
        for (auto it&:v) cin>>it;
        ll sum=0
        for(int i=0;i<n;i++)
        {
            int cur{a[i]};
            j=i;
            while (j<n && sign(v[i])==sign(v[j]))
            {
                
                cur=max(cur,v[j]);
                ++j;
            }
            sum+=cur;
            i=j-1;
        }
        cout<<sum<<"\n";
    }
    


    return 0;
}