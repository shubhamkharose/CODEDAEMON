#include <bits/stdc++.h>
#define ll long long 
using namespace std;
int main()
{
	int t;
	cin >> t;
	while(t--){
		ll n,m;
		cin >> n >> m;
		int a[n][m];
		ll it=4;
		for(ll i=0;i<n;i++){
			for(ll j=0;i%2==0&& j<m;j++){
				a[i][j]=it;
				it*=2;
			}
			for(ll j=m-1;i%2==1&&j>=0;j--){
				a[i][j]=it;
				it*=2;
			}
		}
		long long sum = 0;
		for(int i=0;i<n;i++)
		{
			for(int j=0;j<m;j++)
				sum+=a[i][j];
		}
		cout << sum << endl;
	}
}