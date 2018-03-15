#include <iostream>
using namespace std;
int main()
{
    int t,n,k,i,j,r;
    cin>>t;
    while(t!=0)
    {
        cin>>n>>k;
        int arr[n];
        for(i=0;i<n;i++)
            cin>>arr[i];
        r=0;
        j=0;
        for(i=0;i<n;i++)
            if(arr[i]!=0)
                j+=1;
        if(n-k<j)
            r=1;
        if(r==0)
            cout<<"beautiful\n";
        if(r==1)
        cout<<"not beautiful\n";
        t--;
    }
}
