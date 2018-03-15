#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int gcd(int a,int b)
{
    if(a==0)
        return b;
    if(b==0)
        return a;
    return gcd(b,a%b);    
}
int main()
{
    int t,a,b,o;
    scanf("%d",&t);
    while(t++)
    {
        scanf("%d%d",&a,&b);
        o=gcd(a,b);
        printf("%d\n",o);
    }
}