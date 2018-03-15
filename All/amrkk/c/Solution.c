#include<stdio.h>
#include<math.h>
int main()
{
      int a,b;
      scanf("%d%d",&a,&b);
      int cnt1,cnt2;
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