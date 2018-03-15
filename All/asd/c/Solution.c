#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
int main()
{
    int t;
    scanf("%d",&t);
    
    while(t--)
    {
        char str[17];
        int i,j;
        
        scanf("%s",str);
        int sum=0;
        
        for(i=15;i>=0;i--)
        {
            if(i%2==0)
            {
                int tmp=str[i]-'0';
                tmp*=2;
                if(tmp>9)
                    tmp=tmp%10;
                sum+=tmp;
            }
            else
                sum+=(str[i]-'0');
        }
        printf("%d",sum);
        if(sum%10==0)
            printf("Valid\n");
        else
            printf("Invalid\n");
            
    }
    
    return 0;
}