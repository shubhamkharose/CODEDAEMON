#include<stdio.h>
#include <math.h>
#define ll long long
int main()
{
    ll t;
    cin >> t;
    while(t--){
    ll d = 4;
    
    long long a,b;
    cin >> a >>b;
    b = b*a;
    b = b-1;
    d = d*pow(2,b);
    cout << d << endl;
    }
     return 0;
}