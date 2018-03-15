#include<bits/stdc++.h>
#define MOD (int)(pow(10,9)+7)
using namespace std;
typedef long long int LL;

int main(){
	LL t,n,x;
	cin>>t;
	for(LL i=0;i<t;i++){
	    LL sum=0;
	    cin>>n>>x;
	    for(LL j=0;j<=n;j++){
	        LL tot=(int)pow(x,1),tcnt=1,cnt=1;
	        //cout<<tot<<endl;
	        while(j>=tot){
	            
	            tcnt++;
	            cnt++;
	            tot=(int)pow(x,cnt);
	            
	        }
	        //cout<<j<<" "<<tot<<endl;
	        //cout<<tcnt<<endl;
	        sum+=tcnt;
	    }
	    cout<<sum<<endl;
	}
	return 0;
}