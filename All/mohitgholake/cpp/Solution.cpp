#include <iostream>
using namespace std;
int main()
{
    int t,i,j,n,k,count;
    //char a[10]=""
    cin>>t;
    for(i=0;i<t;i++)
    {
        cin>>n>>k;
        count=0;
        int a[n];
        for(j=0;j<n;j++)
        {
            cin>>a[j];
            //cout<<a[j];
            if(a[j]==0)
                count++;
        }
        if(count>=k)
            cout<<"beautiful"<<"\n";
        else 
            cout<<"not beautiful"<<"\n";
        //cout<<" "<<count;
    }
}
