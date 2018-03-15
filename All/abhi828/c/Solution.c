#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main()
{
    int t;
    scanf("%d",&t);
    for(int ti=0;ti<t;ti++){
        long long int n,b;
        scanf("%lld %lld",&n,&b);
        long long int cnt=0,num=0,d;
        while(num<=n){
            d=num/b+1;
            cnt=cnt+d;
            num++;
        }
        char* s=(char*)malloc(sizeof(char)*1000000000);
        int c,i=0;
        while(cnt!=0){
            c=cnt%10;
            s[i]=c+48;
            i++;
            cnt=cnt/10;
        }
        i=i-1;
        while(i>=0){
            printf("%c ",s[i]);
            i--;
        }
        printf("\n");
    }
}