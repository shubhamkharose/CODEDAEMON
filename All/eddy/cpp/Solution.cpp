#include<iostream>
#include<string>
#include <stdio.h>
using namespace std;

void check(int nw,int n,int bui[][3]){
    for(int i=0;i<n;i++){
        cout << bui[i][0]  << bui[i][1] << bui[i][2] << "\n";
    }
}
int main()
{
    int n;
    cin >> n;
    int bui[n][3];
    for(int i=0;i<n;i++){
        cin >> bui[i][0] >> bui[i][1] >> bui[i][2];
        //
    }
    check(0,n,bui);
}