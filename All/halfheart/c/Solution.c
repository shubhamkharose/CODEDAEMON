#include <stdio.h>
#include <string.h>
int main()
{
       int sum=0,sum1=0,r,result,i=0,p;
       char ope;
       char a[10];
       char b[10];
       char *ptr,*ptr1;
       for(i=0;i<10;i++)
       {
         scanf("%c",&a[i]);
       }
       for(i=0;i<10;i++)
       {
         scanf("%c",&b[i]);
       }
       
       ptr=a;
       ptr1=b;
       while(*ptr!='\0')
       {
           sum=sum+(*ptr%10);
           ptr++;
       }
       while(*ptr1!='\0')
       {
           sum1=sum1+(*ptr%10);
           ptr1++;
       }
       if(ope=='+')
       {
            result=sum+sum1;
       }
       if(ope=='-')
       {
            result=sum-sum1;
       }
       if(ope=='*')
       {
            result=sum*sum1;
       }
       if(ope=='%')
       {
            result=sum%sum1;
       }
       while(result/16!=0)
       {
            p=1;
            a[p-1]=(result%16);
            p++;
       }
      printf(" %s",strrev(a));
      return 0;
}
 
