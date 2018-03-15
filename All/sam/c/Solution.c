#include <stdio.h>
int main(){
       //Enter your code here.
       char* arr[]={"Winter is here","Winter is coming"};
       int n;
       scanf("%d",&n);
       printf("%s",arr[n%2]);
       return 0;
}
