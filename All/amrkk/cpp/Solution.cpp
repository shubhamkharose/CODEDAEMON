#include<bits/stdc++.h>
using namespace std;
int main()
{
      int a,b;
      scanf("%d%d",&a,&b);
      int cnt1=0,cnt2=0;
      for(int i=1;i<b;i++)
      {
        if(i==(floor(sqrt(i))*floor(sqrt(i))))
            cnt1+=i;
        else
            cnt2+=i;
      }
      printf("%d",cnt2-cnt1);
     return 0;
}