#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin>>t;
    
    for(;t;--t)
    {
        string s;
        int i=0;
        int arr[26]={0};
        int flg=0;
        cin>>s;
        for(i=0;i<s.length();i++)
        {
            arr[s[i]-'a']+=1;
        }
        for(i=0;i<26;i++)
        {
            if(arr[i]%2 == 0)
            {
                continue;
            }
            else if(arr[i]%2==1 && flg==0)
            {
                flg=1;
            }
            else
                break;
            
        }
        if(i==26)
            cout<<"YES\n";
        else
            cout<<"NO\n";
    }
      //Enter your code here
     return 0;
}
