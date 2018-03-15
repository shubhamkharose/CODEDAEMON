#include<stdio.h>
int main()
{
    int a,b,z,u=0,d=0;
    scanf("%d%d",&a,&b);
    for( ;a<=b;a++)
    {
    for( ;a>=0;a++)
    {
        z=a%2;
        a=a/2;
        if(z==0)
        d++;
        else
        u++;
    }
    if(a==1)
    u++;
    }
    int f;
    f=d-u;
    if(u>d)
    {
    printf("Yes");
    printf("%d",f);
    }
    else
    printf("No");
     return 0;
}