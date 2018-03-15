#include<bits/stdc++.h>
int a[26];
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--){
        char arr[21];
        int j;
        cin>>arr;
    int i;
        for(i=0;arr[i]!='\0';i++){
            a[arr[i]-97]++;
            
        }
        int cnt=0;
        for(j=0;j<26;j++){
            if(a[j]%2!=0){
               
                cnt++;
            }
           //cout<<a[j]<<" ";
        }
      
        
        if(cnt==1)
            cout<<"YES"<<endl;
        else
            cout<<"NO"<<endl;
    }
    return 0;
}
