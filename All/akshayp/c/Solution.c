#include <math.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <assert.h>
#include <limits.h>
#include <stdbool.h>
int main()
{
      int i,j,sum=0,no;
      scanf("%d",&no);
      while(no)
      {
          sum+=no*no;
          no--;
      }
      printf("%d",sum);
      return 0;
}