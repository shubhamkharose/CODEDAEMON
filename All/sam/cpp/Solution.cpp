#include <iostream>
#include<string>

#include<sstream>
using namespace std;

int main() {
	string s;
	int arr[1000];
	stringstream sso,sso1;
	cin>>s;
	sso << s;
	int a,sum=0;
	sso >> a;
	long int l=0,k,tot=0,i,j,w=0,q=0;
	cin>>k;
	for(j=1;j<=k;j++)
	    q*=10;
	while(a)
	{
	    int tmp=a%q;
	    sum=0;
	    while(tmp)
	    {
	        sum+=tmp%10;
	        tmp/=10;
	    }
	    sum+=w;
	    if(sum>9)
	    {
	        w=sum/10;
	        sum%=10;
	    }
	    
	    arr[l]=sum;
	    l++;
	}
	for(int h=0,g=0;h<l;g*=10,h++)
	{
	    tot+=arr[h]*g;
	}
	cout<< tot;
	return 0;
}