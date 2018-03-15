#include <iostream>
#include <string.h>
#include<stdio.h>
using namespace std;
int main()
{
	char str[1000];
	cin>>str;
	int i=0;
	int l=strlen(str);
	//cout<<l;

	while(i<l)
	{
	    if(((int)str[i])>=48&&((int)str[i])<=57)
	        cout<<str[i];
	       i++; 
	        
	}
	i=0;
		while(i<l)
	{
	    if(((int)str[i])>=97&&((int)str[i])<=122)
	        cout<<str[i];
	       i++; 
	        
	}

	return 0;
}