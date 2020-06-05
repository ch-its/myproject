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
        if(n==2)
        {
          cout<<"/\\"<<"\n";
          
        }
        else
        {
          while(a<n)
        {
            h++;
            a+=(2*h);
        }
        if(a>n)
        {
          h--;
        }
        
        for(int i=h+1;i>0;i--)
        {
          
          for(int j=0;j<i-1;j++)
          {
            cout<<" ";
          }
          for(int j=0;j<h-i+1;j++)
          {
            cout<<"/\\";
          }
          for(int j=0;j<i-1;j++)
          {
            cout<<" ";
          }
          cout<<"\n";
        }
          
        
    }
        
        }
        return 0;

}