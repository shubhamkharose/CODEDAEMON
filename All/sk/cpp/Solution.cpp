#include<bits/stdc++.h>
using namespace std;
typedef long long int ll;

ll trail(int n)
{
    ll cnt=0;
    while(n)
    {
        ll s=n%2;
        if(s==0)    cnt++;
        else break;
        n/=2;
    }
    return cnt;
}



ll tot(int n)
{
    ll cnt=0;
    while(n)
    {
        ll s=n%2;
        if(s==1)    cnt++;
        n/=2;
    }
    return cnt;
}

int main()
{
      ll t,i,j,x=0,y=0,n,a,b;
      cin>>t;
      for(i=0;i<t;i++)
      {
          cin>>a>>b;
          cout<<a<<b;
          cout<<"hello";
          x=y=0;
          for(j=a;j<=b;j++)
          {
              x+=tot(j);
              y+=trail(j);
              //cout<<x<<" "<<y<<endl;
          } 
        if(x>y)
            cout<<"Yes"<<" "<<x-y<<endl;
        else
            cout<<"No"<<" "<<y-x<<endl;
      }
     return 0;
}
