#include <stdio.h>
#include <string.h>
int main()
{
       //type your code here
       int t,n,k,i,cnt=0,x[100];
       scanf("%d",&t);
       while(t>0)
       {
           cnt=0;
           scanf("%d %d",&n,&k);
           for(i=0;i<n;i++)
           {
               scanf("%d",&x[i]);
               if(x[i]==0)
                cnt++;
           }
           if(cnt>=k)
           printf("beautiful\n");
           else
           printf("not beautiful\n");
           t--;
       }
}
