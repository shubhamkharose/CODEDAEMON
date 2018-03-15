#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int gcd(int a,int b)
{
    if(b==0)
    {
        return a;
    }
    return (b,a%b);
}
int main()
{
    int a,b,c;
    cin>>c;
    for(int i=0;i<c;i++)
    {   cin>>a;
        cin>>b;
        cout<<gcd(a,b);
    }
}