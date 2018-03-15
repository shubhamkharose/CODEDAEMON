#include <iostream>
using namespace std;
int min(int a,int b,int c)
{
    if(a>b)
    {
        if(c<b)
        return c;
        else
        return b;
        
    }
    else
    {
        if(c<a)
        return c;
        else
        return a;
    }
}
int main()
{
       int t;
       cin>>t;
       for(int i=0;i<t;i++)
       {
         long a,b,c;
         cin>>a>>b>>c;
         if(a+b>=c && b+c>=a && a+c>=b)
         {
             if(a*a+b*b==c*c || a*a+c*c==b*b || b*b+c*c==a*a)
             cout<<"right\n";
             else
             {
                 if(a<b && c<b)
                 {
                     if(b*b<c*c+a*a)
                     cout<<"acute\n";
                     else
                     cout<<"obtuse\n";
                     
                 }
                 else if(a>c && a>b)
                    {
                        if(b*b+c*c > a*a)
                        cout<<"acute\n";
                        else
                        cout<<"right\n";
                    }
                else if(c>a && c>b)
                    {
                        if(c*c<b*b+a*a)
                        cout<<"acute\n";
                        else
                        cout<<"obtuse";
                    }
                 
             }
         }
         else
         cout<<"no\n";
       }
       return 0;
}

