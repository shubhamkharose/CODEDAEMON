#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include<string>
#include <algorithm>
using namespace std;
int sum(int n)
{
    int x=0;
    while(n)
    {
        x+=(n%10);
        n/=10;
    }
    return x;
}
int main()
{
//add your code here
int t;
cin>>t;
while(t--)
{
    string str;
    cin>>str;
    int s=0;
    for(int i=str.length()-2;i>=0;i-=2)
    {
        if(str[i]>=5)
        s+=sum((str[i]-48)*2);
        
    }
    cout<<s;
}
return 0;
}