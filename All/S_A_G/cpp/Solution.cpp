#include<bits/stdc++.h>
using namespace std;
int main()
{
	string s;
	string d1;
	string d2;
	cin>>s;
	int i,j=0,m=0;
	int l=strlen(&s[0]);
	for(i=0;s[i]!='\0';i++)
	{
	    int ch=(int)(48+s[i]);
	    cout<<ch;
	    if(ch>=48 && ch<=57)
	       d1[j++]=ch;
	    else if(ch>=65 && ch<=90)
	    {
	        d2[m++]=ch;
	    }
	}
	strcat(&d1[0],&d2[0]);
	cout<<d1;
	return 0;
}