#include<stdio.h>
int main()
{
     int a,rem,binary=0;
     scanf("%d",&a);
     while(a>0)
        {
                rem=a%2;
                a/=2;
                binary=binary*10+rem;
        }
    
     return 0;
}