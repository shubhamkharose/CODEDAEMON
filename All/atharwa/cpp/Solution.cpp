#include <iostream>
using namespace std;

int main() 
{
    int a[100]={-1};
	int tot=0;
	int v;
	int j;
	int c=0;
	int o=0;
	int no;
	int i=0;
	
	for(int p=0;p<6;p++)
	cin>>a[i];
	
	int k;
	cin>>k;
	
	while(1)
	{
	    if(a[i]==-1)break;
	    else
	    i++;
	}
	int x[100];
	for(int v=i;v>=0;v-=k)
	{
	 
	   j=v;
        while(1)
    	{   
    	    tot+=a[j];
    	    j--;
    	    i++;
    	    if(i==k)
    	    break;
    	}
    	if(tot>=10)
    	{
    	    no=tot;
    	  	tot=(no%10)+c;
    	  	c=no/10;
    	}
    	else
    	{
    	    tot+=c;
    	    	c=0;
    	}
	
    	x[o]=tot;
	    o++;
	}
    	
    for(int i=o;i>=0;i++)
    {
        cout<<x[i];
    }
	
	return 0;
}