#include <stdio.h>
#include <string.h>
int main()
{
       //type your code here
       int a,b,c,i,j=0;
       scanf("%d %d %d",&a,&b,&c);
       while(j<=b)
       {
       for(i=a;i<=b;i=i+c)
           j++;
           b--;
       }
           printf("%d",j);
}
