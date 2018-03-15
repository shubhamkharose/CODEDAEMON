#include <stdio.h>
int main(){
       int arr[10];
       int rvr[10];
       int a,b;
       for (a=1;a<11;a++)
       { scanf("%d",&arr[a]);
       }
       for (b=10;b>0;b--)
       {rvr[b]=arr[b];
       printf("%2d",rvr[b]);
       }
       return 0;
}
