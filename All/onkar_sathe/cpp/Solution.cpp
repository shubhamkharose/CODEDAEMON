#include<iostream>
using namespace std;
int main()
{
	//freopen("input05.txt","r",stdin);
	//freopen("output05.txt","w",stdout);
	int t;
	cin>>t;
	while(t--)
	{
		int n,k;
		cin>>n>>k;
		int cnt =0;
		while(n--)
		{
			int tmp;
			cin>>tmp;
			if(tmp==0)
				cnt++;
		}
		if(cnt>=k)
			cout<<"beautiful"<<endl;
		else
			cout<<"not beautiful"<<endl;
	}
}