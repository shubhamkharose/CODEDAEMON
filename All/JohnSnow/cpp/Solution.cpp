#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin >> t;
    while(t--){
        int a[3];
        cin >> a[0] >> a[1] >> a[2];
        sort(a,a+3);
        if(a[0]+a[1]<a[2])
            cout <<"no\n";
        else if((a[0]*a[0]+a[1]*a[1])==a[2]*a[2])
            cout << "right\n";
        else if((a[0]*a[0]+a[1]*a[1])<a[2]*a[2])
            cout << "obtuse\n";
        else if((a[0]*a[0]+a[1]*a[1])>a[2]*a[2])
            cout << "acute\n";
        
    }
       //type your code here
}
