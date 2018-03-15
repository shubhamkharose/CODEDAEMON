#include <stdio.h>

int main(void) {
	int t;
	cin>>t;
	while(t--){
	    int n,m;
	    cin>>n>>m;
	    res=0;
	    for(int i=2;i<n*m+2;i++){
	        res=res+pow(2,i);
	    }
	    cout<<res;
	}
	return 0;
}

