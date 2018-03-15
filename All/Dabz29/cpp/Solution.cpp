#include <bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	for(int i=0;i<t;i++)
	{
	    int n,k,sum=0,d,sum1=0;
	    cin>>n>>k;
	    for(int j=1;j<=n;j++)
	    {
	        int a=j;
	        while(a)
	        {
	            d=a%k;
	            if(d==0)
	                sum++;
	            a=a/k;
	        } sum1=sum1+sum;
	       
	    } cout<<sum1<<endl;
	}
}