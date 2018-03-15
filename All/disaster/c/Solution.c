#include<stdio.h>
int main()
{
        //Enter your code
        int i,j,k;
        scanf("%d",&k);
        i=k;
        j=k;
        for(i=0;i<5;i++)
        {
                for(j=0;j<5;j++)
                {
                if (i==j)
                printf("*");
                }
                
        }
        printf("\n");
        return 0;
}