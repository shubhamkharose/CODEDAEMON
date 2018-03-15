#include<stdio.h>
int main()
{
    int n,i,j;
    scanf("%d",&n);
    int a[n][n];
    for(i=0;i<n;i++)
    {
        for(j=0;j<n;j++)
        {   
            if(j==0)
                printf("*");
            else if(j==n-1)
                printf("*");
            else if(i==j)
                printf("*");
            else
                printf(" ");
                
                
        }
        printf("\n");
    }
    return 0;
}