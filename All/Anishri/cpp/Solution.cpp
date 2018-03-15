#include<bits/stdc++.h>
using namespace std;
/*int comparitor(const void *a,const void *b)
{
    return(*(char*)a-*(char*)b);4
}*/
int main()
{
    int i;
	string s;
	cin>>s;
	int l=s.length();
	sort(s.begin(),s.begin()+l);
	for(i=0;i<l;i++)
	{
	    if(s[i]!=' '||(s[i]>='0'&&s[i]<='9')||(s[i]>='a'&&s[i]<='z'))
	    {
	        cout<<s[i];
	    }
	}
	return 0;
}