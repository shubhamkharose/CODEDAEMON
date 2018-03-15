#include <iostream>
using namespace std;
int main()
{
       //type your code here
       int t;
       cin>>t;
       int a,b,c;
       for(int i=0;i<t;i++)
       {
        cin>>a>>b>>c;
        if(a==0 || b==0 || c==0)return 0;
        if(a>b && a>c)
        {
            if(a>=b+c)cout<<"no";
            if((a*a)>((b*b)+(c*c)))
            cout<<"obtuse";
            else if((a*a)<((b*b)+(c*c)))cout<<"acute";
            else if((a*a)==((b*b)+(c*c)))cout<<"right";
        }
         if(b>a && b>c)
        {
            if(b>=a+c)cout<<"no";
            if((b*b)>((a*a)+(c*c)))
            cout<<"obtuse";
            else if((b*b)<((a*a)+(c*c)))cout<<"acute";
            else if((b*b)==((a*a)+(c*c)))cout<<"right";
        }
         if(c>a && c>b)
        {
            if(c>=b+a)cout<<"no";
            if((c*c)>((b*b)+(a*a)))
            cout<<"obtuse";
            else if((c*c)<((b*b)+(a*a)))cout<<"acute";
            else if((c*c)==((b*b)+(a*a)))cout<<"right";
        }
       }
       return 0;
       
}
