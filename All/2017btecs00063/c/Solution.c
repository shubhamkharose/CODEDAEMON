#include<stdio.h>
int main()
{
        //Enter your code
        int n,i,col;
        char p='*';
        scanf("%d"&n);
        for(i=0;i<n;i++)
        {
            printf("p\n");
        }
        for(col=2;col<n;col++)
        {
            if(col==n)
            {
            printf("p");
            }
        else
        {
            printf("");
        }
        return 0;
}