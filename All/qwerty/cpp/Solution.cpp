#include <iostream>
using namespace std;
int main()
{
       int t;
       int c=0,k,n;
       cin>>t;
        for(int h=0;h<t;h++)
        {
           c=0;

           cin>>n>>k;

           int a[n];

           for(int i=0;i<n;i++)
           cin>>a[i];

       //   for(i=0;i<n;i++)printf("%d  ",a[i]);

           for(int i=0;i<n;i++)
           {
               if(a[i]==0)
               c++;
           }
          // printf("\n%d",c);
           if(c >= k)
           cout<<"beautiful";
           else
           cout<<"not beautiful";
        }
       return 0;
}
