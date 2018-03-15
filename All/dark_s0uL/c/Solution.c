#include <stdio.h>
#include <string.h>
#include <stdlib.h>
int main()
{
      int t,n,i,c=0,q,j,k;
      int *x,*y;
      scanf("%d",&t);
      for(i=0;i<t;i++)
      {  
          scanf("%d%d",&n,&k);
            
          x=(int*)malloc(n*sizeof(int));
          y=(int*)malloc(k*sizeof(int));
          for(j=0;j<n;j++)
           { scanf("%d",&x[j]);
                if(x[j]<1 || x[j]>100)
                    continue;
           }
            for(c=0;c<k;c++)
            {
                q=rand()%n;
                y[c]=x[q];
            }  
            
            for(j=0;j<k;j++)
            {
                if(y[j]!=0)
                break;
            }
            if(j==k && k>=0 && k<=n)
            printf("\nbeautiful");
            else
            printf("\nnot beautiful");
            
      }
}
