#include<iostream>
using namespace std;
int main()
{
    int n;
    cin>>n;
    //cout<<"A";
    while(n--)
    {
        char a[17];
    //cout<<"A";
    cin>>a;
    //cout<<"A";
    int b[16],i=0;
    for(i=15;i>=0;i--)
    {
        if(i%2==0)
        {
            b[i]=(a[i]-48)*2;
        }
        else
        {
            b[i]=a[i]-48;
        }
    }
    int cnt=0;
    for(i=0;i<16;i++)
    {
        if(b[i]/10>0)
        {
            int digit1=b[i]/10;
            int digit2=b[i]%10;
            b[i]=digit1+digit2;
        }
        cnt+=b[i];
    }
    if(cnt%10==0)
        cout<<"Valid"<<endl;
    else
        cout<<"Invalid"<<endl;
    }
    return 0;
}
