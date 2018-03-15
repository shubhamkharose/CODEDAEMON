#include<stdio.h>
#include<stdlib.h>
#include<string.h>



int main()
{
    int n1, n2, i, gcd,p,j;
    scanf("%d",&p);

	for(j=0;j<p;j++)
   {
	 scanf("%d %d", &n1, &n2);

    for(i=1; i <= n1 && i <= n2; ++i)
    {
      
        if(n1%i==0 && n2%i==0)
            gcd = i;
             
    }
    printf(" %d\n", gcd);
    
	}
   

    return 0;
}