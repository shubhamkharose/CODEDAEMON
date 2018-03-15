#include <iostream>
#include<cmath>
using namespace std;
typedef long long ll;
int main()
{
       int t;
       cin>>t;
       while(t--)
       {
           ll a,b,c;
           cin>>a>>b>>c;
           ll ans1 = a*a+b*b-2*(c/2)*(c/2);
           cout<<((ll)(sqrt(ans1/2)))<<" ";
           ll ans2 = b*b+c*c-2*(a/2)*(a/2);
           cout<<((ll)(sqrt(ans2/2)))<<" ";
           ll ans3 = a*a+c*c-2*(b/2)*(b/2);
           cout<<((ll)(sqrt(ans3/2)))<<endl;
       }
}
