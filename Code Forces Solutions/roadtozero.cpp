#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
    ll t;
    cin>>t;
    for(ll i=0;i<t;i++)
    {
        ll x,y,a,b,ans{0},c{0},d{0};
        cin>>x>>y;
        cin>>a>>b;
        c=max(x,y);
        d=min(x,y);
        if (2*a<b)
        {
            ans+=(c+d)*a;
        }
        else
        {
            ans+=a*(c-d);
        
        
            ans+=b*d;
        
        }
        
        cout<<ans<<"\n";
    }
    return 0;
}