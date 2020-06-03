#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main()
{
    int t;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        ll n,ans{0},a{2},h{1};
        cin>>n;
        if(n==1)
        {
          cout<<0<<"\n";
          
        }
        else
        {
          while(a<n)
        {
            h++;
            a+=((3*h)-1);
        }
        if(a==n)
        {
            cout<<1<<"\n";
            
        }
        else
        {
            a-=((3*h)-1);
            h-=1;
            while(n>0 && h>=1 && a>0)
            {
                ans+=(n/a);
                n-=(n/a)*a;
                a-=((3*h)-1);
                h-=1;

            }
            cout<<ans<<"\n";
        }
        }
        
        
    }
    return 0;
}