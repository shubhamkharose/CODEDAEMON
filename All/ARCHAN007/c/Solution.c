#include <stdio.h>
int main()
{
    int a[10],b[10],i;
    for(i=0;i<10;i++)
    {
    scanf("%d",&a[i]);
    }
    
    for(i=9;i>=0;i--)
    {
        b[i]=a[9-i];
        
    }
       for(i=0;i<10;i++)

       {
           printf("%d ",b[i]);
       }
       return 0;
}
