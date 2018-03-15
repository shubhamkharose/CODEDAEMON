#include <iostream>
using namespace std;
int no(int n)
{
    int cnt=0;
    while(n)
    {
        if(n%2==1)
        cnt++;
        n/=2;
    }
    return cnt;
}
int tz(int n)
{
    int cnt=0;
    while(n)
    {
        if(n%2==0)
        cnt++;
        else
        break;
        n/=2;
    }
    return cnt;
}
int main() {
	// your code goes here
	int t;
	cin>>t;
	while(t--)
	{
	    int a,b;
	    cin>>a>>b;
	    int c1=0,c2=0;
	    for(int i=a;i<=b;i++)
	    {
	        c1+=no(i);
	        c2+=tz(i);
	    }
	    if(c1>=c2)
	    cout<<"Yes "<<(c1-c2)<<endl;
	    else
	    cout<<"No"<<endl;
	}
	return 0;
}
