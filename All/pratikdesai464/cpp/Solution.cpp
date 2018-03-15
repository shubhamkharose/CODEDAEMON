#include<bits/stdc++.h>

using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        string s;
        cin>>s;
        int flg=0;
        int a[26]={0};
        for(int i=0;i<s.length();i++)
            a[s[i]-97]++;
        int cnt=0,cnt2=0;
        //for(int i=0;i<26;cout<<a[i++]);
        for(int i=0;i<26;i++)
        {
            if(a[i]%2==1)
                cnt++;
        }
        if(cnt==1)
        cout<<"YES";
        else
        cout<<"NO";
        
    }
      //Enter your code here
     return 0;
}
