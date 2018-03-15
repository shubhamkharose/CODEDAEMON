#include <stdio.h>
#include <string.h>
#include<math.h>

int func(int a,int b,int c)
{
    if(a*a==(b*b+c*c))
        return 1;
    else
        return 0;

}

int func1(int a,int b,int c)
{
    if(a*a<(b*b+c*c))
        return 1;
    else
        return 0;
}



int main()
{
       int T,a,b,c,max,m2,m3;
       scanf("%d",&T);
       while(T)
       {
           scanf("%d %d %d",&a,&b,&c);
           if(a+b<c)
           {
            printf("no\n");T--;continue;}
           else if(b+c<a)
           {

            printf("no\n");T--;continue;}
           else
            if(a+c<b)
            {printf("no\n");T--;continue;}



           if(a>b)
           {
               if(a>c)
               {
                max=a;m2=b;m3=c;}
               else
               {
                m2=b;m3=a;
                max=c;}
           }
           else if(b>c)
           {
                max=b; m3=a;m2=c;}
           else {max=c;m2=a;m3=b;}




            if(func( max, m2, m3))
                printf("right\n");
            else if(func1( max, m2, m3))
                printf("acute\n");
            else printf("obtuse\n");


           T--;
       }
}
