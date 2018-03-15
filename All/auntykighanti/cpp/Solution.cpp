#include <iostream>
#include<math.h>
using namespace std;

int main() {
    int i,j,k,n,m,t;
    cin>>n>>m;
    int sum=n*m;
    int tot=0;
    for(i=1;i<=sum;i++)
    {
        tot+=pow(2,i);
    }
   cout<<tot;
	return 0;
}