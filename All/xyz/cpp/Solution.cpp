#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int main()
{
       //type your code here
       int x[3];
       int t,i;
       scanf("%d",&t);
       while(t>0)
       {
       for(i=0;i<3;i++)
        scanf("%d",&x[i]);
       sort(x,x+3);
       if((x[0]*x[0])+(x[1]*x[1])==(x[2]*x[2]))
            cout<<"right\n";
       else if((x[0]*x[0])+(x[1]*x[1])<(x[2]*x[2]))
                cout<<"obtuse\n";
       else if((x[0]*x[0])+(x[1]*x[1])>(x[2]*x[2]))
            cout<<"acute\n";
        if(x[0]+x[1]<x[2])
            printf("no");
       t--;
       }
}
