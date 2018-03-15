#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n, m, i, j, test, sum=0, a[100];
    scanf("%d", &test);
    for(i=0; i<test; i++)
    {
        scanf("%d", &n);
        scanf("%d", &m);
        for(j=0; j<(m*n); j++)
        {
            a[j]=pow(2, j+2);
            sum+=a[j];
        }
    }
    printf("%d", sum);
    return 0;
}