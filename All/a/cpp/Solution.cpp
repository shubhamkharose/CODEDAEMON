#include <iostream>
#include<algorithm>
using namespace std;
int main()
{
       //type your code here
       long t,a,b,c;
       cin>>t;
       while(t-->0)
       {
          int arr[3];
          cin>>arr[0];cin>>arr[1];cin>>arr[2];
          sort(arr,arr+3);
          if(arr[0]+arr[1]>arr[2])
        {
            a=arr[0]*arr[0];
            b=arr[1]*arr[1];
            c=arr[2]*arr[2];
            
            if(a+b>c)
            cout<<"acute\n";
            else if(a+b<c)
            cout<<"obtuse\n";
            else
            cout<<"right";
        }           
        else
        cout<<"no\n";
           
       }
}
