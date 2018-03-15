#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int main()
{
    int t;
    scanf("%d",&t);
    while(t--){
        char a[1000];
        scanf(" %[^\n]s",a);
        printf("%s\n",a);
    }//Enter your code here
}

