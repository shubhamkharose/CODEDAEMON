#include<bits/stdc++.h>
using namespace std;
int main()
{
      //Enter your code here
      int a,b;
      cin>>a>>b;
      int res1=0,res2=0;
      for(int i=a;i<=b;i++)
      {
          if(i%2==0)
            res1=res1+i*i;
        else
            res2=res2+i*i;
      }
      
      if(res1>res2)
        cout<<(res1-res2);
    else
        cout<<(res2-res1);
     return 0;
}
