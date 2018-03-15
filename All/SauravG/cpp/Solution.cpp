#include <iostream>
using namespace std;
int main()
{
       int t;
       cin>>t;
       for(int i=0;i<t;i++)
       {
           int a,b,c;
           cin>>a>>b>>c;
           if(a+b<c||b+c<a||c+a<b)
           
               cout<<"no"<<endl;
           
           else if(a*a+b*b==c*c||b*b+c*c==a*a||c*c+a*a==b*b)
           
               cout<<"right"<<endl;
           
           else if(a*a+b*b>c*c||b*b+c*c>a*a||c*c+a*a>b*b)
          
              cout<<"acute"<<endl;
               
           
           else if(a*a+b*b<c*c||b*b+c*c<a*a||c*c+a*a<b*b)
           
               cout<<"obtuse";
           
       }
}
