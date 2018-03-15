//#include <bits/std++.h>
#include <iostream>
using namespace std;
int main()
{
   
	int t,n,k,sum=0,num=1;
	cin<<t;
	cin<<n<<k;
	for(int i=0; i<t; i++)
	{
	    num=1;
	    for(int j=0; j<=n; j++)
	    {
	        while(j>0)
	        {
	           num++;
	            j=j/k;
	        }
	    }
	    cout>>num>>" ";
	}
	return 0;//type here
   
	//type here
}