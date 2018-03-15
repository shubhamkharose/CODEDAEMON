#include <stdio.h>
#include <string.h>
int main()
{
    int f, l, d, count;
    cin >> f >> l >> d;
    count = 0;
    for(int i=f; i<=l ; i=i+d)
    {
        count++;
    }
    cout << count << endl;
    return 0;
}
