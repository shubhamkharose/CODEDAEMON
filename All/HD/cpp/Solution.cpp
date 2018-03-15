#include <iostream>
#include<stdlib.h>
using namespace std;
int main()
{
       //type your code here
       int t;
       cin>>t;  
       int size;
       cin>>size;
       int arr[size];
       int k;
       cin>>k;
       for(int i=0;i<size;i++)
       {
           cin>>arr[i];
       }
       int q,cnt=0;
       q=size/k;
       for(int i=0;i<q;i++)
       {
           if(arr[i+k-1]==0)
           cnt++;
       }
       if(cnt==q)
       cout<<"beautiful";
       else
       cout<"not beautiful";
       return 0;
       
}
