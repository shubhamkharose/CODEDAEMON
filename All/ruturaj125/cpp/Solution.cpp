#include<bits/stdc++.h>
using namespace std;
int main()
{
    int t,i;
    cin>>t;
    while(t--)
    {
        int n;
        cin>>n;
        int size=2*n+1;
        int ar[size];
        for(i=0;i<size;i++)
        {
            cin>>ar[i];
        }
        long long int num=1,den=1;
        for(i=0;i<size;i++)
        {
            if(ar[i]<=6&&i%2==0&&ar[i]!=0)
            {
                num*=1;
                den*=6;
            }
            else
            {
                if(ar[i]<=6&&i%2!=0&&ar[i]!=0)
                {
                    num*=(6-ar[i]+1);//cout<<" "<<num;
                    den*=6;
                }
                else
                {
                    if(ar[i]>6)
                    {
                        int tmp=ar[i]/6;//cout<<" "<<tmp<<" ";
                        while(tmp--)
                            den*=6;
                        ar[i]%=6;
                            //cout<<den;
                        if(ar[i]<=6&&i%2==0&&ar[i]!=0)
                        {
                            num*=1;
                            den*=6;
                        }
                        else
                        {
                            if(ar[i]<=6&&i%2!=0&&ar[i]!=0)
                            {
                                 num*=(6-ar[i]);
                                den*=6;
                            }
                        }
                    }
                }
            }
            //cout<<num<<"/"<<den<<endl;
        }
        cout<<num<<"/"<<den<<endl;
    }
      //Enter your code here
     return 0;
}