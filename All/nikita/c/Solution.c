#include <stdio.h>
#include<string.h>
int main() {
    char ch[10000];
    scanf("%s",ch);
    long int k,sum=0,i,p=0,m,j;
    scanf("%ld",&k);
    long int l=strlen(ch);
    for(i=l-1;i>=l-k-1;i++)
    {
        sum=p;
        p=0;
        for(int a=0;a<k;a++,i--)
        {
            sum+=ch[i]-48;
            if(sum>9&&a==2)
            {
                j=sum;
                m=1;
                while(j!=0)
                {p=j%10;
                    j=j/10;
                    m*=10;
                }
                m/=10;
                m*=p;
                sum=sum-m;
            }
        }
        printf("%ld",sum);
        
    }
	//code
	return 0;
}