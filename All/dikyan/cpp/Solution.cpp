#include <iostream>

using namespace std;

int main()
{
	//type here
	string s;
	cin>>s;
	char d[100];
	//int l=strlen(s);
	int i=0,j=0;
	char c;
	while(s[i]!='\0')
	{
	    if(s[i]>=48&&s[i]<=57)
	        {
	            d[j]=s[i];
	            j++;
	          
	        }
	        i++;
	}
	i=0;
	while(s[i]!='\0')
	{
	    if(s[i]>=97)
	        {
	           d[j]=s[i];
	            j++;
	          
	        }
	        i++;
	}
	cout<<d;

}