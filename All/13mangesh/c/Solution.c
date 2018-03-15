#include <stdio.h>
int main(){
    int a;
       int arr[10];
       for(a=0;a<10;a++)
        arr[a]=a+1;
       for(a=9;a>=0;a--)
        printf("%d ",arr[a]);
       return 0;
}

