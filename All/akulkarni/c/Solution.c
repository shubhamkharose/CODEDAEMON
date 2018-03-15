#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>
int main()
{
      int n,m,tot,a,b;
      scanf("%d",&n);
      m=n/2;
      a=n*n*n;
      b=m*m*m;
      a/=2;
      a-=b;
      a+=(m+n)/2;
      printf("%d",a);
      
      return 0;
}